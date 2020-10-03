from collections import Counter
#from mappings import SequenciaTextualLabels


# Task 4c
class SequenciaTextual:
    @staticmethod
    def classify(data):
        assert (type(data) == list)
        assert (all([e in SequenciaTextual.labels().keys() for e in data]))
        if len(data) == 0:
            return {}

        c = Counter(data)
        while (c.most_common()[-1][1] != c.most_common()[0][1]):
            data = [v for v in data if v != c.most_common()[-1][0]]
            c = Counter(data)

        type_cat = 'predominante' if len(c) == 1 else 'misto'
        keys_join = '|'.join(list(c.keys()))
        cats_name = '|'.join([SequenciaTextual.labels()[e] for e in list(c.keys())])

        return {
            'type_cat': type_cat,
            'categories': keys_join,
            'count': len(c),
            'categories_name': cats_name,
        }

    @staticmethod
    def seq_transform(seq_list):
        m = {
            # Descrição
            'VERB-DESC': 'SET-DESCRICAO',

            # Denominação
            'DEN-DENON': 'SET-DENOMINACAO',

            # Explicação Histórica
            'CON-CAU': 'SET-EXPLICACAO',  # 'CON-CAU': 'conector causal',
            'CON-TCA': 'SET-EXPLICACAO',  # 'CON-TCA': 'conector temporal-causal',
            'CON-FIN': 'SET-EXPLICACAO',  # 'CON-FIN': 'conector de finalidade',
            'CON-CND': 'SET-EXPLICACAO',  # 'CON-CND': 'conector condicional',
            'VERB-CAUSA': 'SET-EXPLICACAO',  # 'VERB-CAUSA': 'verbo de causa',
        }
        transformed = [m[s] for s in seq_list if s in m.keys()]
        return transformed

    @staticmethod
    def labels():
        return {
            'SET-DESCRICAO': 'Descrição',
            'SET-DENOMINACAO': 'Denominação',
            'SET-EXPLICACAO': 'Explicação',
        }


# Task 4D
class ClasificacaoTextual:
    @staticmethod
    def classify(data):
        assert (type(data) == list)
        assert (all([e in ClasificacaoTextual.labels().keys() for e in data]))
        if len(data) == 0:
            return {}

        c = Counter(data)
        while (c.most_common()[-1][1] != c.most_common()[0][1]):
            data = [v for v in data if v != c.most_common()[-1][0]]
            c = Counter(data)

        type_cat = 'predominante' if len(c) == 1 else 'misto'
        keys_join = '|'.join(list(c.keys()))
        cats_name = '|'.join([ClasificacaoTextual.labels()[e] for e in list(c.keys())])

        return {
            'type_cat': type_cat,
            'categories': keys_join,
            'count': len(c),
            'categories_name': cats_name,
        }

    @staticmethod
    def seq_transform(seq_list):
        m = {
            # Relato Descritivo
            'VERB-DESC': 'CLA-RELDESC',
            'DEN-DENON': 'CLA-RELDESC',

            # Relato Histórico
            'CON-TMP': 'CLA-RELHIST',

            # Explicação Histórica
            'CON-CAU': 'CLA-EXPHIST',  # 'CON-CAU': 'conector causal',
            'CON-TCA': 'CLA-EXPHIST',  # 'CON-TCA': 'conector temporal-causal',
            'CON-FIN': 'CLA-EXPHIST',  # 'CON-FIN': 'conector de finalidade',
            'CON-CND': 'CLA-EXPHIST',  # 'CON-CND': 'conector condicional',
            'VERB-CAUSA': 'CLA-EXPHIST',  # 'VERB-CAUSA': 'verbo de causa',
        }
        transformed = [m[s] for s in seq_list if s in m.keys()]
        return transformed

    @staticmethod
    def labels():
        return {
            'CLA-RELDESC': 'Relato Descritivo',
            'CLA-RELHIST': 'Relato Histórico',
            'CLA-EXPHIST': 'Explicação Histórica',
        }


def test_classificacao():
    pass
    print(ClasificacaoTextual.classify(
        ['CLA-RELDESC', 'CLA-RELDESC', 'CLA-RELHIST', 'CLA-EXPHIST']
    ))

    os = ['O', None, 'CON-CAU', '--', 'CON-FIN', 'AA', 'DEN-DENON', 'DEN-DENON', 'CON-TCA', 'CON-FIN2', True]
    r = ClasificacaoTextual.seq_transform(os)
    print(ClasificacaoTextual.classify(
        r
    ))


def test_sequence():
    pass
    print(SequenciaTextual.classify(
        ['SET-EXPLICACAO', 'SET-DESCRICAO', 'SET-DENOMINACAO', 'SET-EXPLICACAO']
    ))

    os = ['O', None, 'DEN-DENON', 'DEN-DENON', 'CON-CAU', '--', 'CON-FIN', 'AA', 'DEN-DENON', 'DEN-DENON', 'CON-TCA',
          'CON-FIN2', True]
    r = SequenciaTextual.seq_transform(os)
    print(SequenciaTextual.classify(
        r
    ))
    print(r)


if __name__ == '__main__':
    test_classificacao()
    test_sequence()