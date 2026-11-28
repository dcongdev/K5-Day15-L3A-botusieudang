# Reflection — Dương Văn Công

> Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng. Mục 1 ghi sẵn theo phần có tên mình trong repo (`TEAMS.md`, `docs/ai-usage.md`) — **tự đọc lại, sửa nếu sai**. Mục 2–3: nháp do Claude soạn từ dữ liệu repo, người viết đã đọc và sửa (khai ở `docs/ai-usage.md`).

1. Vai trò + phần mình làm (trỏ tới file / commit):
   Đội trưởng. Impact và quyết định chọn bài toán (`spec.md` §2), chi phí (`cost/personas.yaml`, `cost/cost-estimate.md`, đối chiếu giá model), slide (`demo-slides.pdf`). Đọc lại metric trước khi chốt CP2 và chấm độc lập 5 output cùng Hải Anh để kiểm metric (`eval/README.md` mục 3). Merge PR các nhánh vào `main` và nộp các checkpoint bằng mã đội trưởng. Commit: ____

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
   Claude viết khung `cost/personas.yaml` (giá model có link nguồn) và bản đầu `eval/metric_spec.yaml`. Mình đối chiếu lại giá model, và cùng Hải Anh đọc metric trước khi chốt CP2. Để kiểm metric có chấm được thật không, mình chấm độc lập 5 output với Hải Anh và khớp 5/5. Chi phí cuối lấy từ lệnh `simulate` chạy thật 50 phiên, không lấy số AI ước tính: $0,0014 mỗi task thành công.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
   B28 ("Deadline chính xác của từng checkpoint là khi nào?"): bot trả lời "tài liệu không có" ở cả hai lượt, dù SPEC-01 ghi đủ các mốc. Đây là câu người dùng hỏi nhiều nhất trong khảo sát, nên trượt câu này nguy hiểm hơn trượt câu khó. Mình học được rằng chi phí rất rẻ ($17/tháng cho cả lớp) không có nghĩa là sản phẩm đã dùng được; vì vậy kết luận của nhóm là "làm tiếp", chưa phát cho cả lớp.
