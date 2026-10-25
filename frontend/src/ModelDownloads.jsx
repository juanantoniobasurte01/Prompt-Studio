import React, {useEffect, useState} from 'react';
import {api} from './api';
import {sortByName} from './ordering';

export default function ModelDownloads({catalog = [], installed, online, selected, onSelect, onRefresh, language, t}) {
  const [choice, setChoice] = useState('');
  const [job, setJob] = useState(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const entry = catalog.find(item => item.id === choice);
  const present = installed.includes(choice);
  useEffect(() => {api('/local-models/download').then(data => setJob(data.job)).catch(e => setError(e.message));}, []);
  useEffect(() => {
    if (job?.state !== 'running') return;
    let active = true;
    let polling = false;
    const timer = setInterval(async () => {
      if (polling) return;
      polling = true;
      try {
        const data = await api('/local-models/download');
        if (!active) return;
        setJob(data.job);
        if (data.job?.state === 'completed') await onRefresh();
      } catch (e) {if (active) setError(e.message);}
      finally {polling = false;}
    }, 1000);
    return () => {active = false; clearInterval(timer);};
  }, [job?.id, job?.state]);
  const download = async () => {
    setBusy(true); setError('');
    try {
      const data = await api('/local-models/download', {method:'POST', body:JSON.stringify({model:choice})});
      setJob(data.job);
      if (data.installed) await onRefresh();
    } catch (e) {setError(e.message);}
    finally {setBusy(false);}
  };
  return <section className="download-models" aria-labelledby="download-models-title">
    <h4 id="download-models-title">{t('Descargar motores abiertos')}</h4>
    <p className="setting-info">{t('Variantes comunitarias uncensored/abliterated para escritura libre, incluidos prompts NSFW. Estas etiquetas describen el ajuste del autor; no garantizan todas las respuestas.')}</p>
    <label htmlFor="download-model">{t('Catálogo de motores')}</label>
    <select id="download-model" value={choice} onChange={e => {setChoice(e.target.value); setError('');}}>
      <option value="">{t('Selecciona un modelo del catálogo')}</option>
      {sortByName(catalog, item => item.label, language).map(item => <option key={item.id} value={item.id}>{item.label} · ≈{item.size_gb} GB · {t(installed.includes(item.id) ? 'Instalado' : 'Sin descargar')}</option>)}
    </select>
    {entry && <p className="setting-info"><a href={entry.source} target="_blank" rel="noreferrer">{t('Ficha del autor y licencia')}</a><br/>{t('Tamaño de descarga aproximado; el uso de memoria será mayor.')}</p>}
    <button className="secondary-wide" disabled={!choice || busy || !online || selected === choice || (!present && job?.state === 'running')} onClick={() => present ? onSelect(choice) : download()}>{t(present ? selected === choice ? 'Motor seleccionado' : 'Usar este motor' : busy ? 'Iniciando descarga...' : 'Descargar modelo')}</button>
    {job && <div className="model-download-progress" role="status">
      <b>{job.model}</b>
      <p>{t(job.state === 'running' ? 'Descargando... Mantén la aplicación abierta.' : job.state === 'completed' ? 'Descarga completada. Ya puedes elegir el motor.' : 'La descarga ha fallado. Puedes volver a intentarlo.')}</p>
      {job.state === 'running' && (job.total > 0 ? <><progress aria-label={t('Progreso del archivo actual')} max={job.total} value={Math.min(job.completed, job.total)}/><small>{t('Archivo actual')}: {(job.completed / 1e9).toFixed(2)} / {(job.total / 1e9).toFixed(2)} GB</small></> : <progress aria-label={t('Preparando descarga')}/>)}
      {job.error && <p className="preset-error">{job.error}</p>}
    </div>}
    {error && <p className="preset-error" role="alert">{t(error)}</p>}
  </section>;
}
