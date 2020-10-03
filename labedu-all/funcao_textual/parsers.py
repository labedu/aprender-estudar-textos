from spacy.matcher import Matcher

from funcao_textual.examples import sents
from funcao_textual.mappings import verbo_causa, conector_causalidade, action_verbs, time_list
from spacy_parser.load_parser import nlp


class CausalityParser:
    def __init__(self):
        self.verbo_causa = verbo_causa
        self.conector_causalidade = conector_causalidade
        self.matcher = self.get_causal_matcher()

    def get_causal_matcher(self):
        conectors = self.conector_causalidade
        verbs = self.verbo_causa

        matcher = Matcher(nlp.vocab)
        verb_pattern = [(v, [{"LEMMA": v, "POS": "VERB"}]) for v in verbs]  # add verbs
        conn_pattern = [(c, [{"LOWER": c_} for c_ in c.split()]) for c in self.conector_causalidade]  # add connectors
        for verb, patt in verb_pattern:
            matcher.add(verb, None, patt)
        for conn, patt in conn_pattern:
            matcher.add(conn, None, patt)

        return matcher

    def parse_causality(self, spacy_sent):
        matcher = self.matcher
        doc = spacy_sent  # nlp(sent)
        matches = matcher(doc)
        e = [{'span': doc[start:end],
              'text': doc[start:end].text,
              'start': start, 'end': end,
              'size': end - start} for match_id, start, end in matches]
        e = sorted(e, key=lambda x: 1000 * x['start'] - (x['size']))

        # filter e
        e_filtered = []
        last = -1
        for e_ in e:
            if e_['start'] > last:
                e_filtered.append(e_)
                last = e_['end']
        return e_filtered


cp = CausalityParser()


class FuncaoTextualSentenceParser:

    def __init__(self, sent, spacy_sent):
        self.sent = sent
        self.spacy_sent = spacy_sent

        self.table = {
            'lugar': [],
            'participante': [],
            'acontecimento': [],
            'tempo': [],
            'causa': [],
        }
        self.parse_ner()
        self.parse_subject()
        self.get_action()
        self.parse_time()
        self.parse_causality()

    def parse_ner(self):
        loc_ner = [ent.text for ent in self.spacy_sent.ents if ent.label_ == 'LOC']
        self.table['lugar'] = loc_ner

    def parse_subject(self):
        root = [l for l in self.spacy_sent if l.dep_ == 'nsubj']
        if not root:
            return
        root = root[0]
        b, e = list(root.subtree)[0].i, list(root.subtree)[-1].i + 1
        action_reconstructed = self.spacy_sent[b: e].text
        self.table['participante'] = [action_reconstructed]

    def get_action(self):
        root = [token for token in self.spacy_sent if token.pos_ == 'VERB' and token.lemma_ in action_verbs]
        if not root:
            return None

        action_all = []
        for r in root:
            rights = list(r.rights)
            b, e = list(rights)[0].i, list(rights)[-1].i + 1
            bv = r.i
            action_reconstructed = self.spacy_sent[bv: e].text
            action_all.append({'verb': r.text, 'action': action_reconstructed})
        self.table['acontecimento'] = action_all

    def parse_time(self):
        root = [l for l in self.spacy_sent if l.lemma_ in time_list]

        for root_ in root:
            b, e = list(root_.subtree)[0].i, list(root_.subtree)[-1].i + 1
            action_reconstructed = self.spacy_sent[b: e].text
            self.table['tempo'].append(action_reconstructed)

    def parse_causality(self):
        causality_list = cp.parse_causality(self.spacy_sent)

        causa_all = []
        for causa_ in causality_list:
            causa = causa_['span']
            ending = self.spacy_sent[causa[0].i:]
            causa_all.append({'name': causa.text, 'value': ending.text})
        self.table['causa'] = causa_all

    def __repr__(self):
        s = "sent: {}\nspacy_sent: {} \nner: {} ".format(self.sent, self.spacy_sent, self.table)
        return s

def test_01():
    spacy_sents = [nlp(sent) for sent in sents]
    cp = CausalityParser()
    for ss in spacy_sents:
        ee = cp.parse_causality(ss)

        print('sent:', ss)
        for e_ in ee:
            print(e_)

        print()


def test_02():
    spacy_sents = [nlp(sent) for sent in sents]
    idx = 0
    # print(sents[idx],'\n', spacy_sents[idx])
    tf = FuncaoTextualSentenceParser(sents[idx], spacy_sents[idx])
    print(tf)
    pass


def test_03():
    for sent in sents:
        spacy_sent = nlp(sent)
        tf = FuncaoTextualSentenceParser(sent, spacy_sent)
        print(tf)
        print()
    pass


if __name__ == '__main__':
    test_01()
    test_02()
    test_03()

