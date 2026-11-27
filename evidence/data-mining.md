# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Không đào data thì xoá file này. Script / công thức đếm để trong repo (vd `evidence/count.py` hoặc ghi công thức Sheets ngay dưới), người khác chạy lại phải ra cùng số.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## 1. Cách đếm — viết TRƯỚC khi chạy

> **Chỉ làm nếu lấy được bản xuất nhóm chat lớp L3A** (nguồn kiểm lại, không phải nguồn chính — `evidence/hypothesis.md`). Không lấy được thì **xoá file này** trước CP3.

- Data dùng: bản xuất tin nhắn nhóm chat lớp L3A từ 25/11/2026 00:00 đến 27/11/2026 23:59, **đã thay tên người gửi bằng mã U1, U2…** trước khi đọc (bản gốc không commit).
- Đếm gì: số tin nhắn **hỏi** về luật / hạn / format nộp bài hackathon · trên tập nào: mọi tin nhắn có dấu "?" hoặc bắt đầu bằng "cho mình hỏi / ai biết / có được / phải … không" · lọc gì: bỏ tin của BTC / lab coach, bỏ tin hỏi về nội dung bài học (không phải luật nộp).
- **Mẫu số là gì:** tổng số tin nhắn *hỏi* (mọi chủ đề) trong cùng khoảng thời gian, cùng bộ lọc người gửi. Đếm thêm: số người hỏi khác nhau / số người từng nhắn trong nhóm.
- Script / công thức: gắn nhãn tay trên Google Sheets (cột `la_cau_hoi` 1/0, `ve_luat_nop` 1/0) → `=COUNTIFS(la_cau_hoi,1,ve_luat_nop,1) / COUNTIF(la_cau_hoi,1)`. Người thứ hai gắn nhãn lại 20 dòng ngẫu nhiên để kiểm.

## 2. Đọc trước, đếm sau

Đã đọc __ dòng đầu và từ điển cột. Các *kiểu* hành vi thấy được (trước khi định nghĩa thứ cần đếm):
- __
- __

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| | | | |
| | | | |

Ghi dạng "x/N (y%)". "Nhiều bạn…" không phải số.

## 4. ≥5 ví dụ cụ thể (mã dòng / mã đã ẩn danh, không đoán ai là ai)

1.
2.
3.
4.
5.

## 5. Giới hạn của data

Data cho biết người ta **làm gì**, không cho biết **vì sao**. Thiếu gì, lệch về phía nào: __
→ Kiểm lại bằng phỏng vấn / khảo sát nào: __
