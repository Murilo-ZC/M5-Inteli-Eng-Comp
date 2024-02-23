---
sidebar_label: "5 - Encontro de Orientação"
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instrução de Orientação

Preparação dos Entregáveis	

## 1. Objetivos

- Orientação sobre os entregáveis da Sprint 2.
- Manipulação de arquivos com Python.
- Utilizando bancos de dados documentais com Python.

## 2. Slides do Encontro

<!-- <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSG6q7EZA2isyGW3V_1pXMM7IJquzznhrFYcQA0ygtI8Nfv7v7SvdBN_jbO2XuOBN3kg1zpmRzti5Om/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }}></iframe> -->

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

## 3. Material de Autoestudo

:::danger[Acesse a Adalove!]

Esse material NÃO substitui de forma alguma o uso da Adalove. Você DEVE entrar na Adalove com frequência e REGISTRAR O SEU PROGRESSO. Entendeu? Ainda não? Pera aí que vou desenhar:

<img src={useBaseUrl("/img/memes/aviso-adalove.png")} alt="ACESSE A ADALOVE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />

:::

<Tabs>
  <TabItem value="autoestudos-obrigatorios" label="📘 Autoestudos Obrigatórios" default>
     
    <details> 
        <summary mdxType="summary"> Python TinyDB: base de dados em arquivos JSON</summary>

        - https://www.youtube.com/watch?v=99Vm0c9eNOA
    </details> 
    <details> 
        <summary mdxType="summary"> TinyDB - Getting Started</summary>

        - https://tinydb.readthedocs.io/en/latest/getting-started.html
    </details> 
    <details> 
        <summary mdxType="summary"> Como usar JSON em PYTHON - Arquivos e Strings</summary>

        - https://www.youtube.com/watch?v=wdL5ZjMpn-w
    </details> 

  </TabItem>
  <TabItem value="autoestudos-opcionais" label="📔 Autoestudos Opcionais">
     
        <img class="image-intro" src={useBaseUrl("/img/memes/mash_celebrando.gif")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>

  </TabItem>
  <TabItem value="autoestudos-adicionais" label="📓 Autoestudos Adicionais">
    
    <details> 
        <summary mdxType="summary">	Reading and Writing Files in Python (Guide)</summary>

        - https://realpython.com/read-write-files-python/
    </details> 
    <details> 
        <summary mdxType="summary">	File Handling in Python</summary>

        - https://www.geeksforgeeks.org/file-handling-python/
    </details> 
    <details> 
        <summary mdxType="summary">	SQL vs. NoSQL Explained (in 4 Minutes)</summary>

        - https://www.youtube.com/watch?v=_Ss42Vb1SU4
    </details> 
    <details> 
        <summary mdxType="summary">	Which Is Better? SQL vs NoSQL</summary>

        - https://www.youtube.com/watch?v=t0GlGbtMTio
    </details>
    <details> 
        <summary mdxType="summary">	Live de Python #8 - CRUD com SQLite3</summary>

        - https://www.youtube.com/watch?v=2WUo5tD-eIA
    </details>
    <details> 
        <summary mdxType="summary">	DATA SCIENCE SKILLS: Gentle Introduction to sqlite3. Python, SQLite and Databases</summary>

        - https://www.youtube.com/watch?v=llF06RLZbBY
    </details>
  </TabItem>
</Tabs>


## 4. Material de Aula

Chegamos agora ao momento de armazenar nossos dados 🎲🎲!! Um conceito bastante importante, quando nosso programa é executado, os valores manipulados por ele estão na memória RAM do sistema (nosso computador, servidor o que for!). Quando o programa é encerrado, os valores são perdidos. Para que isso não aconteça, precisamos armazenar esses valores em algum lugar. E é aí que entra a ***persistencia***!.

O que é a persistência? É a capacidade de um sistema de armazenar dados de forma que eles possam ser recuperados posteriormente. E é isso que vamos aprender a fazer nesse encontro. Vamos aprender a armazenar nossos dados em arquivos e em bancos de dados.

Tudo que vamos desenvolver estará disponível no diretório [orientacao-5](#). Na dúvida sobre a estrutura básica dos arquivos ou como criar um ambiente virtual? Verificar nosso encontro anterior desta semana!!

### 4.1. Arquivos

A primeira forma de armazenarmos os dados é em arquivos. E para isso, vamos utilizar a biblioteca padrão do Python para manipulação de arquivos. Vamos aprender a abrir, ler, escrever e fechar arquivos. Além disso, vamos aprender a manipular arquivos JSON, que é um formato de arquivo bastante utilizado para armazenar dados.

> ***Mas Murilão por que vamos utilizar arquivos para armazenar os dados?*** Guardar os dados em arquivos é uma prática comum e bastante útil. Por exemplo, imagine que você está desenvolvendo um jogo e quer salvar o progresso do jogador. Você pode salvar esses dados em um arquivo. Ou então, imagine que você está desenvolvendo um sistema de cadastro de clientes. Você pode salvar os dados dos clientes em um arquivo. 

:::danger[CUIDADO COM TAMANHO]

Arquivos de configuração ou mesmo para realizar o armazenamento de arquivos de texto são uma prática comum. No entanto, é importante ressaltar que essa prática não é recomendada para grandes volumes de dados. Para isso, existem os bancos de dados.

:::

A manipulação de arquivos pode ser realizada utilizando bibliotecas built-in do Python. Vamos trabalhar com o arquivo [arquivos.py](#). Para executar ele vamos rodar o comando: `python3 src/arquivos.py`.

```python
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
```

Vamos avaliar este código por partes:

- `escrever_arquivo`: Função para escrever o texto. Ela recebe o nome do arquivo e o texto a ser escrito. A função `open` abre o arquivo no modo de escrita (`'w'`). O arquivo é fechado automaticamente ao final do bloco `with`. O `with` é uma forma de garantir que o arquivo será fechado, mesmo que ocorra algum erro durante a execução do bloco. O método `write` escreve o texto no arquivo.

- `ler_arquivo`: Função para ler o texto. Ela recebe o nome do arquivo e retorna o texto lido. A função `open` abre o arquivo no modo de leitura (`'r'`). O arquivo é fechado automaticamente ao final do bloco `with`. O método `read` lê o texto do arquivo, todo de um única vez. Para que o arquivo seja lido linha a linha, podemos utilizar o método `readline`.

- `gerar_numero`: Função para gerar um número aleatório entre 0 e 100.

- `gerar_lista_numeros`: Função para gerar uma lista de números aleatórios. Ela recebe o tamanho da lista e retorna uma lista com números aleatórios.

- `escrever_lista_arquivo`: Função para escrever uma lista de números em um arquivo. Ela recebe o nome do arquivo e a lista de números. O método `join` junta os números da lista em uma única string, separando-os por quebra de linha. O texto é escrito no arquivo.

- `ler_lista_arquivo`: Função para ler uma lista de números de um arquivo. Ela recebe o nome do arquivo e retorna a lista de números. O texto é lido do arquivo e separado em uma lista de números.

Vale destacar que as funções acima foram todas escritas utilizando o recurso de list comprehension. Caso você não esteja familiarizado com esse recurso, sugiro que dê uma olhada no material de autoestudo. Outra recomendação é reescrever esse código fonte utilizando a notação padrão de listas.

