# Kế hoạch CP2 → CP4 — botusieudang (việc còn lại, ai làm, xong khi nào)

> Bản chạy thử, metric, 20 câu thử, spec, data card đã có. Phần dưới đây là việc **cần người thật làm** (số khảo sát, phỏng vấn, lượt chạy model thật, chấm pass). Không điền số đoán vào chỗ `____`.

## CP2 — 19:30 Thứ Sáu 27/11

| Việc | Ai | Lệnh / file |
|---|---|---|
| Đọc lại `eval/metric_spec.yaml` + `spec.md` §7 — **sau 19:30 không sửa nữa** | Hải Anh, Công | — |
| Gửi form khảo sát (link vào nhóm chat L3A + nhờ lab coach chuyển), ghi giờ mở vào `evidence/survey/questions.md` | Huy | — |
| Hẹn 3 người giữ repo nhóm khác, ghi vai + giờ vào bảng "Lịch hẹn" cuối `evidence/summary.md` | Huy | `evidence/interviews/GUIDE.md` |
| Nếu kịp có ≥ vài phiếu: điền "số đầu tiên + 1 trích dẫn" vào `canvas.md` dòng 4 | Huy | `python evidence/survey/count_survey.py` |
| `python run.py check` không báo gì ngoài dòng "≥1/3 câu từ người dùng" → merge vào `main` | Công (đội trưởng) | `python run.py check` |

## Tối Thứ Sáu — nối model (trước khi ngủ)

1. (Nguyên) `copy .env.example .env` (Windows) / `cp .env.example .env`, điền `MODEL_PROVIDER`, `MODEL_NAME`, `API_KEY`. **Không commit `.env`.**
2. `python run.py` → hỏi 1 câu → thấy câu trả lời thật + token > 0.
3. `python run.py eval --try 5` → Công + Hải Anh chấm độc lập 5 output theo metric spec → ghi số khớp vào `eval/README.md` mục 3.
4. `MODEL_NAME` phải có giá trong `cost/personas.yaml` mục `prices` (đúng tên). Thiếu thì thêm, có link + ngày xem.

## CP3 — 10:00 Thứ Bảy 28/11

| Việc | Ai | Lệnh / file |
|---|---|---|
| Chốt khảo sát (n ≥ 20 ngoài nhóm), ẩn danh → `evidence/survey/results.csv`, chạy script | Huy | `python evidence/survey/count_survey.py` |
| **Đã có B21–B26 (6 câu thật).** Chọn thêm **≥4 câu thật** trong `evidence/survey/benchmark-candidates.csv` (phiếu mới) hoặc từ phỏng vấn, viết `expected` + `pass_criterion` **từ `data/nguon/`** (không nhìn output bot), thêm vào `eval/benchmark.csv` id B21… (tổng ≤30, ≥1/3 `nguoi_dung`) | Hải Anh + Huy | `python run.py check` |
| Phỏng vấn ≥3 người → `P1.md`–`P3.md`; điền `evidence/summary.md` (số chính, ≥5 trích dẫn, kết luận giả thuyết) | Huy | — |
| Điền số thật vào `spec.md` §1 + §2 (thay các thừa số *(tự ước tính)*), `cost/personas.yaml` (share từ câu 7) | Huy, Công | — |
| **Lượt 1:** `python run.py eval` → `eval/run-1.csv` + `traces/run-1.jsonl` | Nguyên | `--wait 4` nếu gói miễn phí |
| Chấm lượt 1: `python eval/cham_nguon.py eval/run-1.csv` → điền cột `pass` (1/0), `ghi_chu` → `python run.py score eval/run-1.csv` | Hải Anh | không sửa cột khác |
| `python run.py simulate --try` (10 phiên) | Công | — |
| Commit `eval/run-1.csv`, `traces/run-1.jsonl`, `evidence/`, `spec.md` §0–§7 → push, merge `main` | Nguyên, Công | — |

## CP4 — 14:30 Thứ Bảy 28/11

| Việc | Ai | Lệnh / file |
|---|---|---|
| `eval/report.md` mục 1–2: gom lỗi lượt 1 thành nhóm có tên, ≥3 lỗi cụ thể | Hải Anh | trace: `traces/run-1.jsonl` |
| **Một lần cải tiến** nhắm nhóm lỗi đau nhất (vd sửa `SYSTEM`, `SYN`, `K` trong `codebase/`), ghi `spec.md` §10 | Nguyên | **không** sửa `data/nguon/`, metric, chuẩn đạt, câu thử |
| **Lượt 2:** `python run.py eval` → `run-2.csv`, chấm như lượt 1, điền `eval/report.md` mục 3–4, `eval/README.md` mục 5–6, `spec.md` §7 | Nguyên, Hải Anh | — |
| `python run.py simulate --rate-from eval/run-2.csv` → chép bảng `cost/simulate-N-summary.md` vào `cost/cost-estimate.md`, điền `spec.md` §8 | Công | — |
| Slide theo `slides/outline.md` → `demo-slides.pdf` ở thư mục gốc · quay video dự phòng, dán link vào README mục 7 | Công + cả nhóm | — |
| *(bonus)* 2–3 người ngoài nhóm dùng thử → `validation/log.md` | Huy | — |
| Kiểm cuối: tải ZIP repo về thư mục mới, chạy "Chạy trong 3 phút"; `git status` không có `.env` | Nguyên | — |

## Sau CP4 — đến 23:59 Thứ Bảy 28/11

- Mỗi người: `reflection/<ten-khong-dau>.md` (chép `reflection/TEMPLATE.md`).
- Sửa theo góp ý → ghi bảng "Sau CP4" trong `spec.md` §10. Không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả lượt đã chạy.
