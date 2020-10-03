# 01. first step - text to features

from pathlib import Path
import pickle

from spacy_parser.load_parser import nlp


def doc_to_format(doc):
  lines = [(token.text, token.pos_, token.dep_) for token in doc]
  anota = []
  space = False
  for ll in lines:
    if ll[0] == '\n':
      space = True
    else:
      anota.append((ll[0], 'N' if space else 'O'))
      space = False

  return anota


def join_clean_raw(doc_clean, anota):
    lines = [(token.text, token.pos_, token.dep_) for token in doc_clean]

    if len(anota) != len(lines):
        print('ERROR: sentences different size!! join_clean_raw(doc_clean, anota) ')
        exit(1)

    joined = []
    for i, a in enumerate(anota):
        if anota[i][0] != lines[i][0]:
            print('ERROR: sentences different words!! join_clean_raw(doc_clean, anota) ')
            exit(1)

        joined.append((anota[i][0], lines[i][1], lines[i][2], anota[i][1]))
        pass
    pass
    return joined


def process_paragraph(sent, without_output = False):
  doc_raw = nlp(sent)
  doc_clean = nlp(sent.replace('\n', ' '))

  annotated = doc_to_format(doc_raw)
  joined_sents = join_clean_raw(doc_clean, annotated)

  if without_output:
    joined_sents = [x[0:-1] for x in joined_sents]

  return joined_sents


if __name__ == '__main__':
    data = Path('./data')

    with open(data / 'texts_55.pkl', 'rb') as d:
        data_d = pickle.load(d)

    for i, text in enumerate(data_d):
        par = text['paragraphs']

        new_p = []
        for p in par:
            pro_p = process_paragraph(p)
            new_p.append(pro_p)

        data_d[i]['ptask'] = new_p

    for i in range(len(data_d)):
        assert (len(data_d[i]['paragraphs']) == len(data_d[i]['ptask']))

    with open(data / 'texts_66_crf.pkl', 'wb') as d:
        pickle.dump(data_d, d)
