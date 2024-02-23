# tinydb_v1.py

from tinydb import TinyDB, Query

def main():
    db = TinyDB('usuarios.json')
    User = Query()
    db.insert({'name': 'John', 'age': 22})
    user = db.search(User.name == 'John')
    print(user)

if __name__ == '__main__':
    main()