// Ordinal subsets lead; remaining categorical choices follow alphabetically.
// Sorting copies arrays so shared option lists and persisted values stay intact.
const scale = text => text.split('|');
export const SCALES = {
  personajes: scale('Sin personas|Una persona|Dos personas|Pareja|Tres personas|Cuatro personas'),
  estatura: scale('Muy baja|Baja|Media|Alta|Muy alta'),
  complexion: scale('Muy delgada|Delgada|Media|Robusta|Corpulenta|Muy corpulenta'),
  musculatura: scale('Poco definida|Definición media|Atlética|Musculosa|Muy musculosa'),
  estructura_corporal: scale('Menuda|Media|Ancha'),
  tono_piel: scale('Muy claro|Claro|Beige claro|Beige medio|Oliva claro|Oliva medio|Bronceado|Marrón claro|Marrón medio|Marrón oscuro|Muy oscuro'),
  labios: scale('Finos|Medios|Carnosos'),
  pestanas: scale('Cortas|Naturales|Largas|Finas|Espesas'),
  cejas: scale('Finas|Dispersas|Pobladas|Gruesas'),
  vello_facial: scale('Afeitado al ras|Sin barba|Barba de tres días|Barba corta|Barba media|Barba larga|Barba completa'),
  cabello_longitud: scale('Sin cabello|Rapado|Muy corto|Corto|Hasta la mandíbula|Media melena|Hasta los hombros|Hasta el pecho|Hasta la cintura|Muy largo'),
  cabello_textura: scale('Liso|Ligeramente ondulado|Ondulado|Rizado suelto|Rizado definido|Rizo cerrado|Afro|Fino|Grueso'),
  ropa_ajuste: scale('Ajustado|Entallado|Recto|Holgado|Oversize|Talle bajo|Talle medio|Talle alto|Mangas ajustadas|Mangas amplias'),
  ritmo_accion: scale('En reposo|Casi inmóvil|Sutil|Muy lento|Pausado|Natural|Enérgico|Rápido|Frenético'),
  cantidad_objetos: scale('Un objeto|Dos objetos|Tres objetos|Varios objetos'),
  epoca: scale('Prehistoria|Antigüedad clásica|Medieval|Renacimiento|Barroco|Siglo XVIII|Época victoriana|Década de 1920|Década de 1930|Década de 1940|Década de 1950|Década de 1960|Década de 1970|Década de 1980|Década de 1990|Década de 2000|Actualidad|Futuro cercano|Futurista|Futuro lejano|Época atemporal'),
  hora_dia: scale('Antes del amanecer|Amanecer|Primera hora de la mañana|Media mañana|Mediodía|Tarde|Última hora de la tarde|Atardecer|Hora azul|Anochecer|Noche|Medianoche'),
  densidad_entorno: scale('Vacío|Minimalista|Pocos elementos|Detalle moderado|Muy detallado|Abundante vegetación'),
  encuadre: scale('Gran plano general|Plano general|Plano conjunto|Plano de cuerpo entero|Plano americano|Plano medio|Plano medio corto|Retrato de busto|Primer plano|Primerísimo primer plano|Plano detalle'),
  dureza_luz: scale('Muy suave|Suave|Semidura|Dura|Muy dura'),
  intensidad_luz: scale('Muy tenue|Tenue|Moderada|Intensa|Muy intensa|Destello breve intenso'),
  exposicion: scale('Muy subexpuesta|Ligeramente subexpuesta|Equilibrada|Ligeramente sobreexpuesta'),
  temperatura_luz: scale('Muy cálida (vela)|Cálida (tungsteno)|Cálida suave|Neutra|Luz de día|Fría|Muy fría'),
  contraste: scale('Suave|Bajo contraste|Contraste medio|Alto contraste|Contraste extremo'),
  planos: scale('Un único plano|Dos planos|Tres planos|Multi-shot'),
  velocidad_video: scale('Pausa temporal|Cámara muy lenta|Cámara lenta|Tiempo real|Velocidad constante|Time-lapse|Hyperlapse'),
};

export function sortByName(items, label = value => value, language = 'es') {
  const collator = new Intl.Collator(language, {numeric:true, sensitivity:'base', ignorePunctuation:true});
  return [...items].sort((a,b) => collator.compare(label(a),label(b)));
}

export function sortFieldOptions([id,,options], t = text => text, language = 'es') {
  const alphabetical = sortByName(options, option => t(option, {context:id}), language);
  const ranks = new Map((SCALES[id] || []).map((value,index) => [value,index]));
  const numeric = value => {
    if (id === 'formato') {const [width,height] = value.split(':').map(Number); return width / height;}
    if (id === 'edad_aparente') return Number(value.match(/\d+/)?.[0] ?? Infinity);
    if (id === 'duracion' || id === 'lente') return /^\d/.test(value) ? parseFloat(value) : Infinity;
    return ranks.get(value) ?? Infinity;
  };
  // Equal numeric/ordinal ranks retain their locale-aware alphabetical order.
  return alphabetical.sort((a,b) => {
    const left = numeric(a), right = numeric(b);
    return left === right ? 0 : left < right ? -1 : 1;
  });
}
