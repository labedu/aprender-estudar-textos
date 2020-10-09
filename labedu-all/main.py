
from funcao_textual.pipeline import TextToJson as TextToJsonFuncao
from classificacao_sequencia_textual.pipeline import TextToJson as TextToJsonTextual
ttjF = TextToJsonFuncao()
ttjT = TextToJsonTextual()

example = {
    "paragraphs": [
        "Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes.",
        "Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."
    ],
    "subtitle": "Os negros escravizados lutaram e resistiram",
    "title": "Lutaram e resistiram"
}


if __name__ == '__main__':
    pars = example['paragraphs']
    r = ttjF.annotate(pars)
    print(r)
    pass