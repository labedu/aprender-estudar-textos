import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from formatacao.cola_et_comatta import paragraph_to_features
from formatacao.rules_based import process_paragraph_rules
from formatacao.rules_based_improved import process_paragraph_rules2
from formatacao.split_paragraphs import split_paragraphs

from vocabulary.vocabulary_extract import vocabulary_paragraphs_non_repeat, vocabulary_paragraphs
from parser.parse import parse_sentences_list
from funcao_textual.pipeline import TextToJson as TextToJsonFuncao
from classificacao_sequencia_textual.pipeline import TextToJson as TextToJsonTextual
ttjF = TextToJsonFuncao()
ttjT = TextToJsonTextual()

sentry_sdk.init(
    dsn="https://f85421ced5d14c22ac768594ca121918@o453483.ingest.sentry.io/5442309",
    integrations=[FlaskIntegration()]
)


app = Flask(__name__)
CORS(app)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


@app.route('/')
def hello():
    return 'main route here test/'

### [1] formatacao START ###


@app.route('/aux/parsetext', methods=['POST'])
def formatacao_split_text():
    if request.method == 'POST':
        data = request.data.decode('utf-8')

        title, subtitle, pars = split_paragraphs(data)
    return jsonify({'title': title, 'subtitle': subtitle, 'paragraphs': pars},)


@app.route('/formatacao/getcolaetcommata', methods=['POST'])
def formatacao_get_colaetcommata():
    if request.method == 'POST':
        json = request.json
        pars = json['paragraphs']

        par_proc = []
        for p in pars:
            par_proc.append(process_paragraph_rules2(p))

    return jsonify({'paragraph_processed': par_proc})


@app.route('/formatacao/getcolaetcommata_simple', methods=['POST'])
def formatacao_get_colaetcommata_simple():
    if request.method == 'POST':
        json = request.json
        pars = json['paragraphs']

        par_proc = []
        for p in pars:
            par_proc.append(process_paragraph_rules(p))

    return jsonify({'paragraph_processed': par_proc})


@app.route('/formatacao/getcolaetcommata_ml', methods=['POST'])
def formatacao_get_colaetcommata_ml():
    if request.method == 'POST':
        json = request.json
        pars = json['paragraphs']

        par_proc = []
        for p in pars:
            par_proc.append(paragraph_to_features(p))

    return jsonify({'paragraph_processed': par_proc})

### [1] formatacao END ###


### [2] vocabulary START ###

@app.route('/vocabulary/getvocabulary', methods=['POST'])
def vocabulary_get_vocabulary():
    if request.method == 'POST':
        json = request.get_json(force=True)
        pars = json['paragraphs']

        # vocabulary_paragraphs_non_repeat
        vocab = vocabulary_paragraphs(pars)

        return jsonify({'vocabulary' : vocab})
    return 'ERROR: Not a POST method!'


@app.route('/vocabulary/getvocabularynr', methods=['POST'])
def vocabulary_get_vocabulary_non_repeat():
    if request.method == 'POST':
        json = request.get_json(force=True)
        pars = json['paragraphs']

        # vocabulary_paragraphs
        vocab = vocabulary_paragraphs_non_repeat(pars)
        # print(vocab)

        return jsonify({'vocabularynr': vocab})
    return 'ERROR: Not a POST method!'

### [2] vocabulary END ###


### [4a] parser  START ###
@app.route('/parser/parse_paragraphs', methods=['POST'])
def parser_parse_paragraphs():
    if request.method == 'POST':
        json = request.get_json(force=True)
        pars = json['paragraphs']

        parsed_pars = [parse_sentences_list(p) for p in pars]

        return jsonify({'paragraphs': parsed_pars})
    return 'ERROR: Not a POST method!'


@app.route('/parser/parse_paragraph', methods=['POST'])
def parser_parse_paragraph():
    if request.method == 'POST':
        json = request.get_json(force=True)
        par = json['paragraph']

        parsed_par = parse_sentences_list(par)

        return jsonify({'paragraph': parsed_par})
    return 'ERROR: Not a POST method!'

### [4a] parser END ###


### [4b]  START ###
@app.route('/funcao/parse_paragraphs_b', methods=['POST'])
def funcao_parse_text_b():
    if request.method == 'POST':

        output = {}
        try:
            json = request.get_json(force=True)
            pars = json['paragraphs']
            r = ttjF.annotate(pars)
            j = jsonify(r)
            output = j
        except Exception as e:
            print(e)
            output = {'error'}

        return output
    return 'ERROR: Not a POST method!'
### [4b]  END ###


### [4cd]  START ###
@app.route('/textual/parse_paragraphs_cd', methods=['POST'])
def parse_text_cd():
    if request.method == 'POST':
        json = request.get_json(force=True)
        pars = json['paragraphs']
        r = ttjT.annotate(pars)
        return jsonify(r)
    return 'ERROR: Not a POST method!'
### [4cd]  END ###


##--
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
