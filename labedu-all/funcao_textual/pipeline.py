
from funcao_textual.examples import text
from spacy_parser.load_parser import nlp
from funcao_textual.parsers import FuncaoTextualSentenceParser
from funcao_textual.examples import text


class FuncaoTextual:
    def __init__(self, spacy_sents):
        self.spacy_sents = spacy_sents
        self.sents = [sent.text for sent in spacy_sents]
        self.m = {'PARTICIPANTE': [],
                  'ACONTECIMENTO': [],
                  'TEMPO': [],
                  'CAUSA': [],
                  'LUGAR': []}


    def parse(self):
        funcao = []
        for sent, spacy_sent in zip(self.sents, self.spacy_sents):
            sent_parser = FuncaoTextualSentenceParser(sent, spacy_sent)
            table = sent_parser.table
            keys = [k.upper() for k, v in table.items() if v]
            for k in keys:
                kl = k.lower()
                self.m[k] += table[kl]
            funcao.append(keys)

        return {'textual_function': [{'sent_id': i,
                                      'sentence': fs[1],
                                      'funcao_textual': fs[0]} for i, fs in enumerate(zip(funcao, self.sents))],
                'table': self.m}


class TextToJson:
    def __init__(self):
        pass

    def annotate(self, pars):

        paragraphs = []
        sentences_all = []
        for i_p, p in enumerate(pars):
            text_rec = p.replace('\n', ' ').strip()
            sentences = [nlp(sent.text.strip()) for sent in nlp(text_rec).sents]
            sentences_all += sentences

            ft = FuncaoTextual(sentences)
            result = ft.parse()

            table = result['table']
            text_func = result['textual_function']

            paragraphs.append({
                'id_par': i_p,
                'funcao_textual': text_func
            })

        ft = FuncaoTextual(sentences_all)
        result = ft.parse()
        table = result['table']

        return {
            'tabela': table,
            'paragraphs': paragraphs
        }


def test_01():
    spacy_sent = [nlp(text)]
    ft = FuncaoTextual(spacy_sent)
    r = ft.parse()
    print(r)


def test_02():
    pars = [text, text]
    ttj = TextToJson()
    r = ttj.annotate(pars)
    print(r)


if __name__ == '__main__':
    test_01()
    test_02()
