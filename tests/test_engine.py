import pytest
from backend.engine import catalog, resolve_profile, compose_messages, clean_result


def test_catalog_has_both_media():
    profiles = catalog()
    assert len(profiles) >= 40
    assert {'image', 'video'} == {p['medium'] for p in profiles}
    assert resolve_profile('image_krea_2')
    assert resolve_profile('video_minimax_h3')


def test_free_without_model_generates_universal_instructions():
    msgs, meta = compose_messages({'medium': 'auto', 'free_prompt': 'a sunrise over the mountains', 'fields': {}})
    assert meta['profile'] is None
    assert 'UNIVERSAL' in msgs[0]['content'].upper() or 'universal' in msgs[0]['content']
    assert 'a sunrise over the mountains' in msgs[1]['content']
    assert 'DOCUMENTACIÓN ESPECÍFICA' not in msgs[0]['content']


def test_manual_fields_are_retained():
    msgs, _ = compose_messages({'medium': 'video', 'model_id': 'video_minimax_h3', 'free_prompt':'Un dragón aterriza', 'fields': {'iluminacion': {'selected':'Luz natural','manual':'una luz roja de emergencia'}}})
    assert 'MiniMax' in msgs[0]['content']
    assert 'una luz roja de emergencia' in msgs[1]['content']
    assert 'Un dragón aterriza' in msgs[1]['content']


def test_unknown_profile_is_rejected():
    with pytest.raises(ValueError):
        compose_messages({'model_id': '../../etc/passwd', 'free_prompt':'ok'})


def test_mismatched_media_is_rejected():
    with pytest.raises(ValueError):
        compose_messages({'medium':'image','model_id':'video_minimax_h3','free_prompt':'ok'})


def test_json_and_fallback():
    assert clean_result('{"prompt":"A scene", "negative_prompt":"blur"}')['negative_prompt'] == 'blur'
    assert clean_result('```json\n{"prompt":"An illustration"}\n```')['prompt'] == 'An illustration'
    assert clean_result('<think>internal</think>Final prompt')['prompt'] == 'Final prompt'


def test_empty_input_rejected():
    with pytest.raises(ValueError):
        compose_messages({'free_prompt':'', 'fields':{}})


def test_requested_negatives_are_exclusions_and_separate_from_scene():
    messages, _ = compose_messages({'free_prompt':'A quiet garden', 'negative_prompt':'blurry, text, watermark'})
    content = messages[1]['content'].split('\nWrite scene descriptions')[0]
    import json
    request = json.loads(content.split('\n', 1)[1])
    assert request['base_prompt'] == 'A quiet garden'
    assert request['negative_prompt'] == 'blurry, text, watermark'
    assert 'exclusiones' in messages[0]['content']
    assert 'nunca elementos que haya que añadir' in messages[0]['content']
