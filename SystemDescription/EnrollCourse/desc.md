# System Use Case: Đăng ký khóa học

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | SUC-STD-003: Đăng ký khóa học |
| **2. Tóm tắt** | Hệ thống xử lý việc Học viên đăng ký khóa học: kiểm tra điều kiện, tạo bản ghi `Enrollments`; nếu khóa học trả phí thì chuyển sang SUC-STD-004 Xử lý thanh toán, áp dụng mã giảm giá. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Hệ thống (System) |
| **4. Use case liên quan** | — **Include:** SUC-STD-004 Xử lý thanh toán, áp dụng mã giảm giá (đối với khóa học trả phí).<br>— **Extend:** SUC-STD-002 Xem khóa học (Học viên có thể đăng ký từ trang chi tiết). |
| **5. Dòng sự kiện chính** | 1. Học viên chọn "Đăng ký khóa học" từ trang chi tiết hoặc danh sách.<br>2. Hệ thống kiểm tra Học viên đã đăng nhập (thông qua `AspNetUsers` và `AspNetUserRoles`).<br>3. Hệ thống kiểm tra bảng `Enrollments` để xác định Học viên chưa đăng ký khóa học này.<br>4. Hệ thống kiểm tra `Courses.Price`:<br>&nbsp;&nbsp;&nbsp;a. Nếu `Price` = 0 (miễn phí): Hệ thống tạo bản ghi `Enrollments` với `Status` = ACTIVE, `EnrolledAt` = thời gian hiện tại.<br>&nbsp;&nbsp;&nbsp;b. Nếu `Price` > 0: Hệ thống chuyển sang SUC-STD-004 để xử lý thanh toán.<br>5. Hệ thống gửi thông báo đăng ký thành công qua `Notifications` và `UserNotifications`.<br>6. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Học viên chưa đăng nhập** (Tại bước 2)<br>1. Hệ thống yêu cầu Học viên đăng nhập hoặc đăng ký tài khoản.<br>2. Sau khi đăng nhập, quy trình quay lại Bước 3.<br><br>**A2 — Học viên đã đăng ký trước đó** (Tại bước 3)<br>1. Hệ thống phát hiện bản ghi `Enrollments` đã tồn tại.<br>2. Hệ thống thông báo "Bạn đã đăng ký khóa học này" và chuyển Học viên vào trang học tập.<br>3. Use case kết thúc.<br><br>**A3 — Khóa học không còn cho phép đăng ký** (Tại bước 4)<br>1. Hệ thống phát hiện khóa học ngừng kinh doanh hoặc hết chỗ.<br>2. Hệ thống thông báo lỗi và đưa Học viên về danh sách khóa học.<br>3. Use case kết thúc. |
| **7. Điều kiện tiên quyết** | 1. Học viên đã đăng nhập.<br>2. Khóa học tồn tại trong `Courses` và đang cho phép đăng ký.<br>3. Học viên chưa đăng ký khóa học này. |
| **8. Hậu điều kiện** | 1. Nếu miễn phí: Bản ghi `Enrollments` được tạo, Học viên có quyền truy cập.<br>2. Nếu trả phí: Đơn hàng được tạo trong `PaymentOrders`, chờ thanh toán thành công mới kích hoạt `Enrollments`. |
