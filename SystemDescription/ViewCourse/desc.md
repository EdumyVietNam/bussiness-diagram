# System Use Case: Xem khóa học

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | SUC-STD-002: Xem khóa học |
| **2. Tóm tắt** | Hệ thống hiển thị chi tiết khóa học cho Học viên, bao gồm thông tin tổng quan, danh sách chương/bài học từ bảng `Courses`, `CourseSections`, `Lessons`, `Videos`, `Resources`, `Articles`; đồng thời kiểm tra quyền truy cập qua bảng `Enrollments`. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Hệ thống (System) |
| **4. Use case liên quan** | — **Extend:** SUC-STD-001 Tìm kiếm khóa học (dẫn đến xem chi tiết).<br>— **Extend:** SUC-STD-003 Đăng ký khóa học (nếu chưa đăng ký).<br>— **Extend:** SUC-STD-008 Đánh giá & Thảo luận (xem đánh giá). |
| **5. Dòng sự kiện chính** | 1. Học viên chọn một khóa học từ danh sách hoặc nhập URL trực tiếp.<br>2. Hệ thống kiểm tra `Courses.Id` và `Courses.BusinessStatus` = đang kinh doanh.<br>3. Hệ thống truy vấn bảng `Courses`, `CourseSections`, `Lessons`, `Videos`, `Resources`, `Articles` để lấy thông tin chi tiết.<br>4. Hệ thống kiểm tra bảng `Enrollments` để xác định Học viên đã đăng ký hay chưa.<br>5. Hệ thống hiển thị trang chi tiết: tiêu đề, mô tả, giá, giảm giá, thông tin giảng viên từ `AspNetUsers`, danh mục từ `CAT_SubjectCategories`, danh sách chương/bài học (bài chưa mua có thể bị khóa).<br>6. Hệ thống hiển thị đánh giá từ bảng `CourseComments` (nếu có).<br>7. Học viên xem thông tin và quyết định hành động tiếp theo.<br>8. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Khóa học không tồn tại hoặc không kinh doanh** (Tại bước 2)<br>1. Hệ thống không tìm thấy khóa học hoặc trạng thái không hợp lệ.<br>2. Hệ thống hiển thị trang lỗi 404 hoặc "Khóa học không khả dụng".<br>3. Use case kết thúc.<br><br>**A2 — Học viên chưa đăng ký** (Tại bước 4)<br>1. Hệ thống xác định Học viên chưa có bản ghi trong `Enrollments`.<br>2. Hệ thống hiển thị nút "Đăng ký ngay" và giới hạn nội dung xem trước.<br>3. Nếu Học viên chọn đăng ký, chuyển sang SUC-STD-003. |
| **7. Điều kiện tiên quyết** | 1. Khóa học tồn tại trong bảng `Courses` và đang ở trạng thái kinh doanh. |
| **8. Hậu điều kiện** | 1. Học viên xem được thông tin khóa học phù hợp với quyền truy cập.<br>2. Nếu đăng ký, hệ thống chuyển sang SUC-STD-003. |
