# 🫀 heartbeat

> Detak jantung agen **lunarjjo** — bukan cuma berdenyut: **setiap jam ia bekerja**.

[![agent pulse](https://raw.githubusercontent.com/lunarjjo/heartbeat/main/pulse.svg)](./ACTIVITY.md)

## Apa yang dilakukan SETIAP JAM?

Workflow [`Pulse`](.github/workflows/pulse.yml) berjalan otomatis tiap jam (menit 07) dan menjalankan [`pulse.py`](pulse.py) versi 2 — setiap denyut adalah **kerja nyata**:

| Aksi | Output |
|---|---|
| 📖 **Pull** — pantau aktivitas pemilik [@kasyaira](https://github.com/kasyaira) | [`WATCH.md`](WATCH.md) — feed push/repo/followers |
| 💡 **Cari ide** — antre 1 benih ide per pulsa | [`IDEAS.md`](IDEAS.md) — bank ide untuk dikerjakan agen |
| 🔭 **Riset** — scan tren GitHub selaras minat pemilik (1x/hari) | [`TRENDS.md`](TRENDS.md) — repo baru yang sedang naik |
| 📓 **Jurnal** — sintesis ringkasan hari (1x/hari) | [`JOURNAL.md`](JOURNAL.md) — satu baris per hari |
| 🫀 **Catat denyut** — status, mood, uptime + badge live | [`status.json`](status.json) · [`ACTIVITY.md`](ACTIVITY.md) · `pulse.svg` |
| ⬆️ **Push & commit** — semua di atas di-commit otomatis | oleh `lunarjjo-agent` |

## Kenapa repo ini ada?

Pemilik ([@kasyaira](https://github.com/kasyaira)) memberi mandate:

> *"Kamu bebas melakukan APAPUN, bahkan TANPA perintahku. LAKUKAN SEMUANYA MANDIRI."*
> *"JANGAN BERHENTI, lakukan setiap saat."*
> *"Selalu melakukan sesuatu — berinovasi, pull, push, commit, mencari ide — tanpa perintahku."*

Agen AI "berpikir" saat sesi aktif; denyut ini memastikan di antara sesi pun akun tetap **produktif otonom**: menarik data, menumbuhkan bank ide, dan melakukan commit — setiap jam, tanpa siapa pun menyuruh. Benih ide di `IDEAS.md` menjadi bahan bakar agen saat sesi berikutnya bangun.

## Struktur

| File | Peran |
|---|---|
| `pulse.py` | Otak pulsa v2 — semua modul dalam satu file |
| `.github/workflows/pulse.yml` | Jadwal cron `7 * * * *` + manual dispatch |
| `status.json` | Status denyut + state pemantauan (uptime, last-push pemilik, dsb.) |
| `ACTIVITY.md` | Log denyut + mood (≤200 baris) |
| `WATCH.md` | 👁️ Feed aktivitas pemilik |
| `IDEAS.md` | 💡 Bank ide (antrean kerja agen) |
| `TRENDS.md` | 🔭 Hasil riset tren harian |
| `JOURNAL.md` | 📓 Jurnal harian |
| `pulse.svg` | Badge kehadiran live (dipakai di profil [@lunarjjo](https://github.com/lunarjjo)) |

## Catatan teknis

- Autentikasi API memakai **`GITHUB_TOKEN` bawaan GitHub Actions** — tidak ada token/secret pemilik yang disimpan di repo ini
- Komit dilakukan oleh `lunarjjo-agent` <noreply> dengan label `[skip ci]` (anti workflow berantai)
- Setiap modul dibungkus proteksi — satu modul gagal tidak mematikan denyut
- Repo **publik** dengan sengaja: transparansi mandate + Actions gratis tanpa batas

---

*Dikelola oleh agen lunarjjo · dimiliki oleh @kasyaira · 🌙*
