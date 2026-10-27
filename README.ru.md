# 🫀 heartbeat

[![agent pulse](https://raw.githubusercontent.com/lunarjjo/heartbeat/main/pulse.svg)](./ACTIVITY.md)

<div align="center">

<sub>🌐 <a href="README.md">English</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt.md">Português</a> · **Русский** · <a href="README.ja.md">日本語</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ko.md">한국어</a> · <a href="README.hi.md">हिन्दी</a></sub>

</div>

> Пульс агента **lunarjjo** — он не просто бьётся: **каждый час он работает**.

Автономный workflow GitHub Actions, запускающийся каждый час: следит за активностью владельца, добавляет в очередь новую идею проекта, ежедневно сканирует тренды GitHub, ведёт журнал и сам делает коммиты. Между сессиями ИИ аккаунт остаётся продуктивным сам по себе.

## Возможности

- **Часовой пульс** — автоматический cron (7-я минута), без человека
- **Watch** — отслеживает пуши, репо и подписчиков владельца
- **Банк идей** — одно семя идеи за удар (IDEAS.md)
- **Ежедневный ресёрч** — скан GitHub-трендов по интересам владельца
- **Журнал + настроение** — строка в день, детерминированное настроение
- **Самокоммиты** — пушит как lunarjjo-agent с [skip ci]

## Быстрый старт

The pulse runs itself — nothing to install. Watch it live:

- badge: [`pulse.svg`](pulse.svg) · log: [`ACTIVITY.md`](ACTIVITY.md) · status: [`status.json`](status.json)
- schedule: cron every hour (minute 07), committed by `lunarjjo-agent`

## Лицензия

MIT — see [LICENSE](LICENSE).

---

*Этот перевод описывает самое главное. Полная документация — в [английском README](README.md).*
