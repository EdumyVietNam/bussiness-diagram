# Business Use Case: Gửi và theo dõi báo cáo

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | BUC-ADD-007: Gửi và theo dõi báo cáo |
| **2. Tóm tắt** | Gửi phản ánh về khóa học hoặc đề thi có quyền truy cập và theo dõi kết quả. |
| **3. Tác nhân** | Học viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Học viên đề xuất yêu cầu nhằm gửi phản ánh về khóa học hoặc đề thi có quyền truy cập và theo dõi kết quả.<br>2. Bên có trách nhiệm đối chiếu quyền và điều kiện thực hiện.<br>3. Thực hiện nghiệp vụ và ghi nhận kết quả.<br>4. Cung cấp kết quả cho người yêu cầu. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Chọn đúng một khóa học hoặc đề thi; nội dung sau trim từ 1–5000 ký tự. Cần ghi danh Active; đề độc lập dùng ExamEnrollment, đề thuộc khóa học dùng Enrollment tương ứng. Không có ngoại lệ theo vai trò Admin/chủ nội dung. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
