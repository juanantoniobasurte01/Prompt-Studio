"""Local-only SQLite persistence. No cloud services or tracking."""
from __future__ import annotations
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
DB = Path(os.environ.get('PROMPT_STUDIO_DB', str(ROOT / 'data' / 'prompts.sqlite3')))


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def connect():
    DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init():
    with connect() as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS presets (
                id TEXT PRIMARY KEY, name TEXT NOT NULL, content TEXT NOT NULL, created TEXT NOT NULL, updated TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS history (
                id TEXT PRIMARY KEY, content TEXT NOT NULL, created TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS ix_history_created ON history(created DESC);
        ''')


def list_records(table: str, limit: int = 100):
    if table not in ('presets', 'history'):
        raise ValueError('Unknown table')
    with connect() as conn:
        rows = conn.execute(f'SELECT * FROM {table} ORDER BY {"updated" if table == "presets" else "created"} DESC LIMIT ?', (limit,)).fetchall()
    return [{**dict(row), 'content': json.loads(row['content'])} for row in rows]


def save(table: str, content: dict, name: str | None = None, key: str | None = None):
    if table not in ('presets', 'history'):
        raise ValueError('Unknown table')
    key, timestamp = key or str(uuid4()), now()
    with connect() as conn:
        if table == 'presets':
            if not (name or '').strip():
                raise ValueError('El preset necesita un nombre.')
            conn.execute('''INSERT INTO presets(id,name,content,created,updated) VALUES(?,?,?,?,?)
                ON CONFLICT(id) DO UPDATE SET name=excluded.name, content=excluded.content, updated=excluded.updated''',
                (key, name.strip()[:120], json.dumps(content, ensure_ascii=False), timestamp, timestamp))
        else:
            conn.execute('INSERT INTO history VALUES (?,?,?)', (key, json.dumps(content, ensure_ascii=False), timestamp))
            conn.execute('DELETE FROM history WHERE id NOT IN (SELECT id FROM history ORDER BY created DESC LIMIT 500)')
    return key


def remove(table: str, key: str):
    if table not in ('presets', 'history'):
        raise ValueError('Unknown table')
    with connect() as conn:
        count = conn.execute(f'DELETE FROM {table} WHERE id=?', (key,)).rowcount
    return bool(count)
