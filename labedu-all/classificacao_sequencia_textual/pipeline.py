from classificacao_sequencia_textual.parsers import ParseConnectors, ParseVerbs, ParseDenominacao
from classificacao_sequencia_textual.utils import join_ab, type_label, size_label, tag_label_to_name, remove_bio
from classificacao_sequencia_textual.examples import sents
from classificacao_sequencia_textual.tasks import SequenciaTextual, ClasificacaoTextual
from spacy_parser.load_parser import nlp


class PipelineAnnotators:
    def __init__(self):
        self.pc = ParseConnectors()
        self.pv = ParseVerbs()
        self.pd = ParseDenominacao()

    def join_tags(self, spacy_sent):
        parsed_pipeline = [
            self.pc.parse(spacy_sent),
            self.pv.parse(spacy_sent),
            self.pd.parse(spacy_sent),
        ]
        self.parsed_pipeline = parsed_pipeline

        assert(len(parsed_pipeline) == 3)
        r = join_ab(parsed_pipeline[0], parsed_pipeline[1])
        r2 = join_ab(r, parsed_pipeline[2])

        self.result = r2
        return self.result


    def show_result(self):
        if not self.parsed_pipeline:
            return ""
        assert (len(self.parsed_pipeline) == 3)
        for p in self.parsed_pipeline:
            print(p)
        print(self.result)
        print()


class SentenceToJson:
    def __init__(self):
        self.pa = PipelineAnnotators()
        self.st = SequenciaTextual()  # 4D
        # self.ct = ClasificacaoTextual()   # 4C
        pass

    def annotate(self, spacy_sentence):
        sentence_tokens = [w.text for w in spacy_sentence]
        tags = self.pa.join_tags(spacy_sentence)
        assert (len(tags) == len(sentence_tokens))

        short_labels = [remove_bio(t) for t in tags if type_label(t) == 'B']
        st_labels = self.st.seq_transform(short_labels)
        st_type = self.st.classify(st_labels)

        sentence_j = [{'id': i,
                       'word': word,
                       'tag_data': {
                           'tag': remove_bio(tag),
                           'p': {'B': 'head', 'I': 'body', 'O': 'outside'}[type_label(tag)],
                           'tag_name': tag_label_to_name(remove_bio(tag))

                       }} for i, (word, tag) in enumerate(zip(sentence_tokens, tags))]

        st_type_expanded = {}
        if st_type:
            st_type_expanded = {

                'obs': st_type['type_cat'],
                # 'type': st_type.keys(),
                'count': st_type['count'],
                'category': st_type['categories_name'].split('|'),
                # 'tokens': sentence_j,
            }

        sentence_all = {
            'tokens': sentence_tokens,
            'textual_sequence_category': st_type_expanded,
            'tokens_expanded': sentence_j,
        }

        return short_labels, sentence_all


class TextToJson:
    def __init__(self):
        self.stj = SentenceToJson()       # sl, m = stj.annotate(n)
        self.ct = ClasificacaoTextual()   # 4C
        pass

    def annotate(self, pars):

      labels = []
      paragraphs = []
      for i_p, p in enumerate(pars):
        text = p
        text = text.replace('\n', ' ').strip()
        sentences = nlp(text).sents
        paragraph = []
        for i,s in enumerate(sentences):
          short_labels, ann = self.stj.annotate(s)
          labels += short_labels
          paragraph.append({
            'sent_id': i,
            'original': s.text,
            'annotation': ann,
          })
        paragraphs.append(paragraph)

        labels_transform = ClasificacaoTextual.seq_transform(labels)
        ct = ClasificacaoTextual.classify(
            labels_transform
        )

      return {
            'text_classification': ct,
            'paragraphs': paragraphs,
      }


def test_ttj():
  paragraph = '\n'.join(sents)
  paragraphs = [paragraph]
  ttj = TextToJson()
  r = ttj.annotate(paragraphs)
  print(r)


def test_ssj():
    for s in sents[:4]:
        n = nlp(s)
        stj = SentenceToJson()
        sl, m = stj.annotate(n)
        print(sl)
        print(m)  ####
        print('======')


if __name__ == '__main__':
    test_ttj()
    test_ssj()
