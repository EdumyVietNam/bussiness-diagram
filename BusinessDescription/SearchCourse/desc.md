# Business Use Case: Tìm kiếm khóa học

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | BUC-STD-001: Tìm kiếm khóa học |
| **2. Tóm tắt** | Học viên tra cứu, tìm hiểu danh mục khóa học đang tuyển sinh phù hợp với nhu cầu học tập của bản thân thông qua tài liệu giới thiệu và sự tư vấn của bộ phận tuyển sinh. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Bộ phận Tư vấn & Tuyển sinh (cung cấp danh mục khóa học, tư vấn lựa chọn) |
| **4. Use case liên quan** | — **Extend:** BUC-STD-002 Xem khóa học (Học viên chọn tìm hiểu chi tiết từ kết quả tra cứu). |
| **5. Dòng sự kiện chính** | 1. Học viên tìm hiểu danh mục khóa học đang tuyển sinh.<br>2. Học viên nêu nhu cầu và tiêu chí lựa chọn (lĩnh vực, mức học phí, thời gian học).<br>3. Bộ phận Tư vấn & Tuyển sinh giới thiệu các khóa học phù hợp với nhu cầu.<br>4. Học viên xem xét và chọn ra khóa học quan tâm.<br>5. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Không có khóa học phù hợp** (Tại bước 4)<br>1. Bộ phận Tư vấn & Tuyển sinh không có khóa học nào đáp ứng nhu cầu.<br>2. Bộ phận Tư vấn ghi nhận nhu cầu và giới thiệu các khóa học sắp mở.<br>3. Học viên cân nhắc hoặc để lại thông tin liên hệ.<br>4. Use case kết thúc. |
| **7. Điều kiện tiên quyết** | 1. Có danh mục khóa học đang trong trạng thái tuyển sinh.<br>2. Bộ phận Tư vấn & Tuyển sinh đang hoạt động. |
| **8. Hậu điều kiện** | 1. Học viên xác định được khóa học quan tâm.<br>2. Nếu chọn tìm hiểu chi tiết, chuyển sang BUC-STD-002 Xem khóa học. |
