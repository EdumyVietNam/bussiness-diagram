# Các cụm database Edumy


## Sơ đồ tổng hợp tinh gọn

Mở [Edumy_Database_Simplified.dbml](Edumy_Database_Simplified.dbml) để xem toàn hệ thống: **65 bảng, 653 field, 94 FK**, chia thành **13 TableGroup**. Mỗi bảng chỉ xuất hiện một lần và lấy field từ bảng chính của từng cụm, không lấy bản tham chiếu rút gọn. Bảng backup `test_vector_backup` được giữ trong nhóm Auxiliary của sơ đồ tổng hợp; không tạo lại thư mục cụm đã bỏ.

Các FK được vẽ trực tiếp; note SQL dài được rút gọn thành tên ràng buộc và dẫn về DBML gốc. PK, unique thông thường và kiểu dữ liệu còn giữ nguyên. File phục vụ đọc thiết kế, không dùng để triển khai database. Chạy `python3 scripts/build_simplified_overview.py` để tái tạo từ các cụm hiện tại.

Nguồn duy nhất: `Edumy_Database.dbml`. SHA256: `8e6e97193434f56f10d28d3be7527d797806c8cf8706738427b3dbf1bf55b4ed`.

Sơ đồ giản lược để đọc thiết kế; không dùng làm schema triển khai. Mỗi cụm có bảng nghiệp vụ chính và bảng tham chiếu gọn. Các FK có đủ bảng/cột được vẽ bằng Ref; phần còn lại ghi Note. Không suy diễn FK từ tên cột. PK và unique được ưu tiên bảo toàn; partial/expression unique và check được ghi bằng Note. Index hiệu năng được ẩn.

| Cụm | Bảng | Field nguồn | Field hiển thị |
| --- | ---: | ---: | ---: |
| [IdentityAccess](IdentityAccess/diagram.dbml) | 8 | 67 | 53 |
| [ProfileInstructor](ProfileInstructor/diagram.dbml) | 6 | 70 | 44 |
| [CourseContent](CourseContent/diagram.dbml) | 10 | 160 | 92 |
| [EnrollmentProgress](EnrollmentProgress/diagram.dbml) | 3 | 27 | 20 |
| [Examination](Examination/diagram.dbml) | 9 | 122 | 78 |
| [EssayCertification](EssayCertification/diagram.dbml) | 3 | 47 | 27 |
| [Payment](Payment/diagram.dbml) | 3 | 58 | 43 |
| [VoucherPromotion](VoucherPromotion/diagram.dbml) | 7 | 108 | 90 |
| [FeedbackReporting](FeedbackReporting/diagram.dbml) | 3 | 48 | 27 |
| [CourseChat](CourseChat/diagram.dbml) | 2 | 24 | 15 |
| [Notification](Notification/diagram.dbml) | 4 | 54 | 42 |
| [AiAssistant](AiAssistant/diagram.dbml) | 6 | 64 | 54 |
| [Auxiliary](Auxiliary/diagram.dbml) | 1 | 3 | 3 |

Tổng: 65 bảng; 51 FK nội bộ; 43 FK xuyên cụm. Field: 852 → 588.

## Field đã ẩn

Các field dưới đây chỉ bị ẩn khỏi bản trình bày, không bị xóa khỏi database.

| Bảng | Field ẩn |
| --- | --- |
| `public.AspNetUsers` | `AccessFailedCount`, `ConcurrencyStamp`, `NormalizedEmail`, `PasswordHash`, `SecurityStamp`, `UpdatedAt` |
| `public.AspNetRoles` | `ConcurrencyStamp` |
| `public.AspNetRoleClaims` | — |
| `public.AspNetUserClaims` | — |
| `public.AspNetUserLogins` | — |
| `public.AspNetUserRoles` | — |
| `public.AspNetUserTokens` | — |
| `public.UserActionTokens` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.InstructorRequests` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.UserDocuments` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.CAT_InstructorApplicationRequirements` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CAT_Levels` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CAT_Occupations` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CAT_Provinces` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.Courses` | `Code`, `CreatedBy`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.CourseSections` | `Code`, `CreatedBy`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.Lessons` | `Code`, `CreatedBy`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.Articles` | `Code`, `CreatedBy`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.Videos` | `AudioBitrate`, `AudioCodec`, `Bitrate`, `Code`, `Codec`, `CreatedBy`, `Description`, `EncodedFileName`, `EncodedFileSize`, `EncoderPreset`, `ErrorMessage`, `FPS`, `HasStorage`, `Height`, `IsDefault`, `JobId`, `MaxRetries`, `Name`, `OriginalFileName`, `OriginalFileSize`, `RetryCount`, `SortOrder`, `StoragePath`, `TempFilePath`, `UpdatedAt`, `Width` |
| `public.Resources` | `Code`, `CreatedBy`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.CAT_CourseTypes` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CAT_SubjectCategories` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CAT_Tags` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CAT_DocumentTypes` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.Enrollments` | — |
| `public.ExamEnrollments` | — |
| `public.EnrollmentSectionCompletions` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.Exams` | `Code`, `CreatedBy`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.Questions` | `Code`, `CreatedBy`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.QuestionOptions` | `Code`, `CreatedBy`, `IsDefault`, `Name`, `UpdatedAt` |
| `public.ExamQuestions` | — |
| `public.ExamAttempts` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.AttemptQuestions` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.AttemptAnswers` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.CAT_ExamCategories` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CAT_GradingRules` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CourseEssayAssignments` | `Code`, `CreatedBy`, `IsDefault`, `SortOrder`, `StoragePath`, `UpdatedAt` |
| `public.CourseEssaySubmissions` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.Certificates` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.PaymentOrders` | `CreatedBy`, `Description`, `IsDefault`, `Name`, `QrUrl`, `SortOrder`, `UpdatedAt` |
| `public.PaymentOrderItems` | — |
| `public.PaymentTransactions` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `RawPayload`, `SortOrder`, `UpdatedAt` |
| `public.Vouchers` | `CreatedBy`, `IsDefault`, `SortOrder`, `UpdatedAt` |
| `public.UserVouchers` | — |
| `public.VoucherGrantCampaigns` | `CreatedBy`, `IsDefault`, `SortOrder`, `UpdatedAt`, `UpdatedBy` |
| `public.VoucherGrantRules` | `Code`, `Name`, `IsDefault`, `SortOrder`, `CreatedBy`, `UpdatedAt` |
| `public.VoucherGrantCampaignResults` | — |
| `public.VoucherUsages` | — |
| `public.CAT_VoucherTypes` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `public.CourseComments` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.ExamComments` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.Reports` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.Conversations` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `LastMessageSnippet`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.ChatMessages` | `UpdatedAt` |
| `public.Notifications` | `Code`, `CreatedBy`, `Description`, `IsDefault`, `Name`, `SortOrder`, `UpdatedAt` |
| `public.UserNotifications` | — |
| `public.NotificationOutbox` | `LastError`, `LeaseUntil` |
| `public.CAT_NotificationTypes` | `CreatedBy`, `IsDefault`, `UpdatedAt` |
| `ai.chunks` | `content_hash` |
| `ai.course_indexes` | `chunking_version`, `embedding_digest`, `normalization_version`, `prefix_version`, `source_fingerprint`, `updated_at` |
| `ai.reindex_jobs` | — |
| `ai.chat_history` | — |
| `ai.chat_sessions` | `updated_at` |
| `ai.course_reindex_outbox` | `last_error`, `lease_until` |
| `public.test_vector_backup` | — |

## FK xuyên cụm

- **IdentityAccess**: `Ref FK_AspNetUsers_CAT_Levels_LevelId: public.AspNetUsers.LevelId > public.CAT_Levels.Id [delete: set null, update: no action]`
- **IdentityAccess**: `Ref FK_AspNetUsers_CAT_Occupations_OccupationId: public.AspNetUsers.OccupationId > public.CAT_Occupations.Id [delete: set null, update: no action]`
- **IdentityAccess**: `Ref FK_AspNetUsers_CAT_Provinces_ProvinceId: public.AspNetUsers.ProvinceId > public.CAT_Provinces.Id [delete: set null, update: no action]`
- **ProfileInstructor**: `Ref FK_InstructorRequests_AspNetUsers_UserId: public.InstructorRequests.UserId > public.AspNetUsers.Id [delete: cascade, update: no action]`
- **ProfileInstructor**: `Ref FK_UserDocuments_AspNetUsers_UserId: public.UserDocuments.UserId > public.AspNetUsers.Id [delete: cascade, update: no action]`
- **CourseContent**: `Ref FK_Courses_AspNetUsers_CreatorId: public.Courses.CreatorId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **EnrollmentProgress**: `Ref FK_Enrollments_AspNetUsers_UserId: public.Enrollments.UserId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **EnrollmentProgress**: `Ref FK_Enrollments_Courses_CourseId: public.Enrollments.CourseId > public.Courses.Id [delete: cascade, update: no action]`
- **EnrollmentProgress**: `Ref FK_Enrollments_PaymentOrders_PaymentOrderId: public.Enrollments.PaymentOrderId > public.PaymentOrders.Id [delete: set null, update: no action]`
- **EnrollmentProgress**: `Ref FK_ExamEnrollments_AspNetUsers_UserId: public.ExamEnrollments.UserId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **EnrollmentProgress**: `Ref FK_ExamEnrollments_Exams_ExamId: public.ExamEnrollments.ExamId > public.Exams.Id [delete: cascade, update: no action]`
- **EnrollmentProgress**: `Ref FK_ExamEnrollments_PaymentOrders_PaymentOrderId: public.ExamEnrollments.PaymentOrderId > public.PaymentOrders.Id [delete: set null, update: no action]`
- **EnrollmentProgress**: `Ref FK_EnrollmentSectionCompletions_CourseSections_SectionId: public.EnrollmentSectionCompletions.SectionId > public.CourseSections.Id [delete: restrict, update: no action]`
- **Examination**: `Ref FK_Exams_AspNetUsers_CreatorId: public.Exams.CreatorId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **Examination**: `Ref FK_Exams_Courses_CourseId: public.Exams.CourseId > public.Courses.Id [delete: set null, update: no action]`
- **Examination**: `Ref FK_Exams_Lessons_LessonId: public.Exams.LessonId > public.Lessons.Id [delete: set null, update: no action]`
- **Examination**: `Ref FK_Questions_AspNetUsers_CreatorId: public.Questions.CreatorId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **Examination**: `Ref FK_ExamAttempts_AspNetUsers_UserId: public.ExamAttempts.UserId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **EssayCertification**: `Ref FK_CourseEssayAssignments_Courses_CourseId: public.CourseEssayAssignments.CourseId > public.Courses.Id [delete: restrict, update: no action]`
- **EssayCertification**: `Ref FK_CourseEssaySubmissions_AspNetUsers_GradedBy: public.CourseEssaySubmissions.GradedBy > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **EssayCertification**: `Ref FK_CourseEssaySubmissions_AspNetUsers_StudentId: public.CourseEssaySubmissions.StudentId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **EssayCertification**: `Ref FK_Certificates_AspNetUsers_UserId: public.Certificates.UserId > public.AspNetUsers.Id [delete: cascade, update: no action]`
- **EssayCertification**: `Ref FK_Certificates_Courses_CourseId: public.Certificates.CourseId > public.Courses.Id [delete: set null, update: no action]`
- **EssayCertification**: `Ref FK_Certificates_Exams_ExamId: public.Certificates.ExamId > public.Exams.Id [delete: set null, update: no action]`
- **Payment**: `Ref FK_PaymentOrders_AspNetUsers_UserId: public.PaymentOrders.UserId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **Payment**: `Ref FK_PaymentOrders_Vouchers_VoucherId: public.PaymentOrders.VoucherId > public.Vouchers.Id [delete: set null, update: no action]`
- **VoucherPromotion**: `Ref FK_UserVouchers_AspNetUsers_UserId: public.UserVouchers.UserId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **VoucherPromotion**: `Ref FK_UserVouchers_PaymentOrders_PaymentOrderId: public.UserVouchers.PaymentOrderId > public.PaymentOrders.Id [delete: set null, update: no action]`
- **VoucherPromotion**: `Ref FK_VoucherGrantCampaignResults_AspNetUsers_UserId: public.VoucherGrantCampaignResults.UserId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **VoucherPromotion**: `Ref FK_VoucherUsages_PaymentOrders_PaymentOrderId: public.VoucherUsages.PaymentOrderId > public.PaymentOrders.Id [delete: restrict, update: no action]`
- **FeedbackReporting**: `Ref FK_CourseComments_AspNetUsers_UserId: public.CourseComments.UserId > public.AspNetUsers.Id [delete: cascade, update: no action]`
- **FeedbackReporting**: `Ref FK_CourseComments_Courses_CourseId: public.CourseComments.CourseId > public.Courses.Id [delete: cascade, update: no action]`
- **FeedbackReporting**: `Ref FK_ExamComments_AspNetUsers_UserId: public.ExamComments.UserId > public.AspNetUsers.Id [delete: cascade, update: no action]`
- **FeedbackReporting**: `Ref FK_ExamComments_Exams_ExamId: public.ExamComments.ExamId > public.Exams.Id [delete: cascade, update: no action]`
- **FeedbackReporting**: `Ref FK_Reports_AspNetUsers_ResolvedBy: public.Reports.ResolvedBy > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **FeedbackReporting**: `Ref FK_Reports_AspNetUsers_UserId: public.Reports.UserId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **FeedbackReporting**: `Ref FK_Reports_Courses_CourseId: public.Reports.CourseId > public.Courses.Id [delete: restrict, update: no action]`
- **FeedbackReporting**: `Ref FK_Reports_Exams_ExamId: public.Reports.ExamId > public.Exams.Id [delete: restrict, update: no action]`
- **CourseChat**: `Ref FK_Conversations_AspNetUsers_InstructorId: public.Conversations.InstructorId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **CourseChat**: `Ref FK_Conversations_AspNetUsers_StudentId: public.Conversations.StudentId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **CourseChat**: `Ref FK_Conversations_Courses_CourseId: public.Conversations.CourseId > public.Courses.Id [delete: restrict, update: no action]`
- **CourseChat**: `Ref FK_ChatMessages_AspNetUsers_SenderId: public.ChatMessages.SenderId > public.AspNetUsers.Id [delete: restrict, update: no action]`
- **Notification**: `Ref FK_UserNotifications_AspNetUsers_UserId: public.UserNotifications.UserId > public.AspNetUsers.Id [delete: cascade, update: no action]`

## Liên kết logic và bảng phụ trợ

- PaymentOrderItems.ItemType + ItemId xác định sản phẩm đa hình, không có FK trực tiếp đến Courses/Exams trong nguồn.
- NotificationOutbox và Notifications có tham chiếu logic; không tự tạo FK cho EntityId, RecipientUserId hoặc NotificationId.
- Các course_id/user_id AI không có FK trong nguồn được giữ là field; không tạo quan hệ mới.
- test_vector_backup thuộc Auxiliary, không phải bảng nghiệp vụ ứng dụng.
- Các file thuộc cùng mô hình nguồn nhưng độc lập để đọc; không ghép lại nhằm triển khai schema đã giản lược.

## Đối chiếu entity System Module

[Xem kết quả đối chiếu mã nguồn và chênh lệch so với snapshot](SystemModuleAudit.md).

## Bảng tham chiếu theo cụm

Cập nhật theo yêu cầu đọc từng cụm độc lập. Số liệu 65 bảng/51 FK nội bộ/43 FK xuyên cụm ở phần trên mô tả phân quyền sở hữu ban đầu; bảng dưới mô tả các file hiện tại. Bảng tham chiếu có thể lặp ở nhiều sơ đồ, không phải entity mới.

User tham chiếu gồm Id, UserName, FullName, Email, PhoneNumber, AvatarUrl, Status. Các vai trò người tạo/người học/người chấm/người gửi/người xử lý nối về cùng AspNetUsers. IdentityAccess giữ bảng User chính với thông tin hồ sơ đã giản lược. Auxiliary không gắn User vì nguồn không có liên kết. AI giữ User/khóa học/ghi danh để đọc ngữ cảnh nhưng không tự tạo FK chưa có.

| Cụm | Bảng chính | Bảng tham chiếu | FK hiển thị |
| --- | ---: | ---: | ---: |
| [IdentityAccess](IdentityAccess/diagram.dbml) | 8 | 3 | 12 |
| [ProfileInstructor](ProfileInstructor/diagram.dbml) | 6 | 3 | 10 |
| [CourseContent](CourseContent/diagram.dbml) | 10 | 1 | 11 |
| [EnrollmentProgress](EnrollmentProgress/diagram.dbml) | 3 | 5 | 13 |
| [Examination](Examination/diagram.dbml) | 9 | 5 | 21 |
| [EssayCertification](EssayCertification/diagram.dbml) | 3 | 5 | 14 |
| [Payment](Payment/diagram.dbml) | 3 | 6 | 13 |
| [VoucherPromotion](VoucherPromotion/diagram.dbml) | 7 | 2 | 14 |
| [FeedbackReporting](FeedbackReporting/diagram.dbml) | 3 | 5 | 17 |
| [CourseChat](CourseChat/diagram.dbml) | 2 | 3 | 8 |
| [Notification](Notification/diagram.dbml) | 4 | 1 | 3 |
| [AiAssistant](AiAssistant/diagram.dbml) | 6 | 3 | 6 |
| [Auxiliary](Auxiliary/diagram.dbml) | 1 | 0 | 0 |

Tổng hợp các sơ đồ bao phủ đủ 94 FK nguồn. Chạy `python3 scripts/add_cluster_context.py` để cập nhật lại phần bảng tham chiếu từ DBML gốc và phần bảng chính hiện tại.
