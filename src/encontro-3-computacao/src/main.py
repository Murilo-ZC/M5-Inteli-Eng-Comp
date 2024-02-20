# main.py
import typer

# Cria uma instância da aplicação
app = typer.Typer()

# Cria um comando do CLI
@app.command()
def soma(a: int, b: int = 0):
    print(a + b)

# Cria um segundo comando do CLI
@app.command()
def subtracao(a: int, b: int = 0):
    print(a - b)

# Executa a aplicação
if __name__ == "__main__":
    app()
