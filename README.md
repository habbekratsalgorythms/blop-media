# blop-media

Overdrachtspunt voor goedgekeurde Blop-video's (AI-personage, altijd als AI gelabeld).

- Claude levert: scripts, render, montage, kwaliteitscontrole en vrijgave.
- ChatGPT leest `releases/index.json` en verwerkt uitsluitend complete releases met `status: READY`: captions, hashtags, Metricool-planning, publicatie, analytics.
- MP4's staan als GitHub Release-assets (publieke URL, `media_url` in het manifest).

## Regels
- Een content-ID (`BLOP-0001`, ...) is uniek en wordt nooit hergebruikt.
- Een READY-release is definitief. Correcties krijgen een nieuw ID met `supersedes`.
- READY alleen na expliciete goedkeuring door de eigenaar via de Claude-workflow. Proef- en testvideo's zijn HOLD.
- Geen secrets, logs, persoonlijke bestanden of ongekeurde video's. Claude publiceert niets zelf.
