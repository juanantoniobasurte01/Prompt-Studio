import React, {useEffect, useState} from 'react';
import {api} from './api';
import {sortByName} from './ordering';
import ModelDownloads from './ModelDownloads';
import './local-models.css';

export default function LocalModelsSettings({model, onSelect, language, t}) {
  const [library, setLibrary] = useState({installed:[], files:[], directory:'', online:false});
  const [filename, setFilename] = useState('');
  const [name, setName] = useState('');
  const [busy, setBusy] = useState('');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');
  const refresh = async () => {
    const data = await api('/local-models');
    setLibrary(data);
    return data;
  };
  useEffect(() => {refresh().catch(e => setError(e.message));}, []);
  const action = async (kind, work) => {
    setBusy(kind); setError(''); setMessage('');
    try {await work();} catch (e) {setError(e.message);}
    finally {setBusy('');}
  };
  const select = value => action('selection', async () => {
    const saved = await api('/local-models/selection', {method:'PUT', body:JSON.stringify({model:value})});
    onSelect(saved.selected);
    setMessage('Motor guardado.');
  });
  const importFile = () => action('import', async () => {
    await api('/local-models/import', {method:'POST', body:JSON.stringify({filename, model:name.trim()})});
    await refresh();
    setMessage('Modelo importado. Ya puedes seleccionarlo en la lista de motores.');
  });
  const openFolder = () => action('folder', async () => {
    const result = await window.pywebview.api.open_models_folder();
    if (!result.ok) throw new Error('No se pudo abrir la carpeta de modelos.');
  });
  return <section className="local-models" aria-labelledby="local-models-heading">
    <h4 id="local-models-heading">{t('Motor de IA')}</h4>
    <label htmlFor="ai-engine">{t('Modelo instalado')}</label>
    <select id="ai-engine" value={model} disabled={Boolean(busy) || !library.online} onChange={e => select(e.target.value)}>
      <option value="" disabled>{t('Selecciona un motor de IA')}</option>
      {model && !library.installed.includes(model) && <option value={model} disabled>{model} — {t('No disponible')}</option>}
      {sortByName(library.installed, value => value, language).map(value => <option key={value} value={value}>{value}</option>)}
    </select>
    <p className="setting-info">{t('La elección se guarda y se aplica también al cargar presets o historial. Seleccionar un motor no lo carga en memoria.')}</p>
    <button className="secondary-wide" disabled={Boolean(busy)} onClick={() => action('refresh', refresh)}>{t(busy === 'refresh' ? 'Actualizando...' : 'Actualizar modelos')}</button>
    <p className="setting-info">{library.online ? t('Ollama disponible. {count} modelos instalados.', {count:library.installed.length}) : t('Ollama sin conexión. Abre Ollama para seleccionar o importar modelos.')}</p>
    <ModelDownloads catalog={library.catalog} installed={library.installed} online={library.online} selected={model} onSelect={select} onRefresh={refresh} language={language} t={t}/>
    <h4>{t('Añadir un archivo GGUF')}</h4>
    <p className="setting-info">{t('Copia un modelo de conversación GGUF compatible en esta carpeta y actualiza la lista.')}</p>
    <code className="models-directory">{library.directory}</code>
    {window.pywebview?.api && <button className="secondary-wide" disabled={Boolean(busy) || !library.directory} onClick={openFolder}>{t('Abrir carpeta de modelos')}</button>}
    <label htmlFor="gguf-file">{t('Archivo local')}</label>
    <select id="gguf-file" value={filename} disabled={Boolean(busy)} onChange={e => {
      setFilename(e.target.value);
      setName(library.files.find(file => file.filename === e.target.value)?.suggested_name || '');
    }}>
      <option value="">{t('Selecciona un archivo GGUF')}</option>
      {sortByName(library.files, file => file.filename, language).map(file => <option key={file.filename} value={file.filename}>{file.filename} ({(file.size / 1024 ** 3).toFixed(2)} GiB)</option>)}
    </select>
    {!library.files.length && <p className="setting-info">{t('No hay archivos GGUF en la carpeta.')}</p>}
    <label htmlFor="gguf-name">{t('Nombre para Ollama')}</label>
    <input id="gguf-name" value={name} disabled={Boolean(busy)} onChange={e => setName(e.target.value)} placeholder="promptstudio/my-model:latest"/>
    <button className="secondary-wide" disabled={Boolean(busy) || !library.online || !filename || !name.trim()} onClick={importFile}>{t(busy === 'import' ? 'Importando... Puede tardar varios minutos.' : 'Importar en Ollama')}</button>
    <p className="setting-info">{t('La importación registra el archivo sin generar texto. Ollama puede guardar otra copia de los pesos. Para GGUF divididos, importa con Ollama y después selecciona el modelo aquí.')}</p>
    {error && <p className="preset-error" role="alert">{t(error)}</p>}
    {message && <p className="setting-info" role="status">{t(message)}</p>}
  </section>;
}
