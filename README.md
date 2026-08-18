# Korea Compass · Master Trip Planner

A calm, beginner-friendly South Korea trip-planning workspace. **Korea Compass** consolidates the travel research supplied across six repositories into one static GitHub Pages app, while preserving a local, attributed snapshot of the original source material.

**Live Pages URL:** <https://karagemop466-tech.github.io/KoreaMasterItinerary1/>

> This is a research and planning tool, not a booking engine or a live travel-data service. Verify event dates, prices, availability, entry requirements, transport operations, eligibility, health guidance, and emergency information with the relevant official provider before acting.

## What is in the master planner

- **Private trip setup** — optional dates, group size, and cities; it does not force a default itinerary.
- **Trip countdown & prep progress** — once dates are set, the overview shows days-to-departure (or your current trip day) plus booking-checklist progress.
- **10 detailed route blueprints** — compare 5 Seoul → Daejeon → Busan → Seoul routes and 5 Seoul → Cheonan → Busan → Seoul routes for the actual Nov. 1–22, 2026 travel window; load any blueprint into the editable planner. Each route deep-links (`#/itineraries/<id>`) and prints as a clean paper itinerary.
- **Interactive decision lens & comparative matrix** — weight your priorities (middle-city experience, rail ease, value, flexibility) and compare any 2 blueprints side by side across all 22 days.
- **Flexible timeline** — add, edit, delete, export, and import plan items when an itinerary is ready. Export as PDF via the browser print dialog, Word-compatible `.doc`, plain `.txt`, JSON, calendar (`.ics`), or CSV.
- **Searchable discovery library** — destinations, dated events, long-form activity ideas, restaurants, hotels, transit routes, and savings notes. Ranked search with highlighted matches, a `/` keyboard shortcut, and a "During my trip dates" filter that surfaces events overlapping your travel window.
- **Offline-ready PWA** — a service worker caches the shell and research data, so a visited planner keeps working without roaming data; it can be installed to a phone home screen.
- **Saved ideas** — a browser-local shortlist of possibilities.
- **Transit kit** — airport transfer, intercity, payments, station, and app research in one place.
- **Bookings & prep** — a local completion checklist with an intentionally non-automated booking workflow.
- **Safety desk** — quick-dial contacts, printable emergency material, and offline-ready reminders.
- **Source desk** — clear provenance back to every linked repository and to the locally preserved snapshot.
- **Portable data** — export/import the user’s own setup, saved ideas, checklist state, and plan items as JSON. No account or backend is used.

The current generated catalog includes **6 research sources**, **10 detailed November 2026 route blueprints**, **15 destinations**, **15 transport routes**, **34 stays**, **50 food bookmarks** (post 18 Aug 2026 audit — 485 template-generated placeholder rows removed after failing verification), **110 dated events**, **437 activity notes** (6 duplicate entries removed), **61 savings notes**, and **9 practical apps**.

## November 2026 route blueprints

The app's **Route options** screen contains detailed, interactive versions of all 10 blueprints. The readable documents are also committed for review or printing:

- [Compare all 10 route blueprints overview](itineraries/README.md)

### Corridor 1: Seoul · Daejeon · Busan (5 Blueprints)
- [1. Classic Explorer (Balanced Heritage & City Depth)](itineraries/seoul-daejeon-busan-classic.md) — Gyeongbokgung, National Science Museum, Sung Sim Dang 1956 bakery, Haeundae Blueline beach train, Jagalchi.
- [2. Foodie & Market Trail (Gastronomy & Street Eats)](itineraries/seoul-daejeon-busan-foodie.md) — Gwangjang, Majang 1++ Hanwoo beef, Daejeon kalguksu & dubu duruchigi, Jagalchi live king crab, Bupyeong night market.
- [3. Heritage & Fine Arts (Joseon Dynasty & Aesthetics)](itineraries/seoul-daejeon-busan-heritage.md) — Changdeokgung Huwon Secret Garden, Leeum Museum, Lee Ungno modernist gallery, Beomeosa mountain temple, F1963 arts space.
- [4. Wellness & Nature (Thermal Springs & Mountain Ridges)](itineraries/seoul-daejeon-busan-wellness.md) — Bukhansan National Park, Yuseong natural mineral hot springs, Gyejoksan red clay earthing, Centum Spa Land hydrotherapy.
- [5. Modern & Pop Culture (K-Innovation & Esports)](itineraries/seoul-daejeon-busan-modern.md) — DDP, Seongsu concept lofts, LoL Park LCK esports arena, KAIST innovation campus, Gwangalli Saturday drone show.

### Corridor 2: Seoul · Cheonan · Busan (5 Blueprints)
- [6. Rail Classic Explorer (Scenic Rail Corridor & Independence Heritage)](itineraries/seoul-cheonan-busan-rail.md) — Lightning 35-min KTX leap, Independence Hall of Korea & Maple Tree Tunnel, Gakwonsa Bronze Buddha, Choryang 168 monorail.
- [7. Value & Local Living (Smart Value & Neighborhood Markets)](itineraries/seoul-cheonan-busan-value.md) — Free Naksan city wall sunset, Tongin brass coin lunchbox, Cheonan Namsan market kalguksu, Dadaepo sunset wetlands.
- [8. Gentle Leisure & Family Comfort (Family Pacing & Open Parks)](itineraries/seoul-cheonan-busan-leisure.md) — Relaxed 10:00 AM starts, Lotte World Tower & Aquarium, Sono Belle thermal waterpark, Hong Dae-yong planetarium, Haeundae Sky Capsules.
- [9. Contemporary Art & Architecture (World Sculpture Parks & Design)](itineraries/seoul-cheonan-busan-arts.md) — Arario Museum in SPACE, Arario Sculpture Park Cheonan (Damien Hirst, Keith Haring), P.ARK shipyard amphitheater, MoCA Busan.
- [10. Regional Gourmet & Artisans (Temple Cuisine & Historic Lineages)](itineraries/seoul-cheonan-busan-gourmet.md) — Balwoo Gongyang Michelin temple food, 1934 Hakhwa Hodu-gwaja, Byeongcheon soondae alley, Dongnae royal pajeon & master makgeolli.

All routes use the corrected travel window: **arrive at ICN at 21:00 on November 1, 2026; depart ICN at 13:00 on November 22, 2026 (21 nights / 22 calendar days)**. They use a 7-night first Seoul leg, 5 nights in the middle city, 7 nights in Busan, and 2 final Seoul nights. That final Seoul buffer is intentional: it protects the international departure from a risky same-day Busan-to-ICN connection.

Each day has explicit target schedule windows, operational/routing notes, reservation checks, food rhythm, cost posture, watchouts, and Plan B fallbacks.

## Research provenance

The source snapshots are retained under [`research/sources/`](research/sources/) so the planner can be refreshed without adding a live scraping dependency to GitHub Pages.

| Source | Imported focus | Source revision used |
| --- | --- | --- |
| [Koreatransport](https://github.com/sassnarep3-star/Koreatransport/tree/arena/019fc955-koreatransport) | routes, airport transfers, cards, apps, stations, logistics | `arena/019fc955-koreatransport` · `251cb01079fa` |
| [Korea-hotels](https://github.com/karagemop466-tech/Korea-hotels/tree/arena/019fc93d-korea-hotels) | hotel comparison data and city/stay guides | `arena/019fc93d-korea-hotels` · `59528de282b2` |
| [KoreaFun](https://github.com/karagemop466-tech/KoreaFun) | events, activities, walking and trip ideas | `main` · `7b075aee8852` |
| [Koreafood](https://github.com/karagemop466-tech/Koreafood) | food bookmarks, city guides, booking notes | `main` · `d373e09b129d` |
| [Korea](https://github.com/buffedlizard55-lab/Korea) | savings, promotions, visitor-action guides | `main` · `9852a2763808` |
| [Korea-emergency](https://github.com/buffedlizard55-lab/Korea-emergency/tree/arena/019fd2e4-korea-emergency) | preparation, emergency contacts, checklists, scenario guides | `arena/019fd2e4-korea-emergency` · `7073740c6d28` |

Source content is a snapshot as of the master-catalog pass on **2026-08-07**. Its inclusion does **not** represent independent re-verification of every claim.

## Run locally

There is no package manager, framework, API key, or build step required for the app.

```bash
python3 -m http.server 8000
# Open http://localhost:8000
```

Use a local server instead of opening `index.html` directly: the browser loads the generated `data/index.json` (and collection files) with `fetch()`.

## GitHub Pages deployment

This repository is configured in GitHub Pages to deploy from:

- **Branch:** `main`
- **Folder:** `/ (root)`

The application is static and its entry point is [`index.html`](index.html), so a merge to `main` publishes it without a build workflow. The [`.nojekyll`](.nojekyll) marker keeps the source vault and static assets from being altered by Jekyll processing.

After merging, allow GitHub Pages a moment to publish, then use:

<https://karagemop466-tech.github.io/KoreaMasterItinerary1/>

## Refreshing source research

The browser reads a small generated index plus per-collection files. The generator uses the committed source snapshots and fails the build if any URL looks like a scraping artifact (odd ports, localhost hosts).

1. Refresh the relevant folder under `research/sources/` from the approved source repository.
2. Update the source revision table in this README and the metadata in [`scripts/build_catalog.py`](scripts/build_catalog.py).
3. Rebuild the catalog:

   ```bash
   python3 scripts/build_catalog.py
   ```

4. If a detailed route blueprint changed, re-render its readable Markdown companion:

   ```bash
   python3 scripts/build_itinerary_docs.py
   ```

5. Review the diff, especially time-sensitive records and links.
6. Validate locally with a static server before merging to `main`.

The PWA icons under `assets/icons/` are rendered reproducibly from vector math (no image tooling required):

```bash
python3 scripts/make_icons.py
```

## Planned next step

Open **Route options**, filter and compare the 10 route blueprints, adjust the decision lens sliders, and use **Use as my editable plan** on your preferred blueprint. The planner will load all 22 calendar days as editable items; hotel confirmations, exact KTX trains, restaurant reservations, and any personal itinerary changes can then be layered in without rebuilding the master repository. From Route options you can export any complete blueprint as PDF (browser print), Word-compatible `.doc`, or `.txt`; from My plan you can export the edited version in those formats plus JSON, calendar, and CSV.
