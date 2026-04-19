# Docker Generation Notes

Use Docker for all notebook package generation in this repository.

## Why

- Host `python` may be missing.
- Windows PowerShell can write UTF-8 BOM by default in some paths.
- Jupyter RTC can fail to open `.ipynb` files that start with BOM.

## Standard Command

```bash
docker compose run --rm --no-deps \
  jupyter \
  python /workspace/scripts/generate_aice_associate.py \
  --profile /workspace/notebooks/credit-card-fraud-associate/profile.json \
  --output-dir /workspace/notebooks/credit-card-fraud-associate
```

## Rules

- The profile path should live with the target notebook package, for example `/workspace/notebooks/<dataset-dir>/profile.json`.
- The output directory is resolved under `/workspace/notebooks/`.
- Generated notebooks must be UTF-8 without BOM.
- Validation should fail if BOM is present.
- If a notebook package includes Mermaid source assets (`*.mmd`), render them to `.svg` with `python /workspace/scripts/render_mermaid_assets.py` before final review.
- Mermaid asset rendering uses `mermaido`, so the image cache should be prepared once with `mermaido install` inside the environment.

## Generator Layout

- `generate_aice_associate.py`: CLI entry point only
- `render_mermaid_assets.py`: render Mermaid `.mmd` assets to `.svg`
- target notebook directory: profile JSON lives next to the generated package, e.g. `notebooks/<dataset-dir>/profile.json`
- `aice_generator/loader.py`: profile loading and normalization
- `aice_generator/models.py`: reusable dataclasses for profile, question, column specs
- `aice_generator/notebook.py`: notebook cell and notebook rendering
- `aice_generator/validator.py`: structural validator template generation
- `aice_generator/builder.py`: package writing orchestration

When adding a new exam, create `profile.json` inside the target notebook directory first and only extend shared modules when the new need is reusable across multiple datasets.
