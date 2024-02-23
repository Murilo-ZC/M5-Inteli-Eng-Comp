# cria_banco_faker.py

import sqlite3

# Fake Data - https://www.jsondataai.com
# https://www.generatedata.com/
# https://www.mockaroo.com/
# https://www.fakenamegenerator.com/
dados = [
  {
    "nome": "John Doe",
    "email": "john.doe@example.com",
    "idade": "32",
    "salario": "50000"
  },
  {
    "nome": "Jane Smith",
    "email": "jane.smith@example.com",
    "idade": "28",
    "salario": "45000"
  },
  {
    "nome": "Michael Johnson",
    "email": "michael.johnson@example.com",
    "idade": "35",
    "salario": "60000"
  },
  {
    "nome": "Emily Davis",
    "email": "emily.davis@example.com",
    "idade": "30",
    "salario": "55000"
  },
  {
    "nome": "David Brown",
    "email": "david.brown@example.com",
    "idade": "40",
    "salario": "70000"
  },
  {
    "nome": "Sarah Miller",
    "email": "sarah.miller@example.com",
    "idade": "27",
    "salario": "42000"
  },
  {
    "nome": "Robert Wilson",
    "email": "robert.wilson@example.com",
    "idade": "33",
    "salario": "52000"
  },
  {
    "nome": "Jennifer Taylor",
    "email": "jennifer.taylor@example.com",
    "idade": "29",
    "salario": "48000"
  },
  {
    "nome": "Christopher Anderson",
    "email": "christopher.anderson@example.com",
    "idade": "38",
    "salario": "65000"
  },
  {
    "nome": "Amanda Thomas",
    "email": "amanda.thomas@example.com",
    "idade": "31",
    "salario": "53000"
  },
  {
    "nome": "Daniel Martinez",
    "email": "daniel.martinez@example.com",
    "idade": "36",
    "salario": "58000"
  },
  {
    "nome": "Melissa Hernandez",
    "email": "melissa.hernandez@example.com",
    "idade": "34",
    "salario": "56000"
  },
  {
    "nome": "Joshua Moore",
    "email": "joshua.moore@example.com",
    "idade": "39",
    "salario": "67000"
  },
  {
    "nome": "Laura Clark",
    "email": "laura.clark@example.com",
    "idade": "26",
    "salario": "40000"
  },
  {
    "nome": "Kevin Rodriguez",
    "email": "kevin.rodriguez@example.com",
    "idade": "37",
    "salario": "59000"
  },
  {
    "nome": "Patricia Lewis",
    "email": "patricia.lewis@example.com",
    "idade": "32",
    "salario": "51000"
  },
  {
    "nome": "Brian Lee",
    "email": "brian.lee@example.com",
    "idade": "28",
    "salario": "47000"
  },
  {
    "nome": "Karen Walker",
    "email": "karen.walker@example.com",
    "idade": "33",
    "salario": "54000"
  },
  {
    "nome": "Jason Hall",
    "email": "jason.hall@example.com",
    "idade": "29",
    "salario": "50000"
  },
  {
    "nome": "Michelle Young",
    "email": "michelle.young@example.com",
    "idade": "35",
    "salario": "60000"
  },
  {
    "nome": "Ryan Allen",
    "email": "ryan.allen@example.com",
    "idade": "30",
    "salario": "55000"
  },
  {
    "nome": "Cynthia King",
    "email": "cynthia.king@example.com",
    "idade": "40",
    "salario": "71000"
  },
  {
    "nome": "Thomas Green",
    "email": "thomas.green@example.com",
    "idade": "27",
    "salario": "43000"
  },
  {
    "nome": "Angela Baker",
    "email": "angela.baker@example.com",
    "idade": "33",
    "salario": "52000"
  },
  {
    "nome": "Jeffrey Nelson",
    "email": "jeffrey.nelson@example.com",
    "idade": "28",
    "salario": "49000"
  },
  {
    "nome": "Stephanie Carter",
    "email": "stephanie.carter@example.com",
    "idade": "37",
    "salario": "57000"
  },
  {
    "nome": "Kyle Perez",
    "email": "kyle.perez@example.com",
    "idade": "31",
    "salario": "54000"
  },
  {
    "nome": "Rebecca Roberts",
    "email": "rebecca.roberts@example.com",
    "idade": "36",
    "salario": "59000"
  },
  {
    "nome": "Gary Turner",
    "email": "gary.turner@example.com",
    "idade": "34",
    "salario": "56000"
  },
  {
    "nome": "Amy Collins",
    "email": "amy.collins@example.com",
    "idade": "39",
    "salario": "65000"
  },
  {
    "nome": "Eric Morgan",
    "email": "eric.morgan@example.com",
    "idade": "26",
    "salario": "42000"
  },
  {
    "nome": "Samantha Ward",
    "email": "samantha.ward@example.com",
    "idade": "32",
    "salario": "51000"
  },
  {
    "nome": "Nicholas Foster",
    "email": "nicholas.foster@example.com",
    "idade": "29",
    "salario": "48000"
  },
  {
    "nome": "Heather Simmons",
    "email": "heather.simmons@example.com",
    "idade": "35",
    "salario": "57000"
  },
  {
    "nome": "Timothy Price",
    "email": "timothy.price@example.com",
    "idade": "30",
    "salario": "53000"
  }
]

def criar_banco(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        -- Cria a tabela "funcionarios" se ela não existir
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            idade INTEGER NOT NULL,
            salario DECIMAL(10,2) NOT NULL
        );
    ''')
    conexao.commit()

def inserir_pessoa(conexao, nome, email, idade, salario):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO funcionarios (nome, email, idade, salario) VALUES (?, ?, ?, ?)
    ''', (nome, email, int(idade), float(salario)))
    conexao.commit()

def main():
    conexao = sqlite3.connect('faker.db')
    criar_banco(conexao)
    for pessoa in dados:
        inserir_pessoa(conexao, pessoa['nome'], pessoa['email'], pessoa['idade'], pessoa['salario'])
    conexao.close()

if __name__ == '__main__':
    main()