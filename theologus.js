/**
 * Theologus Passagem Plugin
 * Busca passagens bíblicas em Português usando a API bible-api.com (tradução Almeida)
 *
 * Uso: passagem('1 Cronicas 4')
 *      passagem('João 3:16')
 *      passagem('Genesis 1:1-3')
 */

const LIVROS_PT = {
  // Antigo Testamento
  'genesis': 'genesis', 'gênesis': 'genesis', 'gn': 'genesis',
  'exodo': 'exodus', 'êxodo': 'exodus', 'ex': 'exodus',
  'levitico': 'leviticus', 'levítico': 'leviticus', 'lv': 'leviticus',
  'numeros': 'numbers', 'números': 'numbers', 'nm': 'numbers',
  'deuteronomio': 'deuteronomy', 'deuteronômio': 'deuteronomy', 'dt': 'deuteronomy',
  'josue': 'joshua', 'josué': 'joshua', 'js': 'joshua',
  'juizes': 'judges', 'juízes': 'judges', 'jz': 'judges',
  'rute': 'ruth', 'rt': 'ruth',
  '1 samuel': '1+samuel', '1samuel': '1+samuel', '1sm': '1+samuel',
  '2 samuel': '2+samuel', '2samuel': '2+samuel', '2sm': '2+samuel',
  '1 reis': '1+kings', '1reis': '1+kings', '1rs': '1+kings',
  '2 reis': '2+kings', '2reis': '2+kings', '2rs': '2+kings',
  '1 cronicas': '1+chronicles', '1 crônicas': '1+chronicles', '1cr': '1+chronicles',
  '2 cronicas': '2+chronicles', '2 crônicas': '2+chronicles', '2cr': '2+chronicles',
  'esdras': 'ezra', 'ed': 'ezra',
  'neemias': 'nehemiah', 'ne': 'nehemiah',
  'ester': 'esther', 'et': 'esther',
  'jo': 'job', 'job': 'job', 'jó': 'job',
  'salmos': 'psalms', 'sl': 'psalms',
  'proverbios': 'proverbs', 'provérbios': 'proverbs', 'pv': 'proverbs',
  'eclesiastes': 'ecclesiastes', 'ec': 'ecclesiastes',
  'cantares': 'song+of+solomon', 'ct': 'song+of+solomon',
  'isaias': 'isaiah', 'isaías': 'isaiah', 'is': 'isaiah',
  'jeremias': 'jeremiah', 'jr': 'jeremiah',
  'lamentacoes': 'lamentations', 'lamentações': 'lamentations', 'lm': 'lamentations',
  'ezequiel': 'ezekiel', 'ez': 'ezekiel',
  'daniel': 'daniel', 'dn': 'daniel',
  'oseias': 'hosea', 'os': 'hosea',
  'joel': 'joel', 'jl': 'joel',
  'amos': 'amos', 'amós': 'amos', 'am': 'amos',
  'abdias': 'obadiah', 'obadias': 'obadiah', 'ob': 'obadiah',
  'jonas': 'jonah', 'jn': 'jonah',
  'miqueias': 'micah', 'mq': 'micah',
  'naum': 'nahum', 'na': 'nahum',
  'habacuque': 'habakkuk', 'hc': 'habakkuk',
  'sofonias': 'zephaniah', 'sf': 'zephaniah',
  'ageu': 'haggai', 'ag': 'haggai',
  'zacarias': 'zechariah', 'zc': 'zechariah',
  'malaquias': 'malachi', 'ml': 'malachi',
  // Novo Testamento
  'mateus': 'matthew', 'mt': 'matthew',
  'marcos': 'mark', 'mc': 'mark',
  'lucas': 'luke', 'lc': 'luke',
  'joao': 'john', 'joão': 'john',
  'atos': 'acts', 'at': 'acts',
  'romanos': 'romans', 'rm': 'romans',
  '1 corintios': '1+corinthians', '1 coríntios': '1+corinthians', '1co': '1+corinthians',
  '2 corintios': '2+corinthians', '2 coríntios': '2+corinthians', '2co': '2+corinthians',
  'galatas': 'galatians', 'gálatas': 'galatians', 'gl': 'galatians',
  'efesios': 'ephesians', 'efésios': 'ephesians', 'ef': 'ephesians',
  'filipenses': 'philippians', 'fp': 'philippians',
  'colossenses': 'colossians', 'cl': 'colossians',
  '1 tessalonicenses': '1+thessalonians', '1ts': '1+thessalonians',
  '2 tessalonicenses': '2+thessalonians', '2ts': '2+thessalonians',
  '1 timoteo': '1+timothy', '1 timóteo': '1+timothy', '1tm': '1+timothy',
  '2 timoteo': '2+timothy', '2 timóteo': '2+timothy', '2tm': '2+timothy',
  'tito': 'titus', 'tt': 'titus',
  'filemom': 'philemon', 'fm': 'philemon',
  'hebreus': 'hebrews', 'hb': 'hebrews',
  'tiago': 'james', 'tg': 'james',
  '1 pedro': '1+peter', '1pe': '1+peter',
  '2 pedro': '2+peter', '2pe': '2+peter',
  '1 joao': '1+john', '1 joão': '1+john', '1jo': '1+john',
  '2 joao': '2+john', '2 joão': '2+john', '2jo': '2+john',
  '3 joao': '3+john', '3 joão': '3+john', '3jo': '3+john',
  'judas': 'jude', 'jd': 'jude',
  'apocalipse': 'revelation', 'ap': 'revelation',
};

/**
 * Faz o parse de uma referência bíblica em português.
 * Suporta livros com número no início como "1 Cronicas 4".
 *
 * @param {string} referencia - Ex: "1 Cronicas 4", "João 3:16", "Genesis 1:1-3"
 * @returns {{ livro: string, capitulo: number, versiculo?: number, versiculoFim?: number } | null}
 */
function parsearReferencia(referencia) {
  const ref = referencia.trim();

  // Regex: captura livros com número inicial (ex: "1 Cronicas") ou sem número (ex: "João")
  // Formato: [número] NomeLivro Capítulo[:Versículo[-VersículoFim]]
  const regex = /^(\d+\s+[A-Za-zÀ-ÿ]+|[A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+)*)\s+(\d+)(?::(\d+)(?:-(\d+))?)?$/;
  const match = ref.match(regex);

  if (!match) {
    return null;
  }

  return {
    livro: match[1].trim(),
    capitulo: parseInt(match[2], 10),
    versiculo: match[3] ? parseInt(match[3], 10) : null,
    versiculoFim: match[4] ? parseInt(match[4], 10) : null,
  };
}

/**
 * Converte o nome do livro em português para o formato da API.
 *
 * @param {string} nomeLivro - Nome em português (ex: "1 Cronicas", "João")
 * @returns {string|null} - Nome para a API (ex: "1+chronicles", "john") ou null se não encontrado
 */
function resolverLivro(nomeLivro) {
  const chave = nomeLivro
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // remove acentos para busca
    .trim();

  // Tenta com acento removido
  for (const [ptKey, apiVal] of Object.entries(LIVROS_PT)) {
    const ptNorm = ptKey
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '');
    if (ptNorm === chave) return apiVal;
  }

  return null;
}

/**
 * Busca uma passagem bíblica e retorna o texto.
 *
 * @param {string} referencia - Referência em português (ex: "1 Cronicas 4")
 * @returns {Promise<{ referencia: string, texto: string, versiculos: Array }>}
 */
async function passagem(referencia) {
  const parsed = parsearReferencia(referencia);

  if (!parsed) {
    throw new Error(
      `Referência inválida: "${referencia}". ` +
      'Use o formato: "Livro Capítulo" ou "Livro Capítulo:Versículo". ' +
      'Exemplo: "1 Cronicas 4", "João 3:16"'
    );
  }

  const apiLivro = resolverLivro(parsed.livro);

  if (!apiLivro) {
    throw new Error(
      `Livro não reconhecido: "${parsed.livro}". ` +
      'Verifique o nome do livro em português.'
    );
  }

  let endpoint = `${apiLivro}+${parsed.capitulo}`;
  if (parsed.versiculo !== null) {
    endpoint += `:${parsed.versiculo}`;
    if (parsed.versiculoFim !== null) {
      endpoint += `-${parsed.versiculoFim}`;
    }
  }

  const url = `https://bible-api.com/${endpoint}?translation=almeida`;

  const resp = await fetch(url);
  if (!resp.ok) {
    throw new Error(`Erro ao buscar passagem: HTTP ${resp.status}`);
  }

  const dados = await resp.json();

  if (dados.error) {
    throw new Error(`Erro da API: ${dados.error}`);
  }

  return {
    referencia: dados.reference,
    texto: dados.text,
    versiculos: dados.verses || [],
  };
}

// Exporta para uso como módulo (Node.js) e também expõe globalmente no browser
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { passagem, parsearReferencia, resolverLivro };
} else {
  window.theologus = { passagem, parsearReferencia, resolverLivro };
}
