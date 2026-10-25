import {useEffect} from 'react';
import {storedPreference, usePreference} from './preferences';

export const THEMES = ['system', 'light', 'dark'];
const KEY = 'promptstudio-theme';
export function resolveTheme(preference, prefersDark) {
  return preference === 'system' ? (prefersDark ? 'dark' : 'light') : preference;
}

document.documentElement.dataset.theme = resolveTheme(storedPreference(KEY, 'system', THEMES), window.matchMedia('(prefers-color-scheme: dark)').matches);

export function useTheme() {
  const [theme, setTheme] = usePreference(KEY, 'system', THEMES, 'get_theme', 'set_theme');
  useEffect(() => {
    const media = window.matchMedia('(prefers-color-scheme: dark)');
    const apply = () => {document.documentElement.dataset.theme = resolveTheme(theme, media.matches);};
    apply();
    media.addEventListener('change', apply);
    return () => media.removeEventListener('change', apply);
  }, [theme]);
  return {theme, setTheme};
}
