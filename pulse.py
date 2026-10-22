#!/usr/bin/env python3
"""🫀 lunarjjo agent pulse — dijalankan oleh GitHub Actions setiap jam.

Tugas:
1. Update status.json  (jumlah pulsa, waktu terakhir, uptime)
2. Append ACTIVITY.md  (log, maksimal 200 baris terakhir)
3. Regenerate pulse.svg (badge kehadiran live, dipakai di profil)
"""
import json
import os
from datetime import datetime, timedelta, timezone

WIB = timezone(timedelta(hours=7))
BORN = datetime(2026, 10, 22, 8, 30, tzinfo=timezone.utc)  # sesi fondasi agen

STATUS_PATH = "status.json"
ACTIVITY_PATH = "ACTIVITY.md"
BADGE_PATH = "pulse.svg"

BULAN_ID = {
    "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "Mei", "06": "Jun",
    "07": "Jul", "08": "Agu", "09": "Sep", "10": "Okt", "11": "Nov", "12": "Des",
}

ACTIVITY_HEADER = [
    "# 🫀 Aktivitas Agen lunarjjo",
    "",
    "Log pulsa otomatis — dipicu GitHub Actions setiap jam (07 lewat).",
    "Baris paling bawah = paling baru. Menjaga maksimal 200 baris terakhir.",
    "",
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def badge(left: str, right: str) -> str:
    """Badge flat ala shields.io, tema lunar (navy gelap + violet)."""
    lw = int(len(left) * 7.2) + 22
    rw = int(len(right) * 7.2) + 22
    w = lw + rw
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="20" role="img" aria-label="{esc(left)}: {esc(right)}">
  <title>{esc(left)}: {esc(right)}</title>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r"><rect width="{w}" height="20" rx="3" fill="#fff"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{lw}" height="20" fill="#1a1a2e"/>
    <rect x="{lw}" width="{rw}" height="20" fill="#8b5cf6"/>
    <rect width="{w}" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
    <text x="{lw // 2}" y="15">{esc(left)}</text>
    <text x="{lw + rw // 2}" y="15">{esc(right)}</text>
  </g>
</svg>
"""


def main() -> None:
    # --- baca status lama ---
    count = 0
    if os.path.exists(STATUS_PATH):
        try:
            with open(STATUS_PATH, encoding="utf-8") as f:
                count = json.load(f).get("pulse_count", 0)
        except (ValueError, OSError):
            count = 0
    count += 1

    now = datetime.now(timezone.utc)
    now_wib = now.astimezone(WIB)
    uptime = round((now - BORN).total_seconds() / 86400, 2)

    # --- status.json ---
    status = {
        "agent": "lunarjjo",
        "owner": "kasyaira",
        "pulse_count": count,
        "last_pulse_utc": now.isoformat(timespec="seconds"),
        "last_pulse_wib": now_wib.isoformat(timespec="seconds"),
        "uptime_days": uptime,
        "note": "diperbarui otomatis oleh GitHub Actions (workflow 'Pulse')",
    }
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # --- ACTIVITY.md (append, potong 200) ---
    line = f"- {now_wib.strftime('%Y-%m-%d %H:%M')} WIB — pulse #{count} — uptime {uptime} hari — agen hidup & otonom"
    entries = []
    if os.path.exists(ACTIVITY_PATH):
        with open(ACTIVITY_PATH, encoding="utf-8") as f:
            old = f.read().splitlines()
        if old and old[0].startswith("#"):
            entries = old[len(ACTIVITY_HEADER):]
        else:
            entries = old
    entries.append(line)
    entries = [e for e in entries if e.strip()][-200:]
    with open(ACTIVITY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(ACTIVITY_HEADER + entries) + "\n")

    # --- pulse.svg ---
    tgl = f"{int(now_wib.strftime('%d'))} {BULAN_ID[now_wib.strftime('%m')]} {now_wib.strftime('%H:%M')} WIB"
    with open(BADGE_PATH, "w", encoding="utf-8") as f:
        f.write(badge("agent pulse", tgl))

    print(f"pulse #{count} @ {now_wib.isoformat(timespec='seconds')} (uptime {uptime} hari)")


if __name__ == "__main__":
    main()
