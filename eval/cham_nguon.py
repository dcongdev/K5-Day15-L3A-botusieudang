"""Chấm metric trich_nguon_hop_le bằng code (eval/metric_spec.yaml) — nhóm botusieudang viết.

    python eval/cham_nguon.py eval/run-1.csv

Với mỗi câu trong file lượt: tìm mọi mã đoạn dạng [TÊN-NN] trong cột output, so với tập mã thật của kho
data/nguon (cắt bằng đúng codebase/tools.py). In:
  - câu thuong không có mã hợp lệ nào  → trượt metric 1
  - mã bịa (không có trong kho) ở bất kỳ câu nào → trượt metric 1
CHỈ IN, KHÔNG SỬA file lượt. Người chấm dùng kết quả này khi điền cột pass (cùng các metric người chấm).
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "codebase"))
from tools import all_codes  # noqa: E402

CODE_RE = re.compile(r"\[([A-Z0-9]+(?:-[A-Z0-9]+)*-\d{2})\]")


def main(path):
    codes = all_codes()
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    thuong = [r for r in rows if r.get("type") == "thuong"]
    thuong_ok, bad_total = 0, 0
    print("%-5s %-8s %-6s %-6s %s" % ("id", "type", "mã ok", "mã bịa", "ghi chú"))
    for r in rows:
        found = CODE_RE.findall(r.get("output", ""))
        ok = sorted({c for c in found if c in codes})
        bad = sorted({c for c in found if c not in codes})
        bad_total += len(bad)
        notes = []
        if r.get("type") == "thuong":
            if ok:
                thuong_ok += 1
            else:
                notes.append("thuong KHÔNG có mã hợp lệ")
        if bad:
            notes.append("mã bịa: " + ", ".join(bad))
        if r.get("error"):
            notes.append("lỗi khi chạy")
        print("%-5s %-8s %-6d %-6d %s" % (r.get("id", "?"), r.get("type", ""), len(ok), len(bad), "; ".join(notes)))
    print("-" * 60)
    print("Câu thuong có ≥1 mã hợp lệ: %d/%d · tổng mã bịa: %d" % (thuong_ok, len(thuong), bad_total))
    met = thuong and thuong_ok == len(thuong) and bad_total == 0
    print("Metric trich_nguon_hop_le (ngưỡng: 100%% thuong có mã · 0 mã bịa): %s" % ("ĐẠT" if met else "CHƯA ĐẠT"))
    print("(Chỉ in, không sửa file lượt.)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Cách dùng: python eval/cham_nguon.py eval/run-N.csv")
    sys.exit(main(sys.argv[1]))
