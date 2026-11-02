# Business Use Case: Trao đổi riêng với giảng viên

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | BUC-ADD-014: Trao đổi riêng với giảng viên |
| **2. Tóm tắt** | Gửi tin nhắn riêng theo khóa học và đọc lịch sử hội thoại. |
| **3. Tác nhân** | Học viên, Giảng viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Học viên, Giảng viên đề xuất yêu cầu nhằm gửi tin nhắn riêng theo khóa học và đọc lịch sử hội thoại.<br>2. Bên có trách nhiệm đối chiếu quyền và điều kiện thực hiện.<br>3. Thực hiện nghiệp vụ và ghi nhận kết quả.<br>4. Cung cấp kết quả cho người yêu cầu. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Chỉ thành viên hội thoại được đọc. Gửi yêu cầu người dùng/khóa học/ghi danh còn hiệu lực và chủ khóa học không đổi; mất quyền gửi vẫn đọc được lịch sử. Tin nhắn trim 1–4000 ký tự; thử lại dùng cùng UUID để tránh trùng. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
