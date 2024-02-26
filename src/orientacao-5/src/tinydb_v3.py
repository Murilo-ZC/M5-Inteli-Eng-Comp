# tinydb_v3.py
# Construindo um CRUD de notas com o TinyDB
from tinydb import TinyDB, Query
from datetime import datetime

class Nota:
    def __init__(self, titulo = None, texto = None):
        self.titulo = titulo
        self.texto = texto
        self.data_modificacao = None
        # Cria o registro da hora que a nota foi criada
        self.data_criado = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f'{self.titulo} - {self.texto} - {self.data_criado} - {self.data_modificacao}'
    
    # Funções auxiliares
    def nota_to_dict(self):
        return {'titulo': self.titulo, 'texto': self.texto, 'data_criado': self.data_criado, 'data_modificacao': self.data_modificacao}
    
    @staticmethod
    def dict_to_nota( nota_dict):
        nota = Nota()
        nota.titulo = nota_dict['titulo']
        nota.texto = nota_dict['texto']
        nota.data_criado = nota_dict['data_criado']
        nota.data_modificacao = nota_dict['data_modificacao']
        return nota
    
    @staticmethod
    def db_to_nota(nota_db):
        nota = Nota(nota_db['titulo'], nota_db['texto'])
        nota.data_criado = nota_db['data_criado']
        nota.data_modificacao = nota_db['data_modificacao']
        return nota
    
# CRUD com as notas
def inserir_nota(db, nota):
    db.insert(nota.nota_to_dict())

def listar_notas(db):
    return [Nota.db_to_nota(nota) for nota in db.all()]


def buscar_nota(db, titulo):
    buscador = Query()
    nota = db.search(buscador.titulo == titulo)
    if nota:
        return Nota.dict_to_nota(nota[0])
    else:
        return None


def atualizar_nota(db, titulo, texto):
    buscador = Query()
    db.update({'texto': texto, 'data_modificacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, buscador.titulo == titulo)

def deletar_nota(db, titulo):
    buscador = Query()
    db.remove(buscador.titulo == titulo)


# Agora lógica prinicipal do programa
def main():
    db = TinyDB('notas.json')
    continuar = True
    while continuar:
        print('1. Inserir nota')
        print('2. Listar notas')
        print('3. Buscar nota')
        print('4. Atualizar nota')
        print('5. Deletar nota')
        print('6. Sair')
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            titulo = input('Digite o título da nota: ')
            texto = input('Digite o texto da nota: ')
            inserir_nota(db, Nota(titulo, texto))
        elif opcao == 2:
            notas = listar_notas(db)
            for nota in notas:
                print(nota)
        elif opcao == 3:
            titulo = input('Digite o título da nota: ')
            nota = buscar_nota(db, titulo)
            print(nota)
        elif opcao == 4:
            titulo = input('Digite o título da nota: ')
            texto = input('Digite o texto da nota: ')
            atualizar_nota(db, titulo, texto)
        elif opcao == 5:
            titulo = input('Digite o título da nota: ')
            deletar_nota(db, titulo)
        elif opcao == 6:
            continuar = False
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()
