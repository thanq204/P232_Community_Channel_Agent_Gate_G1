# AI LOG SETUP

Repo có thư mục `.ai-log/` và script `scripts/log_manual.py`.

## Nội dung mỗi log
- Ngày, người thực hiện và công cụ AI.
- Prompt/mục tiêu.
- Kết quả được dùng.
- Phần nhóm đã sửa, loại bỏ hoặc kiểm chứng.
- File áp dụng.
- Kiểm tra accuracy, policy, privacy và bảo mật.

## Không ghi
- API key, token, mật khẩu.
- Nội dung thật có thông tin định danh.
- Quyết định moderation nhạy cảm chưa ẩn danh.
- Dữ liệu thành viên dùng để lập hồ sơ cá nhân.

## Ví dụ
```bash
python scripts/log_manual.py   --user "Tên thành viên"   --tool "ChatGPT"   --goal "Thiết kế moderation pipeline"   --prompt "So sánh rule, Moderation API và LLM"   --result "Tạo kiến trúc nhiều lớp và HITL"   --changes "Bỏ auto-ban; thêm appeal và admin override"   --files "docs/PRD.md"
```

Nếu repo template P-232 đã có hook Gemini/Claude/Codex/Cursor thì giữ nguyên, không tạo cấu hình trùng.
