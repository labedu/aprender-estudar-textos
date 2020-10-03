from classificacao_sequencia_textual.examples import sents
from classificacao_sequencia_textual.mappings import ConnectorsMap, VerbsMap, DenominacaoMap
from spacy_parser.load_parser import nlp


class ParserTags:
    def __init__(self, label_tokens_map, label_names):
        self.tokens_map = label_tokens_map
        self.labels_map = label_names

        # 1. assert all tokens are different
        assert (self.test_if_unique())

        # 2. get map of tokens - class
        self.token_cla = self.token_cla()

        # 3. create a map tree from tokens
        self.tokens_tree = self.create_map_tree_from_tokens()
        # print(self.tokens_tree)

    def test_if_unique(self):
        # Test if map have no repeated tokens
        tm = self.tokens_map
        m = {}
        for item in tm.items():
            for elem in item[1]:
                if elem in m:
                    #print('Err: ', elem)  ##
                    return False
                else:
                    m[elem] = elem
        return True

    def token_cla(self):
        # Make inversion from tokens to class
        m = {}
        connector_type = self.tokens_map

        for ct in connector_type.items():
            type_e = ct[0]
            for elem in ct[1]:
                m[elem] = type_e
        return m

    def create_map_tree_from_tokens(self):
        # Make all tokens part of a tree with leafs with 'class' values
        m_c = self.token_cla

        mm = {}
        for c in m_c.keys():
            con = c
            cla = m_c[c]

            curr_map = mm
            con_ll = con.split()

            for i in range(len(con_ll)):
                tok = con_ll[i]

                if not (tok in curr_map):
                    curr_map[tok] = {}

                if i == (len(con_ll) - 1):  # last token
                    curr_map[tok] = {**curr_map[tok], 'class': cla}

                else:  # not the last token
                    # curr_map[tok] = {**curr_map[tok], 'class': cla}
                    if not ('child' in curr_map[tok]):
                        curr_map[tok] = {'child': {}}

                    curr_map = curr_map[tok]['child']
        return mm

    def parse(self, sent_ll):
        # parse sentence with values from map
        con_ll = [x.lower() for x in sent_ll]
        map_reconstructed = self.tokens_tree
        sent_tok = ['O'] * len(con_ll)
        # print(map_reconstructed)

        for j in range(len(con_ll)):
            if sent_tok[j] != 'O':
                continue

            mr = map_reconstructed
            for i in range(j, len(con_ll)):
                word = con_ll[i]

                if not (word in mr):
                    break

                mr = mr[word]
                if 'class' in mr:
                    for k in range(j, i + 1):

                        if k == j:
                            sent_tok[k] = mr['class'] + '-B'
                        else:
                            sent_tok[k] = mr['class'] + '-I'

                if 'child' in mr:
                    mr = mr['child']
        return sent_tok


class ParseConnectors:
    def __init__(self):
        self.pc = ParserTags(ConnectorsMap.tokens(), ConnectorsMap.labels())

    def parse(self, spacy_sent):
        text_ll = [w.text for w in spacy_sent]
        return self.pc.parse(text_ll)


class ParseDenominacao:
    def __init__(self):
        self.pc = ParserTags(DenominacaoMap.tokens(), DenominacaoMap.labels())

    def parse(self, spacy_sent):
        text_ll = [w.text for w in spacy_sent]
        return self.pc.parse(text_ll)


class ParseVerbs:
  def __init__(self):
    self.verbs_parser = ParserTags(VerbsMap.tokens(), VerbsMap.labels())

  def parse(self, spacy_sentence):
    sentence_lemma = [x.lemma_.lower() if x.pos_ == 'VERB' else "x" for x in spacy_sentence]
    parsed_result = self.verbs_parser.parse(sentence_lemma)
    return parsed_result


def test_01():
    pc = ParseConnectors()
    pv = ParseVerbs()
    pd = ParseDenominacao()

    for sent in sents:
        spacy_sent = nlp(sent)

        # A. connectors
        print(pc.parse(spacy_sent))

        # B. Verbs
        result = pv.parse(spacy_sent)
        print(result)

        # C. Denominacao
        result = pd.parse(spacy_sent)
        print(result)

def test_02():
    ss = [
        'Por isso ele não foi à escola.',
        'Entendeu-se por isso a culpa.'
    ]
    pc = ParseConnectors()
    pv = ParseVerbs()
    pd = ParseDenominacao()

    for sent in ss:
        spacy_sent = nlp(sent)
        print(spacy_sent)

        # A. connectors
        result = pc.parse(spacy_sent)
        print('[connectors]\n', result)


        # B. Verbs
        result = pv.parse(spacy_sent)
        print('[verbs]\n', result)

        # C. Denominacao
        result = pd.parse(spacy_sent)
        print('[den]\n', result)


def test_03():
    ss = [
        'Entendeu-se por isso a culpa.'
    ]
    spacy_sent = nlp(ss[0])
    pc = ParseConnectors()
    # A. connectors
    result = pc.parse(spacy_sent)
    print('[connectors]\n', result)

if __name__ == '__main__':
    #test_01()
    test_03()
    pass
