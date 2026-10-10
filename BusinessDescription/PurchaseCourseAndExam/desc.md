# Business Use Case: Mua khóa học, đề thi

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | BUC-STD-003: Mua khóa học, đề thi |
| **2. Tóm tắt** | Học viên thực hiện đăng ký mua khóa học hoặc đề thi, hoàn tất thủ tục đóng học phí (có thể áp dụng ưu đãi) và nhận quyền tham gia học tập/thi thử. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Bộ phận Tư vấn & Tuyển sinh (tiếp nhận đăng ký), Bộ phận Kế toán (thu học phí, xuất hóa đơn) |
| **4. Use case liên quan** | — **Extend:** BUC-STD-002 Xem khóa học (Học viên có thể đăng ký sau khi tìm hiểu).<br>— **Extend:** BUC-STD-004 Học tập (sau khi mua, Học viên bắt đầu tham gia học). |
| **5. Dòng sự kiện chính** | 1. Học viên đăng ký mua khóa học/đề thi với Bộ phận Tư vấn & Tuyển sinh.<br>2. Bộ phận Tư vấn lập phiếu đăng ký và thông báo học phí (giá gốc, ưu đãi nếu có, tổng tiền phải nộp).<br>3. Học viên kiểm tra thông tin đăng ký và lựa chọn hình thức thanh toán.<br>4. Học viên cung cấp mã ưu đãi nếu có.<br>5. Bộ phận Tư vấn kiểm tra mã ưu đãi và cập nhật số tiền phải nộp.<br>6. Bộ phận Kế toán thu học phí và xác nhận hoàn tất thanh toán.<br>7. Bộ phận Tư vấn ghi nhận đăng ký thành công và cấp quyền tham gia cho Học viên.<br>8. Học viên nhận xác nhận đăng ký thành công.<br>9. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Mã ưu đãi không hợp lệ** (Tại bước 5)<br>1. Bộ phận Tư vấn thông báo mã ưu đãi không hợp lệ, hết hạn hoặc không đủ điều kiện.<br>2. Học viên cung cấp mã khác hoặc bỏ qua ưu đãi.<br>3. Quy trình quay lại Bước 5.<br><br>**A2 — Thanh toán không thành công** (Tại bước 6)<br>1. Bộ phận Kế toán thông báo thanh toán không thành công và nêu lý do.<br>2. Học viên chọn thanh toán lại hoặc hủy đăng ký.<br>3. Nếu thanh toán lại, quy trình quay lại Bước 6. |
| **7. Điều kiện tiên quyết** | 1. Học viên có hồ sơ cá nhân hợp lệ.<br>2. Khóa học/đề thi đang ở trạng thái cho phép đăng ký.<br>3. Học viên chưa đăng ký khóa học/đề thi này trước đó. |
| **8. Hậu điều kiện** | 1. Học viên được cấp quyền tham gia khóa học/đề thi đã mua.<br>2. Giao dịch đăng ký và học phí được ghi nhận.<br>3. Học viên nhận được xác nhận đăng ký thành công. |
