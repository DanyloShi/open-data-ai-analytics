from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from flask import Flask, render_template, send_from_directory

from common.pipeline_config import PLOTS_DIR, REPORTS_DIR, ensure_directories

app = Flask(__name__, template_folder="templates", static_folder="static")


def _read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


@app.get("/")
def index():
    ensure_directories()
    quality = _read_json(REPORTS_DIR / "quality_report.json")
    research = _read_json(REPORTS_DIR / "research_report.json")
    viz = _read_json(REPORTS_DIR / "visualization_report.json")
    plots = viz.get("plots", []) if isinstance(viz, dict) else []
    return render_template(
        "index.html",
        quality=quality,
        research=research,
        plots=plots,
    )


@app.get("/plots/<path:filename>")
def plots(filename: str):
    return send_from_directory(PLOTS_DIR, filename)


if __name__ == "__main__":
    ensure_directories()
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
