from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from login import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "API está no ar!"


@app.route('/login/<nome_usuario>/<senha>', methods=['POST'])
def login(nome_usuario, senha):
    # Verificação no banco de dados
    result = login_usuario(nome_usuario, senha)

    if result['status'] == 'success':
        return jsonify(result), 200
    else:
        abort(404)


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    print("Dados recebidos:", data)
    nome_usuario = data.get('nome_usuario')
    senha = data.get('senha')
    nome_completo = data.get('nome_completo')
    email = data.get('email')
    acessibilidade_str = data.get('acessibilidade', 'Não')

    print("Dados a serem cadastrados:", nome_usuario, senha, nome_completo, email, acessibilidade_str)

    result = cadastro_usuario(nome_usuario, senha, nome_completo, email, acessibilidade_str)
    print("Resultado do cadastro:", result)
    return jsonify({"mensagem": result})

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
