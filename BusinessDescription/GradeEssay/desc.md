# Business Use Case: Chấm bài tự luận

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | BUC-ADD-013: Chấm bài tự luận |
| **2. Tóm tắt** | Chấm bài đang chờ thuộc khóa học do mình sở hữu. |
| **3. Tác nhân** | Giảng viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Giảng viên đề xuất yêu cầu nhằm chấm bài đang chờ thuộc khóa học do mình sở hữu.<br>2. Bên có trách nhiệm đối chiếu quyền và điều kiện thực hiện.<br>3. Thực hiện nghiệp vụ và ghi nhận kết quả.<br>4. Cung cấp kết quả cho người yêu cầu. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Chỉ giảng viên chủ khóa học chấm bài Pending; kết quả Passed hoặc Failed, điểm nếu có trong khoảng 0–10. Bài đã chấm hoặc thao tác đồng thời trả xung đột. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
