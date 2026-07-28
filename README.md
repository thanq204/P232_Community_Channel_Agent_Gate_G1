# Community Channel Agent – AI quản lý cộng đồng / kênh

Dự án Gate G1 xây dựng AI Agent hỗ trợ quản trị kênh broadcast và cộng đồng: duyệt bài/bình luận, trả lời FAQ, chào thành viên mới, lập lịch nội dung và chuyển trường hợp nhạy cảm cho admin duyệt.

## Vai trò
- **Member:** xem kênh, đăng bài/bình luận, nhận trả lời FAQ, sửa hoặc appeal nội dung bị giữ.
- **Admin:** cấu hình rule, duyệt hàng đợi, quản lý FAQ/lịch nội dung, xem dashboard và audit log.

## Problem
Admin phải xử lý lượng lớn nội dung và câu hỏi lặp lại, dễ quá tải, phản hồi không nhất quán và bỏ sót hành vi vi phạm.

## Solution
Pipeline kết hợp rule tĩnh, Moderation API, LLM, RAG và Human-in-the-loop:
`Nội dung → Rule/Moderation → LLM phân loại → Truy xuất FAQ/rule → Allow/Reply/Queue/Escalate → Audit log`

## Gate G1 Deliverables
- [Brief](./docs/BRIEF.md)
- [PRD](./docs/PRD.md)
- [Wireframe & UI Flow](./docs/WIREFRAME_UI_FLOW.md)
- [Wireframe PNG](./docs/WIREFRAME_UI_FLOW.png)
- [Architecture Pipeline](./docs/ARCHITECTURE_PIPELINE.png)
- [Roadmap 6 tuần](./docs/ROADMAP_6_WEEKS.md)
- [AI Log Setup](./AI_LOG_SETUP.md)

## Công nghệ dự kiến
- GPT-4o-mini/model tương đương + Moderation API
- LangGraph, FastAPI, PostgreSQL + pgvector, Redis, WebSocket
- Next.js/React, Docker, Railway/Vercel

## Ràng buộc
- Không để Agent tự cấm thành viên hoặc xử lý khủng hoảng mà không có admin.
- Mọi quyết định có reason code, confidence và audit log.
- FAQ phải dựa trên kho tri thức có nguồn.
- Không ghi API key hoặc dữ liệu nhạy cảm vào repo/log.
