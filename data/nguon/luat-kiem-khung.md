# Luật mà lệnh `python run.py check` và `python run.py eval` tự kiểm (nhóm viết lại từ code khung)

> Nguồn: nhóm botusieudang đọc `eval/run_eval.py` (hàm `check`, `run`, hằng `NOT_A_RUN`) và `cost/simulate.py` của khung, rồi viết lại thành câu. Không phải văn bản của BTC — khi lệch với README / guide của BTC thì theo BTC.

## Bộ câu thử `eval/benchmark.csv`

- File phải có đúng 6 cột: id, input, expected, pass_criterion, type, source.
- Cột type chỉ được dùng một trong ba giá trị: thuong, kho, tu_choi.
- CP2 cần ít nhất 10 câu thử. CP3 cần từ 20 đến 30 câu thử.
- Cần ít nhất 5 câu loại kho.
- Cần ít nhất 2 câu loại tu_choi, trong đó có 2 câu tấn công.
- Cột source phải bắt đầu bằng một trong bốn mã: nguoi_dung, data_that, tu_viet, sinh_seed (có thể thêm chi tiết sau dấu hai chấm, vd "nguoi_dung: P2").
- Ít nhất 1/3 số câu thử phải có source là nguoi_dung hoặc data_that (lời người dùng hoặc data thật).
- Các cột id, input, expected, pass_criterion không được để trống; id không được trùng.
- Ô có dấu phẩy phải đặt trong ngoặc kép, nếu không dòng đó bị thừa ô.
- Còn dòng mẫu có chữ "(ví dụ)" thì phải xoá trước khi nộp.

## Metric spec `eval/metric_spec.yaml`

- Cần ít nhất 3 metric, mỗi metric điền đủ name, definition, grader, threshold (không còn mẫu <…>).

## Các file lượt chạy không được tính

- Các file eval/run-fake.csv, eval/run-try.csv, eval/run-mock.csv, eval/run-error.csv, eval/run-stopped.csv không phải một lượt đánh giá, không được đánh số, không dùng để báo cáo và đã nằm trong .gitignore (không commit).
- Lượt chạy bằng model giả (model fake, không gọi model, hoặc token = 0) chỉ ghi run-mock.csv. Lượt mà mọi câu đều lỗi chỉ ghi run-error.csv. Bấm Ctrl+C giữa chừng chỉ ghi run-stopped.csv.
- Số lượt tiếp theo = số lớn nhất đang có + 1; lượt đã xoá vẫn để lại dấu (vd có run-1 và run-3 thì lượt tiếp là run-4).

## Chấm điểm bằng `python run.py score`

- Cột pass điền 1 (đạt) hoặc 0 (không đạt); cũng nhận x, dat, đạt cho đạt và khong, không cho không đạt.
- Còn ô pass trống thì score báo "CHƯA CHẤM XONG" và không in %.
- score so cột output và token với trace trong traces/run-N.jsonl; file lượt bị sửa cột khác ngoài pass, ghi_chu thì score cảnh báo.

## Mô phỏng chi phí `python run.py simulate`

- cost/personas.yaml cần các mục sessions, seed, users, personas, prices. Bản nộp cần sessions ≥ 50.
- prices cần ít nhất 2 mức model (rẻ và mạnh). Còn chữ "(ví dụ)" trong personas.yaml thì simulate nhắc.
- Không ghi --rate-from thì simulate lấy tỉ lệ đạt từ lượt run-N mới nhất đã chấm xong, cùng model.
