# from ..data.texts_example import line_01
import sys
import os.path
import spacy

from vocabulary.data.texts_example import line_01, text_01, paragraphs
from spacy_parser.load_parser import nlp

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

stopwords_pt = spacy.lang.pt.stop_words.STOP_WORDS


def vocabulary_of_paragraph(text, exclude_list=[]):
    doc = nlp(text)
    exclude_list = [x.lower() for x in exclude_list]

    # tokens = [token for token in doc]
    elements = [(token.orth_, token.pos_) for token in doc]
    vocabulary = [e[0].upper() for e in elements if e[1] in ['NOUN', 'VERB', 'ADJ', 'PROPN']]
    vocabulary = [x for x in vocabulary if not (x.lower() in stopwords_pt)]
    vocabulary = [x for x in vocabulary if not (x.lower() in exclude_list)]

    final_vocabulary = []
    for i in range(len(vocabulary)):
        word = vocabulary[i]
        if not (word in vocabulary[:i]):
            final_vocabulary.append(word)
        pass

    return final_vocabulary


def vocabulary_paragraphs(pars):
    voc_pars = [vocabulary_of_paragraph(p) for p in pars]
    return voc_pars


def vocabulary_paragraphs_non_repeat(pars):
    voc_pars = vocabulary_paragraphs(pars)
    new_pars = []
    used_voc = []

    for i, p in enumerate(pars):
        # print(i,used_voc)
        voc = vocabulary_of_paragraph(p, used_voc)
        new_pars.append(voc)
        used_voc += voc

    return new_pars


def test_01():
    text = paragraphs[0]

    # voca = vocabulary_of_paragraph(text, stopwords_pt)
    # print(voca)
    voc_pars = vocabulary_paragraphs(paragraphs)
    for v in voc_pars:
        print(v)
    print('---')

    voc_pars_non_repeat = vocabulary_paragraphs_non_repeat(paragraphs)
    for v in voc_pars_non_repeat:
        print(v)


if __name__ == '__main__':
    text = text_01
    print(text)
    test_01()
