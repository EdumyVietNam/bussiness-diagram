# Edumy - Business & System Analysis Repository

Kho lưu trữ này chứa toàn bộ các tài liệu phân tích thiết kế, mô hình hóa nghiệp vụ, đặc tả hệ thống và thiết kế cơ sở dữ liệu cho dự án **Edumy**.

Kiến trúc thư mục được phân tách rõ ràng giữa lớp Nghiệp vụ (Business Layer) và lớp Hệ thống (System Layer) nhằm đảm bảo sự minh bạch trong quá trình phân tích và phát triển phần mềm.

---

## 📂 Trúc trúc thư mục (Directory Architecture)

Mô tả ngắn gọn về vai trò của các thư mục cốt lõi trong repository:

- **`BusinessDescription/`**: Chứa sơ đồ Use Case nghiệp vụ tổng thể (`Edumy_Business_UseCase.drawio`) và các thư mục con chứa file đặc tả (`desc.md`) cho từng luồng nghiệp vụ. Lớp này tập trung vào quy trình tương tác giữa con người và tổ chức, KHÔNG phụ thuộc vào công nghệ.
- **`SystemDescription/`**: Chứa sơ đồ Use Case hệ thống tổng thể (`Edumy_System_Usecase.drawio`) và các thư mục con chứa file đặc tả (`desc.md`) cho các luồng hệ thống. Lớp này tập trung vào tương tác giữa người dùng cuối (End-user) và phần mềm/database.
- **`Database/`**: Chứa các file thiết kế cơ sở dữ liệu (`.dbdiagram`, `.dbml`) phục vụ cho việc tạo ERD (Entity-Relationship Diagram) và generate script SQL.

---

## 🤖 AI Agent Guidelines (Quy tắc bắt buộc dành cho LLMs/Agents)

> **MỤC ĐÍCH:**

### Rule 1: Audit Drawio & Xác định ngữ cảnh

Trước khi tạo bất kỳ file đặc tả nào, Agent cần đối chiếu (nếu có thể đọc) hoặc dựa vào file sơ đồ `.drawio` tương ứng:

- Nếu viết đặc tả Nghiệp vụ: Căn cứ vào `BusinessDescription/Edumy_Business_UseCase.drawio`.
- Nếu viết đặc tả Hệ thống: Căn cứ vào `SystemDescription/Edumy_System_Usecase.drawio`.

### Rule 2: Phân tách rõ ràng Business vs. System Use Case

- **Business Use Case (Nghiệp vụ):** Văn phong hành chính. Tác nhân là các bộ phận, phòng ban, hoặc con người thực. Các bước là quy trình thẩm định, duyệt hồ sơ, nộp giấy tờ thực tế. Không mô tả click chuột, validate form, hay database.
- **System Use Case (Hệ thống):** Văn phong kỹ thuật phần mềm. Tác nhân là User, Admin, System. Bắt buộc có các bước tương tác với UI, xử lý file/dung lượng, validate dữ liệu, lưu Database, và trigger thông báo/email.

### Rule 3: File Naming & Path Convention

Khi sinh ra file đặc tả mới, Agent phải xuất định dạng Markdown và đặt đúng vào cấu trúc thư mục quy định:

- Tên thư mục của Use Case phải viết liền, viết hoa chữ cái đầu (PascalCase). Ví dụ: `RegisterToBecomeAnInstructor`.
- Tên file bắt buộc là: `desc.md`.
- Cấu trúc đường dẫn:
  - `[Layer]Description/[UseCaseName]/desc.md`
  - VD: `SystemDescription/RegisterToBecomeAnInstructor/desc.md`

### Rule 4: Template Cấu trúc Markdown bắt buộc

Tất cả các file `desc.md` phải được trình bày dưới dạng BẢNG (Markdown Table). Không được tự ý thay đổi tên các trường trong bảng. Cấu trúc chuẩn bao gồm 8 trường:

| Trường thông tin            | Nội dung                                                                                     |
| --------------------------- | -------------------------------------------------------------------------------------------- |
| **1. Tên Use case**         | [Tên của Use case]                                                                           |
| **2. Tóm tắt**              | [Mô tả ngắn gọn mục đích của Use case]                                                       |
| **3. Tác nhân**             | [Các Actor tham gia]                                                                         |
| **4. Use case liên quan**   | [Include: ... / Extend: ... (nếu có)]                                                        |
| **5. Dòng sự kiện chính**   | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3...]                                                 |
| **6. Dòng sự kiện phụ**     | A1: [Tên ngoại lệ 1] (Tại bước X)<br>1. [Cách xử lý]<br>A2: [Tên ngoại lệ 2] (Tại bước Y)... |
| **7. Điều kiện tiên quyết** | 1. [Điều kiện 1]<br>2. [Điều kiện 2]                                                         |
| **8. Hậu điều kiện**        | 1. [Kết quả 1]<br>2. [Kết quả 2]                                                             |

_(Agent phải bám sát cấu trúc bảng này để đảm bảo tính đồng nhất cho toàn bộ tài liệu dự án Edumy)._
