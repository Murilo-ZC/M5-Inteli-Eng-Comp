from flask import Flask, render_template, request
from datetime import datetime
# Cria a instância do Flask no App
app = Flask(__name__)

# Banco em memória
banco = []

# Rota de teste
@app.route('/')
def ola():
    banco.append({
    "endereco":request.environ['REMOTE_ADDR'],
    "metodo": request.method,
    "hora":datetime.now()
    })
    return render_template('index.html')

# Rota de logs
@app.route('/logs')
def logs():
    return render_template('logs.html')

# Rota que retorna os acessos
@app.route('/acessos')
def retorna_acessos():
    return render_template('item-log.html', itens=banco)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)