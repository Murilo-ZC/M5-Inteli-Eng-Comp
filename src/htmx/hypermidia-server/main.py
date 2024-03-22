# Aplicação de servidor HTTP Flask que retonar HTML
from flask import Flask, request
from flask_cors import CORS
from random import randint
import time

app = Flask(__name__)

# Habilitar o CORS para todos os domínios
CORS(app)

@app.route('/')
def index():
    return '<h1>Olá, mundo!</h1>'

@app.route('/ola', methods=['POST'])
def ola():
    return '<div><h2>Olá, mundo Diferente!</h2></div>'

@app.route('/numero', methods=['GET'])
def sortea_numero()->int:
    return f'<div>Número Sorteado: {str(randint(1, 100))}</div>'

@app.route('/hora-delay', methods=['GET'])
def devolve_hora_com_delay():
    time.sleep(5)
    return f'<div>Hora: {time.strftime("%H:%M:%S")}</div>'

# Rota para receber dados enviados via POST
@app.route('/recebe-dados', methods=['POST'])
def recebe_dados():
    email = request.form['email']
    nome = request.form['nome']
    return f'<div>Nome: {nome} - Email: {email}</div>'

# Rota para receber dados enviados via POST - dados enviados como JSON
@app.route('/recebe-dados-json', methods=['POST'])
def recebe_dados_json():
    dados = request.get_json()
    email = dados['email']
    nome = dados['nome']
    return f'<div>Nome: {nome} - Email: {email}</div>'

#Rota para receber um arquivo enviado por multipart/form-data
@app.route('/recebe-arquivo', methods=['POST'])
def recebe_arquivo():
    print(request.files)
    arquivo = request.files['arquivo']
    arquivo.save(arquivo.filename)
    return f'<div>Arquivo {arquivo.filename} recebido com sucesso!</div>'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)