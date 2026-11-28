# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Số in từ `python evidence/survey/count_survey.py evidence/survey/raw-ketqua.csv` (bản gốc không commit), bản ẩn danh: `evidence/survey/results.csv`. Cập nhật 08:25 Thứ Bảy 28/11.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☐ không làm — nhóm không có bản xuất nhóm chat lớp đã ẩn danh | — |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ chưa làm kịp trước CP3 | `evidence/interviews/` (kịch bản: `GUIDE.md`) |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ n = 27 | `evidence/survey/` (form: `tao_form.gs`, câu hỏi: `questions.md`, kết quả ẩn danh: `results.csv`) |

**Hai đợt thu:** 12 phiếu tối 27/11 (18:05–18:40, thêm 1 phiếu lúc 01:05) và 15 phiếu sáng 28/11 (08:11–08:20, vào liên tiếp trong 8 phút). Theo nhóm, cả 27 phiếu do người thật ngoài nhóm điền. Số tách riêng đợt tối 27/11 (12 phiếu) để đối chiếu: 10/12 đã phải tra trong tuần · trung vị ≈10 phút · 3/12 từng nộp sai.

## 2. Số chính

- Đào data: không làm.
- Phỏng vấn: chưa có buổi nào.
- Khảo sát **n = 27** (vai: thành viên khác 15 · người giữ repo 6 · đội trưởng 6):
  - Đã phải tra / hỏi lại ≥1 luật nộp bài trong 1 tuần qua (câu 2): **23/27 (85%)** — theo vai: thành viên khác 13/15 · người giữ repo 5/6 · đội trưởng 5/6.
  - Lần gần nhất mất (câu 5, 22 người trả lời): trung vị ≈ **10 phút** (lấy giữa khoảng) · ≥5 phút: 15/22 (68%).
  - Lần đó phải mở ≥2 file hoặc hỏi ≥2 người (câu 6): **20/23 (87%)**.
  - Cách đã làm (câu 4, chọn nhiều): lục README / guide / rubric 17 · hỏi ChatGPT / AI khác 10 · hỏi bạn cùng nhóm 10 · hỏi nhóm chat lớp 7 · đoán rồi làm 4 · hỏi lab coach / TA 4.
  - Số lần tra / tuần (câu 7, n = 26): trung vị 3 · TB 4,4 · ≤1 lần: 4 · 2–4 lần: 15 · ≥5 lần: 7.
  - Từng nộp sai / sửa nhầm vì hiểu sai luật (câu 8): **11/27 (41%)**.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | *(chưa phỏng vấn)* | | | | |
| P2 | | | | | |
| P3 | | | | | |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Có: nộp nhầm link trên LMS." — phiếu #8, câu 8 (đội trưởng)
2. "Tạo sao nộp đúng theo RUBRIC nhưng vẫn ko được điểm" — phiếu #5, câu 3 (người giữ repo)
3. "Yêu cầu về checkpoint 2 cần làm gì?" — phiếu #8, câu 3 (đội trưởng)
4. "Có — Từng sửa code sau mốc quy định mà không chắc có được phép không." — phiếu #15, câu 8 (người giữ repo)
5. "Có — Nhóm từng push nhầm branch nên phải sửa lại." — phiếu #17, câu 8 (đội trưởng)
6. "Đọc luật bài lab và xem xem các file cần Submit là những gì?" — phiếu #6, câu 3 (thành viên khác)
7. *(ngược giả thuyết)* "Tôi luôn tuân thủ đúng quy tắc và đọc hướng dẫn đầy đủ nên ko cần" — phiếu #4, câu 3 (đội trưởng, chưa bao giờ phải tra)
8. *(ngược giả thuyết)* "không-vì tìm hiểu kĩ về luật rồi mới nộp" — phiếu #12, câu 8 (thành viên khác)

## 4. Các nguồn có khớp nhau không

Mới có một nguồn (khảo sát) nên chưa đối chiếu chéo được; phỏng vấn chưa làm kịp. Trong khảo sát, hai đợt thu cho cùng hướng (đợt tối 27/11: 10/12 đã phải tra; cả hai đợt: 23/27). Khảo sát gợi ra hai điều cần kiểm thêm: (a) thành viên thường cũng phải tra (13/15), không chỉ người giữ repo — người dùng có thể rộng hơn lát cắt; (b) 11/27 từng nộp sai và 4/27 "đoán rồi làm" — pain nằm cả ở *làm sai mà không biết*, không chỉ *mất thời gian tra*.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng** — 23/27 (85%) đã phải tra trong tuần (ngưỡng ≥60%), trung vị ≈10 phút (ngưỡng ≥5 phút). Điều vẫn chưa biết: phỏng vấn chưa làm nên chưa nghe được một lần tra cụ thể từ đầu đến cuối; chưa rõ người dùng chính nên mở rộng từ "người giữ repo" sang mọi thành viên không; số lần / tuần khá phân tán (0 đến 20).
