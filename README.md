# Korea Compass · Master Trip Planner

A calm, beginner-friendly South Korea trip-planning workspace. **Korea Compass** consolidates the travel research supplied across six repositories into one static GitHub Pages app, while preserving a local, attributed snapshot of the original source material.

**Live Pages URL:** <https://karagemop466-tech.github.io/KoreaMasterItinerary1/>

> This is a research and planning tool, not a booking engine or a live travel-data service. Verify event dates, prices, availability, entry requirements, transport operations, eligibility, health guidance, and emergency information with the relevant official provider before acting.

## What is in the master planner

- **Private trip setup** — optional dates, group size, and cities; it does not force a default itinerary.
- **Flexible timeline** — add, edit, delete, export, and import plan items when an itinerary is ready.
- **Searchable discovery library** — destinations, dated events, long-form activity ideas, restaurants, hotels, transit routes, and savings notes.
- **Saved ideas** — a browser-local shortlist of possibilities.
- **Transit kit** — airport transfer, intercity, payments, station, and app research in one place.
- **Bookings & prep** — a local completion checklist with an intentionally non-automated booking workflow.
- **Safety desk** — quick-dial contacts, printable emergency material, and offline-ready reminders.
- **Source desk** — clear provenance back to every linked repository and to the locally preserved snapshot.
- **Portable data** — export/import the user’s own setup, saved ideas, checklist state, and plan items as JSON. No account or backend is used.

The current generated catalog includes **6 research sources**, **15 destinations**, **15 transport routes**, **34 stays**, **535 food bookmarks**, **110 dated events**, **443 activity notes**, **61 savings notes**, and **9 practical apps**.

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

Use a local server instead of opening `index.html` directly: the browser loads the generated `data/catalog.json` with `fetch()`.

## GitHub Pages deployment

This repository is configured in GitHub Pages to deploy from:

- **Branch:** `main`
- **Folder:** `/ (root)`

The application is static and its entry point is [`index.html`](index.html), so a merge to `main` publishes it without a build workflow. The [`.nojekyll`](.nojekyll) marker keeps the source vault and static assets from being altered by Jekyll processing.

After merging, allow GitHub Pages a moment to publish, then use:

<https://karagemop466-tech.github.io/KoreaMasterItinerary1/>

## Refreshing source research

The browser reads one generated file: [`data/catalog.json`](data/catalog.json). The generator uses the committed source snapshots.

1. Refresh the relevant folder under `research/sources/` from the approved source repository.
2. Update the source revision table in this README and the metadata in [`scripts/build_catalog.py`](scripts/build_catalog.py).
3. Rebuild the catalog:

   ```bash
   python3 scripts/build_catalog.py
   ```

4. Review the diff, especially time-sensitive records and links.
5. Validate locally with a static server before merging to `main`.

## Planned next step

When the actual itinerary is available, add it through **My plan** (or import a prior export). The existing structure already supports dates, cities, free-form notes, reservations, transit legs, and source-backed saved ideas, so the detailed itinerary can be integrated without rebuilding the master repository.
