# Reflection — Nguyễn Khôi Nguyên

> Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng. Mục 1 ghi sẵn theo phần có tên mình trong repo (`TEAMS.md`, `docs/ai-usage.md`) — **tự đọc lại, sửa nếu sai**. Mục 2–3: nháp do Claude soạn từ dữ liệu repo, người viết đã đọc và sửa (khai ở `docs/ai-usage.md`).

1. Vai trò + phần mình làm (trỏ tới file / commit):
   Thành viên, điều phối và bản chạy thử. Phụ trách `codebase/` (`tools.py` cắt kho + BM25, `agent.py` luồng 3 bước + kiểm nguồn, `ai.py` các nhánh model), nối model thật gemini-3.1-flash-lite, chạy `eval --try`; prompt `SYSTEM` (`spec.md` §5). Người ghi ở phỏng vấn P2, P3 (`evidence/interviews/`). Commit: ____

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
   Claude viết bản đầu `codebase/tools.py` (cắt kho, BM25), `agent.py` (luồng 3 bước, kiểm nguồn), `ai.py` và prompt `SYSTEM`. Mình đọc từng hàm, chạy `python run.py` và `eval --try` để chắc model thật trả lời được; code AI viết mình không sửa (đã khai ở `docs/ai-usage.md`). Với phần nối model, mình kiểm bằng số token lớn hơn 0 trong trace để chắc không phải chế độ giả.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
   B21 ("cách nộp bài đúng quy tắc"): bot nói "điền mọi chỗ có dấu phẩy" (lượt 2 thì nói "<...>"), trong khi tài liệu ghi "điền mọi chỗ `____`". Lỗi nằm ở hàm `_clean` trong `codebase/tools.py`: hàm này xoá ký tự `_`, nên đoạn đưa cho model bị mất ký hiệu và model đoán bừa. Mình học được rằng phần "làm sạch" dữ liệu trước khi đưa cho model cũng có thể sinh ra câu trả lời sai; phải xem chính đoạn model nhận được, không chỉ xem file gốc.
