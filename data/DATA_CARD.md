# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Chấm ở rubric R4.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp.

## Dataset 1 · Kho luật nộp bài `data/nguon/`

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `search_rules` (`codebase/tools.py`) · căn cứ để viết `expected` của bộ câu thử |
| Từ đâu | 22 file = bản chép nguyên các file mẫu của `starter-repo` mà BTC phát (README, AGENTS, TEAMS, spec, canvas, docs/connect-model, docs/ai-usage, eval/README, eval/report, metric_spec.yaml, personas.yaml, cost-estimate, các TEMPLATE, gitignore…) — các file này vốn đã công khai trong repo nhóm, không phải data BTC cấp riêng. 1 file nhóm viết lại: `luat-kiem-khung.md` — luật mà `eval/run_eval.py` và `cost/simulate.py` tự kiểm (vd ≥5 câu `kho`, ≥2 câu `tu_choi`, ≥1/3 câu từ người dùng), ghi rõ là bản viết lại, không phải văn bản BTC |
| Xử lý những bước gì | Đổi tên file cho khỏi trùng (vd `eval/README.md` → `eval-README.md`) · cắt đoạn bằng code lúc chạy (`load_corpus` trong `codebase/tools.py`): mỗi dòng bảng, mỗi gạch đầu dòng, mỗi đoạn văn, mỗi khối code là 1 đoạn; dòng bảng ghép "tên cột: giá trị"; bỏ đoạn < 3 từ · đánh mã `TÊNFILE-NN` theo thứ tự trong file · không ẩn danh (không có dữ liệu cá nhân) |
| Số dòng / số đoạn | 23 file → **365 đoạn** (README 75 · SPEC 44 · CONNECT-MODEL 40 · LUAT-KIEM-KHUNG 21 · AGENTS 17 · …) — in lại bằng `python -c "import sys; sys.path.insert(0,'codebase'); from tools import load_corpus; print(len(load_corpus()))"` |
| Phiên bản / ngày lấy | `starter-repo` bản BTC phát cho K5 Day15, chép ngày 27/11/2026 |
| Nhãn | thật (tài liệu khoá) · `luat-kiem-khung.md`: nhóm tự viết lại từ code khung |
| Giới hạn | **Thiếu `02-guide.md`, `03-rubric.md` và README của repo đề** → câu hỏi về rubric chi tiết, điểm từng khối, luật chỉ có trong guide sẽ bị trả "không có". Không có thông báo mới của BTC trên nhóm chat. Mã đoạn đổi nếu file trong kho bị sửa → sau CP2 **không sửa** file trong `data/nguon/` (thêm file mới thì mã của file cũ giữ nguyên) |

## Dataset 2 · Bộ câu thử `eval/benchmark.csv`

| | |
|---|---|
| Dùng để làm gì | Chạy `python run.py eval`, chấm theo `eval/metric_spec.yaml` |
| Từ đâu | 20 câu `tu_viet` (B01–B20) nhóm viết từ Dataset 1 (4 câu B08, B15, B19, B20 lấy ý từ bản nháp nhánh `nguyenah`), mỗi câu ghi file căn cứ ở cột `source` · ~10 câu `nguoi_dung` (B21–B30, đã có B21–B26) lấy **nguyên văn** câu 3 của khảo sát (`evidence/survey/results.csv`, `source = nguoi_dung: khảo sát phiếu #N`) — thêm trước lượt 1 |
| Xử lý những bước gì | Câu khảo sát: bỏ tên người / tên nhóm nếu có, giữ nguyên cách hỏi (cả không dấu, viết tắt); `expected` viết từ đoạn trong Dataset 1, không nhìn output của bot |
| Số dòng | CP2: 20 (thuong 8 · kho 7 · tu_choi 5) · 27/11 18:55: 26 (thêm B21–B26 `nguoi_dung` từ khảo sát phiếu #1, 2, 3, 5, 6, 8) · CP3: 30 (thêm ≥4 câu `nguoi_dung` nữa) |
| Phiên bản / ngày lấy | 27/11/2026 |
| Nhãn | `tu_viet` · `nguoi_dung` |
| Giới hạn | Câu `tu_viet` do người viết spec đặt → dễ "khớp" cách tra hơn câu thật; vì vậy cần ≥1/3 câu từ người dùng. Chưa có câu hỏi nhiều lượt |

**Data `synthetic`:** không dùng.
