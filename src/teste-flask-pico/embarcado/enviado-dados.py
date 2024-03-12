import network
import urequests
import ujson
import time
import gc
from machine import Pin, ADC



wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NOME_DA_REDE', 'SENHA_DA_REDE')
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

meu_ip = wlan.ifconfig()[0]
print(f"IP:{meu_ip}")

entrada = ADC(Pin(29))

servidor = "http://10.128.0.39:8000"
try:
    while True:
        #requisicao de controle
        try:
            response = urequests.get(f'{servidor}/ping')
        except:
            print("Falha na requisicao")
        # Verifica se já pode enviar os dados
        response = urequests.get(f'{servidor}/status?ip={meu_ip}')
        dados = response.json()
        if dados["status"] == "ON":
            response = urequests.post(url='http://{servidor}/add',
                                      headers = {'content-type': 'application/json'},
                                      json=ujson.dumps({
                "dado": entrada.read_u16(),
                "ip_send":meu_ip
            }))
            print("DADO ENVIADO...")
        else:
            print("AGUARDANDO LIBERACAO...")
        gc.collect()
        time.sleep(4)
except Exception as error:
    print("Programa Encerrado")
    print(error)
    print(type(error))

