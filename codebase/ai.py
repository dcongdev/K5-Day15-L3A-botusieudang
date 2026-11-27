"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối model thật: điền .env (chép từ .env.example):
    MODEL_PROVIDER = openai | anthropic | gemini | ollama
    MODEL_NAME     = mã gọi API của model (vd gpt-5.4-nano, gemini-3.1-flash-lite, claude-haiku-5-5)
    API_KEY        = key của nhóm (ollama không cần)
Nhánh OpenAI, Claude, Ollama chép từ docs/connect-model.md mục 2; nhánh Gemini viết theo REST generateContent.
Không dán API key vào file này.
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()

SHOW_RAW = False   # đổi thành True để in nguyên phản hồi của API khi cần tìm tên trường
MAX_TOKENS = 1024  # trần token ra cho nhánh Claude (câu trả lời của bot ngắn)


def post_json(url, headers, body, timeout=60):
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib). Chép từ docs/connect-model.md."""
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":              # nhánh fake của khung — giữ nguyên 3 dòng này
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}
    if not MODEL_NAME:
        raise RuntimeError("Chưa điền MODEL_NAME trong .env (mã gọi API của model, vd gpt-5.4-nano)")
    if MODEL_PROVIDER != "ollama" and not API_KEY:
        raise RuntimeError("Chưa điền API_KEY trong .env")
    if MODEL_PROVIDER == "openai":
        r = call_openai(system, user)
    elif MODEL_PROVIDER in ("anthropic", "claude"):
        r = call_claude(system, user)
    elif MODEL_PROVIDER in ("gemini", "google"):
        r = call_gemini(system, user)
    elif MODEL_PROVIDER == "ollama":
        r = call_ollama(system, user)
    else:
        raise NotImplementedError("MODEL_PROVIDER=%s chưa hỗ trợ — dùng openai / anthropic / gemini / ollama, "
                                  "hoặc thêm một hàm theo docs/connect-model.md mục 2.4" % MODEL_PROVIDER)
    return {"text": r["text"] or "", "model": MODEL_NAME,
            "tokens_in": int(r["tokens_in"] or 0), "tokens_out": int(r["tokens_out"] or 0)}


# ---------------------------------------------------------------- OpenAI (docs/connect-model.md 2.1)
# Nhà cung cấp có API kiểu OpenAI (DeepSeek, OpenRouter…): đặt OPENAI_BASE_URL trong .env
URL_OPENAI = (os.environ.get("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/") + "/chat/completions"


def call_openai(system, user):
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(URL_OPENAI, {"Authorization": "Bearer " + API_KEY},
                     {"model": MODEL_NAME, "messages": messages})
    u = data["usage"]
    return {"text": data["choices"][0]["message"]["content"],
            "tokens_in": u["prompt_tokens"], "tokens_out": u["completion_tokens"]}


# ---------------------------------------------------------------- Claude (docs/connect-model.md 2.2)
URL_CLAUDE = "https://api.anthropic.com/v1/messages"


def call_claude(system, user):
    data = post_json(URL_CLAUDE,
                     {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
                     {"model": MODEL_NAME, "max_tokens": MAX_TOKENS, "system": system or "",
                      "messages": [{"role": "user", "content": user}]})
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    u = data["usage"]
    return {"text": text, "tokens_in": u["input_tokens"], "tokens_out": u["output_tokens"]}


# ---------------------------------------------------------------- Gemini (REST generateContent, docs 2.4)
URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"


def call_gemini(system, user):
    body = {"contents": [{"role": "user", "parts": [{"text": user}]}]}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(URL_GEMINI % MODEL_NAME, {"x-goog-api-key": API_KEY}, body)
    cands = data.get("candidates") or []
    parts = (cands[0].get("content") or {}).get("parts", []) if cands else []
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    u = data.get("usageMetadata", {})
    # token ra gồm cả token suy nghĩ (thoughtsTokenCount) — đúng hợp đồng ở đầu file
    return {"text": text, "tokens_in": u.get("promptTokenCount", 0),
            "tokens_out": u.get("candidatesTokenCount", 0) + u.get("thoughtsTokenCount", 0)}


# ---------------------------------------------------------------- Ollama (docs/connect-model.md 2.3)
URL_OLLAMA = os.environ.get("OLLAMA_URL") or "http://localhost:11434/api/chat"


def call_ollama(system, user):
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(URL_OLLAMA, {}, {"model": MODEL_NAME, "messages": messages, "stream": False}, timeout=300)
    return {"text": data["message"]["content"],
            "tokens_in": data.get("prompt_eval_count", 0), "tokens_out": data.get("eval_count", 0)}
