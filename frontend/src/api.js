export async function api(path, options = {}) {
  let response;
  try {
    response = await fetch('/api' + path, {
      ...options,
      headers: {'Content-Type': 'application/json', ...(options.headers || {})},
    });
  } catch (error) {
    if (error.name === 'AbortError') throw error;
    throw new Error('No se puede conectar con el servidor local.');
  }
  const data = await response.json().catch(() => ({detail: 'Respuesta no válida del servidor'}));
  if (!response.ok) throw new Error(typeof data.detail === 'string' ? data.detail : 'Datos de entrada no válidos. Revisa los campos y vuelve a intentarlo.');
  return data;
}
