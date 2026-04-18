# Agent Instructions

Use the repository Docker environment as the default execution path for all notebook generation, validation, and Jupyter work.

## Default Environment

- Default image: `aice-study-jupyter`
- Default services: `jupyter`, `jupyter-mcp`
- Compose file: `docker-compose.yml`
- Workspace in container: `/workspace`
- Notebook root in container: `/workspace/notebooks`

## Execution Rules

- Start from Docker first:

```bash
docker compose up --build -d jupyter jupyter-mcp
```

- Do not rely on host `python` for notebook generation or validation.
- Prefer `docker compose run --rm --no-deps jupyter ...` for one-off generation tasks.
- Prefer `docker compose exec -T jupyter ...` only when the Jupyter service is already running and you need to inspect the live container state.

## Notebook File Safety

- All generated `.ipynb` files must be saved as UTF-8 without BOM.
- Do not use Windows PowerShell `Set-Content -Encoding UTF8` for notebook output unless you explicitly remove BOM.
- Validation must fail if a generated notebook starts with the UTF-8 BOM bytes `EF BB BF`.

## Generator Rule

- The canonical generator is `scripts/generate_aice_associate.py`.
- All problem statements, instructions, headings, and guidance cells in generated notebooks must be written in Korean.
- Run it through Docker with:

```bash
docker compose run --rm --no-deps jupyter \
  python /workspace/scripts/generate_aice_associate.py \
  --profile /workspace/scripts/aice_generator/specs/<profile-json> \
  --output-dir /workspace/notebooks/<dataset-dir>
```

- Example:

```bash
docker compose run --rm --no-deps jupyter \
  python /workspace/scripts/generate_aice_associate.py \
  --profile /workspace/scripts/aice_generator/specs/credit-card-fraud-associate.json \
  --output-dir /workspace/notebooks/credit-card-fraud-associate
```

## Notes

- `./notebooks` is mounted to `/workspace/notebooks`.
- `./scripts` is mounted read-only to `/workspace/scripts`.
- If the image changes, rebuild with `docker compose build`.
- Prefer Jupyter MCP for notebook-native editing and verification when it is available in the session.
