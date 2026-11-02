# Business Use Case: Quản lý và cấp phát voucher

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | BUC-ADD-009: Quản lý và cấp phát voucher |
| **2. Tóm tắt** | Quản lý voucher, chiến dịch, điều kiện và kết quả cấp phát. |
| **3. Tác nhân** | Quản trị viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Quản trị viên đề xuất yêu cầu nhằm quản lý voucher, chiến dịch, điều kiện và kết quả cấp phát.<br>2. Bên có trách nhiệm đối chiếu quyền và điều kiện thực hiện.<br>3. Thực hiện nghiệp vụ và ghi nhận kết quả.<br>4. Cung cấp kết quả cho người yêu cầu. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Theo policy AdminOrMaintainer; chiến dịch Published cần bộ điều kiện hợp lệ và voucher khả dụng. Ghi nhận kết quả từng người; không giả định mọi người đều được cấp. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
