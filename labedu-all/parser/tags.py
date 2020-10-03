map_pos = {
  'ADJ': 'Adjetivo',
  'ADP': 'Adposição',
  'ADV': 'Advérbio',
  'AUX': 'Verbo Auxiliar',
  'CONJ': 'Conjunção',
  'CCONJ': 'Conjunção Coordenada',
  'SCONJ': 'Conjunção Subordinada',
  'DET': 'Determinante',
  'INTJ': 'Interjeição',
  'NOUN': 'Substantivo',
  'NUM': 'Numeral',
  'PART': 'Partícula',
  'PRON': 'Pronome',
  'PROPN': 'Nome próprio',
  'PUNCT': 'Pontuação',
  'SCONJ': 'Conjunção Subordinada',
  'SYM': 'Símbolo',
  'VERB': 'Verbo',
  'X': 'outro',
}

morpho_info = {
    ## Gender
    'M': ('gênero', 'Masculino'),
    'F': ('gênero', 'Feminino'),
    'M/F': ('gênero', 'Masculino/Feminino'),

    ##number
    'S': ('número', 'Singular'),
    'P': ('número', 'Plural'),
    'S/P': ('número', 'Singular/Plural'),

    ##case
    'NOM': ('caso', 'Nominativo'),
    'ACC': ('caso', 'Acusativo'),
    'DAT': ('caso', 'Dativo'),
    'PIV': ('caso', 'Genitivo'),

    ##person
    '1': ('pessoa', 'Primeira pessoa'),
    '2': ('pessoa', 'Segunda pessoa'),
    '3': ('pessoa', 'Terceira pessoa'),
    '1/3': ('pessoa', 'Primeira/terceira pessoa'),
    'P1': ('pessoa', 'Primeira pessoa'),
    'P2': ('pessoa', 'Segunda pessoa'),
    'P3': ('pessoa', 'Terceira pessoa'),
    'P1/P3': ('pessoa', 'Primeira/terceira pessoa'),

    ##tense/mode
    'PR': ('tempo', 'Tempo perfeito'),
    'IMPF': ('tempo', 'Imperfeito'),
    'PS': ('tempo', 'Perfeito Simples'),
    'MQP': ('tempo', 'Mais que perfeito'),
    'PS/MQP': ('tempo', 'Perfeito Simples/Mais que perfeito'),
    'FUT': ('tempo', 'Futuro'),
    'COND': ('tempo', 'Condicional'),
    'IND': ('tempo', 'Indicativo'),
    'SUBJ': ('tempo', 'Subjuntivo'),
    'IMP': ('tempo', 'Imperfeito')
}
