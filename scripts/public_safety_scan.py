from pathlib import Path
import re
import sys

ROOT = Path(".")
SELF = Path("scripts/public_safety_scan.py")
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}

patterns = [
    ("OpenAI-style API key", re.compile(r"\\bsk-[A-Za-z0-9_-]{20,}\\b")),
    ("Telegram bot token", re.compile(r"\\b\\d{6,12}:[A-Za-z0-9_-]{20,}\\b")),
    ("Google API key", re.compile(r"\\bAIza[0-9A-Za-z_-]{25,}\\b")),
    ("GitHub token", re.compile(r"\\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\\b")),
    ("AWS access key", re.compile(r"\\bAKIA[0-9A-Z]{16}\\b")),
    ("private key block", re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY")),
    ("private webhook URL", re.compile(r"https?://[^\\s\"']+/webhook(?:-test)?/[^\\s\"']+", re.I)),
    ("live Google document URL", re.compile(r"https?://(?:docs|sheets)\\.google\\.com/", re.I)),
    ("n8n credential object", re.compile(r'"credentials"\\s*:', re.I)),
    ("Telegram file id", re.compile(r"\\bAgAC[A-Za-z0-9_-]{20,}\\b")),
    ("Swiss phone number", re.compile(r"(?:\\+41|0041)[\\s().-]*\\d(?:[\\s().-]*\\d){7,}")),
    ("email address", re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}", re.I)),
]

hits = []
FORBIDDEN_MEDIA = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".mov", ".webm"}

for path in ROOT.rglob("*"):
    if not path.is_file() or path == SELF:
        continue
    if path.suffix.lower() in FORBIDDEN_MEDIA:
        hits.append((str(path), "photo/video media file"))
        continue
    if any(part in SKIP_DIRS for part in path.parts):
        continue
    if path.stat().st_size > 1_000_000:
        continue
    data = path.read_bytes()
    if b"\\x00" in data:
        continue
    text = data.decode("utf-8", errors="ignore")
    for label, pattern in patterns:
        if pattern.search(text):
            hits.append((str(path), label))

if hits:
    print("Public safety scan FAILED.")
    for path, label in hits:
        print(f"- {path}: {label}")
    print("Matched values are intentionally not printed.")
    sys.exit(1)

print("Public safety scan passed.")
