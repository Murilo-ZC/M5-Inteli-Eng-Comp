# arquivos.py

import random

def escrever_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(texto)

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()
    
def gerar_numero():
    return random.randint(0, 100)

def gerar_lista_numeros(tamanho):
    return [gerar_numero() for _ in range(tamanho)]

def escrever_lista_arquivo(nome_arquivo, lista):
    texto = '\n'.join(str(numero) for numero in lista)
    escrever_arquivo(nome_arquivo, texto)

def ler_lista_arquivo(nome_arquivo):
    texto = ler_arquivo(nome_arquivo)
    return [int(numero) for numero in texto.split('\n') if numero]

def main():
    lista = gerar_lista_numeros(10)
    print(lista)
    escrever_lista_arquivo('numeros.txt', lista)
    lista_lida = ler_lista_arquivo('numeros.txt')
    print(lista_lida)

if __name__ == '__main__':
    main()