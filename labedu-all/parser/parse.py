from spacy_parser.load_parser import nlp

from parser.tags import map_pos, morpho_info


def render_pos(tag):
    if tag in map_pos:
        return {'tag_rendered': map_pos[tag]}
    else:
        return {}


def morpho_proc(raw):
    elems = raw.split('|')

    m = {}
    for e in elems:
        if e in morpho_info:
            mi = morpho_info[e]
            m[mi[0]] = mi[1]

    if not m:
        return {}
    else:
        return {'data': m}


def parse_sentence(sent):
    sent = sent.replace('\n', ' ')
    # print(sent)
    doc = nlp(sent)

    word_l = []
    for i, token in enumerate(doc):
        data = {
            'word': token.text,
            'id': i,
            'word_properties': {
                'lemma': token.lemma_,

            },
            # 'morpho': {
            #  'raw': token.tag_,
            #  **morpho_proc(token.tag_)
            # },
            'pos_tag': {
                'tag': token.pos_,
                **render_pos(token.pos_)
            },
            # 'dependency': {
            #    'value':  token.dep_
            # }

        }
        word_l.append(data)

    return word_l


def parse_sentences_list(sents_l):
    sents = sents_l  #not a list
    sents = nlp(sents.replace('\n', ' '))
    sents = [x.text for x in list(sents.sents)]
    sents = [{'sent_id': i,  'original': s, 'parsed': parse_sentence(s)} for i,s in enumerate(sents)]
    return sents



