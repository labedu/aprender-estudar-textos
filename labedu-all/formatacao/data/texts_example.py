
text_exe_01 = """Os negros escravizados\nlutaram e resistiram contra o cativeiro de muitas maneiras:\nqueimaram a lavoura\ne promoveram fugas isoladas.\nAlém disso, era comum sofrerem de profunda depressão,\nque os impedia de trabalhar\ne, muitas vezes, levava-os à morte.\nTambém se manifestavam por meio de revoltas\ne de assassinatos de senhores ou de capatazes."""

text_exe_02 = """Havia também as fugas de grupos,\nque depois formavam povoados organizados,\nconhecidos como quilombos.\nEsses agrupamentos geralmente se fixavam em locais de difícil acesso,\npara impedir a ação dos fazendeiros e das autoridades.\nNesses locais,\nalém dos escravos fugidos,\nviviam alguns indígenas e pessoas livres pobres."""

text_exe_03 = """

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
 
 """




def get_texts():
    text01 =  text_exe_01.replace('\n', ' ')
    text02 =  text_exe_02.replace('\n', ' ')
    return [text01, text02]


