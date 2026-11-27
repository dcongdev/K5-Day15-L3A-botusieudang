"""Đếm kết quả khảo sát "tra luật nộp bài" — nhóm botusieudang (Lê Quang Huy phụ trách).

CÁCH NHANH (khuyên dùng) — một lệnh:
  1. Mở Google Sheet kết quả → Tệp → Tải xuống → CSV → lưu vào thư mục evidence/survey/ với tên bắt đầu bằng raw-
     (vd evidence/survey/raw-ketqua.csv — tên raw-* đã nằm trong .gitignore nên KHÔNG bị commit).
  2. python evidence/survey/count_survey.py evidence/survey/raw-ketqua.csv
     → script tự bỏ cột thời gian + câu 9 (cách liên hệ), tự đổi tiêu đề thành q1…q8,
       ghi bản ẩn danh evidence/survey/results.csv (commit được), rồi đếm.
  3. Muốn điền luôn canvas.md dòng 4 với trích dẫn của phiếu số N:
     python evidence/survey/count_survey.py evidence/survey/raw-ketqua.csv --canvas N
     (trích cột q8 nếu phiếu đó trả lời "Có — …", không thì cột q3.)

Không có tham số: đếm lại từ evidence/survey/results.csv đã ẩn danh.

In ra: số chính cho evidence/summary.md, spec.md §1–§2, cost/personas.yaml
Ghi:   evidence/survey/results.csv (ẩn danh) · evidence/survey/benchmark-candidates.csv (câu 3 nguyên văn → câu thử nguoi_dung)
Cách đếm viết TRƯỚC khi có dữ liệu (27/11/2026) — không đổi cách đếm sau khi xem kết quả.
"""
import csv
import os
import re
import statistics
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RESULTS = os.path.join(HERE, "results.csv")
CANDIDATES = os.path.join(HERE, "benchmark-candidates.csv")
CANVAS = os.path.join(ROOT, "canvas.md")
Q = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]

TRONG_TUAN = {"hôm nay", "hôm qua", "2–7 ngày trước"}
# câu 5 → phút đại diện mỗi khoảng (để lấy trung vị); "không tìm ra" tính là khoảng dài nhất
PHUT = {"dưới 2'": 1, "2–5'": 3.5, "5–15'": 10, "15–30'": 22.5, "trên 30'": 35, "không tìm ra": 35}
THU_TU = ["dưới 2'", "2–5'", "5–15'", "15–30'", "trên 30'", "không tìm ra"]


def norm(s):
    s = (s or "").strip().lower().replace("-", "–").replace("’", "'").replace("phút", "'")
    return re.sub(r"\s+'", "'", s)


def pct(x, n):
    return "%d/%d" % (x, n) if n < 10 else "%d/%d (%.0f%%)" % (x, n, 100.0 * x / n)


def anonymize(raw_path):
    """File xuất từ Google Sheets (cột: dấu thời gian, '1. …' … '9. …') → results.csv chỉ có q1…q8."""
    with open(raw_path, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [r for r in reader if any(c.strip() for c in r)]
    col = {}
    for i, h in enumerate(header):
        m = re.match(r"\s*(\d)\s*[.)]", h)
        if m and 1 <= int(m.group(1)) <= 8:
            col["q" + m.group(1)] = i
    if set(Q) - set(col):
        if [h.strip().lower() for h in header[:8]] == Q:      # đã là file ẩn danh
            col = {q: i for i, q in enumerate(Q)}
        else:
            sys.exit("Không nhận ra cột câu %s trong %s. Tiêu đề cột phải bắt đầu bằng số câu (\"1. …\", \"2. …\")."
                     % (", ".join(sorted(set(Q) - set(col))), raw_path))
    with open(RESULTS, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(Q)
        for r in rows:
            w.writerow([(r[col[q]] if col[q] < len(r) else "").strip() for q in Q])
    print("Đã ghi bản ẩn danh %s (%d phiếu; đã bỏ cột thời gian và câu 9)\n" % (os.path.relpath(RESULTS, ROOT), len(rows)))


def load():
    if not os.path.exists(RESULTS):
        sys.exit("Chưa có %s — chạy: python evidence/survey/count_survey.py evidence/survey/raw-<tên>.csv"
                 % os.path.relpath(RESULTS, ROOT))
    with open(RESULTS, encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]
    if rows and set(Q) - set(rows[0].keys()):
        sys.exit("results.csv thiếu cột (dòng tiêu đề phải là %s)" % ",".join(Q))
    return rows


def count(rows):
    n = len(rows)
    out = {"n": n, "gap": 0, "med": None}
    print("Khảo sát — n = %d phiếu (cần ≥20 người ngoài nhóm)\n" % n)
    if not n:
        return out
    roles = {}
    for r in rows:
        k = r["q1"].strip() or "(trống)"
        roles[k] = roles.get(k, 0) + 1
    print("Câu 1 — vai:", " · ".join("%s %d" % kv for kv in sorted(roles.items(), key=lambda kv: -kv[1])))

    gap = [r for r in rows if norm(r["q2"]) in TRONG_TUAN]
    out["gap"] = len(gap)
    print("Câu 2 — đã phải tra / hỏi lại ≥1 luật trong 1 tuần qua: %s" % pct(len(gap), n))
    for role in sorted(roles, key=lambda k: -roles[k]):  # đếm theo từng vai, không cộng chung (evidence/summary.md)
        rr = [r for r in rows if (r["q1"].strip() or "(trống)") == role]
        print("        %-16s %s" % (role + ":", pct(sum(1 for r in rr if norm(r["q2"]) in TRONG_TUAN), len(rr))))

    mins = [PHUT[norm(r["q5"])] for r in gap if norm(r["q5"]) in PHUT]
    dist = {}
    for r in gap:
        dist[norm(r["q5"])] = dist.get(norm(r["q5"]), 0) + 1
    print("Câu 5 — thời gian lần gần nhất (trong %d người đã gặp): %s"
          % (len(gap), " · ".join("%s %d" % (k, dist.get(k, 0)) for k in THU_TU)))
    med = statistics.median(mins) if mins else None
    out["med"] = med
    if med is not None:
        print("        trung vị ≈ %s phút (lấy giữa khoảng) · ≥5 phút: %s"
              % (med, pct(sum(1 for m in mins if m >= 5), len(mins))))

    if gap:
        many = sum(1 for r in gap if r["q6"].strip() in ("2", "3", "4+"))
        print("Câu 6 — mở ≥2 file / hỏi ≥2 người lần đó: %s" % pct(many, len(gap)))

    cach = {}
    for r in rows:
        for part in [p.strip() for p in r["q4"].split(",") if p.strip()]:
            cach[part] = cach.get(part, 0) + 1
    print("Câu 4 — đã làm thế nào (chọn nhiều):",
          " · ".join("%s %d" % kv for kv in sorted(cach.items(), key=lambda kv: -kv[1])) or "—")

    week = []
    for r in rows:
        try:
            week.append(float(r["q7"].replace(",", ".")))
        except ValueError:
            pass
    if week:
        it = sum(1 for w in week if w <= 1)
        vua = sum(1 for w in week if 1 < w <= 4)
        nhieu = sum(1 for w in week if w > 4)
        print("Câu 7 — số lần / tuần: trung vị %s · TB %.1f · ≤1 lần: %d · 2–4: %d · ≥5: %d (n=%d) → share persona: %.2f / %.2f / %.2f"
              % (statistics.median(week), statistics.mean(week), it, vua, nhieu, len(week),
                 it / len(week), vua / len(week), nhieu / len(week)))
        for name, grp in (("tra_vua (2–4 lần/tuần)", [w for w in week if 1 < w <= 4]),
                          ("tra_nhieu (≥5 lần/tuần)", [w for w in week if w > 4])):
            if grp:
                print("        %s: TB %.1f lần/tuần → uses_per_month ≈ %d" % (name, statistics.mean(grp), round(4 * statistics.mean(grp))))

    sai = [(i, r["q8"].strip()) for i, r in enumerate(rows, start=1) if r["q8"].strip().lower().startswith("có")]
    print("Câu 8 — từng nộp sai / sửa nhầm vì hiểu sai luật: %s" % pct(len(sai), n))
    for i, t in sai[:8]:
        print("   phiếu #%d: %s" % (i, t[:160]))

    print("\nĐối chiếu giả thuyết (evidence/hypothesis.md): đúng nếu ≥60% gặp VÀ trung vị ≥5 phút; sai nếu <40% hoặc trung vị <2 phút")
    share = len(gap) / n
    if med is not None:
        verdict = ("ĐÚNG" if share >= 0.6 and med >= 5 else "SAI" if share < 0.4 or med < 2 else "PHẢI ĐỔI / một phần")
        print("   → %s (gặp %.0f%%, trung vị %s phút)%s" % (verdict, 100 * share, med,
              "" if n >= 20 else " — CHƯA đủ 20 phiếu, chỉ là số đầu tiên"))

    print("\nCâu 3 (câu hỏi thật) — chọn 1 phiếu làm trích dẫn bằng --canvas <số phiếu>:")
    for i, r in enumerate(rows, start=1):
        if r["q3"].strip():
            print("   phiếu #%d: %s" % (i, r["q3"].strip()[:160]))

    with open(CANDIDATES, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["phieu", "input", "expected", "pass_criterion", "type", "source"])
        for i, r in enumerate(rows, start=1):
            q = r["q3"].strip()
            if len(q) >= 8:
                w.writerow([i, q, "", "", "thuong", "nguoi_dung: khảo sát phiếu #%d" % i])
    print("\nĐã ghi %s → chọn ~10 câu, viết expected từ data/nguon/, chép vào eval/benchmark.csv (id B21…)."
          % os.path.relpath(CANDIDATES, ROOT))
    return out


def fill_canvas(rows, stats, k):
    if not 1 <= k <= len(rows):
        sys.exit("--canvas %d: chỉ có phiếu #1 đến #%d" % (k, len(rows)))
    r = rows[k - 1]
    q8 = r["q8"].strip()
    quote = q8 if q8.lower().startswith("có") else r["q3"].strip()
    if not quote:
        sys.exit("Phiếu #%d không có câu 3 / câu 8 để trích — chọn phiếu khác." % k)
    quote = quote.replace('"', "'").replace("|", "/").replace("\n", " ")
    n = stats["n"]
    so = "khảo sát n = %d%s, %s đã phải tra / hỏi lại luật nộp bài trong 1 tuần qua" % (
        n, "" if n >= 20 else " (mới %d phiếu, form còn mở đến CP3)" % n, pct(stats["gap"], n))
    if stats.get("med") is not None:
        so += ", trung vị lần gần nhất ≈ %s phút" % stats["med"]
    new = '**CP2 — số đầu tiên:** %s; trích: "%s" (phiếu #%d, `evidence/survey/results.csv`).' % (so, quote, k)
    with open(CANVAS, encoding="utf-8") as f:
        text = f.read()
    pat = re.compile(r"\*\*CP2 — số đầu tiên:\*\*.*?(?= \|\s*$)", re.M)
    if not pat.search(text):
        sys.exit("Không tìm thấy chỗ \"**CP2 — số đầu tiên:**\" ở canvas.md dòng 4 — điền tay dòng sau:\n" + new)
    text = pat.sub(lambda m: new, text, count=1)
    with open(CANVAS, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("\nĐã điền canvas.md dòng 4:\n  " + new)


def main(argv):
    raw, k = None, None
    i = 0
    while i < len(argv):
        if argv[i] == "--canvas" and i + 1 < len(argv):
            k = int(argv[i + 1])
            i += 2
        else:
            raw = argv[i]
            i += 1
    if raw:
        anonymize(raw)
    rows = load()
    stats = count(rows)
    if k is not None:
        fill_canvas(rows, stats, k)


if __name__ == "__main__":
    main(sys.argv[1:])
