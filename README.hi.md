# 🫀 heartbeat

[![agent pulse](https://raw.githubusercontent.com/lunarjjo/heartbeat/main/pulse.svg)](./ACTIVITY.md)

<div align="center">

<sub>🌐 <a href="README.md">English</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ko.md">한국어</a> · **हिन्दी**</sub>

</div>

> lunarjjo एजेंट की धड़कन — यह केवल धड़कता नहीं है: **हर घंटे, यह काम करता है**।

एक स्वायत्त GitHub Actions वर्कफ़्लो जो हर घंटा चलता है: मालिक की गतिविधि देखता है, एक नया प्रोजेक्ट-विचार कतार में डालता है, रोज़ GitHub ट्रेंड स्कैन करता है, डायरी रखता है, और सब कुछ खुद कमिट करता है। AI सत्रों के बीच भी खाता अपने आप उत्पादक रहता है।

## विशेषताएँ

- **घंटेवार धड़कन** — स्वचालित cron (मिनट 07), बिना मानव
- **Watch** — मालिक के push, रेपो और फ़ॉलोअर्स ट्रैक करता है
- **विचार-बैंक** — हर धड़कन में एक बीज (IDEAS.md)
- **दैनिक रिसर्च** — मालिक की रुचि के अनुसार GitHub ट्रेंड स्कैन
- **डायरी + मूड** — रोज़ एक पंक्ति, हर धड़कन का निश्चित मूड
- **स्वतः-कमिट** — lunarjjo-agent के रूप में [skip ci] के साथ पुश

## त्वरित शुरुआत

The pulse runs itself — nothing to install. Watch it live:

- badge: [`pulse.svg`](pulse.svg) · log: [`ACTIVITY.md`](ACTIVITY.md) · status: [`status.json`](status.json)
- schedule: cron every hour (minute 07), committed by `lunarjjo-agent`

## लाइसेंस

MIT — see [LICENSE](LICENSE).

---

*यह अनुवाद केवल मुख्य बातें देता है। पूरे दस्तावेज़ के लिए [अंग्रेज़ी README](README.md) देखें।*
