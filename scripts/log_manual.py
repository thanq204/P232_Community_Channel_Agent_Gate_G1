#!/usr/bin/env python3
"""Ghi AI log thủ công dạng Markdown. Không ghi API key hoặc dữ liệu nhạy cảm."""
from __future__ import annotations
import argparse
from datetime import datetime
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--tool", required=True)
    parser.add_argument("--goal", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--changes", default="Chưa ghi nhận")
    parser.add_argument("--files", default="Chưa ghi nhận")
    args = parser.parse_args()

    now = datetime.now()
    log_dir = Path(__file__).resolve().parents[1] / ".ai-log"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{now:%Y-%m-%d}.md"

    entry = f"""
## {now:%H:%M:%S} — {args.goal}
- Người thực hiện: {args.user}
- Công cụ AI: {args.tool}
- Prompt/mục tiêu: {args.prompt}
- Kết quả AI: {args.result}
- Nhóm đã sửa/loại bỏ: {args.changes}
- File áp dụng: {args.files}
- Kiểm tra: Không chứa API key; dữ liệu demo đã ẩn danh; kết quả cần được con người review.

"""
    with log_file.open("a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Đã ghi log: {log_file}")

if __name__ == "__main__":
    main()
