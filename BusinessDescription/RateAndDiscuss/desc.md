# Business Use Case: Đánh giá & Thảo luận

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | BUC-STD-006: Đánh giá & Thảo luận |
| **2. Tóm tắt** | Học viên đánh giá chất lượng khóa học/đề thi và trao đổi, thảo luận với Giảng viên hoặc học viên khác trong cộng đồng học tập. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Giảng viên (phản hồi, giải đáp), Ban quản trị (kiểm duyệt nội dung theo quy chế cộng đồng) |
| **4. Use case liên quan** | — **Extend:** BUC-STD-002 Xem khóa học (tham khảo đánh giá trước khi đăng ký).<br>— **Extend:** BUC-STD-004 Học tập (đặt câu hỏi, trao đổi trong quá trình học).<br>— **Extend:** BUC-STD-003 Mua khóa học, đề thi (thảo luận về đề thi đã mua). |
| **5. Dòng sự kiện chính** | 1. Học viên phản hồi, đánh giá chất lượng khóa học/đề thi đã tham gia.<br>2. Học viên đặt câu hỏi, tham gia thảo luận với Giảng viên và học viên khác.<br>3. Giảng viên hoặc học viên khác tiếp nhận và phản hồi.<br>4. Ban quản trị kiểm duyệt nội dung theo quy chế cộng đồng.<br>5. Nội dung đánh giá/thảo luận được công bố để các bên tham khảo.<br>6. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Nội dung vi phạm quy chế cộng đồng** (Tại bước 4)<br>1. Ban quản trị phát hiện nội dung không phù hợp.<br>2. Ban quản trị từ chối đăng tải và thông báo lý do cho Học viên.<br>3. Học viên chỉnh sửa và gửi lại.<br>4. Quy trình quay lại Bước 4.<br><br>**A2 — Học viên chưa đủ điều kiện đánh giá** (Tại bước 1)<br>1. Ban quản trị phát hiện Học viên chưa tham gia khóa học/đề thi.<br>2. Ban quản trị thông báo chỉ học viên đã tham gia mới được đánh giá.<br>3. Use case kết thúc. |
| **7. Điều kiện tiên quyết** | 1. Đối với đánh giá: Học viên đã tham gia khóa học/đề thi.<br>2. Đối với thảo luận: Học viên có quyền truy cập khóa học/đề thi hoặc diễn đàn công khai. |
| **8. Hậu điều kiện** | 1. Đánh giá/thảo luận được công bố thành công.<br>2. Nội dung hiển thị trên kênh thông tin khóa học/đề thi.<br>3. Các bên liên quan nhận được phản hồi. |
