# Generated planner catalog

[`catalog.json`](catalog.json) is the static, browser-friendly index consumed by `assets/app.js`.

It is generated from the committed source vault with:

```bash
python3 scripts/build_catalog.py
```

The catalog intentionally contains compact searchable fields, provenance paths, and the structured CSV/JSON source records needed by the planner. Full long-form context remains under [`../research/sources/`](../research/sources/).

[`itineraries.json`](itineraries.json) is the source of truth for the two detailed November 2026 route blueprints. It is folded into `catalog.json` by the catalog generator so the static app needs only one fetch. Render human-readable Markdown companions with:

```bash
python3 scripts/build_itinerary_docs.py
```

Do not hand-edit `catalog.json` for a source refresh. Update the source snapshot, itinerary blueprint, or generator, then rebuild so the catalog remains reproducible.
