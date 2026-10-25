import {useEffect, useRef, useState} from 'react';

export function storedPreference(key, fallback, allowed) {
  try {
    const value = localStorage.getItem(key);
    return allowed.includes(value) ? value : fallback;
  } catch {return fallback;}
}

export function usePreference(key, fallback, allowed, getter, setter) {
  const [value, setValue] = useState(() => storedPreference(key, fallback, allowed));
  const [desktopReady, setDesktopReady] = useState(false);
  const revision = useRef(0);
  useEffect(() => {
    let active = true;
    const sync = async () => {
      if (!window.pywebview?.api) return;
      const initialRevision = revision.current;
      try {
        const saved = await window.pywebview.api[getter]();
        if (active && initialRevision === revision.current && allowed.includes(saved)) setValue(saved);
      } finally {if (active) setDesktopReady(true);}
    };
    const onReady = () => {sync().catch(() => {});};
    window.addEventListener('pywebviewready', onReady);
    onReady();
    return () => {active = false; window.removeEventListener('pywebviewready', onReady);};
  }, [key, getter]);
  useEffect(() => {
    try {localStorage.setItem(key, value);} catch { /* Storage may be unavailable. */ }
    if (desktopReady) window.pywebview?.api?.[setter](value).catch(() => {});
  }, [key, value, desktopReady, setter]);
  const change = next => {
    if (allowed.includes(next)) {revision.current += 1; setValue(next);}
  };
  return [value, change];
}
