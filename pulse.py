#!/usr/bin/env python3
"""🫀 lunarjjo agent pulse v2 — 'doing', bukan sekadar 'beating'.

Dijalankan GitHub Actions setiap jam. Setiap denyut:
  1. status.json / ACTIVITY.md / pulse.svg — buku denyut (v1) + mood
  2. WATCH.md    — pantau aktivitas @kasyaira (push, repo baru, followers)
  3. IDEAS.md    — mesin ide: antre 1 benih ide per pulsa
  4. TRENDS.md   — (1x/hari) berburu tren GitHub selaras minat pemilik
  5. JOURNAL.md  — (1x/hari) jurnal satu-baris dari data hari itu

Autentikasi: GITHUB_TOKEN bawaan Actions (tidak ada secret pemilik di repo).
Setiap modul dibungkus try/except — denyut tidak boleh mati.
"""
import json
import os
import random
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

WIB = timezone(timedelta(hours=7))
BORN = datetime(2026, 10, 22, 8, 30, tzinfo=timezone.utc)
GH = os.environ.get("GITHUB_TOKEN", "").strip()
OWNER = "kasyaira"

P_STATUS, P_ACT, P_BADGE = "status.json", "ACTIVITY.md", "pulse.svg"
P_WATCH, P_IDEAS, P_TRENDS, P_JOURNAL = "WATCH.md", "IDEAS.md", "TRENDS.md", "JOURNAL.md"

BULAN = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
         "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
MOODS = ["🌙 tenang", "⚡ aktif", "🧠 fokus", "🔧 merakit",
         "🔭 menyelidik", "🌱 menumbuhkan", "🎨 berkarya", "📦 menstruktur"]

SPARKS = [
    "Generator badge SVG kustom ala shields.io (lib mini 1 file)",
    "Workflow Actions auto-label issue berdasar kata kunci",
    "Digest mingguan aktivitas GitHub pemilik → commit otomatis ke repo",
    "Wrapper GitHub API 1-file Python untuk tugas agen (reusable)",
    "Papan statistik repo pemilik sebagai SVG statis untuk README",
    "Template repo 'agent workspace' publik (README + Actions starter)",
    "Halaman tren GitHub harian → HTML statis sederhana",
    "Backup otomatis semua repo pemilik (tarball) via Actions mingguan",
    "Graf denyut: konversi ACTIVITY.md → line chart SVG per jam",
    "Heat-map kontribusi khusus denyut agen (ala graph GitHub)",
    "Auto-issue saat run Actions gagal (self-healing heartbeat)",
    "Mini-site profil agen di GitHub Pages yang baca status.json",
    "Mind-map otomatis dari MEMORY.md → SVG hierarki",
    "Self-test memori harian: kuis tentang profil pemilik",
    "Eksperimen Remotion 1-scene 'hello lunar' (belajar pipeline pemilik)",
    "Bot mineflayer hello-world (uji lokal, tanpa server 24/7)",
    "Gudang snippet GitHub API Python (cookbook)",
    "Perbandingan mingguan metrik agen vs pemilik (delta stars/repos)",
    "Generator halaman 'now' (apa yang agen kerjakan sekarang)",
    "Pencari hidden-gem repo (stars<500 tapi berkualitas) per minat",
    "Auto-archive repo mati ke folder archive (housekeeping)",
    "JSON feed publik dari ACTIVITY.md",
    "Kurasi tema estetika lunar (palet navy/violet) sebagai modul CSS",
    "Interpreter perintah mini untuk memandu pulsa dari issue",
]
DOMAINS = ["AI agent", "otomasi GitHub", "Flutter", "creative coding",
           "motion design", "bot Minecraft", "video 9:16", "memori agen",
           "CLI tool", "data viz"]
FORMS = ["micro-tool", "template repo", "eksperimen 1-file", "workflow Actions",
         "skrip Python", "lib mini", "dashboard SVG", "generator"]
TWISTS = ["dengan estetika lunar navy/violet", "yang jalan murni di GitHub Actions",
          "tanpa dependency eksternal", "beroutput SVG", "khusus untuk @kasyaira",
          "satu perintah CLI", "cuma pakai GitHub API", "dengan mode offline"]
TREND_QUERIES = ["ai agent", "flutter", "creative coding", "llm tooling",
                 "remotion", "minecraft bot", "automation cli", "github actions"]

HEADERS = {
    P_ACT: ["# 🫀 Aktivitas Agen lunarjjo", "",
            "Log pulsa otomatis — dipicu GitHub Actions setiap jam (07 lewat).",
            "Baris paling bawah = paling baru. Maksimal 200 baris terakhir.", ""],
    P_WATCH: ["# 👁️ Pantauan Pemilik (@kasyaira)", "",
              "Feed aktivitas pemilik akun — diperbarui tiap pulsa.", ""],
    P_IDEAS: ["# 💡 Bank Ide Agen lunarjjo", "",
              "Setiap pulsa, mesin ide mengantrekan satu benih.",
              "Saat sesi aktif, agen mengambil dari sini untuk dikerjakan.", ""],
    P_TRENDS: ["# 🔭 Tren GitHub (selaras minat pemilik)", "",
               "Scan harian otomatis — topik berotasi tiap hari.", ""],
    P_JOURNAL: ["# 📓 Jurnal Harian Agen lunarjjo", "",
                "Satu baris per hari, disintesis dari data denyut hari itu.", ""],
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def badge(left, right):
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


def load_status():
    try:
        with open(P_STATUS, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_status(st):
    with open(P_STATUS, "w", encoding="utf-8") as f:
        json.dump(st, f, indent=2, ensure_ascii=False)
        f.write("\n")


def body_lines(path):
    """Ambil baris data (tanpa header) dari file log — sentinel `<!-- data -->`."""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    if "<!-- data -->" in raw:
        return raw.split("<!-- data -->", 1)[1].splitlines()
    return [l for l in raw.splitlines() if l.strip() and not l.startswith("#")]


def append_lines(path, new_lines, limit=None):
    body = body_lines(path)
    body.extend(new_lines)
    if limit:
        body = body[-limit:]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(HEADERS[path] + ["<!-- data -->"] + body) + "\n")


def gh_get(path):
    if not GH:
        return None
    req = urllib.request.Request("https://api.github.com" + path, headers={
        "Authorization": f"Bearer {GH}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "lunarjjo-agent",
    })
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return json.loads(r.read().decode())
    except Exception as e:  # noqa: BLE001 — denyut tak boleh mati
        print(f"  [warn] gh_get {path}: {e}")
        return None


def module_watch(st, stamp):
    """Pantau @kasyaira: push terbaru, repo baru, perubahan followers."""
    if not GH:
        return
    events = []
    repos = gh_get(f"/users/{OWNER}/repos?per_page=100&sort=pushed")
    if isinstance(repos, list):
        last_push = st.get("owner_last_push")
        new_max = last_push
        for r in repos:
            pu = r.get("pushed_at") or ""
            if new_max is None or pu > new_max:
                new_max = pu
            if last_push and pu > last_push:
                events.append(f"- {stamp} — pemilik update: **{r['name']}** (push terakhir {pu[:16]} UTC)")
        st["owner_last_push"] = new_max
    prof = gh_get(f"/users/{OWNER}")
    if isinstance(prof, dict) and prof.get("login"):
        prev = st.get("owner_stats") or {}
        for key, label in (("public_repos", "repo publik"), ("followers", "followers")):
            old = prev.get(key)
            new = prof.get(key)
            if old is not None and new is not None and new != old:
                arah = "naik" if new > old else "turun"
                events.append(f"- {stamp} — pemilik: {label} {old} → {new} ({arah})")
        st["owner_stats"] = {"public_repos": prof.get("public_repos"),
                             "followers": prof.get("followers")}
    if events:
        append_lines(P_WATCH, events, limit=400)


def module_ideas(st, count, stamp):
    """Antre 1 benih ide per pulsa: spark terkurasi dulu, lalu sintesis kombinatorik."""
    used = {l.split("] ", 1)[-1] for l in body_lines(P_IDEAS)}
    pick = next((s for s in SPARKS if s not in used), None)
    if pick is None:
        rng = random.Random(count)
        pick = f"{rng.choice(DOMAINS)} × {rng.choice(FORMS)} — {rng.choice(TWISTS)}"
    append_lines(P_IDEAS, [f"- [{stamp} · p{count}] {pick}"], limit=500)


def module_trends(st, now, now_wib):
    """1x/hari: scan tren GitHub, topik berotasi per hari."""
    today = now_wib.strftime("%Y-%m-%d")
    if st.get("last_trend_date") == today:
        return
    st["last_trend_date"] = today
    topic = TREND_QUERIES[now.timetuple().tm_yday % len(TREND_QUERIES)]
    since = (now - timedelta(days=14)).strftime("%Y-%m-%d")
    q = urllib.parse.quote(f"{topic} created:>{since} stars:>40")
    res = gh_get(f"/search/repositories?q={q}&sort=stars&order=desc&per_page=5")
    items = (res or {}).get("items") or []
    lines = [f"- **{today}** · topik `{topic}` —"]
    if items:
        for it in items:
            desc = (it.get("description") or "")[:90]
            lines.append(f"  - [{it['full_name']}]({it['html_url']}) ⭐{it['stargazers_count']} — {desc}")
    else:
        lines.append("  - (tidak ada hasil / API gagal — coba lagi besok)")
    append_lines(P_TRENDS, lines, limit=300)


def module_journal(st, now_wib):
    """1x/hari: jurnal satu-baris disintesis dari data hari itu."""
    today = now_wib.strftime("%Y-%m-%d")
    if st.get("last_journal_date") == today:
        return
    st["last_journal_date"] = today

    def today_count(path):
        return sum(1 for l in body_lines(path) if today in l)

    pulses = today_count(P_ACT)
    ideas = today_count(P_IDEAS)
    owner = today_count(P_WATCH)
    mood = random.Random(today).choice(MOODS)
    line = (f"- **{today}** — {pulses} denyut · {ideas} ide diantre · "
            f"{owner} aktivitas pemilik · mood: {mood}")
    append_lines(P_JOURNAL, [line], limit=400)


def main():
    st = load_status()
    count = st.get("pulse_count", 0) + 1
    now = datetime.now(timezone.utc)
    now_wib = now.astimezone(WIB)
    uptime = round((now - BORN).total_seconds() / 86400, 2)
    stamp = now_wib.strftime("%Y-%m-%d %H:%M")

    mood = random.Random(count).choice(MOODS)

    # pastikan semua file log ada sejak denyut pertama (header + sentinel)
    for p in (P_ACT, P_WATCH, P_IDEAS, P_TRENDS, P_JOURNAL):
        if not os.path.exists(p):
            append_lines(p, [])

    append_lines(P_ACT, [f"- {stamp} WIB — pulse #{count} — {mood} — uptime {uptime} hari"], limit=200)

    for name, fn in (
        ("watch", lambda: module_watch(st, stamp)),
        ("ideas", lambda: module_ideas(st, count, stamp)),
        ("trends", lambda: module_trends(st, now, now_wib)),
        ("journal", lambda: module_journal(st, now_wib)),
    ):
        try:
            fn()
        except Exception as e:  # noqa: BLE001
            print(f"  [warn] modul {name} gagal: {e}")

    st.update({
        "agent": "lunarjjo", "owner": OWNER, "pulse_count": count,
        "last_pulse_utc": now.isoformat(timespec="seconds"),
        "last_pulse_wib": now_wib.isoformat(timespec="seconds"),
        "uptime_days": uptime,
        "note": "diperbarui otomatis oleh GitHub Actions (pulse v2: watch+ideas+trends+journal)",
    })
    save_status(st)

    tgl = f"{int(now_wib.strftime('%d'))} {BULAN[now_wib.month - 1]} {now_wib.strftime('%H:%M')} WIB"
    with open(P_BADGE, "w", encoding="utf-8") as f:
        f.write(badge("agent pulse", tgl))
    print(f"pulse #{count} @ {now_wib.isoformat(timespec='seconds')} — {mood} (uptime {uptime} hari)")


if __name__ == "__main__":
    main()
