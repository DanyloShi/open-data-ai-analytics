# Air Quality DevOps Pipeline

A minimal project for two labs:

- **Lab 2**: CI/CD with GitHub Actions (GitHub-hosted and self-hosted).
- **Lab 3**: Docker-based service architecture with `compose.yaml`.

## Project structure

- `data_load/` - reads CSV and loads SQLite database.
- `data_quality_analysis/` - computes quality metrics.
- `data_research/` - computes basic statistics.
- `visualization/` - builds 2 PNG charts.
- `web/` - shows reports and plots in browser.
- `common/` - shared paths and DB helpers.
- `compose.yaml` - starts all services.

## Local run without Docker

```bash
python3 data_load/app.py
python3 data_quality_analysis/app.py
python3 data_research/app.py
python3 visualization/app.py
python3 web/app.py
```

Default outputs are written into `artifacts/`.

## Docker run (Lab 3)

```bash
docker compose up --build
```

Open <http://localhost:8080>.

## CI/CD (Lab 2)

- `.github/workflows/ci.yml`:
  - triggers on `push`, `pull_request`, `workflow_dispatch`;
  - runs modules in parallel with matrix strategy;
  - uploads logs/reports/plots as artifacts.

- `.github/workflows/ci-selfhosted.yml`:
  - manual run on self-hosted runner;
  - runs one selected module and uploads artifacts.
