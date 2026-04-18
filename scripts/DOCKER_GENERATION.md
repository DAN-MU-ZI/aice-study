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
  --profile /workspace/scripts/aice_generator/specs/credit-card-fraud-associate.json \
  --output-dir /workspace/notebooks/credit-card-fraud-associate
```

## Rules

- The profile path is resolved under `/workspace/scripts/`.
- The output directory is resolved under `/workspace/notebooks/`.
- Generated notebooks must be UTF-8 without BOM.
- Validation should fail if BOM is present.

## Generator Layout

- `generate_aice_associate.py`: CLI entry point only
- `aice_generator/specs/`: reusable dataset profile JSON files
- `aice_generator/loader.py`: profile loading and normalization
- `aice_generator/models.py`: reusable dataclasses for profile, question, column specs
- `aice_generator/notebook.py`: notebook cell and notebook rendering
- `aice_generator/validator.py`: structural validator template generation
- `aice_generator/builder.py`: package writing orchestration

When adding a new exam, prefer creating a new profile JSON first and only extend shared modules when the new need is reusable across multiple datasets.
