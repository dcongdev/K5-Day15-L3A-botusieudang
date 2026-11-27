# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude (trợ lý AI) | Viết bản đầu `codebase/tools.py` (cắt kho, BM25), `agent.py` (luồng 3 bước, kiểm nguồn), `ai.py` (nhánh openai / anthropic / gemini / ollama theo docs/connect-model.md) | Nguyên đọc từng hàm, chạy `python run.py`, `eval --try`; sửa: ____ | Nguyễn Khôi Nguyên |
| Prompt / thiết kế lời gọi mô hình | Claude | Viết bản đầu `SYSTEM` (4 loại quyết định, JSON, luật chống đổi vai) | Nguyên + Hải Anh đọc lại theo `spec.md` §5; sửa sau lượt 1 ghi ở `spec.md` §10 | Nguyễn Khôi Nguyên |
| Đào data (viết script đếm, gợi ý nhãn) | Claude | Viết `evidence/survey/count_survey.py` (đếm khảo sát) và cách đếm chat ở `evidence/data-mining.md` — **không** đọc / sinh dữ liệu khảo sát | Huy kiểm tay 5 phiếu đầu so với số script in ra, khớp ____/5 | Lê Quang Huy |
| Rà câu hỏi phỏng vấn / khảo sát | Claude | Viết kịch bản `evidence/interviews/GUIDE.md`; chỉ rà câu dẫn dắt | Huy duyệt câu hỏi trước khi hỏi | Lê Quang Huy |
| Viết câu thử (benchmark) | Claude | Viết bản đầu 20 câu `tu_viet` B01–B20 kèm `expected` từ `data/nguon/` | Hải Anh đối chiếu từng `expected` với file nguồn ghi ở cột `source`; câu `nguoi_dung` (B21…) lấy nguyên văn khảo sát, không do AI viết | Nguyễn Hải Anh |
| Metric spec | Claude | Viết bản đầu 4 metric + chuẩn "đạt" | Hải Anh + Công (đội trưởng) thống nhất trước 19:30 Thứ Sáu 27/11; người thứ hai chấm thử 5 output | Nguyễn Hải Anh |
| Sinh data `synthetic` (nếu có) | — | Không dùng | — | — |
| Chấm cột `pass` bằng LLM (nếu có) | — | Không dùng: metric 1 chấm bằng code (`eval/cham_nguon.py`), metric 2–4 người chấm | — | Nguyễn Hải Anh |
| Slide, văn bản | Claude | Khung `spec.md`, `README.md`, `data/DATA_CARD.md`, `eval/README.md`, `cost/personas.yaml` (giá model có link nguồn) | Mỗi người đọc lại mục có tên mình; giá model: Công đối chiếu lại | Cả nhóm |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
