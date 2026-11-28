# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu — `it_tra` 15% · 4 phiên / tháng · 1 lượt; `tra_vua` 58% · 12 · 2; `tra_nhieu` 27% · 39 · 3. Nguồn: tỉ lệ và số phiên từ khảo sát câu 7 (n = 26, 28/11 — `python evidence/survey/count_survey.py`); số lượt / phiên *(tự ước tính)*.
- **Số người dùng thật** 3 kịch bản: thấp 140 · cơ sở 175 · cao 700. Nguồn: lớp L3 hơn 700 học viên (README hackathon, cần kiểm lại) ÷ 5 / ÷ 4 người mỗi nhóm; cao = mọi học viên L3 cùng dùng *(tự ước tính)*.
- **Giá** 3 mức model (giá gói trả phí, USD / 1M token vào · ra): gpt-5.4-nano 0,20 · 1,25 ([OpenAI](https://developers.openai.com/api/docs/models/gpt-5.4-nano), xem 27/11/2026) · gemini-3.1-flash-lite 0,25 · 1,50 ([Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/), xem 27/11/2026) · gpt-5.4-mini 0,75 · 4,50 (bảng giá OpenAI, xem 27/11/2026). Đối chiếu với `further-reading/model-prices.md` của repo đề.
- **Tỉ lệ đạt** dùng để tính: ____/____ (__%) — lượt `run-2` (lượt 2) → `python run.py simulate --rate-from eval/run-2.csv`
- Đo token trên model **gemini-3.1-flash-lite** (MODEL_NAME trong `.env`; thử 27/11: ~1.400–1.900 token vào, ~100 token ra mỗi câu), tính giá model gpt-5.4-nano, gemini-3.1-flash-lite và gpt-5.4-mini. Mỗi câu hỏi = 1 lần gọi model (workflow cố định), ngữ cảnh ≤ 8 đoạn luật.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-[N].csv` · run ID [__] · 50 phiên · seed 42 · tỉ lệ đạt lấy từ `eval/run-2.csv`: [__/__ = __%]

Lệnh (sau khi lượt 2 chấm xong): `python run.py simulate --rate-from eval/run-2.csv --wait 4` → chép bảng từ `cost/simulate-[N]-summary.md` vào đây.

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (140) | / tháng — cơ sở (175) | / tháng — cao (700) | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| gpt-5.4-nano | [$] | [$] | [$] | [$] | [$] | [$] |
| gemini-3.1-flash-lite *(model đo token)* | [$] | [$] | [$] | [$] | [$] | [$] |
| gpt-5.4-mini | [$] | [$] | [$] | [$] | [$] | [$] |

*Lượt THỬ 10 phiên (27/11 19:05, `simulate --try`, chưa có tỉ lệ đạt, 1/10 phiên lỗi timeout — không phải số nộp):* chi phí / phiên gpt-5.4-nano $0,00085 · gemini-3.1-flash-lite $0,0010 · gpt-5.4-mini $0,0031; tháng cơ sở $6,28 · $7,77 · $23,30. Token / phiên: it_tra ~1.800 vào / 82 ra · tra_vua ~2.830 / 211 · tra_nhieu ~4.580 / 267.

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): 12 lần × 10 phút = **120 phút** *(khảo sát câu 7 n = 26, câu 5 n = 22)*
- Chi phí / người / tháng (cơ sở, model gemini-3.1-flash-lite): **[$__]** *(thử 10 phiên: ≈ $0,044)* · chi phí / task thành công: [$__]
- **Kết luận một dòng — đáng làm không:** [đáng / không đáng] — [$__] / người / tháng để tiết kiệm ~120 phút tra tay và giảm rủi ro nộp sai (11/27 từng nộp sai).

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
