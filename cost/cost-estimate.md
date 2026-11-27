# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu — `it_tra` 12% · 4 phiên / tháng · 1 lượt; `tra_vua` 38% · 12 · 2; `tra_nhieu` 50% · 51 · 3. Nguồn: tỉ lệ và số phiên từ khảo sát câu 7 (n = 8, số tạm 27/11 — `python evidence/survey/count_survey.py`); số lượt / phiên *(tự ước tính)*.
- **Số người dùng thật** 3 kịch bản: thấp 140 · cơ sở 175 · cao 700. Nguồn: lớp L3 hơn 700 học viên (README hackathon, cần kiểm lại) ÷ 5 / ÷ 4 người mỗi nhóm; cao = mọi học viên L3 cùng dùng *(tự ước tính)*.
- **Giá** 3 mức model (giá gói trả phí, USD / 1M token vào · ra): gpt-5.4-nano 0,20 · 1,25 ([OpenAI](https://developers.openai.com/api/docs/models/gpt-5.4-nano), xem 27/11/2026) · gemini-3.1-flash-lite 0,25 · 1,50 ([Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/), xem 27/11/2026) · gpt-5.4-mini 0,75 · 4,50 (bảng giá OpenAI, xem 27/11/2026). Đối chiếu với `further-reading/model-prices.md` của repo đề.
- **Tỉ lệ đạt** dùng để tính: ____/____ (__%) — lượt `run-2` (lượt 2) → `python run.py simulate --rate-from eval/run-2.csv`
- Đo token trên model ____ (MODEL_NAME trong `.env`), tính giá model gpt-5.4-nano, gemini-3.1-flash-lite và gpt-5.4-mini. Mỗi câu hỏi = 1 lần gọi model (workflow cố định), ngữ cảnh ≤ 8 đoạn luật.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-__.csv` · run ID __ · __ phiên · seed __

*(dán bảng từ `cost/simulate-N-summary.md`)*

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): __
- Chi phí / người / tháng (cơ sở, model __): __
- **Kết luận một dòng — đáng làm không:** __

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
