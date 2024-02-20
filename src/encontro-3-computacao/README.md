# Para executar o sistema

Você vai precisar instalar as dependências necessárias:

```bash
python3 -m pip install -r requirements.txt
```

Lembre-se de sempre utilizar um ambiente virtual para a execução do código.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

E também lembre-se de adicionar o `.venv` criado no `.gitignore` para que não seja enviado para o repositório.

```bash
echo ".venv" >> .gitignore
```