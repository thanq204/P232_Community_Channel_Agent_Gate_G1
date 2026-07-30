# PRODUCT REQUIREMENTS DOCUMENT (PRD)

## 1. Tổng quan

| Thuộc tính | Nội dung |
|---|---|
| Tên sản phẩm | Community Channel Agent |
| Mã đề tài | CHAT-10 |
| Vai trò | Member, Admin |
| Nền tảng | Web responsive |
| Mục tiêu | Hỗ trợ moderation, FAQ, tương tác và vận hành kênh |
| MVP | RBAC, moderation, FAQ/RAG, HITL queue, scheduling, dashboard |
| Thời gian | 6 tuần |
| Công nghệ | LLM + Moderation API, LangGraph, FastAPI, PostgreSQL/pgvector, Redis, WebSocket, Next.js |

## 2. Bối cảnh và cơ hội
Admin thường phải xử lý nhiều nội dung và câu hỏi giống nhau. Hệ thống tự động có thể giảm tải, nhưng moderation là bài toán có rủi ro false positive/false negative nên cần pipeline nhiều lớp và con người phê duyệt.

## 3. Mục tiêu sản phẩm
### 3.1. Mục tiêu người dùng
- Member nhận phản hồi nhanh, hiểu vì sao nội dung bị giữ và có thể appeal.
- Admin tập trung vào trường hợp quan trọng thay vì thao tác lặp lại.

### 3.2. Mục tiêu doanh nghiệp
- Chuẩn hóa cách áp dụng nội quy.
- Giảm thời gian moderation và FAQ.
- Có dữ liệu đo sức khỏe, xu hướng và chi phí vận hành kênh.

## 4. Persona
### Member – An, 24 tuổi
Thường dùng điện thoại, muốn hỏi nhanh, không muốn bị chặn sai và cần biết quy tắc rõ ràng.

### Admin – Linh, 31 tuổi
Quản lý nhiều kênh, cần hàng đợi ưu tiên, bằng chứng, reason code và quyền quyết định cuối.

## 5. User Stories
### Member
- Tôi muốn đăng bài/bình luận và biết ngay nội dung có vi phạm quy tắc hay không.
- Tôi muốn nhận câu trả lời FAQ có nguồn.
- Tôi muốn sửa hoặc appeal khi nội dung bị giữ.

### Admin
- Tôi muốn cấu hình nội quy và ngưỡng escalation.
- Tôi muốn xem nội dung, rule khớp, confidence và lịch sử trước khi quyết định.
- Tôi muốn lên lịch bài và duyệt gợi ý nội dung.
- Tôi muốn theo dõi latency, false positive, chi phí và tải moderation.

## 6. Yêu cầu chức năng
### FR-01 Authentication & RBAC
- Đăng nhập bằng email/OTP.
- Member chỉ truy cập kênh được cấp quyền.
- Admin truy cập moderation queue, rule, FAQ và dashboard.

### FR-02 Nội dung realtime
- Tạo bài, bình luận, reply.
- WebSocket cập nhật feed và trạng thái moderation.

### FR-03 Moderation pipeline
- Rule: từ cấm, spam pattern, link/domain, rate limit.
- Moderation API: harassment, hate, sexual, self-harm, violence và nhóm policy liên quan.
- LLM chỉ xử lý trường hợp cần hiểu ngữ cảnh/sắc thái.
- Output chuẩn: `risk_level`, `policy_id`, `reason`, `confidence`, `suggested_action`.

### FR-04 Hành động
- Allow.
- Soft warning + gợi ý sửa.
- Hold for review.
- Escalate high-risk.
- Không tự ban vĩnh viễn trong MVP.

### FR-05 FAQ / RAG
- Truy xuất câu trả lời từ FAQ, nội quy, lịch sự kiện.
- Trả lời có nguồn và ngày cập nhật.
- Không có nguồn phù hợp thì nói chưa đủ dữ liệu và chuyển admin.

### FR-06 Welcome & scheduling
- Chào thành viên mới bằng template có thể chỉnh.
- Lập lịch bài; nội dung do Agent gợi ý phải được admin duyệt.

### FR-07 Admin queue & appeal
- Sắp xếp theo risk, thời gian và confidence.
- Cho phép approve/reject/edit/escalate.
- Lưu quyết định để đánh giá model/rule.
- Member theo dõi trạng thái appeal.

### FR-08 Dashboard
- Số bài/bình luận, tỷ lệ auto-handled, queue size.
- False positive/overturn rate.
- Latency P50/P95.
- Cost/token và rate limit.
- Xu hướng chủ đề và sentiment ở mức tổng hợp, không lập hồ sơ cá nhân nhạy cảm.

## 7. Phạm vi
### Trong MVP
RBAC, feed cơ bản, moderation nhiều lớp, FAQ, HITL queue, appeal, scheduling và dashboard.

### Ngoài MVP
Auto-ban, crisis response hoàn toàn tự động, profiling tâm lý cá nhân, quảng cáo cá nhân hóa sâu.

## 8. Dữ liệu cần chuẩn bị
- `users`, `roles`, `channels`, `memberships`.
- `posts`, `comments`, `reports`, `appeals`.
- Bộ `policies` và `rules` có version.
- FAQ/nội quy/lịch sự kiện và metadata nguồn.
- Dataset nội dung đã ẩn danh với label risk/action.
- Quyết định admin để đo overturn và cải thiện threshold.
- Log latency, token/cost, lỗi và feedback.

## 9. Kiến trúc
`Member → Next.js → FastAPI/WebSocket → Rule Engine → Moderation API → LangGraph/LLM → RAG PostgreSQL+pgvector → Action Policy → Member/Admin Queue`

Redis dùng cho cache, queue, rate limit và trạng thái realtime.

## 10. Yêu cầu phi chức năng
### Hiệu năng
- P50 ≤ 1.5 giây, P95 ≤ 3 giây với nội dung thường.
- Timeout LLM 4 giây; fallback sang rule/queue.
- Cache FAQ phổ biến.

### Bảo mật
- RBAC ở backend, không dựa vào frontend.
- Audit log bất biến cho quyết định moderation.
- Không đưa API key hoặc dữ liệu thật chưa ẩn danh vào log.
- Có cơ chế xóa dữ liệu và giới hạn retention.

### Độ chính xác và an toàn
- High-risk luôn đưa HITL.
- Câu trả lời FAQ phải có source.
- Threshold được hiệu chỉnh trên pilot; không hứa accuracy tuyệt đối.
- Admin có thể override và quyết định override được lưu lại.

## 11. Chỉ số thành công

| Chỉ số | Mục tiêu MVP |
|---|---:|
| P95 moderation/FAQ response | ≤ 3 giây |
| FAQ xử lý không cần admin | ≥ 40% |
| High-risk vào HITL | 100% |
| False positive moderation | ≤ 5% pilot |
| Overturn rate của admin | Theo dõi, mục tiêu giảm dần |
| Uptime demo | ≥ 99% trong tuần demo |
| Admin rating | ≥ 4/5 |

## 12. Rủi ro và giảm thiểu

| Rủi ro | Giảm thiểu |
|---|---|
| Chặn nhầm nội dung | Soft warning, appeal, admin override, theo dõi overturn |
| Bỏ sót nội dung nguy cơ | Rule + Moderation API + LLM; ngưỡng cao đưa HITL |
| LLM bịa FAQ | RAG có nguồn; không đủ nguồn thì không trả lời chắc chắn |
| Prompt injection | Tách system policy, sanitize input, tool allowlist |
| Lộ dữ liệu | RBAC, encryption, masking, retention |
| Chi phí tăng | Model routing, cache, giới hạn token, dashboard |
| Độ trễ cao | WebSocket, Redis, timeout và fallback queue |

## 13. Acceptance Criteria
- Member đăng bình luận bình thường và thấy xuất hiện ≤ 3 giây.
- Nội dung vi phạm rule rõ ràng được giữ và hiển thị lý do.
- Nội dung nguy cơ cao xuất hiện trong admin queue với policy, confidence và evidence.
- FAQ có link/source.
- Admin quyết định và audit log được lưu.
- Không có API key trong repo và `.env` đã bị ignore.
