import React from 'react';
import {sortFieldOptions} from './ordering';

export default function GuidedField({field, value = {}, onChange, t = text => text, language = 'es'}) {
  const [id, label] = field;
  const selected = value.selected || '';
  const options = sortFieldOptions(field, t, language);
  const visible = selected && !options.includes(selected) ? [selected, ...options] : options;

  return <div className="field-card">
    <label htmlFor={`field-${id}`}>{t(label)}</label>
    <select
      id={`field-${id}`}
      value={selected}
      onChange={event => onChange(id, 'selected', event.target.value)}
    >
      <option value="">{t('Sin seleccionar')}</option>
      {visible.map(option => <option value={option} key={option}>{t(option, {context:id})}</option>)}
    </select>
    <textarea
      rows="2"
      aria-label={t('{label}: entrada manual', {label:t(label)})}
      value={value.manual || ''}
      onChange={event => onChange(id, 'manual', event.target.value)}
      placeholder={t('Introducir manualmente...')}
    />
  </div>;
}
