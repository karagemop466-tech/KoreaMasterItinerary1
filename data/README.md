# Generated planner catalog

[`catalog.json`](catalog.json) is the static, browser-friendly index consumed by `assets/app.js`.

It is generated from the committed source vault with:

```bash
python3 scripts/build_catalog.py
```

The catalog intentionally contains compact searchable fields, provenance paths, and the structured CSV/JSON source records needed by the planner. Full long-form context remains under [`../research/sources/`](../research/sources/).

Do not hand-edit `catalog.json` for a source refresh. Update the source snapshot or generator, then rebuild so the catalog remains reproducible.
