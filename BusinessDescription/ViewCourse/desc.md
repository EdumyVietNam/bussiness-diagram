# Business Use Case: Xem khóa học

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | BUC-STD-002: Xem khóa học |
| **2. Tóm tắt** | Học viên tìm hiểu thông tin chi tiết về một khóa học (nội dung chương trình, giảng viên phụ trách, học phí, lịch học) trước khi quyết định đăng ký tham gia. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Giảng viên (giới thiệu nội dung khóa học), Bộ phận Tư vấn & Tuyển sinh |
| **4. Use case liên quan** | — **Extend:** BUC-STD-001 Tìm kiếm khóa học (kết quả tra cứu dẫn đến xem chi tiết).<br>— **Extend:** BUC-STD-003 Mua khóa học, đề thi (nếu Học viên quyết định đăng ký).<br>— **Extend:** BUC-STD-006 Đánh giá & Thảo luận (tham khảo đánh giá của học viên đã tham gia). |
| **5. Dòng sự kiện chính** | 1. Học viên chọn một khóa học cần tìm hiểu.<br>2. Bộ phận Tư vấn & Tuyển sinh hoặc Giảng viên cung cấp thông tin chi tiết: đề cương chương trình, danh sách bài học, học phí, lịch học.<br>3. Học viên xem xét nội dung và tham khảo ý kiến đánh giá của học viên đã tham gia trước đó.<br>4. Học viên đưa ra quyết định tiếp tục đăng ký hoặc dừng tìm hiểu.<br>5. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Khóa học không còn tuyển sinh** (Tại bước 2)<br>1. Bộ phận Tư vấn & Tuyển sinh thông báo khóa học đã ngừng tuyển sinh hoặc tạm dừng.<br>2. Bộ phận Tư vấn giới thiệu khóa học tương đương khác.<br>3. Use case kết thúc. |
| **7. Điều kiện tiên quyết** | 1. Khóa học tồn tại và đang ở trạng thái tuyển sinh. |
| **8. Hậu điều kiện** | 1. Học viên nắm được thông tin khóa học.<br>2. Nếu quyết định đăng ký, chuyển sang BUC-STD-003 Mua khóa học, đề thi. |
