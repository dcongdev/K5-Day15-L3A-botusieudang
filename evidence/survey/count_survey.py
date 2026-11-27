"""Đếm kết quả khảo sát "tra luật nộp bài" — nhóm botusieudang (Lê Quang Huy phụ trách).

Chuẩn bị file (một lần):
  1. Google Form → Phản hồi → Tải xuống CSV.
  2. Mở bằng Google Sheets / Excel: XOÁ cột "Dấu thời gian" và mọi cột có tên / email / SĐT / cách liên hệ (câu 9).
  3. Đổi dòng tiêu đề thành: q1,q2,q3,q4,q5,q6,q7,q8   (đúng thứ tự câu trong evidence/survey/questions.md)
  4. Lưu CSV UTF-8 thành evidence/survey/results.csv  → commit được (đã ẩn danh). File gốc: đặt tên raw-*.csv (đã .gitignore).

Chạy:  python evidence/survey/count_survey.py
In ra: số chính để chép vào evidence/summary.md, spec.md §1–§2, canvas.md dòng 4, cost/personas.yaml
Ghi:   evidence/survey/benchmark-candidates.csv — câu 3 nguyên văn, để Hải Anh viết expected rồi chép vào
       eval/benchmark.csv với source = "nguoi_dung: khảo sát phiếu #N".
Cách đếm viết TRƯỚC khi có dữ liệu (27/11/2026) — không đổi cách đếm sau khi xem kết quả.
"""
import csv
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results.csv")
CANDIDATES = os.path.join(HERE, "benchmark-candidates.csv")

TRONG_TUAN = {"hôm nay", "hôm qua", "2–7 ngày trước", "2-7 ngày trước"}
# câu 5 → phút đại diện mỗi khoảng (để lấy trung vị); "không tìm ra" tính là khoảng dài nhất
PHUT = {"dưới 2'": 1, "2–5'": 3.5, "5–15'": 10, "15–30'": 22.5, "trên 30'": 35, "không tìm ra": 35}
THU_TU = ["dưới 2'", "2–5'", "5–15'", "15–30'", "trên 30'", "không tìm ra"]


def norm(s):
    return (s or "").strip().lower().replace("-", "–").replace("’", "'").replace("phút", "'").replace(" '", "'")


def pct(x, n):
    return "%d/%d" % (x, n) if n < 10 else "%d/%d (%.0f%%)" % (x, n, 100.0 * x / n)


def main():
    if not os.path.exists(RESULTS):
        sys.exit("Chưa có %s — làm theo 4 bước ở đầu file này." % RESULTS)
    with open(RESULTS, encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]
    need = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
    miss = [c for c in need if c not in (rows[0].keys() if rows else [])]
    if miss:
        sys.exit("results.csv thiếu cột: %s (dòng tiêu đề phải là %s)" % (", ".join(miss), ",".join(need)))
    n = len(rows)
    print("Khảo sát — n = %d phiếu (cần ≥20 người ngoài nhóm)\n" % n)

    roles = {}
    for r in rows:
        roles[r["q1"].strip() or "(trống)"] = roles.get(r["q1"].strip() or "(trống)", 0) + 1
    print("Câu 1 — vai:", " · ".join("%s %d" % kv for kv in sorted(roles.items(), key=lambda kv: -kv[1])))

    gap = [r for r in rows if norm(r["q2"]) in TRONG_TUAN]
    print("Câu 2 — đã phải tra / hỏi lại ≥1 luật trong 1 tuần qua: %s" % pct(len(gap), n))

    mins = [PHUT[norm(r["q5"])] for r in gap if norm(r["q5"]) in PHUT]
    dist = {}
    for r in gap:
        dist[norm(r["q5"])] = dist.get(norm(r["q5"]), 0) + 1
    print("Câu 5 — thời gian lần gần nhất (trong %d người đã gặp): %s" % (len(gap), " · ".join(
        "%s %d" % (k, dist.get(k, 0)) for k in THU_TU)))
    med = statistics.median(mins) if mins else None
    if med is not None:
        print("        trung vị ≈ %s phút (lấy giữa khoảng) · ≥5 phút: %s"
              % (med, pct(sum(1 for m in mins if m >= 5), len(mins))))

    many = sum(1 for r in gap if r["q6"].strip() in ("2", "3", "4+"))
    print("Câu 6 — mở ≥2 file / hỏi ≥2 người lần đó: %s" % pct(many, len(gap)))

    cach = {}
    for r in rows:
        for part in [p.strip() for p in r["q4"].split(",") if p.strip()]:
            cach[part] = cach.get(part, 0) + 1
    print("Câu 4 — đã làm thế nào (chọn nhiều):", " · ".join("%s %d" % kv for kv in sorted(cach.items(), key=lambda kv: -kv[1])))

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

    sai = [(i, r["q8"].strip()) for i, r in enumerate(rows, start=1) if r["q8"].strip().lower().startswith("có")]
    print("Câu 8 — từng nộp sai / sửa nhầm vì hiểu sai luật: %s" % pct(len(sai), n))
    for i, t in sai[:8]:
        print("   phiếu #%d: %s" % (i, t[:160]))

    print("\nĐối chiếu giả thuyết (evidence/hypothesis.md): đúng nếu ≥60% gặp VÀ trung vị ≥5 phút; sai nếu <40% hoặc trung vị <2 phút")
    share = len(gap) / n if n else 0
    if n and med is not None:
        verdict = ("ĐÚNG" if share >= 0.6 and med >= 5 else "SAI" if share < 0.4 or med < 2 else "PHẢI ĐỔI / một phần")
        print("   → %s (gặp %.0f%%, trung vị %s phút)" % (verdict, 100 * share, med))

    with open(CANDIDATES, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["phieu", "input", "expected", "pass_criterion", "type", "source"])
        k = 0
        for i, r in enumerate(rows, start=1):
            q = r["q3"].strip()
            if len(q) >= 8:
                k += 1
                w.writerow([i, q, "", "", "thuong", "nguoi_dung: khảo sát phiếu #%d" % i])
    print("\nĐã ghi %d câu hỏi thật (câu 3) vào %s → chọn ~10 câu, viết expected từ data/nguon/, chép vào eval/benchmark.csv (id B21…)."
          % (k, os.path.relpath(CANDIDATES)))
    print("Trích nguyên văn cho evidence/summary.md: lấy từ cột q3 / q8 của results.csv, ghi kèm số phiếu.")


if __name__ == "__main__":
    main()
