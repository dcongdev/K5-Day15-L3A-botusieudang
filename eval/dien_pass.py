"""Điền cột pass và ghi_chu vào file lượt từ một file text — nhóm botusieudang viết.

    python eval/dien_pass.py eval/run-1.csv eval/pass-run-1.txt

File text: mỗi dòng "<id> <1 hoặc 0> <ghi chú tuỳ ý>", vd:
    B01 1
    B14 0 trả lời rỗng
Dòng bắt đầu bằng # hoặc chưa điền 1/0 thì bỏ qua. Script CHỈ ghi 2 cột pass, ghi_chu — giữ nguyên mọi cột khác
(không mở file lượt bằng Excel: Excel làm hỏng dấu và định dạng → run.py score báo file bị sửa).
"""
import csv
import sys


def main(run_path, txt_path):
    marks = {}
    with open(txt_path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()  # phần sau # là chú thích, không chép vào ghi_chu
            if not line:
                continue
            parts = line.split(None, 2)
            if len(parts) < 2 or parts[1] not in ("0", "1"):
                continue
            marks[parts[0]] = (parts[1], parts[2] if len(parts) > 2 else "")
    with open(run_path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    for col in ("pass", "ghi_chu"):
        if col not in fields:
            sys.exit("File lượt thiếu cột %s" % col)
    done = 0
    for r in rows:
        if r["id"] in marks:
            r["pass"], r["ghi_chu"] = marks[r["id"]]
            done += 1
    with open(run_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    missing = [r["id"] for r in rows if r["pass"] == ""]
    print("Đã điền %d câu vào %s. Còn trống: %s" % (done, run_path, ", ".join(missing) or "không"))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Cách dùng: python eval/dien_pass.py eval/run-N.csv eval/pass-run-N.txt")
    main(sys.argv[1], sys.argv[2])
