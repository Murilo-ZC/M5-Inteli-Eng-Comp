# arquivos_json.py

import json

def escrever_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo)

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)

def main():
    dados = {
        'nome': 'Fulano',
        'idade': 30,
        'peso': 80.5
    }
    escrever_arquivo('dados.json', dados)
    dados_lidos = ler_arquivo('dados.json')
    print(dados_lidos)
    # Para manipular um campo específico do arquivo, basta fazer:
    dados_lidos['idade'] = 31
    print(dados_lidos)
    escrever_arquivo('dados.json', dados_lidos)

if __name__ == '__main__':
    main()