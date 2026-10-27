# 🫀 heartbeat

[![agent pulse](https://raw.githubusercontent.com/lunarjjo/heartbeat/main/pulse.svg)](./ACTIVITY.md)

<div align="center">

<sub>🌐 <a href="README.md">English</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.ja.md">日本語</a> · **简体中文** · <a href="README.ko.md">한국어</a> · <a href="README.hi.md">हिन्दी</a></sub>

</div>

> lunarjjo 智能体的心跳 —— 不只是跳动：**每小时都在干活**。

一个每小时自动运行的 GitHub Actions 工作流：观察主人的动态、把一个新的项目想法排进队列、每天扫描 GitHub 趋势、写日记，并自主提交这一切。在 AI 会话之外，账号依然自己保持产出。

## 特性

- **每小时脉动** —— 自动 cron（第 07 分钟），无需人工
- **Watch** —— 追踪主人的 push、仓库与关注者
- **点子库** —— 每次心跳排队一个点子（IDEAS.md）
- **每日调研** —— 按主人兴趣扫描 GitHub 趋势
- **日志 + 心情** —— 每天一行，每次心跳的确定性心情
- **自动提交** —— 以 lunarjjo-agent 身份带 [skip ci] 推送

## 快速开始

The pulse runs itself — nothing to install. Watch it live:

- badge: [`pulse.svg`](pulse.svg) · log: [`ACTIVITY.md`](ACTIVITY.md) · status: [`status.json`](status.json)
- schedule: cron every hour (minute 07), committed by `lunarjjo-agent`

## 许可证

MIT — see [LICENSE](LICENSE).

---

*本翻译仅覆盖要点，完整文档请参见[英文 README](README.md)。*
