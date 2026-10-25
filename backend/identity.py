"""Separate known historical compound choices while retaining explicit dedicated fields."""
import json
from pathlib import Path

RULES = json.loads((Path(__file__).resolve().parents[1] / 'recursos/identity_legacy.json').read_text(encoding='utf-8'))


def normalize_identity(fields: dict) -> dict:
    result = {key:dict(value) if isinstance(value, dict) else value for key,value in fields.items()}
    for key,rules in RULES.items():
        original = fields.get(key)
        if not isinstance(original, dict):
            continue
        for kind in ('selected','manual'):
            rule = rules.get(str(original.get(kind) or '').strip())
            if rule:
                result[key][kind] = rule['value']
        effective = str(original.get('manual') or '').strip() or str(original.get('selected') or '').strip()
        for target,value in rules.get(effective, {}).get('extras', {}).items():
            current = result.get(target) or {}
            if not isinstance(current, dict) or not any(str(current.get(kind) or '').strip() for kind in ('selected','manual')):
                result[target] = {'selected':'','manual':value}
    return result
