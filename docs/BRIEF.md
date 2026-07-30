# BRIEF – 1 TRANG

## Community Channel Agent – AI quản lý cộng đồng / kênh

**Mã đề tài:** CHAT-10  
**Loại hệ thống:** AI Agent + Human-in-the-loop  
**Vai trò:** Member và Admin

### 1. Thực trạng
Các kênh broadcast và cộng đồng của doanh nghiệp có lượng bài viết, bình luận và câu hỏi lớn. Admin phải duyệt nội dung, trả lời các câu hỏi lặp lại, giữ trật tự và duy trì nhịp tương tác nên dễ quá tải.

### 2. Vấn đề
- Phản hồi chậm hoặc không nhất quán.
- Khó phát hiện sớm spam, công kích, lộ thông tin cá nhân hoặc xung đột leo thang.
- Admin mất thời gian cho FAQ và tác vụ lặp lại.
- Rule tĩnh không hiểu đủ ngữ cảnh, nhưng để LLM tự quyết hoàn toàn lại thiếu an toàn.

### 3. Giải pháp
Xây dựng Agent điều phối pipeline:
1. Kiểm tra quyền, spam, rate limit và rule.
2. Moderation API đánh giá nhóm rủi ro.
3. LLM phân tích intent/ngữ cảnh cho trường hợp mơ hồ.
4. RAG truy xuất FAQ, nội quy và lịch sự kiện.
5. Agent chọn: cho đăng, gợi ý sửa, trả lời FAQ, đưa vào hàng đợi hoặc escalates.
6. Admin duyệt quyết định nhạy cảm; mọi hành động được ghi audit log.

### 4. Người dùng
- **Member:** cần môi trường an toàn, phản hồi nhanh và có quyền appeal.
- **Admin:** cần giảm việc lặp lại, ưu tiên đúng nội dung nguy cơ và theo dõi sức khỏe kênh.

### 5. Phạm vi MVP
- Đăng nhập và RBAC cho Member/Admin.
- Duyệt bài/bình luận theo rule + moderation.
- Trả lời FAQ có nguồn và chào thành viên mới.
- Hàng đợi admin và appeal.
- Lập lịch đăng nội dung cơ bản.
- Dashboard số lượng nội dung, escalations, latency và chi phí.

### 6. Ngoài phạm vi MVP
- Tự động cấm thành viên vĩnh viễn.
- Tự xử lý khủng hoảng truyền thông.
- Phân tích tâm lý cá nhân hoặc lưu hồ sơ nhạy cảm dài hạn.
- Tự xuất bản nội dung quan trọng khi chưa có admin duyệt.

### 7. Giá trị
Giảm tải admin, tăng tốc độ phản hồi, giữ quy tắc nhất quán và vẫn bảo đảm con người giữ quyền quyết định cuối trong trường hợp nhạy cảm.

### 8. Chỉ số thành công
- P95 phản hồi nội dung thường ≤ 3 giây.
- ≥ 40% câu hỏi lặp lại được xử lý bằng FAQ.
- 100% nội dung nguy cơ cao được đưa vào hàng đợi HITL.
- False positive moderation mục tiêu ≤ 5% trong pilot.
- ≥ 80% admin đánh giá hàng đợi giúp ưu tiên công việc tốt hơn.
