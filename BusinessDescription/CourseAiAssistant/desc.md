# Business Use Case: Hỏi đáp với trợ lý AI

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | BUC-ADD-015: Hỏi đáp với trợ lý AI |
| **2. Tóm tắt** | Hỏi đáp theo nội dung khóa học đã ghi danh khi chỉ mục sẵn sàng. |
| **3. Tác nhân** | Học viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Học viên đề xuất yêu cầu nhằm hỏi đáp theo nội dung khóa học đã ghi danh khi chỉ mục sẵn sàng.<br>2. Bên có trách nhiệm đối chiếu quyền và điều kiện thực hiện.<br>3. Thực hiện nghiệp vụ và ghi nhận kết quả.<br>4. Cung cấp kết quả cho người yêu cầu. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Cần ghi danh Active và chỉ mục ready. Chưa sẵn sàng thì khóa gửi và cho thử lại; câu hỏi tối đa 2000 ký tự. Lịch sử phân biệt theo tài khoản và khóa học. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
