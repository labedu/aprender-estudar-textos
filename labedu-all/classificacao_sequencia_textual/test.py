
from classificacao_sequencia_textual.examples import sents
from classificacao_sequencia_textual.pipeline import TextToJson


def test():
  paragraph = '\n'.join(sents)
  paragraphs = [paragraph]
  ttj = TextToJson()
  r = ttj.annotate(paragraphs)
  print(r)


if __name__ == '__main__':
  test()

