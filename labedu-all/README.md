# Labedu Tasks

# Running code in docker

1. Build docker

```
docker build -t labedu-tasks .
```
2. Run docker
 
```
docker run -d -p 5000:5000 labedu-tasks
```

# Postman file

* Ppen postman/LabeduAPIfinal.postman_collection.json in [Postman](https://www.postman.com/) software to have access to more examples on how to call this api.

# Task 0: pre-processing text

###Task auxiliar -> Transforma texto em títulos e parágraphos
* Títulos devem começar com # Subtítulos começam com ##
* Parágrafos devem ser separados por pelo menos uma linha em branco.

### POST call: part raw text to identify paragraphs
* http://0.0.0.0:5000/aux/parsetext
* Body > raw > Text
* How to encode raw text:

```
# --> One sharp means title (optional)
## --> Two shart means subtitle (optional)

Add a whiteline between every paragraph!! (required!)

```

* sending this raw text:

```

# Lutaram e resistiram

## Os negros escravizados lutaram e resistiram

Os negros escravizados
lutaram e resistiram contra o cativeiro de muitas maneiras:
queimaram a lavoura
e promoveram fugas isoladas.
Além disso, era comum sofrerem de profunda depressão,
que os impedia de trabalhar
e, muitas vezes, levava-os à morte.
Também se manifestavam por meio de revoltas
e de assassinatos de senhores ou de capatazes.

Havia também as fugas de grupos,
que depois formavam povoados organizados,
conhecidos como quilombos.
Esses agrupamentos geralmente se fixavam em locais de difícil acesso,
para impedir a ação dos fazendeiros e das autoridades.
 Nesses locais,
 além dos escravos fugidos,
 viviam alguns indígenas e pessoas livres pobres.
 
 
```

* will get this json:
```
{
    "paragraphs": [
        "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ],
    "subtitle": "Os negros escravizados lutaram e resistiram",
    "title": "Lutaram e resistiram"
}
```

# Task 1: OCR (not part of this package)

# Task 2 : Labedu Formatação (labedu-formatacao)

* Entra texto Json formatado em parágrafos e retorna formatação cola et commata
* O texto deve entrar em formato json separado por parágrafos.

### POST call: get cola e commata "formatação"
* http://0.0.0.0:5000/formatacao/getcolaetcommata
* Body > raw > application/json
* sending this json:
```
{
    "paragraphs": [
        "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ],
    "subtitle": "Os negros escravizados lutaram e resistiram",
    "title": "Lutaram e resistiram"
}

```
* will get json:
```
{
    "paragraph_processed": [
        "Os negros escravizados lutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém d isso,\nera comum sofrerem de profunda depressão,\nque os impedia de trabalhar e, muitas vezes, levava- os à morte.\nTambém se manifestavam por meio de revoltas e de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ]
}
```

# Task 3: Labedu Vocabulary (labedu-vocabulary)

* Task 03a --> Do texto em json para vocabulary por parágrafos
* Task 03b --> Do texto em json para vocabulary por parágrafos (vocabulário não se repete)

1. POST call: get vocabulary [with repetition among paragraphs]
* http://0.0.0.0:5000/vocabulary/getvocabulary
* Body > raw > application/json
* sending this json:

```
{
    "paragraphs": [
        "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ],
    "subtitle": "Os negros escravizados lutaram e resistiram",
    "title": "Lutaram e resistiram"
}
```

* will get json:

```
{ "vocabulary": [ [ "ESCRAVIZADOS", "LUTARAM", "RESISTIRAM", "CATIVEIRO", "MANEIRAS", "QUEIMARAM", "LAVOURA", "PROMOVERAM", "FUGAS", "ISOLADAS", "COMUM", "SOFREREM", "PROFUNDA", "DEPRESS\u00c3O", "IMPEDIA", "TRABALHAR", "LEVAVA", "MORTE", "MANIFESTAVAM", "REVOLTAS", "ASSASSINATOS", "SENHORES", "CAPATAZES" ], [ "HAVIA", "FUGAS", "GRUPOS", "FORMAVAM", "POVOADOS", "ORGANIZADOS", "CONHECIDOS", "QUILOMBOS", "AGRUPAMENTOS", "FIXAVAM", "LOCAIS", "DIF\u00cdCIL", "ACESSO", "IMPEDIR", "A\u00c7\u00c3O", "FAZENDEIROS", "AUTORIDADES", "NESSES", "ESCRAVOS", "FUGIDOS", "VIVIAM", "IND\u00cdGENAS", "PESSOAS", "LIVRES", "POBRES" ] ] }
```

2. POST call: get vocabulary [without repetition among paragraphs]
* http://0.0.0.0:5000/vocabulary/getvocabularynr
* Body > raw > application/json
* sending this json:

```
{
    "paragraphs": [
        "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ],
    "subtitle": "Os negros escravizados lutaram e resistiram",
    "title": "Lutaram e resistiram"
}
```

* will get json:


```
{ "vocabularynr": [ [ "ESCRAVIZADOS", "LUTARAM", "RESISTIRAM", "CATIVEIRO", "MANEIRAS", "QUEIMARAM", "LAVOURA", "PROMOVERAM", "FUGAS", "ISOLADAS", "COMUM", "SOFREREM", "PROFUNDA", "DEPRESS\u00c3O", "IMPEDIA", "TRABALHAR", "LEVAVA", "MORTE", "MANIFESTAVAM", "REVOLTAS", "ASSASSINATOS", "SENHORES", "CAPATAZES" ], [ "HAVIA", "GRUPOS", "FORMAVAM", "POVOADOS", "ORGANIZADOS", "CONHECIDOS", "QUILOMBOS", "AGRUPAMENTOS", "FIXAVAM", "LOCAIS", "DIF\u00cdCIL", "ACESSO", "IMPEDIR", "A\u00c7\u00c3O", "FAZENDEIROS", "AUTORIDADES", "NESSES", "ESCRAVOS", "FUGIDOS", "VIVIAM", "IND\u00cdGENAS", "PESSOAS", "LIVRES", "POBRES" ] ] }
```

# Task 4a: Labedu Parser

* Task 04A_a (single paragraph) --> Entra texto Json formatado em um parágrafo e: (1) quebra o parágrafo em linhas; (2) para cada linha separa em palavras; (3) para cada palavra busca informações de parsing: - palavra - lema - etiquetas pós - informações morfológicas.
* Task 04A_b (many paragraphs) --> Entra texto Json formatado em parágrafos (assim como a task 04A_a) e realiza o mesmo processamento de 04A_a para vários parágrafos ao mesmo tempo.

1. POST on http://localhost:5000/parser/parse_paragraph
* Body > raw > application/json
* sending this json:
```


{"paragraph": "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes."}

```

* will get json:
```
{
    "paragraph": [
        {
            "original": "Os negros escravizados lutaram e resistiram contra o cativeiro de muitas maneiras:",
            "parsed": [
                {
                    "id": 0,
                    "pos_tag": {
                        "tag": "DET",
                        "tag_rendered": "Determinante"
                    },
                    "word": "Os",
                    "word_properties": {
                        "lemma": "Os"
                    }
                },
        (..omitted..) 
                {
                    "id": 15,
                    "pos_tag": {
                        "tag": "PUNCT",
                        "tag_rendered": "Pontuação"
                    },
                    "word": ".",
                    "word_properties": {
                        "lemma": "."
                    }
                }
            ],
            "sent_id": 3
        }
    ]
}
```

2. POST on http://localhost:5000/parser/parse_paragraphs
* Body > raw > application/json
* sending this json:
```

{
    "paragraphs": [
        "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ],
    "subtitle": "Os negros escravizados lutaram e resistiram",
    "title": "Lutaram e resistiram"
} 

```

* will get json:
```
{
    "paragraphs": [
        [
            {
                "original": "Os negros escravizados lutaram e resistiram contra o cativeiro de muitas maneiras:",
                "parsed": [
                    {
                        "id": 0,
                        "pos_tag": {
                            "tag": "DET",
                            "tag_rendered": "Determinante"
                        },
                        "word": "Os",
                        "word_properties": {
                            "lemma": "Os"
                        }
                    },
            
		(..omitted..)
                  {
                        "id": 15,
                        "pos_tag": {
                            "tag": "PUNCT",
                            "tag_rendered": "Pontuação"
                        },
                        "word": ".",
                        "word_properties": {
                            "lemma": "."
                        }
                    }
                ],
                "sent_id": 2
            }
        ]
    ]
}

```

# Task 4b: Função Textual 

* Task 04B (many paragraphs) --> Entra texto Json formatado em parágrafos e: (1) quebra o parágrafo em linhas; (2) para cada linha extrai anotações relativas a função textual (PARTICIPANTE, ACONTECIMENTO, CAUSA, LUGAR e/ou TEMPO); (3) Extrai uma tabela geral com expressões extraídas no texto todo em relação aos 5 elementos de função textual citada acima.

* POST on http://localhost:5000/funcao/parse_paragraphs_b
* Body > raw > application/json

* sending this json:
```
{
    "paragraphs": [
        "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ],
    "subtitle": "Os negros escravizados lutaram e resistiram",
    "title": "Lutaram e resistiram"
}
```
* will get json:
```
{
    "paragraphs": [
        {
            "funcao_textual": [
                {
                    "funcao_textual": [
                        "PARTICIPANTE"
                    ],
                    "sent_id": 0,
                    "sentence": "Os negros escravizados lutaram e resistiram contra o cativeiro de muitas maneiras:"
                },
                {
                    "funcao_textual": [
                        "ACONTECIMENTO",
                        "CAUSA"
                    ],
                    "sent_id": 1,
                    "sentence": "queimaram a lavoura e promoveram fugas isoladas."
                },
                {
                    "funcao_textual": [
                        "PARTICIPANTE",
                        "ACONTECIMENTO"
                    ],
                    "sent_id": 2,
                    "sentence": "Além disso, era comum sofrerem de profunda depressão, que os impedia de trabalhar e, muitas vezes, levava-os à morte."
                },
                {
                    "funcao_textual": [],
                    "sent_id": 3,
                    "sentence": "Também se manifestavam por meio de revoltas e de assassinatos de senhores ou de capatazes."
                }
            ],
            "id_par": 0
        },
        {
            "funcao_textual": [
                {
                    "funcao_textual": [
                        "PARTICIPANTE"
                    ],
                    "sent_id": 0,
                    "sentence": "Havia também as fugas de grupos, que depois formavam povoados organizados, conhecidos como quilombos."
                },
                {
                    "funcao_textual": [
                        "PARTICIPANTE",
                        "CAUSA"
                    ],
                    "sent_id": 1,
                    "sentence": "Esses agrupamentos geralmente se fixavam em locais de difícil acesso, para impedir a ação dos fazendeiros e das autoridades."
                },
                {
                    "funcao_textual": [
                        "PARTICIPANTE",
                        "ACONTECIMENTO"
                    ],
                    "sent_id": 2,
                    "sentence": "Nesses locais, além dos escravos fugidos, viviam alguns indígenas e pessoas livres pobres."
                }
            ],
            "id_par": 1
        }
    ],
    "tabela": {
        "ACONTECIMENTO": [
            {
                "action": "promoveram fugas",
                "verb": "promoveram"
            },
            {
                "action": "trabalhar e, muitas vezes, levava-os",
                "verb": "trabalhar"
            },
            {
                "action": "fugidos,",
                "verb": "fugidos"
            },
            {
                "action": "viviam alguns indígenas e pessoas livres pobres.",
                "verb": "viviam"
            }
        ],
        "CAUSA": [
            {
                "name": "promoveram",
                "value": "promoveram fugas isoladas."
            },
            {
                "name": "para",
                "value": "para impedir a ação dos fazendeiros e das autoridades."
            }
        ],
        "LUGAR": [],
        "PARTICIPANTE": [
            "Os negros escravizados",
            "que",
            "que",
            "Esses agrupamentos",
            "alguns indígenas e pessoas livres pobres"
        ],
        "TEMPO": []
    }
}


````

# Task 4cd: Classificação e Sequência Texual. 

* Task 04C_e_04D (many paragraphs) --> Entra texto Json formatado em parágrafos e: (1) quebra o parágrafo em linhas; (2) para cada linha extrai anotação relativa a (i) Etiquetas encontradas: identifica elementos linguísticos (usando etiquetas) em sequências de palavras (head’ e ‘body’ são parte de um mesmo elemento, ‘outside’ corresponde à palavras sem etiquetas e fora de qualquer elemento linguístico. (ii) Identificação de sequências textuais, que podem ser: Descrição, Denominação, Explicação ou inexistente. (3) Realiza classificação do texto: Relato Descritivo, Relato Histórico ou Explicação Histórica.

* POST on http://localhost:5000/textual/parse_paragraphs_cd
* Body > raw > application/json

* sending this json:
```

{
    "paragraphs": [
        "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ],
    "subtitle": "Os negros escravizados lutaram e resistiram",
    "title": "Lutaram e resistiram"
}
```
* will get json:
```

{
    "paragraphs": [
        [
            {
                "annotation": {
                    "textual_sequence_category": {},
                    "tokens": [
                        "Os",
                        "negros",
                        "escravizados",
                        "lutaram",
                        "e",
                        "resistiram",
                        "contra",
                        "o",
                        "cativeiro",
                        "de",
                        "muitas",
                        "maneiras",
                        ":"
                    ],
                    "tokens_expanded": [
                        {
                            "id": 0,
                            "tag_data": {
                                "p": "outside",
                                "tag": "O",
                                "tag_name": ""
                            },
                            "word": "Os"
                        },
                                      (..omitted..)           {
                        {    "id": 12,
                            "tag_data": {
                                "p": "outside",
                                "tag": "O",
                                "tag_name": ""
                            },
                            "word": ":"
                        }
                    ]
                },
                "original": "Os negros escravizados lutaram e resistiram contra o cativeiro de muitas maneiras:",
                "sent_id": 0
            },
           (..omitted..) 
    "text_classification": {
        "categories": "CLA-EXPHIST",
        "categories_name": "Explicação Histórica",
        "count": 1,
        "type_cat": "predominante"
    }
}

```
