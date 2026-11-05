"""Add source-backed reference tables to simplified cluster DBMLs (idempotent)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / 'Database'
source = (DB / 'Edumy_Database.dbml').read_text()
checksum = hashlib.sha256((DB / 'Edumy_Database.dbml').read_bytes()).hexdigest()
blocks = {m[1]: m[0] for m in re.finditer(r'^Table ([\w.]+)[^\n]*\{\n.*?^}', source, re.M | re.S)}
refs = []
for line in source.splitlines():
    if line.startswith('Ref '):
        ends = re.findall(r'((?:public|ai)\.\w+)\.(\([^)]*\)|\w+)', line)
        assert len(ends) == 2
        refs.append((line, [(n, tuple(c.strip() for c in cols.strip('()').split(','))) for n, cols in ends]))

def fields(block):
    body = re.split(r'^  (?:(?:indexes|checks) \{|Note:)', block, flags=re.M)[0]
    return {m[1]: m[0] for m in re.finditer(r'^  (\w+) [^\n]+', body, re.M)}

def pk_lines(block):
    return [line for line in block.splitlines() if re.match(r'^    \(', line) and 'pk]' in line]

def pk_fields(block):
    return {v.strip() for line in pk_lines(block) for v in re.search(r'\(([^)]+)\)', line)[1].split(',')}

# Additional context needed to explain enrollment, participants and entitlement.
extra = {
    'IdentityAccess': 'AspNetRoles AspNetUserRoles',
    'ProfileInstructor': 'AspNetUsers AspNetRoles AspNetUserRoles',
    'CourseContent': 'AspNetUsers',
    'EnrollmentProgress': 'AspNetUsers Courses CourseSections Exams PaymentOrders',
    'Examination': 'AspNetUsers Courses Lessons ExamEnrollments Enrollments',
    'EssayCertification': 'AspNetUsers Courses Exams Enrollments ExamAttempts',
    'Payment': 'AspNetUsers Courses Exams Enrollments ExamEnrollments Vouchers',
    'VoucherPromotion': 'AspNetUsers PaymentOrders',
    'FeedbackReporting': 'AspNetUsers Courses Exams Enrollments ExamEnrollments',
    'CourseChat': 'AspNetUsers Courses Enrollments',
    'Notification': 'AspNetUsers',
    'AiAssistant': 'AspNetUsers Courses Enrollments',
    'Auxiliary': '',
}
user_basic = {'Id', 'UserName', 'FullName', 'Email', 'PhoneNumber', 'AvatarUrl', 'Status'}
context_fields = {
    'Courses': {'Id', 'Title', 'CreatorId', 'Status', 'BusinessStatus', 'HasCertificate', 'HasEssay'},
    'CourseSections': {'Id', 'CourseId', 'Title', 'Order', 'Status'},
    'Lessons': {'Id', 'SectionId', 'Title', 'Type', 'Order', 'Status'},
    'Exams': {'Id', 'Title', 'CreatorId', 'CourseId', 'LessonId', 'Status', 'BusinessStatus', 'PassingScore'},
    'PaymentOrders': {'Id', 'Code', 'UserId', 'VoucherId', 'OrderStatus', 'TotalAmount', 'PaidAt'},
    'Vouchers': {'Id', 'Code', 'Name', 'Status', 'DiscountType', 'DiscountValue'},
    'ExamAttempts': {'Id', 'UserId', 'ExamId', 'Score', 'PassingScoreSnapshot', 'Status', 'SubmitAt'},
}
summary = []
coverage = set()
for group, names in extra.items():
    path = DB / group / 'diagram.dbml'
    current = path.read_text().split('// BEGIN REFERENCE CONTEXT')[0]
    primary = {m[1]: m[0] for m in re.finditer(r'^Table ([\w.]+)[^\n]*\{\n.*?^}', current, re.M | re.S)}
    local = set(primary)
    support = {'public.' + n for n in names.split()} - local
    # Include actual direct FK targets of primary tables, without recursively importing modules.
    for line, ends in refs:
        if ends[0][0] in local and ends[1][0] not in local:
            support.add(ends[1][0])
    present = local | support
    available = {n: fields(b) for n, b in primary.items()}
    for n in support:
        full = fields(blocks[n]); short = n.split('.')[1]
        if short == 'AspNetUsers': selected = user_basic.copy()
        elif short in context_fields: selected = context_fields[short].copy()
        elif short.startswith('CAT_'): selected = {'Id', 'Code', 'Name', 'ParentId', 'Status'}
        else:
            # Link tables retain their compact source-backed business fields.
            selected = set(full) - {'CreatedBy', 'UpdatedBy', 'UpdatedAt', 'IsDefault', 'SortOrder', 'Description', 'Name', 'Code'}
            if short == 'AspNetRoles': selected = {'Id', 'Name'}
        selected |= pk_fields(blocks[n])
        for line, ends in refs:
            if all(t in present for t, cols in ends):
                for t, cols in ends:
                    if t == n: selected.update(cols)
        available[n] = {f: line for f, line in full.items() if f in selected}
    included = []
    for line, ends in refs:
        if all(n in available and set(cols) <= available[n].keys() for n, cols in ends):
            included.append(line); coverage.add(line)
    def clean_note(match):
        original = json.loads(match[1])
        parts = [part for part in original.split('\n') if not (part.startswith('External FK: ') and part[len('External FK: '):] in included)]
        return '  Note: ' + json.dumps('\n'.join(parts), ensure_ascii=False) if parts else ''
    out = [f'// Source SHA256: {checksum}', '// Simplified reading diagram; not a full migration schema.',
           '// Primary tables own the domain; reference tables provide local context.',
           f"Project Edumy{group} {{\n  database_type: 'PostgreSQL'\n}}", '']
    for n, b in primary.items():
        b = re.sub(r'^  Note: (".*")$', clean_note, b, flags=re.M)
        out.extend([b, ''])
    out.append('// BEGIN REFERENCE CONTEXT')
    for n in sorted(support):
        out.append(f"Table {n} [note: 'Reference table: simplified context from Edumy_Database.dbml; not owned by this cluster.'] {{")
        out.extend(available[n].values())
        pks = pk_lines(blocks[n])
        if pks: out.extend(['  indexes {', *pks, '  }'])
        # Explain only foreign keys whose destination is outside this view.
        pending = [line for line, ends in refs if ends[0][0] == n and line not in included]
        if pending: out.append('  Note: ' + json.dumps('\n'.join('External FK: '+line for line in pending), ensure_ascii=False))
        out.extend(['}', ''])
    out.extend(included)
    out.extend(['', '// Context-only links without physical FKs in source are described, never fabricated as Ref.'])
    if group == 'AiAssistant': out.append('// ai.* course_id/user_id and public.Courses/AspNetUsers: logical context only; no physical FK in source.')
    if group == 'Auxiliary': out.append('// Backup table only; no User or artificial relationship is added.')
    path.write_text('\n'.join(out)+'\n')
    summary.append((group, len(local), len(support), len(included)))
assert coverage == {line for line, ends in refs}, 'Source FK coverage incomplete: ' + repr({line for line, ends in refs} - coverage)
readme = DB / 'README.md'
s = readme.read_text()
s = s.replace('Chỉ chứa bảng nội bộ. FK ngoài cụm được giữ cột và ghi Note.', 'Mỗi cụm có bảng nghiệp vụ chính và bảng tham chiếu gọn. Các FK có đủ bảng/cột được vẽ bằng Ref; phần còn lại ghi Note.')
s = s.split('\n## Bảng tham chiếu theo cụm')[0]
s += '\n## Bảng tham chiếu theo cụm\n\nCập nhật theo yêu cầu đọc từng cụm độc lập. Số liệu 65 bảng/51 FK nội bộ/43 FK xuyên cụm ở phần trên mô tả phân quyền sở hữu ban đầu; bảng dưới mô tả các file hiện tại. Bảng tham chiếu có thể lặp ở nhiều sơ đồ, không phải entity mới.\n\n'
s += 'User tham chiếu gồm Id, UserName, FullName, Email, PhoneNumber, AvatarUrl, Status. Các vai trò người tạo/người học/người chấm/người gửi/người xử lý nối về cùng AspNetUsers. IdentityAccess giữ bảng User chính với thông tin hồ sơ đã giản lược. Auxiliary không gắn User vì nguồn không có liên kết. AI giữ User/khóa học/ghi danh để đọc ngữ cảnh nhưng không tự tạo FK chưa có.\n\n'
s += '| Cụm | Bảng chính | Bảng tham chiếu | FK hiển thị |\n| --- | ---: | ---: | ---: |\n'
for g,p,r,f in summary: s += f'| [{g}]({g}/diagram.dbml) | {p} | {r} | {f} |\n'
s += '\nTổng hợp các sơ đồ bao phủ đủ 94 FK nguồn. Chạy `python3 scripts/add_cluster_context.py` để cập nhật lại phần bảng tham chiếu từ DBML gốc và phần bảng chính hiện tại.\n'
readme.write_text(s)
print(json.dumps(summary))
