from __future__ import annotations

import sqlite3
import time
from pathlib import Path


def connect(db_path: Path) -> sqlite3.Connection:
    return sqlite3.connect(db_path)


def wait_for_table(db_path: Path, table_name: str, timeout_seconds: int = 60) -> None:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        if db_path.exists():
            with connect(db_path) as conn:
                row = conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                    (table_name,),
                ).fetchone()
                if row:
                    return
        time.sleep(1)
    raise TimeoutError(f"Timed out waiting for table '{table_name}' in {db_path}")
