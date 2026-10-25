"""Bundled editable examples, kept separate from the user's SQLite presets."""
from __future__ import annotations

import json
from pathlib import Path
from .engine import catalog

SCENES = Path(__file__).with_name('preset_scenes.json')


def preset_library(language: str = 'es', model_id: str | None = None) -> list[dict]:
    profiles = catalog()
    if model_id:
        profiles = [p for p in profiles if p['id'] == model_id]
        if not profiles:
            raise ValueError('El perfil seleccionado no existe en la biblioteca.')
    scenes = json.loads(SCENES.read_text(encoding='utf-8'))
    result = []
    for profile in profiles:
        for scene in scenes:
            text = scene[language]
            is_video = profile['medium'] == 'video'
            fields = {key: {'selected': '', 'manual': value} for key, value in text['fields'].items()}
            free = text['video'] if is_video else text['image']
            instructions = text['instructions']
            if is_video:
                fields.update({key: {'selected': '', 'manual': value} for key, value in text['motion'].items()})
                duration = {'video_gemini_omni_flash':8, 'video_google_veo_3_1_legacy':8,
                            'video_luma_ray_3_14':5, 'video_adobe_firefly_video':5,
                            'video_wan_2_2_local':5, 'video_hunyuanvideo_1_5':5,
                            'video_cogvideox':5}.get(profile['id'], 6)
                duration_text = (f'{duration} segundos como objetivo; confirmar duración admitida en el generador. Conservar la acción completa.' if language == 'es' else
                                 f'Target {duration} seconds; confirm supported duration in the generator. Preserve the complete action.')
                fields['duracion'] = {'selected': '', 'manual': duration_text}
                mode = 'T2VA' if profile['id'] == 'video_minimax_h3' else 'T2V'
                if profile['id'] == 'video_vidu_q4_q3':
                    mode = 'Q4 Preview I2V'
                    reference = ('Adjuntaré en Vidu una imagen inicial con el estado inicial descrito. Mantener I2V; la imagen está pendiente de adjuntar en el destino.' if language == 'es' else
                                 'I will attach a starting image in Vidu matching the described initial state. Keep I2V; attachment in the target generator is pending.')
                    fields['referencias_video'] = {'selected': '', 'manual': reference}
                    free += '\n' + reference
                fields['modalidad_video'] = {'selected': '', 'manual': mode}
            elif profile['id'] == 'image_flux_1_kontext':
                reference = ('Edición Kontext: aportaré una imagen base con esta composición. Cambiar únicamente el vestuario al descrito; conservar personas, rostros, postura, objetos, fondo y encuadre. No se ha adjuntado la imagen en este editor.' if language == 'es' else
                             'Kontext edit: I will supply a base image with this composition. Change only the clothing to the described wardrobe; preserve people, faces, pose, objects, background and framing. The image is not attached in this editor.')
                fields['referencias'] = {'selected': '', 'manual': reference}
                fields['restricciones'] = {'selected': '', 'manual': (
                    'Modificar solo el vestuario al indicado. Conservar identidad, cantidad de personas, postura, objetos, luz, fondo y composición de la imagen base.' if language == 'es' else
                    'Change only the wardrobe to the specified clothing. Preserve identity, number of people, pose, props, light, background and composition of the base image.')}
                instructions += '\n' + reference
            result.append({
                'id': f"builtin:{profile['id']}:{scene['id']}",
                'name': text['name'], 'source': 'builtin', 'model_id': profile['id'],
                'model_label': profile['label'], 'medium': profile['medium'],
                'description': text['summary'],
                'content': {'medium': profile['medium'], 'model_id': profile['id'], 'manual_model': '',
                            'mode': 'guided', 'free_prompt': free, 'fields': fields,
                            'extra_instructions': instructions,
                            'output_language': 'English' if language == 'en' else 'Español',
                            'temperature': 0.35},
            })
    return result
