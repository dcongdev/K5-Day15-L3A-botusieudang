# Reflection — Lê Quang Huy

> Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng. Mục 1 ghi sẵn theo phần có tên mình trong repo (`TEAMS.md`, `docs/ai-usage.md`) — **tự đọc lại, sửa nếu sai**. Mục 2–3: nháp do Claude soạn từ dữ liệu repo, người viết đã đọc và sửa (khai ở `docs/ai-usage.md`).

1. Vai trò + phần mình làm (trỏ tới file / commit):
   Thành viên, phụ trách bằng chứng pain. Soạn form khảo sát (`evidence/survey/questions.md`, `tao_form.gs`), gửi học viên L3A ngoài nhóm, ẩn danh và đếm 27 phiếu bằng `evidence/survey/count_survey.py` → `evidence/survey/results.csv`; người hỏi ở 3 phỏng vấn `evidence/interviews/P1.md`–`P3.md`; tổng hợp `evidence/summary.md`. Chuyển 10 câu hỏi thật trong khảo sát thành câu thử `nguoi_dung` B21–B30 (`eval/benchmark.csv`). Chạy lượt 1, lượt 2 và mô phỏng trên máy mình (`eval/run-1.csv`, `eval/run-2.csv`, `cost/simulate-1.csv`), chấm lượt 1, quay video demo. Commit trên nhánh `lequanghuy` (máy dùng tên git Nguyễn Khôi Nguyên).

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
   Mình dùng Claude để viết `evidence/survey/tao_form.gs`, `count_survey.py` và kịch bản phỏng vấn `evidence/interviews/GUIDE.md`; số khảo sát mình kiểm tay 5 phiếu đầu so với số script in ra (khớp 5/5). Ở lượt 1, Claude đọc 30 output và gợi ý 1/0 kèm lý do; lúc đầu mình đánh cả 30 câu là 1, đọc lại thì phải sửa vì B14 trả lời trống không thể là đạt. Phần sửa `codebase/agent.py` trước lượt 2 do Claude viết; mình chạy lượt 2 và ghi lại ở `spec.md` §10. Claude từ chối viết số liệu khảo sát hay phỏng vấn giả, nên nhóm phải đi lấy dữ liệu thật.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
   B14 ("run-try.csv có cần commit không?"): ở lượt 1 người dùng nhận câu trả lời trống dù hệ thống đã tra đúng đoạn. Nguyên nhân là model ghi tên trường JSON thành `tra_li`, còn code chỉ đọc `tra_loi`. Sau khi sửa code, lượt 2 hết trống nhưng vẫn thiếu ý "run-N phải commit". Mình học được rằng lỗi có thể nằm ở code của nhóm chứ không phải ở model, và chấm phải đọc đúng output so với tiêu chí, không chấm theo cảm giác "trông có vẻ ổn".
