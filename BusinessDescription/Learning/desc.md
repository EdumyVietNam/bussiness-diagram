# Business Use Case: Học tập

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | BUC-STD-004: Học tập |
| **2. Tóm tắt** | Học viên tham gia học tập theo chương trình của khóa học đã đăng ký, hoàn thành các bài học và theo dõi tiến độ học tập của bản thân. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Giảng viên (giảng dạy, hướng dẫn nội dung bài học) |
| **4. Use case liên quan** | — **Include:** BUC-STD-003 Mua khóa học, đề thi (Học viên phải đăng ký trước để có quyền tham gia).<br>— **Extend:** BUC-STD-006 Đánh giá & Thảo luận (Học viên đặt câu hỏi, trao đổi trong quá trình học). |
| **5. Dòng sự kiện chính** | 1. Học viên được xếp lớp và nhận lịch học của khóa học đã đăng ký.<br>2. Học viên tham gia các buổi học theo chương trình.<br>3. Giảng viên giảng dạy và hướng dẫn nội dung bài học.<br>4. Học viên thực hành, làm bài tập và hoàn thành các bài học.<br>5. Học viên theo dõi tiến độ học tập cá nhân.<br>6. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Học viên chưa đăng ký khóa học** (Tại bước 1)<br>1. Bộ phận Tư vấn & Tuyển sinh phát hiện Học viên chưa có quyền tham gia khóa học.<br>2. Bộ phận Tư vấn đề xuất Học viên thực hiện đăng ký mua khóa học.<br>3. Use case kết thúc hoặc chuyển sang BUC-STD-003.<br><br>**A2 — Bài học chưa được mở** (Tại bước 2)<br>1. Giảng viên thông báo Học viên cần hoàn thành bài học trước đó trước khi tham gia bài kế tiếp.<br>2. Học viên quay lại hoàn thành các bài trước. |
| **7. Điều kiện tiên quyết** | 1. Học viên đã đăng ký khóa học và quyền tham gia còn hiệu lực. |
| **8. Hậu điều kiện** | 1. Tiến độ học tập của Học viên được ghi nhận.<br>2. Học viên có thể tiếp tục tham gia các bài học tiếp theo.<br>3. Nếu hoàn thành toàn bộ chương trình, khóa học được ghi nhận hoàn thành. |
