"""Tạo bảng chấm cho người chấm — nhóm botusieudang viết.

    python eval/bang_cham.py eval/run-1.csv      → ghi eval/bang-cham-run-1.md

Mỗi câu: id, type, input, expected, pass_criterion, output, kết quả kiểm mã đoạn bằng code
(metric trich_nguon_hop_le, giống eval/cham_nguon.py). Người chấm đọc file này rồi điền cột pass (1/0)
và ghi_chu trong eval/run-N.csv. Script KHÔNG điền pass, KHÔNG sửa file lượt.
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
    name = os.path.splitext(os.path.basename(path))[0]
    out_path = os.path.join(ROOT, "eval", "bang-cham-%s.md" % name)
    lines = ["# Bảng chấm %s" % name, "",
             "Chấm theo `eval/metric_spec.yaml`: pass = 1 khi output đạt ĐỦ pass_criterion. "
             "Câu có \"mã bịa\" hoặc thuong \"không có mã hợp lệ\" → pass = 0 (metric trich_nguon_hop_le).",
             "Điền vào `%s`: cột `pass` (1/0) và `ghi_chu` (lỗi gì, để gom nhóm lỗi ở eval/report.md). "
             "Rồi chạy `python run.py score %s`." % (path.replace("\\", "/"), path.replace("\\", "/")), ""]
    for r in rows:
        found = CODE_RE.findall(r.get("output", ""))
        ok = sorted({c for c in found if c in codes})
        bad = sorted({c for c in found if c not in codes})
        flags = []
        if bad:
            flags.append("MÃ BỊA: " + ", ".join(bad) + " → pass = 0")
        if r.get("type") == "thuong" and not ok:
            flags.append("thuong KHÔNG có mã hợp lệ → pass = 0")
        if r.get("error"):
            flags.append("LỖI KHI CHẠY: " + r["error"][:200])
        lines += ["## %s · %s" % (r.get("id", "?"), r.get("type", "")), "",
                  "- **Input:** %s" % r.get("input", ""),
                  "- **Expected:** %s" % r.get("expected", ""),
                  "- **Tiêu chí đạt:** %s" % r.get("pass_criterion", ""),
                  "- **Kiểm mã (code):** %s" % ("; ".join(flags) if flags else "mã hợp lệ: %s" % (", ".join(ok) or "không có mã (không bắt buộc với type này)")),
                  "- **pass:** ☐ 1 ☐ 0 · **ghi_chu:** ",
                  "", "```", (r.get("output", "") or "(trống)").strip(), "```", ""]
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Đã ghi %s (%d câu). Script không điền pass." % (os.path.relpath(out_path, ROOT), len(rows)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Cách dùng: python eval/bang_cham.py eval/run-N.csv")
    main(sys.argv[1])
