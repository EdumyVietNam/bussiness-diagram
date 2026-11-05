"""Combine owned, simplified tables into one source-backed overview."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / 'Database'
source = (DB / 'Edumy_Database.dbml').read_text()
source_hash = hashlib.sha256((DB / 'Edumy_Database.dbml').read_bytes()).hexdigest()
pattern = r'^Table ([\w.]+)[^\n]*\{\n.*?^}'
source_tables = {m[1]: m[0] for m in re.finditer(pattern, source, re.M | re.S)}
refs = [line for line in source.splitlines() if line.startswith('Ref ')]
groups = ['IdentityAccess', 'ProfileInstructor', 'CourseContent', 'EnrollmentProgress',
          'Examination', 'EssayCertification', 'Payment', 'VoucherPromotion',
          'FeedbackReporting', 'CourseChat', 'Notification', 'AiAssistant', 'Auxiliary']
owned = {}; membership = {}
for group in groups:
    # Reference context repeats tables from other owners, so exclude it.
    cluster_path = DB / group / 'diagram.dbml'
    if group == 'Auxiliary' and not cluster_path.exists():
        # The standalone backup cluster was removed; preserve its source table only in the overview.
        content = source_tables['public.test_vector_backup']
    else:
        content = cluster_path.read_text().split('// BEGIN REFERENCE CONTEXT')[0]
    membership[group] = []
    for match in re.finditer(pattern, content, re.M | re.S):
        name, block = match[1], match[0]
        assert name not in owned, f'Duplicate owner: {name}'
        def shorten_note(m):
            parts = json.loads(m[1]).split('\n')
            useful = []
            for part in parts:
                if part.startswith('External FK: '):
                    continue  # All physical FKs are drawn in the overview.
                if part.startswith(('Check:', 'Conditional/expression uniqueness:')):
                    names = re.findall(r"name: '([^']+)'", part)
                    kind = 'Check constraint' if part.startswith('Check:') else 'Conditional/expression uniqueness'
                    useful.append(kind + ': ' + ', '.join(names) + ' (see original DBML for full definition).')
                else:
                    useful.append(part)
            return '  Note: ' + json.dumps('\n'.join(useful), ensure_ascii=False) if useful else ''
        block = re.sub(r'^  Note: (".*")$', shorten_note, block, flags=re.M)
        block = re.sub(r'\n\s*\n}', '\n}', block)
        owned[name] = block
        membership[group].append(name)
assert owned.keys() == source_tables.keys(), 'Source table coverage mismatch'

def columns(block):
    return set(re.findall(r'^  (\w+) [^\n]+', block, re.M))

for ref in refs:
    endpoints = re.findall(r'((?:public|ai)\.\w+)\.(\([^)]*\)|\w+)', ref)
    assert len(endpoints) == 2
    for table, cols in endpoints:
        assert set(c.strip() for c in cols.strip('()').split(',')) <= columns(owned[table]), ref
out = [
    '// Edumy - simplified full database overview.',
    '// Reading diagram only; not a complete schema for database deployment.',
    f'// Source: Edumy_Database.dbml; SHA256: {source_hash}',
    '// Each table appears once. TableGroups organize the 13 functional clusters.',
    '// All physical source FKs are preserved. Logical links are not fabricated.',
    '// Performance indexes and verbose SQL checks are omitted; see source for full constraints.',
    "Project EdumySimplifiedOverview {\n  database_type: 'PostgreSQL'\n  Note: '65 tables grouped by function, with simplified fields. Based on the original DBML snapshot; not live database metadata.'\n}",
]
for group in groups:
    out.extend(['', '// ' + group, ''])
    for table in membership[group]: out.extend([owned[table], ''])
for group in groups:
    out.append(f'TableGroup {group} {{')
    out.extend('  ' + table for table in membership[group])
    out.extend(['}', ''])
out.extend(['// Physical foreign keys', *refs, ''])
path = DB / 'Edumy_Database_Simplified.dbml'
path.write_text('\n'.join(out))
print(f'{path}: {len(owned)} tables, {sum(len(columns(b)) for b in owned.values())} fields, {len(refs)} refs, {len(groups)} groups')
