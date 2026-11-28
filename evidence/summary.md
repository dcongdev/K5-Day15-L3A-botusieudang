# Tổng hợp bằng chứng pain

Điền ở guide bước 1.2, xong trước *CP3 10:00 Thứ Bảy 28/11* (cập nhật bổ sung P2, P3 cho CP4). Chấm ở rubric R1.

Số in từ `python evidence/survey/count_survey.py evidence/survey/raw-ketqua.csv` (bản gốc không commit), bản ẩn danh: `evidence/survey/results.csv`. Cập nhật khảo sát 08:25 và phỏng vấn 11:20 Thứ Bảy 28/11.

## 1. Nguồn đã dùng

| *Nguồn* | *Đạt ngưỡng?* | *File* |
| ----- | ----- | ----- |
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☐ không làm — nhóm không có bản xuất nhóm chat lớp đã ẩn danh | — |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☑ 3/3 (P1 nhắn tin 09:10; P2, P3 qua Google Form 10:32–10:36 ngày 28/11) | `evidence/interviews/P1.md`, `P2.md`, `P3.md` (kịch bản: `GUIDE.md`) |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ n = 27 | `evidence/survey/` (form: `tao_form.gs`, câu hỏi: `questions.md`, kết quả ẩn danh: `results.csv`) |

*Hai đợt thu:* 12 phiếu tối 27/11 (18:05–18:40, thêm 1 phiếu lúc 01:05) và 15 phiếu sáng 28/11 (08:11–08:20, vào liên tiếp trong 8 phút). Theo nhóm, cả 27 phiếu do người thật ngoài nhóm điền. Số tách riêng đợt tối 27/11 (12 phiếu) để đối chiếu: 10/12 đã phải tra trong tuần · trung vị ≈10 phút · 3/12 từng nộp sai.

## 2. Số chính

- Đào data: không làm.
- Phỏng vấn: **3 người** thuộc lớp L3A, đều ngoài nhóm (1 đội trưởng / người trực tiếp commit là P3; 2 thành viên thường là P1, P2). Cả **3/3** đều phải tra luật nộp bài (P1: 4 lần/tuần, mất ≈40 phút; P2: mỗi lần làm bài lab, mất ≈5 phút; P3: 2 lần/2 CP, mất ≈2 phút). Chưa ai từng nộp sai.
- Khảo sát **n = 27** (vai: thành viên khác 15 · người giữ repo 6 · đội trưởng 6):
  - Đã phải tra / hỏi lại ≥1 luật nộp bài trong 1 tuần qua (câu 2): **23/27 (85%)** — theo vai: thành viên khác 13/15 · người giữ repo 5/6 · đội trưởng 5/6.
  - Lần gần nhất mất (câu 5, 22 người trả lời): trung vị ≈ **10 phút** (lấy giữa khoảng) · ≥5 phút: 15/22 (68%).
  - Lần đó phải mở ≥2 file hoặc hỏi ≥2 người (câu 6): **20/23 (87%)**.
  - Cách đã làm (câu 4, chọn nhiều): lục README / guide / rubric 17 · hỏi ChatGPT / AI khác 10 · hỏi bạn cùng nhóm 10 · hỏi nhóm chat lớp 7 · đoán rồi làm 4 · hỏi lab coach / TA 4.
  - Số lần tra / tuần (câu 7, n = 26): trung vị 3 · TB 4,4 · ≤1 lần: 4 · 2–4 lần: 15 · ≥5 lần: 7.
  - Từng nộp sai / sửa nhầm vì hiểu sai luật (câu 8): **11/27 (41%)**.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | *Vai* | *Gặp pain?* | *Số lần / 1 tháng qua* | *Lần gần nhất mất* | *Đang xoay xở bằng* |
| ----- | ----- | ----- | ----- | ----- | ----- |
| P1 | Thành viên (nhóm trưởng nộp bài) | Có | 4 lần / 1 tuần qua | ≈40 phút tự đọc README / hướng dẫn rồi bỏ cuộc, hỏi lab coach | Hỏi thẳng lab coach khi sắp hết giờ |
| P2 | Thành viên nhóm Tứ Bất Tử (làm form, slide, hỗ trợ CP3) | Có | Mỗi lần làm bài lab | ≈5 phút (hỏi AI) | Hỏi AI vì thấy hiệu quả để tra cứu |
| P3 | Đội trưởng / người commit nhóm COLOR | Có | 2 lần (khi nộp 2 CP) | ≈2 phút (hỏi AI) | Dùng AI vì chưa biết có cách nào tốt hơn không |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Có: nộp nhầm link trên LMS." — phiếu #8, câu 8 (đội trưởng)
2. "Tạo sao nộp đúng theo RUBRIC nhưng vẫn ko được điểm" — phiếu #5, câu 3 (người giữ repo)
3. "Yêu cầu về checkpoint 2 cần làm gì?" — phiếu #8, câu 3 (đội trưởng)
4. "Có — Từng sửa code sau mốc quy định mà không chắc có được phép không." — phiếu #15, câu 8 (người giữ repo)
5. "Có — Nhóm từng push nhầm branch nên phải sửa lại." — phiếu #17, câu 8 (đội trưởng)
6. "Đọc luật bài lab và xem xem các file cần Submit là những gì?" — phiếu #6, câu 3 (thành viên khác)
7. *(ngược giả thuyết)* "Tôi luôn tuân thủ đúng quy tắc và đọc hướng dẫn đầy đủ nên ko cần" — phiếu #4, câu 3 (đội trưởng, chưa bao giờ phải tra)
8. *(ngược giả thuyết)* "không-vì tìm hiểu kĩ về luật rồi mới nộp" — phiếu #12, câu 8 (thành viên khác)
9. "Đọc hết các file readme và hướng dẫn, khoảng 40 phút bỏ cuộc rồi mới hỏi labcoach." — P1 (thành viên)
10. "Cứ hỏi thẳng labcoach khi sắp hết giờ cho họ hướng dẫn nộp là được." — P1 (thành viên)
11. "Là hôm nay khi có bạn nhờ mình làm phụ CP3. Mình cần biết CP3 cần nộp những file nào." — P2 (thành viên)
12. "Mình vẫn hỏi AI. Vì AI vẫn hiệu quả để tra cứu." — P2 (thành viên)
13. "Lần gần nhất là sáng nay, khi đó tôi rất cần biết phải hoàn thành những gì, có những yêu cầu gì cho từng mục." — P3 (đội trưởng)
14. "Giờ tôi vẫn dùng AI vì tôi k biết có cách nào tốt hơn không." — P3 (đội trưởng)

## 4. Các nguồn có khớp nhau không

Cả hai nguồn (khảo sát `n = 27` và phỏng vấn `3/3`) đều **khớp hướng**:
- **Tần suất & đối tượng:** Cả 3/3 người phỏng vấn đều phải tra luật nộp bài (khớp khảo sát 23/27 = 85%), trong đó có cả đội trưởng trực tiếp commit (P3) lẫn thành viên thường hỗ trợ làm bài (P1, P2 — khớp khảo sát 13/15 thành viên thường cũng phải tra).
- **Cách xoay xở:** Phỏng vấn cho thấy đúng hai nhánh hành vi phổ biến nhất trong khảo sát: P1 tự đọc README/hướng dẫn mất ≈40 phút rồi bỏ cuộc đi hỏi lab coach (khớp 17/27 lục tài liệu, 4/27 hỏi lab coach); trong khi P2 (≈5 phút) và P3 (≈2 phút) chọn hỏi AI để tra nhanh hơn (khớp 10/27 hỏi ChatGPT/AI khác).
- **Điểm lệch & gợi ý sản phẩm:** Cả 3/3 người phỏng vấn đều chưa từng nộp sai (khảo sát: 11/27 từng sai), một phần vì P1 chịu tốn thời gian hỏi lại cho chắc, còn P2 và P3 đã dùng AI hỗ trợ. Tuy nhiên, việc P2 và P3 dùng AI chung chung (không khóa nguồn theo từng file/dòng luật của repo đề) cho thấy sản phẩm của nhóm cần tạo giá trị rõ ràng hơn AI đại trà ở chỗ: **trả lời nhanh hơn (<1 phút), trích đúng nguồn `file:dòng` để kiểm chứng ngay, và từ chối trung thực khi luật không quy định** thay vì bịa câu trả lời.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng** — đạt cả hai nguồn bằng chứng (khảo sát `n = 27`: 85% đã phải tra trong tuần, vượt ngưỡng ≥60%; trung vị ≈10 phút, vượt ngưỡng ≥5 phút; và 3/3 phỏng vấn đều xác nhận nhu cầu tra luật nộp bài cho cả đội trưởng lẫn thành viên).

Điều vẫn cần theo dõi: số lần tra / tuần khá phân tán (0 đến 20); người dùng thực tế rộng hơn lát cắt ban đầu (gồm cả thành viên thường chứ không chỉ đội trưởng/người giữ repo); và với nhóm đã quen hỏi AI chung (như P2, P3), trợ lý cần chứng minh độ tin cậy vượt trội nhờ trích nguồn chính xác và chống bịa.
