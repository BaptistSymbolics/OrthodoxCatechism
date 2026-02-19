import base64, io, requests, time, concurrent.futures as cf
from pathlib import Path

OLLAMA = "http://127.0.0.1:11434"
MODEL  = "qwen2.5vl:7b"
INPUT_DIR = Path("pages")
OUT_DIR   = Path("ocr_out"); OUT_DIR.mkdir(exist_ok=True)
MAX_WORKERS = 3  # increase if you have headroom

def img_b64(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            max_edge = 2000
            w, h = im.size
            s = min(1.0, max_edge / float(max(w, h)))
            if s < 1.0:
                im = im.resize((int(w*s), int(h*s)))
            buf = io.BytesIO(); im.save(buf, format="JPEG", quality=92)
            return base64.b64encode(buf.getvalue()).decode("ascii")
    except Exception:
        return base64.b64encode(Path(path).read_bytes()).decode("ascii")

def call_ollama(b64, retries=1):
    payload = {
        "model": MODEL,
        "prompt": "Extract all text verbatim from this image. Output plain text only.",
        "images": [b64],
        "stream": False,
        "keep_alive": "30m",
    }
    for attempt in range(retries + 1):
        try:
            r = requests.post(f"{OLLAMA}/api/generate", json=payload, timeout=(5, 600))
            r.raise_for_status()
            j = r.json()
            return j.get("response") or j.get("message", {}).get("content") or ""
        except Exception as e:
            if attempt < retries:
                time.sleep(1.0)
            else:
                raise

def process(path: Path):
    try:
        text = call_ollama(img_b64(path), retries=1)
        (OUT_DIR / f"{path.stem}.txt").write_text(text, encoding="utf-8")
        return path.name, "ok"
    except Exception as e:
        with open(OUT_DIR / "failures.log", "a", encoding="utf-8") as log:
            log.write(f"{path} :: {e}\n")
        return path.name, f"fail: {e}"

if __name__ == "__main__":
    files = [p for p in sorted(INPUT_DIR.iterdir()) if p.suffix.lower() in {".png",".jpg",".jpeg",".webp"}]
    # warm model once
    requests.post(f"{OLLAMA}/api/generate", json={"model": MODEL, "prompt":"ready", "stream":False, "keep_alive":"30m"}, timeout=(5,60))
    with cf.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        for name, status in ex.map(process, files):
            print(f"{name} -> {status}")