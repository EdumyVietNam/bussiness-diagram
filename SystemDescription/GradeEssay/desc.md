# System Use Case: Chấm bài tự luận

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | SUC-ADD-013: Chấm bài tự luận |
| **2. Tóm tắt** | Chấm bài đang chờ thuộc khóa học do mình sở hữu. |
| **3. Tác nhân** | Giảng viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Giảng viên mở chức năng và nhập/chọn dữ liệu.<br>2. Hệ thống kiểm tra phiên, quyền sở hữu và dữ liệu đầu vào.<br>3. Hệ thống thực hiện yêu cầu, đọc/ghi dữ liệu nghiệp vụ tương ứng.<br>4. Giao diện hiển thị kết quả; phát thông báo chỉ khi luồng triển khai có hỗ trợ. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Chỉ giảng viên chủ khóa học chấm bài Pending; kết quả Passed hoặc Failed, điểm nếu có trong khoảng 0–10. Bài đã chấm hoặc thao tác đồng thời trả xung đột. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
