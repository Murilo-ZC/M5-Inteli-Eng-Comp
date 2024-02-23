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