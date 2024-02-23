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