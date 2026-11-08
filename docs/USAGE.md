# Daily use

- **Launch:** native Kindle library → KUAL → KOReader → Start KOReader.
- **WeRead:** Tools → WeRead → QR login. Confirm on your own phone.
- **RSS:** RSS Reader → 中文阅读 or 英文阅读 → category → feed. The 必读 AI 博客 Top 6 account aggregates Simon Willison, Lilian Weng, Armin Ronacher, Chip Huyen, Hamel Husain, Nathan Lambert. 中文阅读 → 中文 AI 源 · 2026-11 covers 9 additional verified-China-direct Chinese AI feeds (Kexue.fm, Baoyu, QbitAI, Meituan, InfoQ, Tw93, pseudoyu, DIYgod, V2EX). Jiqizhixin / 36Kr / CoolShell are **not** in the list because their RSS markup fails the reader's stock parser.
- **Dictionary:** long-press an English word. Review saved words in Vocabulary Builder.
- **Notes:** use Export highlights with Markdown enabled; copy exported files privately to your computer.
- **AI:** AI Assistant → Settings → Providers and Models → edit DeepSeek → enter your own API Key → Test → Save. Select a short passage and choose Translate / Explain. Labels can vary with translation/version.
- **Local comics:** open CBZ/PDF from the file manager. Single page is a good starting point on a 6-inch Oasis; ComicReader adds optional dual-page settings.
- **Online manga:** Rakuyomi → Search mangas → pick a title → long-press a chapter to download. The `zh` language is enabled in settings.example.json; four direct-connect Chinese sources (zh.baozimanhua, zh.manhuagui, zh.dm5, zh.mangabz) come verified in this seed config. One-Piece Chapter 1 is pre-downloaded to `documents/Comics/海贼王-第01话.cbz`; additional manga can be fetched on demand.

Normally exit KOReader before connecting USB to edit configuration. Restart KOReader after changes. A full device reboot is a recovery measure, not a substitute for diagnosing recurring failures.

HTTP inspector and SSH are not enabled by these examples. If temporarily enabled for diagnostics, disable the service and auto-start afterwards; do not expose them to the Internet.
