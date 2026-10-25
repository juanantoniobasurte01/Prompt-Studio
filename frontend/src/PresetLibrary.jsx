import React, {useEffect, useState} from 'react';
import {Save, Trash2} from 'lucide-react';
import {api} from './api';
import {sortByName} from './ordering';

const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

export default function PresetLibrary({language, t, profiles, currentModel, presets, onLoad, onSave, onRemove, onError}) {
  const [model, setModel] = useState(currentModel || '');
  const [search, setSearch] = useState('');
  const [name, setName] = useState('');
  const [examples, setExamples] = useState([]);
  const [loading, setLoading] = useState(true);
  const [failed, setFailed] = useState(false);
  const [saveError, setSaveError] = useState('');
  useEffect(() => {
    const controller = new AbortController();
    setLoading(true); setFailed(false);
    const query = new URLSearchParams({language});
    if (model) query.set('model_id', model);
    api('/preset-library?' + query, {signal: controller.signal})
      .then(setExamples)
      .catch(error => {if (error.name !== 'AbortError') {setFailed(true); onError(error.message);}})
      .finally(() => {if (!controller.signal.aborted) setLoading(false);});
    return () => controller.abort();
  }, [language, model]);
  const query = normalize(search);
  const visible = sortByName(examples.filter(p => normalize(p.name + ' ' + p.model_label + ' ' + p.description).includes(query)), p => t(p.model_label) + ' ' + p.name, language);
  const savedPresets = sortByName(presets, p => p.name, language);
  const save = async () => {
    setSaveError('');
    if (!name.trim()) {setSaveError('Escribe un nombre para el preset.'); return;}
    if (await onSave(name)) setName('');
  };
  return <div className="drawer-body preset-library">
    <h4>{t('Mis presets')}</h4>
    <label htmlFor="preset-name">{t('Guardar la configuración actual')}</label>
    <div className="inline-input"><input id="preset-name" placeholder={t('Nombre del preset...')} value={name} onChange={e => setName(e.target.value)}/><button title={t('Guardar preset')} aria-label={t('Guardar preset')} onClick={save}><Save size={16}/></button></div>
    {saveError && <p className="preset-error" role="alert">{t(saveError)}</p>}
    {!presets.length ? <p className="empty">{t('Todavía no hay presets guardados.')}</p> : savedPresets.map(p => <div className="record" key={p.id}><button onClick={() => onLoad(p.content)}><b>{p.name}</b><small>{p.updated?.slice(0,10)}</small></button><button title={t('Eliminar')} aria-label={t('Eliminar preset {name}', {name:p.name})} onClick={() => onRemove(p.id)}><Trash2 size={16}/></button></div>)}
    <div className="library-heading"><h4>{t('Ejemplos por modelo')}</h4><span className="chip">{t('6 por modelo')}</span></div>
    <p className="setting-info">{t('Carga un ejemplo completo y adáptalo. Para conservar tus cambios, guárdalo en Mis presets.')}</p>
    <label htmlFor="preset-model">{t('Filtrar por modelo')}</label>
    <select id="preset-model" value={model} onChange={e => setModel(e.target.value)}><option value="">{t('Todos los modelos')}</option>{['image','video'].map(medium => <optgroup key={medium} label={t(medium === 'video' ? 'Vídeo' : 'Imagen')}>{profiles.filter(p => p.medium === medium).map(p => <option key={p.id} value={p.id}>{t(p.label)}</option>)}</optgroup>)}</select>
    <label htmlFor="preset-search">{t('Buscar presets')}</label><input id="preset-search" type="search" value={search} onChange={e => setSearch(e.target.value)} placeholder={t('Persona, acción, contexto o modelo...')}/>
    <p className="option-feedback" role="status">{loading ? t('Cargando presets...') : failed ? t('No se pudo cargar la biblioteca.') : t(visible.length === 1 ? '{count} preset disponible' : '{count} presets disponibles', {count:visible.length})}</p>
    {!loading && !failed && !visible.length && <p className="empty">{t('No hay presets que coincidan con la búsqueda.')}</p>}
    {!loading && !failed && visible.map(p => <div className="record example-record" key={p.id}><button onClick={() => onLoad(p.content, true)}><small>{t(p.model_label)} · {t(p.medium === 'video' ? 'Vídeo' : 'Imagen')}</small><b>{p.name}</b><p>{p.description}</p><span>{t('Cargar y editar')}</span></button></div>)}
  </div>;
}
