##importando bibliotecas
from flask import Flask, make_response, jsonify, request
from BD import Carros

##instanciando o Flask
app = Flask(__name__)

##tirando a ordenação alfabética do flask para respostas de requisições
app.config['JSON_SORT_KEYS'] = False


##definindo a função GET para buscar a lista de carros
#adicionando decorator do flask
@app.route('/carros', methods=['GET'])
def getCarros():
    return make_response(
        jsonify(
            message='Lista de Carros.',
            data=Carros
            )
    )

@app.route('/carros', methods=['POST'])
def createCarro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            message='Carro cadastrado com sucesso!',
            data=carro
        )
    )   

##colocando a api para rodar
app.run()

