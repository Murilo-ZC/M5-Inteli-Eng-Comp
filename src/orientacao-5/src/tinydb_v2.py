# tinydb_v2.py

from tinydb import TinyDB, Query

class Ponto:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z}) - {self.r}'
    
def inserir_ponto(db, ponto):
    db.insert({'x': ponto.x, 'y': ponto.y, 'z': ponto.z, 'r': ponto.r})

def listar_pontos(db):
    return db.all()

def main():
    db = TinyDB('pontos.json')
    buscador = Query()
    inserir_ponto(db, Ponto(1, 2, 3, 4))
    inserir_ponto(db, Ponto(5, 6, 7, 8))
    pontos_inseridos = listar_pontos(db)
    print(pontos_inseridos)

if __name__ == '__main__':
    main()