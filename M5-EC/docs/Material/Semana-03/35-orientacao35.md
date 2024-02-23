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

> ***Observação Importante***: Repare que quando apenas o nome do arquivo é passado para a função `open`, ele é aberto no mesmo diretório do arquivo que está sendo executado. Caso você queira abrir um arquivo em outro diretório, você deve passar o caminho completo do arquivo.

> ***Mas Murilão, e se eu quiser abrir um arquivo em outro diretório?*** Você pode passar o caminho completo do arquivo. Por exemplo, se você quiser abrir o arquivo `numeros.txt` que está no diretório `dados`, você pode passar o caminho completo do arquivo: `dados/numeros.txt`.

Pessoal vocês viram que para manipular o conteúdo do arquivo, utilizamos a função `open` que é uma função built-in do Python. Ela nos permite abrir arquivos em diferentes modos. Os principais modos são:

- `'r'`: Abre o arquivo para leitura. O arquivo deve existir. Caso o arquivo não exista, um erro será lançado.
- `'w'`: Abre o arquivo para escrita. Se o arquivo já existir, ele será apagado. Se o arquivo não existir, ele será criado.
- `'a'`: Abre o arquivo para escrita. Se o arquivo já existir, o conteúdo será mantido e os novos dados serão adicionados ao final do arquivo. Se o arquivo não existir, ele será criado.

Além desses modos, existem outros modos que podem ser utilizados. Para mais informações, consulte a [documentação oficial](https://docs.python.org/3/library/functions.html#open).

Pessoal outra observação importante é que o arquivo é fechado automaticamente ao final do bloco `with`. Isso é muito importante, pois garante que o arquivo será fechado, mesmo que ocorra algum erro durante a execução do bloco. Caso você não utilize o bloco `with`, é importante que você feche o arquivo manualmente utilizando o método `close`.

> ***Mas Murilão, e se eu não fechar o arquivo?*** Se você não fechar o arquivo, ele continuará aberto e ocupando memória. Isso pode causar problemas, como por exemplo, o arquivo não ser acessível para outros programas. Além disso, se você tentar abrir muitos arquivos sem fechá-los, você pode atingir o limite de arquivos abertos pelo sistema operacional.

> ***Mas Murilão, tenho que ler todo o conteúdo do arquivo de forma sequêncial?*** Não necessariamente. Você pode ler o conteúdo do arquivo de forma sequêncial, ou seja, lendo todo o conteúdo de uma vez, ou então, você pode ler o conteúdo do arquivo linha a linha. Para isso, você pode utilizar o método `readline`.

Mas será que não existe uma forma mais interessante de armazenar os dados? Algo que facilite a leitura de um valor específico, como o que foi setado para uma configuração específica? Claro que existe! Podemos trabalhar com arquivos JSON.

### 4.2. Arquivos JSON

O JSON (JavaScript Object Notation) é um formato de arquivo bastante utilizado para armazenar dados. Ele é um formato de texto que é fácil de ler e escrever. Além disso, ele é fácil de ser interpretado e gerado por máquinas. O JSON é um formato de arquivo bastante utilizado para armazenar configurações, dados de usuários, dados de jogos, entre outros.

O JSON veio do JavaScript, mas é um formato de arquivo independente de linguagem. Isso significa que ele pode ser utilizado em qualquer linguagem de programação. No Python, o JSON é suportado pela biblioteca `json`, que é uma biblioteca built-in do Python. O JSON é um formado de arquivo bastante similar a um dicionário. Ele é composto por pares de chave e valor. As chaves são strings e os valores podem ser strings, números, objetos, arrays, booleanos ou nulos. Para saber mais sobre o JSON, consulte a [documentação oficial](https://www.json.org/json-en.html).

Vamos trabalhar com o arquivo [arquivos_json.py](#). Para executar ele vamos rodar o comando: `python3 src/arquivos_json.py`.

```python
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
```

Vamos avaliar o código anterior por partes:

- `import json`: Importa a biblioteca `json`. Ela é uma biblioteca built-in do Python que nos permite trabalhar com arquivos JSON.

- `escrever_arquivo`: Função para escrever os dados em um arquivo JSON. Ela recebe o nome do arquivo e os dados a serem escritos. O método `dump` escreve os dados no arquivo. ***Importante Destacar***: o método `dump` recebe como parâmetro o objeto a ser escrito e o arquivo onde ele será escrito. Este objeto pode ser um dicionário, uma lista, um número, uma string, um booleano ou um nulo.

- `ler_arquivo`: Função para ler os dados de um arquivo JSON. Ela recebe o nome do arquivo e retorna os dados lidos. O método `load` lê os dados do arquivo. ***Importante Destacar***: o método `load` recebe como parâmetro o arquivo de onde os dados serão lidos. Ele retorna o objeto lido do arquivo.

> ***Mas Murilão, e se for necessário manipular diversas entradas?*** É possível sim, o JSON é um formato de arquivo bastante flexível. Ele suporta objetos, arrays, strings, números, booleanos e nulos. Isso significa que você pode armazenar diversos tipos de dados em um arquivo JSON. Além disso, você pode armazenar objetos dentro de objetos, arrays dentro de objetos, objetos dentro de arrays, entre outras combinações.

Mas pessoal, está ficando complexo a manipulação de arquivos. Será que não existe uma forma mais interessante de armazenar os dados? Algo que facilite a leitura de um valor específico, como o que foi setado para uma configuração específica? Claro que existe! Podemos trabalhar com bancos de dados.

### 4.3. Bancos de Dados Relacionais

Uma das formas mais comuns de armazenar dados é utilizando bancos de dados. Os bancos de dados são sistemas que permitem armazenar, manipular e recuperar dados. Existem diversos tipos de bancos de dados, como por exemplo, os bancos de dados relacionais, os bancos de dados documentais, os bancos de dados de séries temporais, os bancos de dados de grafos, entre outros.

Os bancos de dados relacionais são um dos tipos mais comuns de bancos de dados. Eles são baseados no modelo relacional, que é um modelo de dados que organiza os dados em tabelas. Cada tabela é composta por linhas e colunas. As linhas representam os registros e as colunas representam os campos. Os bancos de dados relacionais são bastante utilizados em sistemas de informação, sistemas de gerenciamento de conteúdo, sistemas de gerenciamento de relacionamento com o cliente, entre outros.

<img src="https://jelvix.com/wp-content/uploads/2020/05/whats-a-relational-database.jpg" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

Cada linha de uma tabela é um registro. Cada coluna de uma tabela é um campo. Cada tabela tem um nome único. Cada campo tem um nome único. Cada campo tem um tipo de dado. Cada registro tem um valor para cada campo. Cada registro é único. Cada campo pode ser uma chave primária, que é um campo que identifica unicamente um registro. Cada campo pode ser uma chave estrangeira, que é um campo que referencia um registro de outra tabela.

Quando estamos trabalhando com bancos relacionais, precisamos definir o esquema do banco de dados. O esquema é a estrutura do banco de dados. Ele define as tabelas, os campos, os tipos de dados, as chaves primárias, as chaves estrangeiras, as restrições, entre outros. O esquema é definido utilizando uma linguagem de definição de dados, como por exemplo, o SQL (Structured Query Language).

Existem diversos tipos de software que permitem trabalhar com os bancos de dados relacionais. Eles são os responsáveis por garantir a integridade dos dados, a segurança dos dados, a recuperação dos dados, entre outros. Alguns exemplos de software de bancos de dados relacionais são o MySQL, o PostgreSQL, o SQLite, o Oracle, o SQL Server, entre outros.

Vamos trabalhar com o banco de dados relacional SQLite. O SQLite é um banco de dados relacional que é embutido na maioria dos sistemas operacionais. Ele é um banco de dados relacional que é bastante utilizado em sistemas embarcados, sistemas de desktop, sistemas móveis, entre outros. O SQLite é um banco de dados relacional que é bastante leve e que não requer um servidor. Ele é um banco de dados relacional que é bastante rápido e que suporta a maioria das funcionalidades do SQL. Para maiores informações, consulte a [documentação oficial](https://www.sqlite.org/index.html).

De forma build-in, o Python já possui uma biblioteca para trabalhar com o SQLite. Vamos trabalhar com o arquivo [sqlite_v1.py](#). Para executar ele vamos rodar o comando: `python3 src/sqlite_v1.py`.

```python
# sqlite_v1.py

import sqlite3

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
    conexao.commit()

def inserir_pessoa(conexao, nome, idade):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO pessoa (nome, idade) VALUES (?, ?)
    ''', (nome, idade))
    conexao.commit()

def listar_pessoas(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT id, nome, idade FROM pessoa
    ''')
    for pessoa in cursor.fetchall():
        print(pessoa)

def main():
    conexao = sqlite3.connect('pessoas.db')
    criar_tabela(conexao)
    inserir_pessoa(conexao, 'Fulano', 30)
    inserir_pessoa(conexao, 'Ciclano', 25)
    listar_pessoas(conexao)
    conexao.close()

if __name__ == '__main__':
    main()
```

Vamos avaliar o código anterior por partes:

- `import sqlite3`: Importa a biblioteca `sqlite3`. Ela é uma biblioteca built-in do Python que nos permite trabalhar com o SQLite.

- `criar_tabela`: Função para criar a tabela no banco de dados. Ela recebe a conexão com o banco de dados. O método `cursor` cria um cursor para executar comandos SQL. O método `execute` executa o comando SQL para criar a tabela. Dentro do método `execute`, utilizando os comandos SQL para criar a tabela `pessoa`, com os campos: `id`, `nome` e `idade`. O método `commit` confirma a transação.

- `inserir_pessoa`: Função para inserir uma pessoa na tabela do banco de dados. Ela recebe a conexão com o banco de dados, o nome e a idade da pessoa. O método `cursor` cria um cursor para executar comandos SQL. O método `execute` executa o comando SQL para inserir a pessoa na tabela. Dentro do método `execute`, utilizando os comandos SQL para inserir a pessoa na tabela `pessoa`. O método `commit` confirma a transação.

- `listar_pessoas`: Função para listar as pessoas da tabela do banco de dados. Ela recebe a conexão com o banco de dados. O método `cursor` cria um cursor para executar comandos SQL. O método `execute` executa o comando SQL para listar as pessoas da tabela. O método `fetchall` retorna todas as linhas do resultado da consulta. O método `print` imprime as pessoas.

> ***Mas Murilão, e se for necessário manipular diversas entradas?*** É possível sim, o SQLite é um banco de dados relacional que suporta a maioria das funcionalidades do SQL. Isso significa que você pode criar tabelas, inserir registros, listar registros, atualizar registros, deletar registros, entre outras operações.

Podemos observar que o arquivo `pessoas.db` foi criado no mesmo diretório do arquivo que está sendo executado. Caso você queira criar o arquivo em outro diretório, você deve passar o caminho completo do arquivo. Por exemplo, se você quiser criar o arquivo `pessoas.db` no diretório `dados`, você pode passar o caminho completo do arquivo: `dados/pessoas.db`.

Este arquivo pode ser manipulado utilizando editores de banco de dados, como por exemplo, o DBeaver, o DB Browser for SQLite, entre outros. 

Agora vamos trabalhar com o arquivo [sqlite_v2.py](#). Para executar ele vamos rodar o comando: `python3 src/sqlite_v2.py`. Ele vai acessar o banco de dados `faker.db` que está no diretório `src`.

```python
# sqlite_v2.py

import sqlite3

class Funcionario:
    def __init__(self, nome, email, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.email = email
    
    def __str__(self):
        return f'{self.nome} - {self.email} - {self.idade} - {self.salario}'

def ler_funcionario(conexao, id):
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT nome, email, idade, salario FROM funcionarios WHERE id = ?
    ''', (id))
    pessoa = cursor.fetchone()
    if pessoa:
        print(pessoa)
        return Funcionario(*pessoa)
    else:
        print('Pessoa não encontrada')
        return None
    
def listar_funcionarios(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT nome, email, idade, salario FROM funcionarios
    ''')
    for pessoa in cursor.fetchall():
        print(pessoa)

def main():
    conexao = sqlite3.connect('faker.db')
    listar_funcionarios(conexao)
    conexao.close()

if __name__ == '__main__':
    main()
```

A primeira grande diferença que podemos observar é que não estamos mais criando nosso banco, estamos acessando um banco que já foi criado. Além disso, estamos utilizando uma classe para representar os dados que estamos manipulando. Isso é uma prática bastante comum quando estamos trabalhando com bancos de dados.

