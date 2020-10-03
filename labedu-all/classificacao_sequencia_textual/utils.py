from classificacao_sequencia_textual.mappings import ConnectorsMap, VerbsMap, DenominacaoMap


def tag_label_to_name(tag):
    if tag == 'O':
        return ''

    types = {'DEN': DenominacaoMap.labels(),
             'VERB': VerbsMap.labels(),
             'CON': ConnectorsMap.labels()}

    res = tag.split('-')[0]
    return types[res][tag]


def type_label(label):
    if label == 'O':
        return label

    return label.split('-')[-1]


def remove_bio(label):
    if label == 'O':
        return label

    assert(type_label(label) in 'BIO')

    return '-'.join(label.split('-')[:-1])


def size_label(v, start_i):
    assert (type_label(v[start_i]) == 'B')
    size = len(v)

    last_valid_i = start_i
    for i in range(start_i + 1, len(v)):
        label = type_label(v[i])
        if label in ['O', 'B']:
            break
        last_valid_i = i

    return last_valid_i - start_i + 1


def join_ab(a, b):
    assert (len(a) == len(b))
    r = []

    current, size_tag = None, 0
    for i in range(len(a)):
        if size_tag == 0:
            size_tag_a = size_label(a, i) if a[i] != 'O' else 0
            size_tag_b = size_label(b, i) if b[i] != 'O' else 0
            if size_tag_a >= size_tag_b:
                current, size_tag = a, size_tag_a
            else:
                current, size_tag = b, size_tag_b

        if size_tag > 0:
            r.append(current[i])
            size_tag -= 1
        else:
            r.append('O')

    return r


def test_04():
    ll = ['LOC-B', 'LOC-B', 'O', 'O', 'O', 'O', 'LOC-B', 'LOC-B', 'LOC-I', 'LOC-I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
          'O', 'LOC-B']
    lm = ['LOC-B', 'LOC-B', 'LOC-I', 'O', 'O', 'O', 'LOC-B', 'LOC-B', 'LOC-I', 'LOC-I', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
          'O', 'ALOC-B', 'ALOC-I']

    a = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'CON-ADT-B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O']
    b = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'VERB-DIZER-B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O']
    c = ['O', 'LOC-B', 'LOC-I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O']

    print(len(a), len(b), len(c))
    r = join_ab(a, b)
    print(r)
    print(tag_label_to_name('VERB-DIZER'))


if __name__ == '__main__':
    test_04()


