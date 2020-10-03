last_symbol_line = "!,.:;?)}]"
first_symbol_line = "({["


def ch_split(ch):
  if ch in first_symbol_line:
    return ['\n',ch]
  elif ch in last_symbol_line:
    return [ch, '\n']
  #else:
  return [ch]


def process_paragraph_rules(sent):
  sent = sent.strip()
  sent = sent.replace('\n', ' ')
  sent = sent.replace('  ', '')

  sent2 =  ''.join([s for s in sent for s in ch_split(s)])
  sent2 = sent2.replace('\n ','\n')
  sent2 = sent2.strip()

  return sent2


def test():
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


  sent2 = process_paragraph_rules(sent)
  print(sent2)
  print('({})'.format(sent2[-1]))


if __name__ == '__main__':
  test()
