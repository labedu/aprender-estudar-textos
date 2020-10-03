
conector_final = sorted(['a fim de', 'a fim de que', 'a propósito', 'através',
                       'com o intuito de', 'com o objetivo de', 'para',
                       'para esse fim', 'para isso', 'para que', 'para tanto'], reverse=True)

conector_causal = sorted(['assim', 'causado por', 'com isso', 'como consequência',
                        'como resultado', 'consequentemente', 'dado que',
                        'dessa forma', 'dessa maneira', 'desse modo', 'diante disso',
                        'em resposta', 'já que', 'logo', 'nesse caso', 'pois', 'pois que',
                        'por causa', 'por causa que', 'por conseguinte', 'por essa razão',
                        'por esse motivo', 'por isso', 'por isso que', 'por quanto', 'porque',
                        'portanto', 'sendo assim', 'tanto mais que',
                        'uma vez que', 'visto como', 'visto que'], reverse=True)

# important
verbo_causa = sorted(['acarretar', 'afetar', 'ajudar', 'arriscar', 'atingir',
                    'ativar', 'aumentar', 'auxiliar', 'avivar', 'capacitar',
                    'captar', 'causar', 'cessar', 'condicionar',
                    'confundir', 'contribuir', 'criar', 'danificar',
                    'dar', 'deixar', 'derrubar', 'descontinuar', 'desencadear',
                    'desistir', 'destruir', 'determinar', 'devastar', 'dificultar',
                    'dispensar', 'disponibilizar', 'efetuar', 'engendrar', 'ensinar',
                    'estimular', 'facilitar', 'fazer', 'finalizar', 'fomentar',
                    'fornecer', 'garantir', 'gerar', 'impor', 'impossibilitar',
                    'instigar', 'irritar', 'levar', 'melhorar', 'motivar', 'mudar',
                    'obter', 'ocasionar', 'originar', 'perder', 'permitir',
                    'possibilitar', 'preocupar', 'preservar', 'produzir',
                    'programar', 'promover', 'propiciar', 'proporcionar',
                    'provocar', 'puxar', 'reduzir', 'resultar', 'servir', 'solucionar',
                    'subsidiar', 'suprir', 'surgir', 'suscitar',
                    'tornar', 'trazer', 'viabilizar', 'visar'], reverse=True)

action_verbs = sorted(['acarretar', 'afetar', 'ajudar', 'apresentar', 'arriscar', 'atingir',
                'ativar', 'aumentar', 'auxiliar', 'avivar', 'capacitar', 'captar', 'causar',
                'cessar', 'classificar', 'condicionar', 'confundir', 'contribuir', 'criar', 'danificar',
                'dar', 'definir', 'deixar', 'derrubar', 'descontinuar', 'desencadear', 'desistir', 'destruir',
                'determinar', 'devastar', 'dificultar', 'dispensar', 'disponibilizar', 'efetuar', 'engendrar', 'ensinar',
                'estar', 'estimular', 'existir', 'facilitar', 'fazer', 'ficar', 'finalizar', 'fomentar', 'fornecer',
                'garantir', 'gerar', 'habitar', 'haver', 'impor', 'impossibilitar', 'instigar', 'irritar', 'levar',
                'medir', 'melhorar', 'morar', 'motivar', 'mudar', 'obter', 'ocasionar', 'originar', 'perder', 'permitir',
                'pertencer', 'pesar', 'possibilitar', 'possuir', 'preocupar', 'preservar', 'produzir', 'programar',
                'promover', 'propiciar', 'proporcionar', 'provocar', 'puxar', 'reduzir', 'residir', 'resultar',
                'ser', 'servir', 'solucionar', 'subsidiar', 'subsistir', 'suprir', 'surgir', 'suscitar',
                'tornar', 'trazer', 'viabilizar', 'visar', 'viver', 'fugir', 'trabalhar'], reverse=True)

time_list = sorted(['afinal', 'ainda', 'antes', 'apenas', 'após', 'atualmente', 'depois', 'enquanto',
                    'finalmente', 'frequentemente', 'mal', 'posteriormente', 'primeiramente', 'quando',
                    'século', 'década', 'ano', 'mês', 'dia', 'período', 'época',
                    'durante', 'meados', 'janeiro', 'fevereiro', 'março', 'abril',
                    'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
                    'novembro', 'dezembro'], reverse=True)

conector_causalidade = conector_final + conector_causal
