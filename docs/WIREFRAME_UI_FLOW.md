# WIREFRAME & UI FLOW

## Màn hình
1. **Đăng nhập & vai trò:** email/OTP, Member/Admin.
2. **Bảng tin:** đọc bài, bình luận, hỏi FAQ.
3. **Cảnh báo moderation:** lý do, rule, sửa hoặc appeal.
4. **Admin queue:** risk, confidence, evidence và hành động.
5. **Dashboard:** auto-handled, queue, latency, cost.
6. **Lịch nội dung:** lịch đăng và gợi ý cần duyệt.

## Luồng chính
`Đăng nhập → Tạo/đọc nội dung → Rule + Moderation → LLM/RAG nếu cần → Allow/Reply/Hold/Escalate → Admin duyệt → Ghi audit`

## Nhánh FAQ
`Câu hỏi → Intent detection → Retrieve FAQ/rule → Trả lời có nguồn → Feedback`

## Nhánh moderation
`Nội dung → Rule → Moderation API → LLM context → Action policy → Soft warning hoặc Admin Queue`

Xem bản vẽ tại [WIREFRAME_UI_FLOW.png](./WIREFRAME_UI_FLOW.png).
