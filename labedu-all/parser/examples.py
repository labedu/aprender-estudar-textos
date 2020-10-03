
sent_exe_0 = "Ninguém gosta de chuva."

sents = ["Ninguém gosta de chuva",
"Retomar o controle foi difícil.",
"A cidade era toda de vidro.",
"Seja quem for.",
"Tem gente morrendo de fome no Brasil.",
"Fugiram do zôo um hipopótamo e um crocodilo.",
]

def get_paragraph():
    js = '\n'.join(sents)
    js = js.replace('\n', ' ')
    return js

par_exe_01 = get_paragraph()

if __name__ == '__main__':
    print(par_exe_01)