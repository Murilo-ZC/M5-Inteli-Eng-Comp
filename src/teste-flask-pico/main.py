from flask import Flask, render_template, request, redirect, json
from tinydb import TinyDB, Query
import time

app = Flask(__name__)
db_data = TinyDB('db.json')
db_status = TinyDB('status.json')

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

@app.route('/', methods=['GET', 'POST'])
def index():
    dados = db_data.all()
    return render_template('index.html', dados=dados)

@app.route('/add', methods=['POST'])
def add():
    dados = json.loads(request.json)
    print(type(dados))
    dado = dados['dado']
    ip_send = dados['ip_send']
    timestamp = time.time()
    db_data.insert({'dado': dado, 'ip_send': ip_send, 'timestamp': timestamp})
    return {"status": "ok"}

@app.route('/status', methods=['GET', 'POST'])
def status_rasp():
    if request.method == 'POST':
        dados = request.json
        ip = dados['ip']
        status = dados['status']
        db_status.upsert({'status': status, 'ip_send':ip}, Query().ip_send == ip)
    elif request.method == 'GET':
        ip = request.args.get('ip')
    dados = db_status.search(Query().ip_send==ip)
    if not dados:
        return {"status": "not found"}
    return {"status": dados[0]['status']}

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)