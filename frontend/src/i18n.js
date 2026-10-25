import {useEffect} from 'react';
import {usePreference} from './preferences';
import editorEnglish from './locales/en-editor.json';
import uiEnglish from './locales/en-ui.json';

const english = {...editorEnglish, ...uiEnglish};

export function translate(text, language = 'es', parameters = {}) {
  const upstream = String(text ?? '').match(/^Ollama devolvió (\d+): (.*)$/s);
  if (upstream) {
    text = 'Ollama devolvió {status}: {detail}';
    parameters = {...parameters, status:upstream[1], detail:upstream[2]};
  }
  const translated = language === 'en' ? (english[`${parameters.context}::${text}`] ?? english[text] ?? text) : text;
  return String(translated ?? '').replace(/\{(\w+)\}/g, (match, key) => parameters[key] ?? match);
}

const LANGUAGES = ['es', 'en'];

export function useLocale() {
  const [language, setLanguage] = usePreference('prompt-studio-language', 'es', LANGUAGES, 'get_interface_language', 'set_interface_language');
  useEffect(() => {document.documentElement.lang = language;}, [language]);
  return {language, setLanguage, t: (text, parameters) => translate(text, language, parameters)};
}
