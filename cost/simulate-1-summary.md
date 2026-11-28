# Tóm tắt mô phỏng simulate-1@20261128-095227

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| it_tra | 5 | 1 | 1659 | 84 | 1.0 | 1.0 |
| tra_vua | 32 | 2 | 3070 | 200 | 2.0 | 2.0 |
| tra_nhieu | 13 | 3 | 4586 | 294 | 3.0 | 3.0 |

Tỉ lệ đạt dùng để tính: 25/30 (83%) — lượt run-2@20261128-094339

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (140 người) | Chi phí / tháng — cơ sở (175 người) | Chi phí / tháng — cao (700 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.00093 | $0.0011 | $0.00052 | $2.77 | $3.47 | $13.87 | $0.0198 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0012 | $0.0014 | $0.00064 | $3.43 | $4.28 | $17.13 | $0.0245 |
| gpt-5.4-mini (vào 0.75 · ra 4.5 $/1M) | $0.0035 | $0.0041 | $0.0019 | $10.28 | $12.85 | $51.40 | $0.0734 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.2) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.1-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
