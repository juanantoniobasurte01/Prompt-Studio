import legacy from '../../recursos/identity_legacy.json';

const populated = value => Boolean(value?.selected?.trim() || value?.manual?.trim());

// Normalize known old choices without rewriting arbitrary custom descriptions or SQLite.
export function normalizeIdentity(fields = {}) {
  const result = Object.fromEntries(Object.entries(fields).map(([key,value]) => [key,{...value}]));
  for (const [key,rules] of Object.entries(legacy)) {
    const original = fields[key];
    if (!original) continue;
    for (const type of ['selected','manual']) {
      const rule = rules[original[type]?.trim()];
      if (rule) result[key][type] = rule.value;
    }
    const effective = original.manual?.trim() || original.selected?.trim();
    for (const [target,value] of Object.entries(rules[effective]?.extras || {})) {
      if (!populated(result[target])) result[target] = {selected:'', manual:value};
    }
  }
  return result;
}
