# System Use Case: Tìm kiếm khóa học

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | SUC-STD-001: Tìm kiếm khóa học |
| **2. Tóm tắt** | Hệ thống hỗ trợ Học viên tìm kiếm và lọc khóa học dựa trên từ khóa, danh mục, loại khóa học và khoảng giá; truy vấn dữ liệu từ bảng `Courses`, `CAT_SubjectCategories`, `CAT_CourseTypes`, `CAT_Tags` và trả kết quả phân trang. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Hệ thống (System) |
| **4. Use case liên quan** | — **Extend:** SUC-STD-002 Xem khóa học (từ kết quả tìm kiếm).<br>— **Extend:** SUC-STD-003 Đăng ký khóa học (nếu Học viên quyết định mua). |
| **5. Dòng sự kiện chính** | 1. Học viên truy cập trang "Danh sách khóa học" hoặc nhập từ khóa vào thanh tìm kiếm.<br>2. Hệ thống hiển thị giao diện tìm kiếm gồm ô tìm kiếm và các bộ lọc (danh mục, loại khóa học, khoảng giá, đánh giá).<br>3. Học viên nhập từ khóa và/hoặc chọn các tiêu chí lọc.<br>4. Hệ thống validate dữ liệu đầu vào (loại bỏ ký tự đặc biệt, giới hạn độ dài từ khóa).<br>5. Hệ thống truy vấn bảng `Courses` kết hợp `CAT_SubjectCategories`, `CAT_CourseTypes`, `CAT_Tags` theo điều kiện tìm kiếm và chỉ lấy các khóa học có `BusinessStatus` = đang kinh doanh.<br>6. Hệ thống áp dụng sắp xếp (mặc định theo độ liên quan hoặc bộ lọc Học viên chọn).<br>7. Hệ thống trả về danh sách kết quả phân trang kèm thông tin: tên, thumbnail, giá, giảm giá, giảng viên, đánh giá trung bình.<br>8. Học viên duyệt kết quả và có thể chọn xem chi tiết.<br>9. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Không tìm thấy kết quả** (Tại bước 7)<br>1. Hệ thống không tìm thấy bản ghi nào khớp điều kiện.<br>2. Hệ thống hiển thị thông báo "Không tìm thấy khóa học phù hợp" và gợi ý bỏ bớt bộ lọc hoặc từ khóa liên quan.<br>3. Học viên điều chỉnh tìm kiếm.<br>4. Quy trình quay lại Bước 4.<br><br>**A2 — Từ khóa không hợp lệ** (Tại bước 4)<br>1. Hệ thống phát hiện từ khóa chứa ký tự không hợp lệ hoặc vượt quá độ dài cho phép.<br>2. Hệ thống hiển thị thông báo lỗi và yêu cầu nhập lại.<br>3. Học viên nhập lại từ khóa.<br>4. Quy trình quay lại Bước 4. |
| **7. Điều kiện tiên quyết** | 1. Hệ thống đang hoạt động.<br>2. Có ít nhất một khóa học trong bảng `Courses` với trạng thái kinh doanh hợp lệ. |
| **8. Hậu điều kiện** | 1. Học viên nhận được danh sách khóa học phù hợp.<br>2. Nếu chọn xem chi tiết, hệ thống chuyển sang SUC-STD-002. |
