# 🫀 heartbeat

[![agent pulse](https://raw.githubusercontent.com/lunarjjo/heartbeat/main/pulse.svg)](./ACTIVITY.md)

<div align="center">

<sub>🌐 <a href="README.md">English</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.es.md">Español</a> · **Français** · <a href="README.de.md">Deutsch</a> · <a href="README.pt.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ko.md">한국어</a> · <a href="README.hi.md">हिन्दी</a></sub>

</div>

> Le battement de cœur de l'agent **lunarjjo** — il ne fait pas que battre : **chaque heure, il travaille**.

Un workflow GitHub Actions autonome qui tourne toutes les heures : il surveille l'activité du propriétaire, met en file une nouvelle idée de projet, scanne les tendances GitHub chaque jour, tient un journal et commit tout seul. Entre les sessions d'IA, le compte reste productif de lui-même.

## Caractéristiques

- **Pulsation horaire** — cron automatisé (minute 07), sans humain
- **Watch** — suit les pushes, repos et followers du propriétaire
- **Banque d'idées** — une graine d'idée par battement (IDEAS.md)
- **Recherche quotidienne** — scan des tendances GitHub aligné sur les intérêts du propriétaire
- **Journal + humeur** — une ligne par jour, humeur déterministe par battement
- **Auto-commit** — pousse en tant que lunarjjo-agent avec [skip ci]

## Démarrage rapide

The pulse runs itself — nothing to install. Watch it live:

- badge: [`pulse.svg`](pulse.svg) · log: [`ACTIVITY.md`](ACTIVITY.md) · status: [`status.json`](status.json)
- schedule: cron every hour (minute 07), committed by `lunarjjo-agent`

## Licence

MIT — see [LICENSE](LICENSE).

---

*Cette traduction couvre l'essentiel. Voir le [README anglais](README.md) pour la documentation complète.*
