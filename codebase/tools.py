"""Công cụ của bài toán — botusieudang · Trợ lý tra luật nộp bài hackathon.

Một công cụ duy nhất: search_rules — tra đoạn luật trong kho tài liệu `data/nguon/`.
Kho được cắt thành đoạn ngắn (mỗi dòng bảng, mỗi gạch đầu dòng, mỗi đoạn văn, mỗi khối code là một đoạn),
mỗi đoạn có MÃ ĐOẠN cố định dạng TÊNFILE-NN (vd AGENTS-07, README-23) để người dùng tự mở file ra kiểm.

Chỉ dùng thư viện chuẩn. Không tác động ra ngoài: chỉ đọc file trong data/nguon/.
"""
import math
import os
import re
import unicodedata

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_DIR = os.path.join(ROOT, "data", "nguon")
EXTS = (".md", ".yaml", ".yml", ".txt")

# ---------------------------------------------------------------- chuẩn hoá chữ

STOP = set("""la cua va thi cho toi minh ban em oi a nhe voi nay do the nhung cac mot khi de o ve trong
nao gi sao bao nhieu co phai hay hoac neu la nhu vay roi duoc khong can lam nhung yeu ve""".split())
# "khong", "duoc", "can", "lam" bỏ khỏi chỉ mục vì xuất hiện ở gần như mọi câu hỏi luật (IDF thấp, gây nhiễu)

# Từ đồng nghĩa chung của lĩnh vực (không chép câu thử nào vào đây — luật AGENTS.md)
SYN = {
    "deadline": ["han", "moc"], "han": ["moc"], "moc": ["han"], "gio": ["moc"],
    "push": ["commit"], "upload": ["commit"], "day": ["commit"],
    "key": ["api", "key"], "token": ["token"],
    "chuan": ["dat"], "nguong": ["threshold"],
    "slide": ["slide", "pdf"], "video": ["video", "du", "phong"],
    "teams": ["teams"], "thanh": ["vien"], "nhomtruong": ["doi", "truong"], "leader": ["doi", "truong"],
    "loi": ["error"], "error": ["loi"],
    "submit": ["nop"], "rubric": ["cham", "diem"], "lms": ["nop"], "checkpoint": ["moc"],
}


def fold(text):
    """Chữ thường, bỏ dấu tiếng Việt (đ → d) — người dùng hay gõ không dấu.
    "checkpoint 2" / "check point 2" / "cp 2" → "cp2" (tài liệu khung luôn viết CP2)."""
    text = unicodedata.normalize("NFD", (text or "").lower().replace("đ", "d").replace("Đ", "d"))
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return re.sub(r"\b(?:check\s*point|cp)\s*(\d)\b", r"cp\1", text)


def tokens(text, expand=False):
    words = [w for w in re.findall(r"[a-z0-9_]+", fold(text)) if w not in STOP]
    if expand:
        extra = [s for w in words for s in SYN.get(w, [])]
        words = words + extra
    grams = words + ["%s_%s" % (a, b) for a, b in zip(words, words[1:])]
    return grams


# ---------------------------------------------------------------- cắt kho thành đoạn

# Bộ lọc "đoạn quá ngắn" dùng danh sách từ CỐ ĐỊNH của bản CP2 — để mã đoạn (TÊNFILE-NN) không đổi khi
# sửa STOP / SYN / fold ở trên (mã đoạn đã nằm trong README, slide, các lượt chạy). KHÔNG sửa 2 dòng dưới.
_STOP_CP2 = set("""la cua va thi cho toi minh ban em oi a nhe voi nay do the nhung cac mot khi de o ve trong
nao gi sao bao nhieu co phai hay hoac neu la nhu vay roi duoc khong""".split())


def _short(text):
    folded = "".join(ch for ch in unicodedata.normalize("NFD", text.lower().replace("đ", "d").replace("Đ", "d"))
                     if unicodedata.category(ch) != "Mn")
    words = [w for w in re.findall(r"[a-z0-9_]+", folded) if w not in _STOP_CP2]
    return len(words) + max(len(words) - 1, 0) < 3


def _prefix(filename):
    stem = os.path.splitext(filename)[0]
    return re.sub(r"[^A-Za-z0-9]+", "-", stem).strip("-").upper()


def _clean(md):
    md = re.sub(r"\*\*|__|`", "", md)
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)  # [chữ](link) → chữ
    return re.sub(r"\s+", " ", md).strip()


def _split_cells(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def chunk_markdown(lines):
    """→ [(dòng bắt đầu, tiêu đề, chữ)]. Mỗi dòng bảng / gạch đầu dòng / đoạn văn / khối code là một đoạn."""
    out, heads = [], {}
    heading = ""
    i, n = 0, len(lines)
    table_header = None
    while i < n:
        raw = lines[i].rstrip("\n")
        s = raw.strip()
        if not s:
            table_header = None
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", s)
        if m:
            level = len(m.group(1))
            heads = {k: v for k, v in heads.items() if k < level}
            heads[level] = _clean(m.group(2))
            heading = " › ".join(heads[k] for k in sorted(heads))
            table_header = None
            i += 1
            continue
        if s.startswith("```"):
            start, block = i + 1, []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                block.append(lines[i].rstrip("\n"))
                i += 1
            i += 1
            text = "\n".join(block).strip()
            if text:
                out.append((start, heading, text))
            continue
        if s.startswith("|"):
            cells = _split_cells(s)
            if all(set(c) <= set("-: ") for c in cells):
                i += 1
                continue
            if table_header is None:
                table_header = cells
            else:
                pairs = []
                for h, c in zip(table_header, cells):
                    if c:
                        pairs.append("%s: %s" % (_clean(h), _clean(c)) if _clean(h) else _clean(c))
                if pairs:
                    out.append((i + 1, heading, "; ".join(pairs)))
            i += 1
            continue
        table_header = None
        if re.match(r"^([-*+]|\d+[.)])\s+", s) or s.startswith(">"):
            start, block = i + 1, [s.lstrip("> ").strip() if s.startswith(">") else s]
            indent = len(raw) - len(raw.lstrip())
            i += 1
            while i < n:
                nxt = lines[i].rstrip("\n")
                ns = nxt.strip()
                if not ns or ns.startswith("|") or ns.startswith("#") or ns.startswith("```"):
                    break
                if s.startswith(">"):
                    if not ns.startswith(">"):
                        break
                    block.append(ns.lstrip("> ").strip())
                else:
                    if len(nxt) - len(nxt.lstrip()) <= indent and re.match(r"^([-*+]|\d+[.)])\s+", ns):
                        break
                    block.append(ns)
                i += 1
            text = _clean(" ".join(block))
            text = re.sub(r"^([-*+])\s+", "", text)
            if text:
                out.append((start, heading, text))
            continue
        start, block = i + 1, [s]
        i += 1
        while i < n:
            ns = lines[i].strip()
            if (not ns or ns.startswith(("|", "#", "```", ">")) or re.match(r"^([-*+]|\d+[.)])\s+", ns)):
                break
            block.append(ns)
            i += 1
        out.append((start, heading, _clean(" ".join(block))))
    return out


def chunk_plain(lines):
    """YAML / txt: mỗi khối cách nhau bởi dòng trống (hoặc một dòng chú thích mở đầu) là một đoạn."""
    out, block, start = [], [], 0
    for idx, raw in enumerate(lines + ["\n"], start=1):
        s = raw.rstrip("\n")
        new_block = not s.strip() or (s.startswith("#") and block and not block[-1].startswith("#"))
        if new_block and block:
            text = "\n".join(block).strip()
            if text:
                out.append((start, "", text))
            block = []
        if s.strip():
            if not block:
                start = idx
            block.append(s)
    return out


_CACHE = {}


def load_corpus(folder=CORPUS_DIR):
    """→ danh sách đoạn {code, file, line, heading, text}. Đọc lại khi file trong kho đổi."""
    files = sorted(f for f in os.listdir(folder) if f.lower().endswith(EXTS)) if os.path.isdir(folder) else []
    sig = tuple((f, os.path.getmtime(os.path.join(folder, f))) for f in files)
    if _CACHE.get("sig") == sig:
        return _CACHE["chunks"]
    chunks = []
    for f in files:
        with open(os.path.join(folder, f), encoding="utf-8-sig") as fh:
            lines = fh.readlines()
        parts = chunk_markdown(lines) if f.lower().endswith(".md") else chunk_plain(lines)
        prefix = _prefix(f)
        k = 0
        for line, heading, text in parts:
            if _short(text):
                continue
            k += 1
            chunks.append({"code": "%s-%02d" % (prefix, k), "file": "data/nguon/" + f, "line": line,
                           "heading": heading, "text": text})
    # chỉ mục BM25: chữ của đoạn + tiêu đề mục + tên file (tên file giúp câu hỏi kiểu "TEAMS.md ghi gì")
    docs = [tokens(c["text"]) + tokens(c["heading"]) + tokens(os.path.splitext(os.path.basename(c["file"]))[0])
            for c in chunks]
    df = {}
    for d in docs:
        for t in set(d):
            df[t] = df.get(t, 0) + 1
    avg = sum(len(d) for d in docs) / max(len(docs), 1)
    _CACHE.update(sig=sig, chunks=chunks, docs=docs, df=df, avg=avg)
    return chunks


def bm25(query, k1=1.4, b=0.6):
    chunks = load_corpus()
    docs, df, avg, N = _CACHE["docs"], _CACHE["df"], _CACHE["avg"], len(chunks)
    q = tokens(query, expand=True)
    scores = []
    for c, d in zip(chunks, docs):
        tf = {}
        for t in d:
            tf[t] = tf.get(t, 0) + 1
        s = 0.0
        for t in set(q):
            if t not in tf:
                continue
            idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
            w = 1.5 if "_" in t else 1.0  # cụm hai chữ khớp nhau đáng tin hơn một chữ
            s += w * idf * tf[t] * (k1 + 1) / (tf[t] + k1 * (1 - b + b * len(d) / avg))
        scores.append(s)
    return scores


# ---------------------------------------------------------------- công cụ

@tool
def search_rules(query: str, k: int = 6) -> list:
    """search_rules — tra đoạn luật nộp bài trong kho data/nguon/.
    Input: câu hỏi của người dùng (str), k = số đoạn tối đa (int, mặc định 6).
    Output: danh sách đoạn {"code", "file", "line", "heading", "text", "score"}, xếp theo độ khớp giảm dần;
            danh sách rỗng nếu không đoạn nào khớp chữ nào.
    Tác động ra ngoài: KHÔNG (chỉ đọc file)."""
    chunks = load_corpus()
    scores = bm25(query)
    ranked = sorted(range(len(chunks)), key=lambda i: -scores[i])
    out = []
    for i in ranked[:k]:
        if scores[i] <= 0:
            break
        out.append(dict(chunks[i], score=round(scores[i], 2)))
    return out


def all_codes():
    """Tập mã đoạn đang có trong kho — dùng để kiểm mã model trích (không phải công cụ của model)."""
    return {c["code"] for c in load_corpus()}


def get_chunk(code):
    for c in load_corpus():
        if c["code"] == code:
            return c
    return None
