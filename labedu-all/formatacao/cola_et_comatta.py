# 03. Cola et commata
from formatacao.data.texts_example import get_texts
from formatacao.text_to_features import process_paragraph
from formatacao.train_crf import sent2features

import pickle


def load_model():
    from pathlib import Path
    data = Path('./formatacao/data')
    path_model = data / 'crf_model.pkl'

    # load it again
    with open(path_model, 'rb') as fid:
        crf = pickle.load(fid)
    return crf


crf = load_model()


def build_sents(par_words, y_pred):
    assert(len(par_words) == len(y_pred))
    import string

    par = par_words[0]
    for i in range(1,len(par_words)):
        if y_pred[i] == 'N':
            par += '\n' + par_words[i]
        elif (len(par_words[i]) == 1) and par_words[i] in string.punctuation:
            par += par_words[i]
        else:
            par += ' ' + par_words[i]

    return par


def paragraph_to_features(text):
    par = process_paragraph(text)
    feats = sent2features(par)
    y_pred = crf.predict([feats])

    par_words = [x[0] for x in par]

    paragraph_rebuilt = build_sents(par_words, y_pred[0])
    return paragraph_rebuilt


if __name__ == '__main__':
    texts = get_texts()
    par = paragraph_to_features(texts[0])
    print(par)



