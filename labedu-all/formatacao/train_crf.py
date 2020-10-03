# 02. Train CRF
from pathlib import Path

import sklearn_crfsuite
from sklearn_crfsuite import metrics


def load_data():
    # Load Data

    import pickle
    from pathlib import Path
    data = Path('./data')

    with open(data / 'texts_66_crf.pkl', 'rb') as d:
        data_d = pickle.load(d)

    return data_d


def get_train_test(data):
    from sklearn.model_selection import train_test_split
    pars = []

    for d in data:
        for dd in d['ptask']:
            pars.append(dd)

    train, test = train_test_split(pars, shuffle=True, test_size=0.01, random_state=42)
    return train, test


def word2features(sent, i):
    # text to features
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent):
    return [label for token, postag,_,  label in sent]


def sent2tokens(sent):
    return [token for token, postag,_,  label in sent]


### END text to features ###

def train_crf(train, test, show_results = False):
    X_train = [sent2features(s) for s in train]
    y_train = [sent2labels(s) for s in train]

    X_test = [sent2features(s) for s in test]
    y_test = [sent2labels(s) for s in test]

    # before tunned: 0.97
    # tunned: best params: {'c1': 0.3016955332878351, 'c2': 0.02184787646680812}
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.3016955332878351,  # 0.1,
        c2=0.02184787646680812,  # 0.1,
        max_iterations=100,
        all_possible_transitions=True
    )
    crf.fit(X_train, y_train)

    if show_results:
        labels = crf.classes_

        y_pred = crf.predict(X_test)
        metrics.flat_f1_score(y_test, y_pred,
                              average='weighted', labels=labels)

        # group B and I results
        sorted_labels = sorted(
            labels,
            key=lambda name: (name[1:], name[0])
        )
        print(metrics.flat_classification_report(
            y_test, y_pred, labels=sorted_labels, digits=3
        ))

    return crf


def save_crf_to_pickle(crf):
    import pickle

    path_model = Path('./data/crf_model.pkl')
    with open(path_model, 'wb') as fid:
        pickle.dump(crf, fid)
    pass


def get_results():
    pass


if __name__ == '__main__':
    data_d = load_data()
    train, test = get_train_test(data_d)
    crf = train_crf(train, test)
    save_crf_to_pickle(crf)
    print(data_d[0])
    print(train[0])
    print(sent2features(train[0])[0])
    pass
