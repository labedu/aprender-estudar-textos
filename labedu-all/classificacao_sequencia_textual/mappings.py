class VerbsMap:

    @staticmethod
    def tokens():
        return {
            'VERB-DESC': sorted(list(set(['apresentar', 'classificar', 'definir', 'estar', 'existir', 'ficar', 'habitar', 'haver', 'medir', 'morar', 'pertencer', 'pesar', 'possuir', 'residir', 'ser', 'subsistir', 'ter a', 'viver', 'sou', 'és', 'é', 'somos', 'sois', 'são', 'eras', 'era', 'éramos', 'éreis', 'eram', 'fui', 'foste', 'foi', 'fomos', 'fostes', 'foras', 'fora', 'fôramos', 'fôreis', 'foram', 'serei', 'serás', 'será', 'seremos', 'sereis', 'serão', 'serias', 'seria', 'seríamos', 'seríeis', 'seriam', 'sejas', 'sejais', 'fosses', 'fosse', 'fôssemos', 'fôsseis', 'fossem', 'fores', 'for', 'formos', 'fordes', 'forem', 'sê', 'seja', 'sejamos', 'sede', 'sejam', 'estou', 'estás', 'estamos', 'estais', 'estão', 'estavas', 'estava', 'estávamos', 'estáveis', 'estavam', 'estive', 'estiveste', 'esteve', 'estivemos', 'estivestes', 'estiveras', 'estivera', 'estivéramos', 'estivéreis', 'estiveram', 'estarei', 'estarás', 'estará', 'estaremos', 'estareis', 'estarão', 'estarias', 'estaria', 'estaríamos', 'estaríeis', 'estariam', 'estejas', 'estejais', 'estivesses', 'estivesse', 'estivéssemos', 'estivésseis', 'estivessem', 'estiveres', 'estiver', 'estivermos', 'estiverdes', 'estiverem', 'está', 'esteja', 'estejamos', 'estai', 'estejam', 'tenho', 'tens', 'temos', 'tendes', 'têm', 'tinhas', 'tinha', 'tínhamos', 'tínheis', 'tinham', 'tive', 'tiveste', 'teve', 'tivemos', 'tivestes', 'tiveras', 'tivera', 'tivéramos', 'tivéreis', 'tiveram', 'terei', 'terás', 'terá', 'teremos', 'tereis', 'terão', 'terias', 'teria', 'teríamos', 'teríeis', 'teriam', 'tenhas', 'tenhais', 'tivesses', 'tivesse', 'tivéssemos', 'tivésseis', 'tivessem', 'tiveres', 'tiver', 'tivermos', 'tiverdes', 'tiverem', 'tem', 'tenha', 'tenhamos', 'tende', 'tenham', 'hei', 'hás', 'havemos', 'haveis', 'hão', 'havias', 'havia', 'havíamos', 'havíeis', 'haviam', 'houveste', 'houve', 'houvemos', 'houvestes', 'houveras', 'houvera', 'houvéramos', 'houvéreis', 'houveram', 'haverei', 'haverás', 'haverá', 'haveremos', 'havereis', 'haverão', 'haverias', 'haveria', 'haveríamos', 'haveríeis', 'haveriam', 'hajas', 'hajais', 'hajam', 'houvesses', 'houvesse', 'houvéssemos', 'houvésseis', 'houvessem', 'houveres', 'houver', 'houvermos', 'houverdes', 'houverem', 'há', 'haja', 'hajamos', 'havei', 'hajam'])), reverse=True),
            'VERB-CAUSA': sorted(['acarretar', 'afetar', 'ajudar', 'arriscar', 'atingir', 'ativar', 'aumentar', 'auxiliar', 'avivar', 'capacitar', 'captar', 'causar', 'cessar', 'condicionar', 'confundir', 'contribuir', 'criar', 'danificar', 'dar', 'deixar', 'derrubar', 'descontinuar', 'desencadear', 'desistir', 'destruir', 'determinar', 'devastar', 'dificultar', 'dispensar', 'disponibilizar', 'efetuar', 'engendrar', 'ensinar', 'estimular', 'facilitar', 'fazer', 'finalizar', 'fomentar', 'fornecer', 'garantir', 'gerar', 'impor', 'impossibilitar', 'instigar', 'irritar', 'levar', 'melhorar', 'motivar', 'mudar', 'obter', 'ocasionar', 'originar', 'perder', 'permitir', 'possibilitar', 'preocupar', 'preservar', 'produzir', 'programar', 'promover', 'propiciar', 'proporcionar', 'provocar', 'puxar', 'reduzir', 'resultar', 'servir', 'solucionar', 'subsidiar', 'suprir', 'surgir', 'suscitar', 'tornar', 'trazer', 'viabilizar', 'visar'], reverse=True),
            'VERB-DIZER': sorted(['abençoar', 'aborrecer', 'aconselhar', 'acusar', 'admitir', 'adorar', 'advertir', 'agitar', 'agourar', 'aguentar', 'alegar', 'alertar', 'aludir', 'amaldiçoar',  'animar', 'anunciar', 'apitar', 'aplaudir', 'apontar', 'apregoar', 'aprovar', 'argumentar', 'articular', 'assegurar', 'augurar', 'aventar', 'avisar', 'berrar', 'bisbilhotar', 'blefar', 'cacarejar', 'caluniar', 'cantar', 'cantarolar', 'censurar', 'choramingar', 'chorar', 'citar', 'comentar', 'comunicar', 'conceder', 'conclamar', 'confessar', 'confirmar', 'consentir', 'contar', 'contestar', 'conversar', 'convocar', 'copiar', 'corrigir', 'criticar', 'cumprimentar', 'decidir',  'declarar', 'defender', 'delinear', 'denominar', 'deplorar', 'descrever', 'desdenhar', 'designar', 'desmoralizar', 'desonrar', 'desvendar', 'desvirtuar', 'discordar', 'discutir', 'divagar', 'divulgar', 'dizer', 'documentar', 'elevar', 'elogiar', 'enaltecer', 'encorajar', 'endereçar', 'enfrentar', 'engrandecer', 'entoar', 'esboçar', 'esclarecer', 'escrever', 'esmorecer', 'esquichar', 'exaltar', 'excitar', 'exclamar', 'exigir', 'exortar', 'explicar', 'expor', 'expressar', 'falar', 'felicitar', 'fofocar', 'fungar', 'gabar', 'gaguejar', 'gemer', 'glorificar', 'gorgear', 'gritar', 'grunhir', 'guinchar', 'historiar', 'implorar', 'incentivar', 'incitar', 'indicar', 'inflamar', 'informar', 'inquerir', 'insinuar', 'insistir', 'instituir', 'interromper', 'intimar', 'lamentar', 'lamuriar', 'ler', 'levantar', 'mandar', 'maravilhar', 'martelar', 'mencionar', 'mentir', 'murmurar', 'narrar', 'negar', 'nomear', 'noticiar', 'notificar', 'oferecer', 'ordenar', 'palestrar', 'parabenizar', 'participar', 'perguntar', 'persuadir', 'piar', 'pleitear', 'prantear', 'preconizar', 'pregar', 'pressagiar', 'prezar', 'proclamar', 'proferir', 'professar', 'prognosticar', 'proibir', 'pronunciar', 'propor', 'questionar', 'receitar', 'reclamar', 'recomendar', 'recontar', 'recorrer', 'recusar', 'referir', 'rejeitar', 'relatar', 'renegar', 'repetir', 'reportar', 'repreender', 'reprimir', 'resmungar', 'responder', 'resumir', 'revelar', 'rir', 'rogar', 'ronronar', 'rosnar', 'rugir', 'sancionar', 'segredar', 'solicitar', 'soluçar', 'subscrever', 'sugerir', 'suplicar', 'suspirar', 'sussurrar', 'tagarelar', 'tergiversar', 'transcrever', 'transmitir', 'tratar', 'uivar', 'vacilar', 'vaticinar', 'visionar', 'vocalizar', 'vociferar'], reverse=True),
            'VERB-PENSARSENTIR': sorted(['absorver', 'abstrair', 'acalmar', 'aceitar', 'achar', 'acreditar', 'adivinhar', 'adotar', 'almejar', 'amar', 'ambicionar', 'analisar', 'ansiar', 'antecipar', 'antever', 'aparentar', 'aprender', 'apurar', 'arquitetar', 'aspirar', 'atender', 'avaliar', 'avistar', 'calcular', 'ceder', 'cheirar', 'cobiçar', 'cogitar', 'compreender', 'conceber',  'confiar',  'conhecer', 'conjeturar', 'considerar', 'crer', 'cultuar', 'curtir', 'decifrar', 'decorar', 'deparar', 'desacreditar', 'descobrir', 'desconfiar', 'desconhecer', 'desejar', 'desfazer', 'desgostar', 'desprezar', 'desvelar', 'detectar', 'detestar', 'dever', 'diferenciar', 'discriminar', 'distinguir', 'duvidar', 'elaborar', 'enganar', 'engenhar', 'engolir', 'enjoar', 'enobrecer', 'enrolar', 'entender', 'entreter', 'entristecer', 'entusiasmar', 'envergonhar', 'envolver', 'enxergar', 'escandalizar', 'escutar', 'espantar', 'espiar', 'espionar', 'esquecer', 'estimar', 'estranhar', 'estremecer', 'estudar', 'evocar', 'examinar', 'exaurir', 'exultar', 'fantasear', 'farejar', 'fascinar', 'fatigar', 'favorecer', 'ferir', 'figurar', 'fingir', 'frustrar', 'gostar', 'hipotetizar', 'horrorizar', 'humilhar', 'idealizar', 'idear', 'identificar', 'idolatrar', 'iludir', 'iluminar', 'ilustrar', 'imaginar', 'importar', 'impressionar', 'incomodar', 'indagar', 'indignar', 'induzir', 'influir', 'inquietar', 'inquirir', 'inspirar', 'interpretar', 'intimidar', 'intuir', 'invejar', 'inventar', 'investigar', 'julgar', 'lastimar', 'legitimar', 'lembrar', 'levar em conta', 'magoar', 'meditar', 'menosprezar', 'mirar', 'necessitar', 'notar', 'observar', 'odiar', 'olhar', 'oprimir', 'padecer', 'palpitar', 'pensar', 'perceber', 'planejar', 'postergar', 'precisar', 'predizer', 'preferir', 'prefigurar', 'premeditar', 'prenunciar', 'presenciar', 'pressentir', 'pressupor', 'prestigiar', 'presumir', 'pretender', 'pretextar', 'prevenir', 'prever', 'profetizar', 'profundar', 'projetar', 'prometer', 'proteger', 'provar', 'querer', 'raciocinar', 'realizar', 'recear', 'reconhecer', 'refletir', 'representar', 'resolver', 'respeitar', 'saber', 'seduzir', 'simular', 'socorrer', 'sofrer', 'sondar', 'sonhar', 'sufocar', 'supor', 'surpreender', 'suspeitar', 'temer', 'tencionar', 'teorizar', 'ter esperança', 'ter impressão', 'ter vontade', 'testemunhar', 'tolerar', 'tomar', 'trair', 'tranquilizar', 'vasculhar', 'velar', 'venerar', 'ver', 'verificar', 'vislumbrar', 'visualizar'], reverse=True),
            'VERB-ACAO': sorted(['investir', 'unir', 'entrar', 'cair', 'negociar', 'manter', 'enviar', 'trocar', 'conquistar', 'suportar', 'rever', 'convencer', 'acompanhar', 'virar', 'ligar', 'pedir', 'partilhar', 'libertar', 'cobrar', 'subir', 'brincar', 'despertar', 'espalhar', 'sentir', 'lutar', 'cumprir', 'concordar', 'devolver', 'pegar', 'fumar', 'capturar', 'reunir', 'explorar', 'cometer', 'executar', 'beijar', 'agradecer', 'desenhar', 'estragar', 'parlamentar', 'demonstrar', 'desligar', 'dançar', 'começar', 'manifestar', 'reforçar', 'esperar', 'descer', 'adaptar', 'transformar', 'lançar', 'perdoar', 'agir', 'nascer', 'convidar', 'destacar', 'divertir', 'sentar', 'fechar', 'aplicar', 'prestar', 'concluir', 'encontrar', 'colar', 'tocar', 'abandonar', 'segurar', 'vestir', 'separar', 'tirar', 'dirigir', 'matar', 'arranjar', 'gastar', 'atirar', 'passar', 'resistir', 'cancelar', 'avançar', 'integrar', 'substituir', 'cobrir', 'justificar', 'aproximar', 'introduzir', 'juntar', 'chamar', 'piorar', 'mover', 'pesquisar', 'guardar', 'ouvir', 'andar', 'entregar', 'cortar', 'marcar', 'estabelecer', 'jogar', 'expandir', 'seguir', 'iniciar', 'comer', 'focar', 'editar', 'testar', 'atrair', 'queimar', 'acontecer', 'sorrir', 'instalar', 'mexer', 'meter', 'procurar', 'receber', 'ocupar', 'vir', 'gravar', 'comparar', 'ampliar', 'pintar', 'rezar', 'exercer', 'conduzir', 'impedir', 'baixar', 'prazer', 'assumir', 'formar', 'montar', 'sair', 'sustentar', 'correr', 'partir', 'atuar', 'demorar', 'evitar', 'comprar', 'continuar', 'mostrar', 'postar', 'praticar', 'escolher', 'fortalecer', 'apanhar', 'aproveitar', 'concentrar', 'assinar', 'salvar', 'encarar', 'diminuir', 'alimentar', 'afirmar', 'descansar', 'trabalhar', 'voltar', 'apertar', 'transportar', 'colher', 'lavar', 'curar', 'recuperar', 'desenvolver', 'terminar', 'contratar', 'visitar', 'publicar', 'aparecer', 'competir', 'organizar', 'casar', 'usar', 'conferir', 'vencer', 'alcançar', 'quebrar', 'acabar', 'utilizar', 'ter', 'limpar', 'soltar', 'relaxar', 'combater', 'ignorar', 'pular', 'chegar', 'valer', 'buscar', 'apoiar', 'tentar', 'retornar', 'incluir', 'concorrer', 'forçar', 'votar', 'encerrar', 'bloquear', 'operar', 'assistir', 'dedicar', 'apagar', 'deitar', 'caminhar', 'registrar', 'afastar', 'bater', 'variar', 'circular', 'navegar', 'cuidar', 'calar', 'respirar', 'conseguir', 'retirar', 'deter', 'dormir', 'abrir', 'crescer', 'colocar', 'militar', 'fugir', 'largar', 'construir', 'adquirir', 'beber', 'acordar', 'regressar', 'significar', 'invadir', 'preencher', 'roubar', 'voar', 'ocorrer', 'livrar', 'pôr', 'sobreviver', 'arrumar', 'ganhar', 'carregar', 'conter', 'encher', 'dividir', 'completar', 'alterar', 'prender', 'atacar', 'ir', 'distribuir', 'parar', 'pagar', 'recolher', 'compartilhar', 'adicionar', 'preparar', 'eliminar', 'gozar', 'explodir'], reverse=True),
        }

    @staticmethod
    def labels():
        return {
            'VERB-DESC': 'verbo descritivo',
            'VERB-CAUSA': 'verbo de causa',
            'VERB-DIZER': 'verbo dizer',
            'VERB-PENSARSENTIR': 'verbo pensar sentir',
            'VERB-ACAO': 'verbo acao',
        }


class ConnectorsMap:

  @staticmethod
  def tokens():
    return {
      'CON-TMP': sorted(['a partir daí', 'a partir de', 'a seguir', 'afinal', 'ainda', 'ainda hoje', 'antes', 'antes de', 'antes que', 'ao final', 'ao mesmo tempo que', 'ao passo que', 'apenas', 'após', 'assim que', 'até então', 'até que', 'atualmente', 'cada vez que', 'com o tempo', 'depois', 'depois que', 'diante de', 'em seguida', 'enquanto', 'finalmente', 'frequentemente', 'logo após', 'logo que', 'mais tarde', 'mal', 'no final', 'no momento', 'por fim', 'por longo tempo', 'posteriormente', 'primeiramente', 'primeiro que', 'sempre que', 'toda vez que', 'todas as vezes que', 'no fim'], reverse=True),
      'CON-TPO': sorted(['século', 'década', 'ano', 'mês', 'dia', 'período', 'época', 'durante', 'meados', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro', 'séculos', 'décadas', 'anos', 'meses', 'dias', 'períodos', 'épocas'], reverse=True),
      'CON-ADT': sorted(['e', 'em geral', 'nem', 'também'], reverse=True),
      'CON-CNT': sorted(['apesar de que', 'ainda assim', 'ainda quanto', 'ainda que', 'antes bem', 'ao contrário', 'ao invés de', 'ao invés disso', 'apesar de', 'apesar disso', 'caso contrário', 'contrariamente', 'contudo', 'em contrapartida', 'em contraste', 'em lugar de', 'em paralelo', 'em troca', 'em vez de', 'embora', 'entretanto', 'mas', 'mesmo que', 'não obstante', 'nem bem', 'nem que', 'no entanto', 'pelo contrário', 'por mais', 'por menos', 'por muito que', 'por outro lado', 'porém', 'posto que', 'se bem que', 'todavia'], reverse=True),
      'CON-CMP': sorted(['assim como', 'da mesma forma', 'de modo semelhante', 'do mesmo modo que', 'em comparação', 'mais que', 'menos que', 'tal qual', 'tanto quanto', 'tão quanto'], reverse=True),
      'CON-CAU': sorted(['assim', 'causado por', 'com isso', 'como consequência', 'como resultado', 'consequentemente', 'dado que', 'dessa forma', 'dessa maneira', 'desse modo', 'diante disso', 'em resposta', 'já que', 'logo', 'nesse caso', 'pois', 'pois que', 'por causa', 'por causa que', 'por conseguinte', 'por essa razão', 'por esse motivo', 'por isso', 'por isso que', 'por quanto', 'porque', 'portanto', 'sendo assim', 'tanto mais que', 'uma vez que', 'visto como', 'visto que'], reverse=True),
      'CON-CND': sorted(['a medida que', 'a menos que', 'a não ser que', 'caso', 'contanto que', 'desde que', 'exceto se', 'salvo se', 'sem que'], reverse=True),
      'CON-FIN': sorted(['a fim de', 'a fim de que', 'a propósito', 'através', 'com o intuito de', 'com o objetivo de', 'para', 'para esse fim', 'para isso', 'para que', 'para tanto'], reverse=True),
      'CON-ELB': sorted(['adicionalmente', 'além de', 'além disso', 'bem como', 'como exemplo', 'como também', 'como, por exemplo,', 'em adição', 'em particular', 'especificamente', 'inclusive', 'por exemplo', 'principalmente'], reverse=True),
      'CON-CAE': sorted(['como'], reverse=True),
      'CON-TCA': sorted(['então', 'quando'], reverse=True),
    }

  @staticmethod
  def labels():
   return {
    'CON-TMP': 'conector temporal',
    'CON-TPO': 'conector tempo',
    'CON-ADT': 'conector aditivo',
    'CON-CNT': 'conector contrastivo',
    'CON-CMP': 'conector comparativo',
    'CON-CAU': 'conector causal',
    'CON-CND': 'conector condicional',
    'CON-FIN': 'conector de finalidade',
    'CON-ELB': 'conector exemplificacao-elaboracao',
    'CON-CAE': 'conector causal-exemplificacao',
    'CON-TCA': 'conector temporal-causal',
  }


class DenominacaoMap:

    @staticmethod
    def tokens():
        return {
            'DEN-DENON': sorted(['chamado de', 'chamados de', 'conhecido como', 'conhecidos como', 'conhecido com o nome de', 'conhecidos com o nome de', 'chamada de', 'chamadas de', 'conhecida como', 'conhecidas como', 'conhecida com o nome de', 'conhecidas com o nome de'])

        }

    @staticmethod
    def labels():
        return {
            'DEN-DENON': 'denominacao',
        }

#class SequenciaTextualLabels:

    #@staticmethod
    #def tokens():
    #    return {
    #    }

#    @staticmethod
#    def labels():
#        return {
#            'SEQ-DESC': 'Sequência com descrição',
#            'SEQ-DEN': 'Sequência com denominação',
#            'SEQ-EXP': 'Sequência com explicação',
#        }

if __name__ == '__main__':
    print(VerbsMap.tokens())
    print(VerbsMap.labels())
    print(ConnectorsMap.tokens())
    print(ConnectorsMap.labels())
    print(DenominacaoMap.tokens())
    print(DenominacaoMap.labels())
