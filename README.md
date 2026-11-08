# kindle-oasis-hack

Configuration bundle for a jailbroken first-gen Kindle Oasis: KOReader, Chinese/English RSS feeds, verified Chinese manga sources, and an optional DeepSeek-backed reading assistant.

[中文安装记录](docs/SETUP.zh-CN.md) · [Usage](docs/USAGE.md) · [Privacy](SECURITY.md)

This repository contains a documented setup process and **credential-free examples** — not a device backup, not a firmware image, no copyrighted content.

## Reference device

- Kindle Oasis 1 (2016, 8th generation), Wi-Fi
- Firmware: **5.16.2.1.1**
- Setup recorded October–November 2026

Do not assume these packages work on another model or firmware. The boundary at firmware 5.16.3 changes the KOReader/ARM build required.

## Components

| Component | Recorded version | Purpose |
|---|---|---|
| WinterBreak2 | 1.1.0 | Jailbreak entry; installed jailbreak script reported 2.4.0 |
| KOReader | 2026.07.1, `kindlepw2` | EPUB, PDF, CBZ and plugins |
| KUAL / PEKI | Upstream release used during setup | Launcher |
| WeRead plugin | 1.6.0 | WeRead books and account sync |
| SimpleUI | 3.0.1 | Home screen and shortcuts |
| RSS Reader | 1.21.0 | Local Chinese/English feed accounts |
| ECDICT | 1.0.28 StarDict release | Offline English–Chinese lookup |
| AI Assistant | 1.21 | DeepSeek-backed translation/explanations (key left blank, fill on device) |
| ComicReader | 0.0.7 | Optional dual-page comic display |
| Rakuyomi | 1.44.3, `kindlea9` | Manga source search and chapter download |

## What's seeded in `config/`

- **RSS** — 3 local accounts: `必读 AI 博客 Top 6` (Simon Willison / Lilian Weng / Armin Ronacher / Chip Huyen / Hamel Husain / Nathan Lambert), plus a verified-China-direct group `中文 AI 源 · 2026-11` (Kexue.fm, Baoyu, QbitAI, Meituan Tech, InfoQ, Tw93, pseudoyu, DIYgod, V2EX). Jiqizhixin, 36Kr and CoolShell were tested and **rejected** (broken XML or timeouts).
- **Rakuyomi** — settings enable the `zh` language tag so Chinese sources appear; four verified-direct sources: `zh.baozimanhua`, `zh.manhuagui`, `zh.dm5`, `zh.mangabz`. `multi.mangadex` was removed after confirming api.mangadex.org times out on the reference Wi-Fi. Page concurrency is 4 for the single-core Oasis.
- **Assistant** — DeepSeek preset (`deepseek-flash`, api.deepseek.com) with an **empty** `api_key`.

## Start here

1. Read [the setup record](docs/SETUP.zh-CN.md) and the upstream jailbreak guide for your exact device.
2. Download releases from upstream projects, not from untrusted mirrors.
3. Back up privately, install one component at a time, restart KOReader between changes.
4. Enter login/API credentials **on the device**; never commit them here.
5. Use [the examples](config/) as merge references, not drop-in replacements for live settings.

## Privacy boundary

No device serials, Wi-Fi data, API keys, session state, books, reading history, or SQLite databases are in this repo. See [SECURITY.md](SECURITY.md) and run `python3 scripts/check-publication.py` before pushing anything.

## Upstream projects

[Kindle Modding](https://kindlemodding.org/) · [KOReader](https://github.com/koreader/koreader) · [WeRead](https://github.com/finlater/weread.koplugin) · [SimpleUI](https://github.com/doctorhetfield-cmd/simpleui.koplugin) · [RSS Reader](https://github.com/omer-faruq/rssreader.koplugin) · [ECDICT](https://github.com/skywind3000/ECDICT) · [AI Assistant](https://github.com/omer-faruq/assistant.koplugin) · [ComicReader](https://github.com/KORComic/comicreader.koplugin) · [Rakuyomi](https://github.com/tachibana-shin/rakuyomi)

Upstream software and content retain their respective licenses; nothing copyrighted is redistributed here. This repo's own docs/configs follow the LICENSE in this repository.
