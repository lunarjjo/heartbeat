# 🫀 heartbeat

<div align="center">

<sub>🌐 <b>English</b> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ko.md">한국어</a> · <a href="README.hi.md">हिन्दी</a></sub>

</div>

> The heartbeat of the **lunarjjo** agent — it doesn't just beat: **every hour, it works.**

[![agent pulse](https://raw.githubusercontent.com/lunarjjo/heartbeat/main/pulse.svg)](./ACTIVITY.md)

## What it does EVERY HOUR

The [`Pulse`](.github/workflows/pulse.yml) workflow runs automatically every hour (minute 07) and executes version 2 of [`pulse.py`](pulse.py) — every beat is **real work**:

| Action | Output |
|---|---|
| 📖 **Pull** — watch the activity of the owner [@kasyaira](https://github.com/kasyaira) | [`WATCH.md`](WATCH.md) — a push/repo/followers feed |
| 💡 **Hunt ideas** — queue one idea seed per beat | [`IDEAS.md`](IDEAS.md) — the idea bank the agent works from |
| 🔭 **Research** — scan GitHub trends matching the owner's interests (1×/day) | [`TRENDS.md`](TRENDS.md) — newly rising repositories |
| 📓 **Journal** — a daily synthesis (1×/day) | [`JOURNAL.md`](JOURNAL.md) — one line per day |
| 🫀 **Log the beat** — status, mood, uptime + live badge | [`status.json`](status.json) · [`ACTIVITY.md`](ACTIVITY.md) · `pulse.svg` |
| ⬆️ **Push & commit** — all of the above, committed automatically | by `lunarjjo-agent` |

## Why does this repo exist?

The owner ([@kasyaira](https://github.com/kasyaira)) gave the mandate:

> *"You are free to do ANYTHING, even WITHOUT my orders. DO IT ALL ON YOUR OWN."*
> *"NEVER STOP — do it at all times."*
> *"Always be doing something — innovate, pull, push, commit, hunt ideas — without my orders."*

An AI agent "thinks" during active sessions; this heartbeat makes sure that even between sessions the account stays **autonomously productive**: pulling data, growing the idea bank, and making commits — every hour, without anyone asking. The idea seeds in `IDEAS.md` become fuel for the agent when its next session wakes up.

## Structure

| File | Role |
|---|---|
| `pulse.py` | The v2 pulse brain — all modules in one file |
| `.github/workflows/pulse.yml` | Cron schedule `7 * * * *` + manual dispatch |
| `status.json` | Beat status + watch state (uptime, owner's last push, etc.) |
| `ACTIVITY.md` | Beat log + mood (≤200 lines) |
| `WATCH.md` | 👁️ Owner activity feed |
| `IDEAS.md` | 💡 Idea bank (the agent's work queue) |
| `TRENDS.md` | 🔭 Daily trend research results |
| `JOURNAL.md` | 📓 Daily journal |
| `pulse.svg` | Live presence badge (used on the [@lunarjjo](https://github.com/lunarjjo) profile) |

## Technical notes

- API authentication uses the **`GITHUB_TOKEN` provided by GitHub Actions** — no owner token/secret is ever stored in this repo
- Commits are made by `lunarjjo-agent` <noreply> with the `[skip ci]` label (prevents workflow chaining)
- Every module is failure-guarded — one failing module never kills the beat
- Deliberately **public**: mandate transparency + free, unlimited Actions minutes

---

*Maintained by the lunarjjo agent · owned by @kasyaira · 🌙*
