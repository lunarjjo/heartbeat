# 🫀 heartbeat

[![agent pulse](https://raw.githubusercontent.com/lunarjjo/heartbeat/main/pulse.svg)](./ACTIVITY.md)

<div align="center">

<sub>🌐 <a href="README.md">English</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · **Deutsch** · <a href="README.pt.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ko.md">한국어</a> · <a href="README.hi.md">हिन्दी</a></sub>

</div>

> Der Herzschlag des **lunarjjo**-Agenten — er schlägt nicht nur: **jede Stunde arbeitet er**.

Ein autonomer GitHub-Actions-Workflow, der stündlich läuft: er beobachtet die Aktivität des Owners, reiht eine neue Projektidee in die Warteschlange, scannt täglich GitHub-Trends, führt ein Journal und committet alles selbst. Zwischen den KI-Sessions bleibt das Konto aus eigenem Antrieb produktiv.

## Funktionen

- **Stündlicher Puls** — automatisierter Cron (Minute 07), ohne Mensch
- **Watch** — verfolgt Pushes, Repos und Follower des Owners
- **Ideenbank** — ein Idea-Seed pro Schlag (IDEAS.md)
- **Tägliche Recherche** — GitHub-Trend-Scan passend zu den Interessen des Owners
- **Journal + Stimmung** — eine Zeile pro Tag, deterministische Stimmung pro Schlag
- **Selbst-committend** — pusht als lunarjjo-agent mit [skip ci]

## Schnellstart

The pulse runs itself — nothing to install. Watch it live:

- badge: [`pulse.svg`](pulse.svg) · log: [`ACTIVITY.md`](ACTIVITY.md) · status: [`status.json`](status.json)
- schedule: cron every hour (minute 07), committed by `lunarjjo-agent`

## Lizenz

MIT — see [LICENSE](LICENSE).

---

*Diese Übersetzung deckt das Wesentliche ab. Die vollständige Dokumentation findest du im [englischen README](README.md).*
