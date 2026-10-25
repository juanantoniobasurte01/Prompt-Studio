"""Community open-weight engines; tags and sizes checked against author listings."""
FAMILIES = {
    'deepseek-r1-abliterated': ('DeepSeek R1 Abliterated', [('1.5b', 1.1), ('7b', 4.7), ('8b', 5.0), ('14b', 9.0)]),
    'dolphin3-abliterated': ('Dolphin 3 Abliterated', [('8b', 4.9)]),
    'gemma3-abliterated': ('Gemma 3 Abliterated', [('1b', 0.806), ('4b', 8.6), ('12b', 24.0)]),
    'llama3.2-abliterate': ('Llama 3.2 Abliterated', [('1b', 0.955), ('3b', 2.2)]),
    'qwen3-abliterated': ('Qwen 3 Abliterated', [('1.7b', 1.1), ('4b', 2.5), ('8b', 5.0), ('14b', 9.0), ('32b', 20.0)]),
}


def engine_catalog() -> list[dict]:
    return sorted([
        {'id': f'huihui_ai/{family}:{tag}', 'label': f'{label} {tag.upper()}',
         'size_gb': size, 'source': f'https://ollama.com/huihui_ai/{family}',
         'category': 'uncensored', 'verified': '2026-10-23'}
        for family, (label, variants) in FAMILIES.items() for tag, size in variants
    ], key=lambda entry: entry['label'].casefold())
