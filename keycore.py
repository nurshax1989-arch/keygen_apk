"""Parol hisoblash (kompyuterdagi keygen.py / autocall.license bilan AYNAN bir xil algoritm)."""
import hashlib
import hmac
import time

BASE_YEAR = 2024
SECRET = bytes.fromhex("cb61fb1d760542a6e480ca10297f387b86416cb17523b4ffd5db8c11d0e6ccf0")


def period(ts=None) -> int:
    t = time.localtime(ts if ts is not None else time.time())
    return (t.tm_year - BASE_YEAR) * 12 + t.tm_mon - 1


def period_label(per: int) -> str:
    return f"{BASE_YEAR + per // 12}-{per % 12 + 1:02d}"


def password_for(code: str) -> str:
    d = hmac.new(SECRET, ("TRV1|" + code).encode(), hashlib.sha256).digest()
    return f"{int.from_bytes(d[:8], 'big') % 10_000_000:07d}"


def generate(raw: str):
    """(parol, izoh). Kod noto'g'ri bo'lsa ValueError."""
    code = "".join(ch for ch in raw if ch.isdigit())
    if len(code) != 8:
        raise ValueError("Kod 8 ta raqamdan iborat bo'lishi kerak (masalan 1234 5678).")
    per, now, note = int(code[5:]), period(), ""
    if per < now - 1:
        note = f"Diqqat: kod eski ({period_label(per)}). Mijozdan yangi kod so'rang - bu parol ishlamaydi."
    elif per > now + 1:
        note = "Diqqat: kod kelajak oyiga tegishli - telefon soatini tekshiring."
    return password_for(code), note
