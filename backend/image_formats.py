"""Validate explicitly requested image prompt structures, not visual quality."""
import json


FORMAT_ERROR = 'El modelo local no ha respetado el formato de imagen solicitado. Vuelve a generar.'


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _box(value):
    return (isinstance(value, list) and len(value) == 4
            and all(type(n) is int and 0 <= n <= 1000 for n in value)
            and value[0] < value[2] and value[1] < value[3])


def validate_image_format(output, prompt_format, required_sections=()):
    """Reject malformed native JSON/required edit sections before copying them."""
    prompt = output['prompt']
    try:
        if prompt_format in ('json', 'ideogram_json'):
            data = json.loads(prompt)
            if not isinstance(data, dict) or not data:
                raise ValueError
            if prompt_format == 'ideogram_json':
                composition = data.get('compositional_deconstruction', {})
                if (not _text(data.get('high_level_description'))
                        or not isinstance(composition, dict)
                        or not isinstance(composition.get('background'), str)
                        or not isinstance(composition.get('elements'), list)):
                    raise ValueError
                for element in composition['elements']:
                    if (not isinstance(element, dict) or element.get('type') not in ('obj', 'text')
                            or not _text(element.get('desc'))
                            or (element['type'] == 'text' and not _text(element.get('text')))
                            or ('bbox' in element and not _box(element['bbox']))):
                        raise ValueError
                style = data.get('style_description')
                if style is not None and (not isinstance(style, dict)
                                          or ('photo' in style and 'art_style' in style)):
                    raise ValueError
        positions = [prompt.find(label) for label in required_sections]
        if positions and (min(positions) < 0 or positions != sorted(positions)):
            raise ValueError
        if prompt_format == 'midjourney' and output['negative_prompt']:
            raise ValueError
    except (ValueError, TypeError, KeyError) as exc:
        raise RuntimeError(FORMAT_ERROR) from exc
