# Đối chiếu SystemManagementModule với DBML

Nguồn kiểm tra: mã nguồn local SystemManagementModule tại commit `6633698`; ApplicationDbContext, AiModelConfiguration, entity models và migration AllowAiChatOutOfScope. Không truy vấn database đang chạy.

## Entity và field bổ sung

| Thành phần | Kết quả | Cụm |
| --- | --- | --- |
| CourseEssayAssignment / CourseEssayAssignments | Đã có; PublicUrl và StoragePath nullable hỗ trợ đề nháp | EssayCertification |
| CourseEssaySubmission / CourseEssaySubmissions | Đã có; người nộp, người chấm, kết quả, điểm, nhận xét và chống nhiều bài Pending | EssayCertification |
| Report / Reports | Đã có; đúng một đối tượng CourseId hoặc ExamId, thông tin xử lý | FeedbackReporting |
| Course.HasEssay | Đã có; boolean nullable, default false | CourseContent |
| VoucherGrantRange / VoucherGrantPaidAmountRule | Owned types, không phải bảng mới; được flatten thành các cột min/max và khoảng thời gian | VoucherPromotion |

ApplicationDbContext khai báo 57 DbSet. Đối chiếu tên bảng tương ứng và các scalar property của entity nghiệp vụ chưa phát hiện bảng nghiệp vụ mới bị thiếu trong DBML. Bảy bảng Identity kế thừa và bảng test_vector_backup được xử lý riêng; helper/DTO/navigation không tính là bảng độc lập. Đây là kiểm tra tĩnh, không thay thế so sánh metadata database thực tế.

## Điểm lệch cần lưu ý

`AiModelConfiguration` và migration `20261102120000_AllowAiChatOutOfScope` cho phép `ai.chat_history.answer_basis` nhận thêm `out_of_scope`. DBML nguồn và sơ đồ AiAssistant đang phản ánh snapshot cũ, chỉ có course, model_knowledge, course_and_model_knowledge. Không có bảng hoặc cột mới trong thay đổi này; đây là thay đổi check constraint `ck_chat_history_basis`.

Giữ nguyên Edumy_Database.dbml và các sơ đồ sinh từ nó để tuân thủ nguồn chuẩn đã chọn. Khi nâng phiên bản snapshot, cập nhật check constraint rồi sinh lại cụm AiAssistant; chưa xác nhận migration đã được áp dụng trên database live.
