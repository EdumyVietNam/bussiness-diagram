# Business Use Case: Nộp bài tự luận

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | BUC-ADD-012: Nộp bài tự luận |
| **2. Tóm tắt** | Nộp tệp bài làm và theo dõi lịch sử chấm. |
| **3. Tác nhân** | Học viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Học viên đề xuất yêu cầu nhằm nộp tệp bài làm và theo dõi lịch sử chấm.<br>2. Bên có trách nhiệm đối chiếu quyền và điều kiện thực hiện.<br>3. Thực hiện nghiệp vụ và ghi nhận kết quả.<br>4. Cung cấp kết quả cho người yêu cầu. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Tệp tài liệu/ảnh hợp lệ theo cấu hình, mặc định tối đa 20 MiB. Bài gần nhất Pending hoặc Passed chặn nộp lại; Failed cho phép thử lại. FE yêu cầu tiến độ 100%; API nộp bài hiện kiểm tra ghi danh, không enforce tiến độ. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
