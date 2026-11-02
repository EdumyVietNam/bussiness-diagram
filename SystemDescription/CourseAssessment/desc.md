# System Use Case: Làm bài kiểm tra trong khóa học

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | SUC-ADD-010: Làm bài kiểm tra trong khóa học |
| **2. Tóm tắt** | Làm bài kiểm tra thuộc khóa học và xem kết quả. |
| **3. Tác nhân** | Học viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Học viên mở chức năng và nhập/chọn dữ liệu.<br>2. Hệ thống kiểm tra phiên, quyền sở hữu và dữ liệu đầu vào.<br>3. Hệ thống thực hiện yêu cầu, đọc/ghi dữ liệu nghiệp vụ tương ứng.<br>4. Giao diện hiển thị kết quả; phát thông báo chỉ khi luồng triển khai có hỗ trợ. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Dữ liệu và đối tượng liên quan còn hợp lệ; phạm vi thao tác theo quyền thực tế. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
