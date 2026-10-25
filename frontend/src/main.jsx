import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {BookOpen, Settings, History, RefreshCcw, Copy, Download, Check, AlertTriangle, ChevronRight, X, Sparkles, FolderOpen, Wifi, WifiOff} from 'lucide-react';
import {SECTIONS, VIDEO} from './sections';
import GuidedField from './GuidedField';
import PresetLibrary from './PresetLibrary';
import LocalModelsSettings from './LocalModelsSettings';
import {api} from './api';
import {useLocale} from './i18n';
import {useTheme} from './theme';
import {sortByName} from './ordering';
import {normalizeIdentity} from './identity';
import './style.css';
import './themes.css';
import appLogo from '../../recursos/PS.png';

const BASE = {medium:'auto', model_id:'', manual_model:'', mode:'free', free_prompt:'', fields:{}, extra_instructions:'', negative_prompt:'', output_language:'English', ollama_model:'', temperature:0.45};
const EMPTY_OUTPUT = {prompt:'', negative_prompt:'', notes:''};
const sectionsFor = medium => medium === 'video' ? [...SECTIONS, ...VIDEO] : SECTIONS;

function App() {
  const {language, setLanguage, t} = useLocale();
  const {theme, setTheme} = useTheme();
  const [form, setForm] = useState(BASE);
  const [profiles, setProfiles] = useState([]);
  const [tab, setTab] = useState('subject');
  const [panel, setPanel] = useState('');
  const [presets, setPresets] = useState([]);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState(null);
  const [output, setOutput] = useState(EMPTY_OUTPUT);
  const [error, setError] = useState('');
  const [done, setDone] = useState('');
  const update = (key, value) => setForm(f => ({...f, [key]:value}));
  const loadData = () => {
    api('/presets').then(setPresets).catch(() => {});
    api('/history').then(setHistory).catch(() => {});
  };
  const refreshStatus = () => api('/ollama/status').then(setStatus).catch(() => setStatus({online:false, installed:[]}));
  useEffect(() => {
    api('/models').then(data => {
      setProfiles(data.profiles || []);
      if (data.default_ollama_model) setForm(f => ({...f, ollama_model:data.default_ollama_model}));
    }).catch(e => setError(e.message));
    loadData(); refreshStatus();
  }, []);
  const profile = profiles.find(p => p.id === form.model_id);
  const derivedMedium = profile?.medium || form.medium;
  const displaySections = sectionsFor(derivedMedium);
  const current = displaySections.find(s => s.id === tab) || displaySections[0];
  const sortedProfiles = sortByName(profiles, p => t(p.label), language);
  const filtered = sortedProfiles.filter(p => form.medium === 'auto' || p.medium === form.medium);
  const updateField = (id, type, value) => setForm(f => ({...f, fields:{...f.fields, [id]:{selected:f.fields[id]?.selected || '', manual:f.fields[id]?.manual || '', [type]:value}}}));
  const filled = Object.values(form.fields).filter(value => value?.selected || value?.manual).length;
  const ready = Boolean(form.free_prompt.trim() || filled);
  const run = async () => {
    if (!form.ollama_model) {setPanel('settings'); return;}
    setLoading(true); setError(''); setDone('');
    try {
      const result = await api('/generate', {method:'POST', body:JSON.stringify({...form, model_id:form.model_id || null, interface_language:language})});
      setOutput(result); setDone('Prompt generado correctamente.'); loadData();
    } catch (e) { setError(e.message); }
    finally { setLoading(false); }
  };
  const loadState = (saved, builtin = false) => {
    setForm({...BASE, ...saved, manual_model:'', fields:normalizeIdentity(saved?.fields), ollama_model:form.ollama_model, ...(builtin ? {output_language:form.output_language} : {})});
    setOutput(EMPTY_OUTPUT); setPanel(''); setTab('subject'); setError(''); setDone('');
  };
  const storePreset = async name => {
    if (!name.trim()) {setError('Escribe un nombre para el preset.'); return false;}
    try {
      await api('/presets', {method:'POST', body:JSON.stringify({name, content:form})});
      setDone('Preset guardado.'); loadData(); return true;
    } catch (e) {setError(e.message); return false;}
  };
  const removePreset = async id => {
    try {await api('/presets/' + id, {method:'DELETE'}); loadData();}
    catch (e) {setError(e.message);}
  };
  const copy = async () => {
    try {
      const text = output.prompt + (output.negative_prompt ? '\n\nNEGATIVE:\n' + output.negative_prompt : '');
      if (window.pywebview?.api) {
        const result = await window.pywebview.api.copy_text(text);
        if (!result.ok) throw new Error('Clipboard failed');
      } else await navigator.clipboard.writeText(text);
      setDone('Copiado al portapapeles.');
    }
    catch {setError('No se pudo copiar.');}
  };
  const exportJSON = async () => {
    const content = JSON.stringify({input:form, output}, null, 2);
    const filename = 'promptstudio-' + new Date().toISOString().slice(0,10) + '.json';
    try {
      if (window.pywebview?.api) {
        const result = await window.pywebview.api.export_json(filename, content);
        if (!result.ok) throw new Error('Export failed');
      } else {
        const blob = new Blob([content], {type:'application/json'});
        const url = URL.createObjectURL(blob); const link = document.createElement('a');
        link.href = url; link.download = filename; link.click(); URL.revokeObjectURL(url);
      }
    } catch {setError('No se pudo exportar el archivo.');}
  };
  const togglePanel = name => setPanel(panel === name ? '' : name);
  const close = () => setPanel('');
  return <div className="shell">
    <header className="topbar">
      <div className="brand"><img className="brand-icon" src={appLogo} alt=""/><div><strong>prompt<span>studio</span></strong><small>{t('MOTOR LOCAL DE PROMPTS')}</small></div></div>
      <div className="header-right">
        <span className={'connection ' + (status?.online ? 'ok' : 'no')} title={t(status?.online ? 'Ollama disponible' : 'Ollama sin conexión')}>{status?.online ? <Wifi size={15}/> : <WifiOff size={15}/>}<span>{t(status?.online ? 'Ollama conectado' : 'Ollama desconectado')}</span></span>
        <button className={'header-action ' + (panel === 'presets' ? 'active' : '')} aria-label={t('Presets')} title={t('Presets')} onClick={() => togglePanel('presets')}><FolderOpen size={17}/> {t('Presets')}</button>
        <button className={'header-action ' + (panel === 'history' ? 'active' : '')} aria-label={t('Historial')} title={t('Historial')} onClick={() => togglePanel('history')}><History size={17}/> {t('Historial')}</button>
        <button className={'icon-btn ' + (panel === 'settings' ? 'active' : '')} title={t('Configuración')} aria-label={t('Configuración')} onClick={() => togglePanel('settings')}><Settings size={18}/></button>
      </div>
    </header>
    <main className="workspace">
      <aside className="sidebar">
        <div className="sidebar-top"><div className="eyebrow">{t('CONFIGURACIÓN')}</div><div className="label">{t('Tipo de generación')}</div>
          <div className="medium-buttons">{[['auto','Auto'],['image','Imagen'],['video','Vídeo']].map(([value,label]) => <button key={value} className={form.medium === value ? 'selected' : ''} onClick={() => {setForm(f => ({...f, medium:value, model_id:profiles.find(p => p.id === f.model_id && p.medium === value)?.id || ''})); setTab('subject');}}>{t(label)}</button>)}</div>
          <label className="label" htmlFor="target-model">{t('Modelo de destino')} <em>{t('opcional')}</em></label>
          <select id="target-model" value={form.model_id} onChange={e => {const id = e.target.value; const p = profiles.find(item => item.id === id); setForm(f => ({...f, model_id:id, ...(p ? {medium:p.medium} : {})})); setTab('subject');}}><option value="">{t('Sin modelo (universal)')}</option>{filtered.map(p => <option value={p.id} key={p.id}>{t(p.label)}{p.legacy && !/legacy|legado/i.test(p.label) ? ' (' + t('legado') + ')' : ''}</option>)}</select>
          {form.model_id && <div className="doc-loaded" title={t(profile?.description || '')}><BookOpen size={14}/> {t(profile?.verification_status === 'parcial' ? 'Guía con verificación parcial' : 'MD especializado cargado')}</div>}
          <div className="eyebrow section-eyebrow">{t('MODO DE TRABAJO')}</div>
          <div className="mode-switch"><button className={form.mode === 'free' ? 'selected' : ''} onClick={() => update('mode','free')}>{t('Prompt libre')}</button><button className={form.mode === 'guided' ? 'selected' : ''} onClick={() => update('mode','guided')}>{t('Editor guiado')}</button></div>
          <div className="sidebar-note">{t('Puedes usar ambos modos a la vez: el texto libre siempre está disponible y se combinará con los parámetros.')}</div>
        </div>
        {form.mode === 'guided' && <div className="sidebar-sections"><div className="eyebrow">{t('SECCIONES')}</div>{displaySections.map(s => <button className={'section-button ' + (current.id === s.id ? 'active' : '')} key={s.id} onClick={() => setTab(s.id)}><span>{t(s.title)}</span><ChevronRight size={15}/></button>)}</div>}
      </aside>
      <section className="editor">
        <div className="page-head"><div className="eyebrow">{t('EDITOR DE PROMPTS')}</div><h1>{t(form.mode === 'free' ? 'Mejora tu idea' : 'Construye tu prompt')}</h1><p>{t(form.mode === 'free' ? 'Introduce cualquier prompt. La IA lo perfeccionará respetando tu intención.' : 'Organiza los parámetros. Nada es obligatorio y todo admite entrada manual.')}</p></div>
        <section className="panel-base"><div className="panel-title"><div><span className="step">01</span><strong>{t('Prompt libre')}</strong></div><span className="chip">{t('Siempre disponible')}</span></div>
          <textarea className="free-input" aria-label={t('Prompt libre')} value={form.free_prompt} onChange={e => update('free_prompt', e.target.value)} placeholder={t('Escribe una idea o pega un prompt completo...')}/>
          <div className="helper">{t('También puedes dejarlo vacío y trabajar únicamente con campos guiados.')}</div>
        </section>
        {form.mode === 'guided' && <section className="panel-base guided"><div className="panel-title"><div><span className="step">02</span><strong>{t(current.title)}</strong></div><span className="chip">{t('{count} campos definidos', {count:filled})}</span></div><p className="group-hint">{t(current.hint)}</p><div className="fields-grid">{current.fields.map(field => <GuidedField key={field[0]} field={field} value={form.fields[field[0]]} onChange={updateField} t={t} language={language}/>)}</div></section>}
        <section className="panel-base additional"><div className="panel-title"><div><span className="step">{form.mode === 'guided' ? '03' : '02'}</span><strong>{t('Indicaciones adicionales')}</strong></div><span className="chip">{t('Opcional')}</span></div><textarea rows="2" aria-label={t('Indicaciones adicionales')} value={form.extra_instructions} onChange={e => update('extra_instructions',e.target.value)} placeholder={t('Indica cualquier criterio adicional: fidelidad, idioma, nivel de detalle, tipo de salida...')}/></section>
        <section className="panel-base negative-input"><div className="panel-title"><div><span className="step">{form.mode === 'guided' ? '04' : '03'}</span><label htmlFor="input-negative-prompt"><strong>{t('Prompt negativo')}</strong></label></div><span className="chip">{t('Opcional')}</span></div><textarea id="input-negative-prompt" rows="2" maxLength={5000} value={form.negative_prompt} onChange={e => update('negative_prompt',e.target.value)} placeholder={t('Qué quieres evitar: desenfoque, texto, marcas de agua...')}/><p className="helper">{t('Las exclusiones se adaptan al modelo de destino. Si no admite negativos separados, se indicará en las notas.')}</p></section>
        <div className="create-bar"><div><b>{t('Motor local')}: {form.ollama_model || t('Selecciona un motor de IA en Configuración.')}</b><span>{profile ? t(profile.label) : t('Prompt universal sin modelo')}</span></div><button className="primary" disabled={!ready || loading} onClick={run}>{loading ? <RefreshCcw size={17} className="spin"/> : <Sparkles size={17}/>} {t(!form.ollama_model ? 'Elegir motor de IA' : loading ? 'Generando...' : output.prompt ? 'Regenerar prompt' : 'Generar prompt')}</button></div>
        {error && <div className="message error" role="alert"><AlertTriangle size={17}/>{t(error)}<button aria-label={t('Cerrar mensaje')} onClick={() => setError('')}><X size={15}/></button></div>}
        {done && <div className="message success" role="status"><Check size={17}/>{t(done)}<button aria-label={t('Cerrar mensaje')} onClick={() => setDone('')}><X size={15}/></button></div>}
      </section>
      <aside className="result-column"><div className="result-head"><div className="eyebrow">{t('RESULTADO')}</div><h2>{t('Prompt optimizado')}</h2><p>{t('Editable, listo para copiar y llevar a tu generador.')}</p></div>
        <div className="output-box"><div className="output-title">{t('PROMPT POSITIVO')} <span>{form.output_language === 'Español' ? 'ES' : 'EN'}</span></div><textarea className="prompt-output" aria-label={t('Prompt positivo')} value={output.prompt} onChange={e => setOutput(o => ({...o,prompt:e.target.value}))} placeholder={t('Aquí aparecerá tu prompt generado por la IA local...')}/></div>
        <div className="output-box negative"><div className="output-title">{t('PROMPT NEGATIVO')} <span>{t('SI APLICA')}</span></div><textarea aria-label={t('Prompt negativo generado')} value={output.negative_prompt} onChange={e => setOutput(o => ({...o,negative_prompt:e.target.value}))} placeholder={t('Solo si el modelo admite prompt negativo.')}/></div>
        {output.notes && <div className="result-notes"><b>{t('Notas de optimización')}</b><p>{output.notes}</p></div>}
        <div className="result-actions"><button onClick={copy} disabled={!output.prompt}><Copy size={16}/> {t('Copiar')}</button><button onClick={exportJSON} disabled={!output.prompt}><Download size={16}/> {t('Exportar JSON')}</button></div>
      </aside>
    </main>
    {panel && <><button aria-label={t('Cerrar panel')} className="scrim" onClick={close}/><div className="drawer" role="dialog" aria-modal="true" aria-labelledby="drawer-title"><div className="drawer-head"><h3 id="drawer-title">{t(panel === 'presets' ? 'Biblioteca de presets' : panel === 'history' ? 'Historial' : 'Configuración local')}</h3><button className="icon-btn" aria-label={t('Cerrar panel')} onClick={close}><X size={18}/></button></div>
      {panel === 'presets' && <PresetLibrary language={language} t={t} profiles={sortedProfiles} currentModel={form.model_id} presets={presets} onLoad={loadState} onSave={storePreset} onRemove={removePreset} onError={setError}/>}
      {panel === 'history' && <div className="drawer-body">{!history.length ? <p className="empty">{t('Sin generaciones previas.')}</p> : history.map(h => <div className="record" key={h.id}><button onClick={() => {loadState(h.content.input); setOutput({...EMPTY_OUTPUT,...h.content.result});}}><b>{(h.content?.result?.prompt || 'Prompt').slice(0,92)}</b><small>{h.created?.replace('T',' ').slice(0,16)}</small></button></div>)}</div>}
      {panel === 'settings' && <div className="drawer-body">
        <div className="theme-setting"><span id="theme-label" className="setting-label">{t('Tema de la interfaz')}</span><div className="theme-switch" role="group" aria-labelledby="theme-label">{[['system','Sistema'],['light','Claro'],['dark','Oscuro']].map(([value,label]) => <button type="button" key={value} aria-pressed={theme === value} className={theme === value ? 'selected' : ''} onClick={() => setTheme(value)}>{t(label)}</button>)}</div><p className="setting-info">{t('Sistema sigue automáticamente el modo claro u oscuro de tu equipo.')}</p></div>
        <label htmlFor="settings-language">{t('Idioma de la interfaz')}</label><select id="settings-language" value={language} onChange={e => setLanguage(e.target.value)}><option value="es">Español</option><option value="en">English</option></select><p className="setting-info">{t('El idioma de la interfaz es independiente del idioma del prompt. Tu texto y tus selecciones se conservan al cambiarlo.')}</p>
        <LocalModelsSettings model={form.ollama_model} onSelect={value => update('ollama_model',value)} language={language} t={t}/>
        <label htmlFor="temperature">{t('Temperatura creativa')}: {form.temperature}</label><input id="temperature" type="range" min="0" max="1.5" step="0.05" value={form.temperature} onChange={e => update('temperature',Number(e.target.value))}/>
        <label htmlFor="output-language">{t('Idioma del prompt')}</label><select id="output-language" value={form.output_language} onChange={e => update('output_language',e.target.value)}><option value="English">{t('Inglés')}</option><option value="Español">{t('Español')}</option></select>
      </div>}
    </div></>}
  </div>;
}

createRoot(document.getElementById('root')).render(<App/>);
