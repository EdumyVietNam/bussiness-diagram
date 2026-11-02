# Business Use Case: Xử lý báo cáo

| Trường thông tin | Nội dung |
| --- | --- |
| **1. Tên Use case** | BUC-ADD-008: Xử lý báo cáo |
| **2. Tóm tắt** | Xem báo cáo đang chờ và ghi nhận kết quả xử lý. |
| **3. Tác nhân** | Quản trị viên |
| **4. Use case liên quan** | Liên kết theo bảng truy vết; các nghiệp vụ trước đó là điều kiện, không mặc định là include. |
| **5. Dòng sự kiện chính** | 1. Quản trị viên đề xuất yêu cầu nhằm xem báo cáo đang chờ và ghi nhận kết quả xử lý.<br>2. Bên có trách nhiệm đối chiếu quyền và điều kiện thực hiện.<br>3. Thực hiện nghiệp vụ và ghi nhận kết quả.<br>4. Cung cấp kết quả cho người yêu cầu. |
| **6. Dòng sự kiện phụ** | A1 — Không đủ quyền/điều kiện (bước 2): từ chối yêu cầu và nêu lý do.<br>A2 — Thực hiện thất bại (bước 3): thông báo thất bại, giữ dữ liệu nhập để thử lại; không khẳng định nghiệp vụ thành công. |
| **7. Điều kiện tiên quyết** | Có quyền tham gia nghiệp vụ. Chỉ Admin xử lý báo cáo Pending; ghi chú sau trim từ 1–2000 ký tự. Chuyển sang Resolved và lưu người/thời gian xử lý. Không tự động hoàn tiền hoặc khóa nội dung. |
| **8. Hậu điều kiện** | Kết quả được ghi nhận khi thành công; thất bại không tạo kết quả thành công giả. |
