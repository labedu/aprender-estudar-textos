from parser.tags import map_pos
from parser.tags import morpho_info
from parser.examples import sent_exe_0, par_exe_01
from parser.parse import parse_sentence
from parser.parse import parse_sentences_list


def test():
    print(map_pos['NOUN'])
    print(morpho_info['PR'])
    print('sent: ', sent_exe_0)
    print('par: ', par_exe_01)
    print(parse_sentence(sent_exe_0))


if __name__ == '__main__':
    test()
