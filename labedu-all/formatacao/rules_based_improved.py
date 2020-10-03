from spacy_parser.load_parser import nlp


class ColaEtCommata:
    # a. Paragraph come in.
    # b. remove all line breaks '\n' to ' '
    # c. tokenize lines
    # d. For each line: tokenize and find pos_tags (in list)
    # e. build rules on top of lines.

    def __init__(self, paragraph):
        self.last_symbol_line = "!,.:;?)}]"
        self.first_symbol_line = "({["
        self.prep_ll = ['para', 'por', 'pelo', 'pela', 'pelo', 'pelas']
        self.consonants = 'bcdfghjklmnpqrstvwxyz'

        self.paragraph = paragraph.replace('\n', ' ')  # (a) and (b)
        # self.lines = [x.text for x in list(nlp(self.paragraph).sents)] # (c)
        self.lines = nlp(self.paragraph).sents

        self.tokenized_lines = []  # (d)
        for line in self.lines:
            self.tokenized_lines.append([(token.text, token.pos_) for token in line])

    def get_tokenized_lines(self):
        return self.tokenized_lines

    def __ch_split(self, curr_i, curr_ii=None):
        ch = curr_i[0]
        pos = curr_i[1]
        if ch in self.first_symbol_line:
            return [('\n', 'NEWLINE'), curr_i]
        elif ch in self.last_symbol_line:
            return [curr_i, ('\n', 'NEWLINE')]
        elif 'CONJ' in pos:
            return [('\n', 'NEWLINE'), curr_i]
        elif 'ADP' in pos and (ch.lower() in self.prep_ll):
            return [('\n', 'NEWLINE'), curr_i]
        return [curr_i]

    def __rule_line_commata(self, sent_tok):
        max_len = len(sent_tok)  # - 1
        result = []
        for i in range(max_len):
            result += self.__ch_split(sent_tok[i])  # , sent_tok[i + 1])

        return result

    def __reconstruct_sentence(self, sent_pos_ll):
        lines = []
        line_s = ""

        for elem, _ in sent_pos_ll:
            if elem == '\n':
                lines.append(line_s.strip())
                line_s = ""
            elif elem in self.last_symbol_line:
                line_s += elem
            else:
                space = ' '
                if len(line_s) > 2:
                    if (line_s[-2] == ' ') and line_s[-1] in self.consonants:  # and (elem[0] in 'aeiou'):
                        space = ''

                line_s = line_s + space + elem

        if line_s:
            lines.append(line_s.strip())

        lines = [line.strip() for line in lines if line.strip()]

        return lines

    def process(self):

        res = []
        for line in self.tokenized_lines:
            line_c = self.__rule_line_commata(line)
            res_line = self.__reconstruct_sentence(line_c)
            for rl in res_line:
                res.append(rl)

        return res


def process_paragraph_rules2(sent):
  sent = sent.strip()
  sent = sent.replace('\n', ' ')
  for i in range(3):
    sent = sent.replace('  ', ' ')

  cec = ColaEtCommata(sent)
  sent2 = '\n'.join(cec.process())

  sent2 = sent2.replace('\n ','\n')
  sent2 = sent2.strip()

  return sent2


def test2():
  sent = """Os negros escravizados
lutaram e resistiram contra o cativeiro de muitas maneiras:
queimaram a lavoura
e promoveram fugas isoladas.
Além disso, era comum sofrerem de profunda depressão,
que os impedia de trabalhar
e, muitas vezes, levava-os à morte.
Também se manifestavam por meio de revoltas
e de assassinatos de senhores ou de capatazes.
"""


  sent2 = process_paragraph_rules2(sent)
  print(sent2)


def test1():
    cec = ColaEtCommata(' Olá mundo. Estou para teste.')
    res = '\n'.join(cec.process())
    print(res)


if __name__ == '__main__':
    test1()
    test2()
