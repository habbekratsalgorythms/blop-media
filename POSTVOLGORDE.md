# Blop tipfilms - postvolgorde (16 nov 2026)
Volgorde van alle 18 tipfilms (previews/blop-tip-<naam>-60fps.mp4). Regel: geen twee aangrenzende films met hetzelfde product/thema; kabels (4 films), wifi/router (2), account-beveiliging (4) en AI (2) staan nooit achter elkaar, en twee films met een telefoon als held-prop ook niet. Gecontroleerd met een script op de thema-tags hieronder (0 aangrenzende paren).

| # | film | thema | batch | muziek |
|---|------|-------|-------|---|
| 1 | cable-label | kabels | batch 1 | 0 |
| 2 | phone-lens | telefoon (camera) | batch 2 | 1 |
| 3 | monitor-height | scherm/ergonomie | batch 2 | 2 |
| 4 | two-step-login | account-beveiliging (telefoon) | batch 1 | 0 |
| 5 | usbc-which | kabels | batch 1 | 0 |
| 6 | ai-prompt | AI | batch 2 | 3 |
| 7 | router-spot | wifi/router | batch 2 | 0 |
| 8 | email-link | account-beveiliging (mail) | batch 2 | 1 |
| 9 | binder-clip | kabels | batch 1 | 0 |
| 10 | webcam-light | beeldbellen/licht | batch 2 | 2 |
| 11 | 321-backup | data/opslag | batch 1 | 0 |
| 12 | reopen-tab | browser/toetsenbord | batch 2 | 3 |
| 13 | coil-over-under | kabels | batch 1 | 0 |
| 14 | laptop-vents | laptop (hardware) | batch 2 | 1 |
| 15 | passphrase | account-beveiliging (wachtwoord) | batch 1 | 0 |
| 16 | wifi-24-or-5 | wifi/router | batch 1 | 0 |
| 17 | ai-sources | AI | batch 1 | 0 |
| 18 | auto-update | account-beveiliging (software) | batch 2 | 2 |

Muziek (17 nov 2026): precies 4 liedjes (0 = origineel pizzicato, 1 = marimba-arpeggio, 2 = stuiterend staccato, 3 = kalme pad). Batch 1 = 0 (live, niet aangeraakt); batch 2 zo gekozen dat geen twee buren dezelfde variant hebben (batch-2 films naast een batch-1 film zijn nooit 0). Vastgelegd als `music_variant` in concepts/blop-tip-<naam>.json.

Opmerking: de eerste batch (9 films) staat zo gemengd dat de 4 kabelfilms op plek 1, 5, 9 en 13 vallen (minimaal 3 andere films ertussen). Bij uitval van een film schuift de rest op; controleer dan opnieuw dat buren niet hetzelfde thema hebben.

## Metricool-overdracht voor Claude (17 nov 2026)

Dit is de feitelijke planning van de eerste goedgekeurde batch op TikTok. De onderstaande berichten zijn ingepland voor automatische publicatie; een geslaagde publicatie op TikTok is nog niet vastgesteld. Tijdzone: Europe/Amsterdam. Controleer bij vervolgwerk eerst planner én gepubliceerde video’s op hetzelfde onderwerp/ID om dubbelen te voorkomen.

| Content-ID | Geplande datum en tijd | Metricool-post-ID | Stand |
|---|---|---:|---|
| BLOP-0001 | 18-11-2026 10:00 | 432003082 | PENDING |
| BLOP-0002 | 19-11-2026 10:00 | 432003702 | PENDING |
| BLOP-0003 | 20-11-2026 10:00 | 432023633 | PENDING |
| BLOP-0004 | 21-11-2026 10:00 | 432004432 | PENDING |
| BLOP-0005 | 22-11-2026 10:00 | 432004536 | PENDING |
| BLOP-0006 | 23-11-2026 10:00 | 432023742 | PENDING |
| BLOP-0007 | 24-11-2026 10:00 | 432004647 | PENDING |
| BLOP-0008 | 25-11-2026 10:00 | 432004771 | PENDING |
| BLOP-0009 | 26-11-2026 10:00 | 432004846 | PENDING |

Alle zeven zijn teruggelezen met een MP4-bijlage, `autoPublish: true` en `tiktokData.isAigc: true`. De captions zijn op onderwerp gekoppeld aan CAPTIONS.md, met de vijf hashtags en `Blop is an AI character.`. De negen bronvideo’s van BLOP-0001 t/m 0009 gaven HTTP 200 en een passende SHA-256 conform releases/index.json. Vóór planning was de toekomstige planner leeg en toonden de beschikbare TikTok-analytics sinds 1 november geen gepubliceerde video.

**Update later op 17 november:** CAPTIONS.md op main bevat nu voor secties 2 en 3 `GEREED` met verwijzingen naar de uitgewerkte captions in §10 en §11. Na hercontrole van de bronvideo's en van de planner zijn BLOP-0003 en BLOP-0006 op de vrije dagen 20 en 23 november ingepland. Alle negen TikTok-combinaties uit de expliciet goedgekeurde batch zijn daarmee ingepland, ieder op een afzonderlijke dag. De eerdere blokkade is opgelost. BLOP-0010 t/m 0018 zijn buiten deze goedgekeurde batch gelaten.

**Invoer voor de koppeling:** de publieke MP4-URL werkt als item in `info.media`, met `providers: [{"network":"tiktok"}]`, `publicationDate` in Europe/Amsterdam, `autoPublish: true`, `tiktokData.title` en `tiktokData.isAigc: true`. Het aparte `mediaFiles`-argument wees een GitHub-URL als bestandspad af; een lokaal pad gaf `INVALID_ARGUMENT`. Na de werkende invoer nam Metricool de media over. De reeds ingeplande volgorde volgt content-ID’s en is niet de gemengde creatieve volgorde in de tabel hierboven; wijzig bestaande posts niet zonder opdracht.
