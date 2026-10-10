# Business Use Case: Quản lý hồ sơ cá nhân

| Trường thông tin | Nội dung |
| ---------------- | -------- |
| **1. Tên Use case** | BUC-STD-007: Quản lý hồ sơ cá nhân |
| **2. Tóm tắt** | Học viên cập nhật, bổ sung và quản lý thông tin cá nhân trong hồ sơ học viên của nền tảng, đảm bảo thông tin luôn chính xác và đầy đủ. |
| **3. Tác nhân** | **Chính:** Học viên<br>**Phụ:** Bộ phận Quản lý Hành chính (tiếp nhận, đối chiếu và xác minh thông tin) |
| **4. Use case liên quan** | — **Extend:** BUC-STD-004 Học tập (hồ sơ cá nhân phục vụ quản lý học viên trong quá trình học). |
| **5. Dòng sự kiện chính** | 1. Học viên rà soát thông tin cá nhân hiện đang lưu trong hồ sơ.<br>2. Học viên cung cấp thông tin cần cập nhật (họ tên, ngày sinh, số điện thoại, địa chỉ, ảnh đại diện).<br>3. Bộ phận Quản lý Hành chính tiếp nhận, đối chiếu và xác minh thông tin mới.<br>4. Bộ phận Quản lý Hành chính cập nhật hồ sơ học viên.<br>5. Học viên xác nhận thông tin đã được cập nhật chính xác.<br>6. Use case kết thúc. |
| **6. Dòng sự kiện phụ** | **A1 — Thông tin cung cấp thiếu hoặc không hợp lệ** (Tại bước 3)<br>1. Bộ phận Quản lý Hành chính phát hiện thông tin thiếu hoặc sai lệch.<br>2. Bộ phận Quản lý Hành chính thông báo và yêu cầu Học viên bổ sung, chỉnh sửa.<br>3. Học viên cung cấp lại thông tin.<br>4. Quy trình quay lại Bước 3.<br><br>**A2 — Học viên đổi mật khẩu** (Tại bước 2)<br>1. Học viên yêu cầu đổi mật khẩu đăng nhập.<br>2. Bộ phận Quản lý Hành chính xác minh danh tính và thực hiện đổi mật khẩu.<br>3. Use case kết thúc. |
| **7. Điều kiện tiên quyết** | 1. Học viên có hồ sơ đang được lưu trữ.<br>2. Học viên cung cấp được thông tin xác minh danh tính khi cần. |
| **8. Hậu điều kiện** | 1. Thông tin cá nhân của Học viên được cập nhật chính xác trong hồ sơ.<br>2. Học viên nhận được xác nhận cập nhật thành công. |
