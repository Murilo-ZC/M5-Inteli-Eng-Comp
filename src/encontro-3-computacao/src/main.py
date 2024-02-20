# main.py
import typer
import inquirer

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

# Cria um terceiro comando do CLI
@app.command()
def soma_interativa():
    continuar = True
    while continuar:
        a = typer.prompt("Digite o primeiro número")
        b = typer.prompt("Digite o segundo número")
        print(int(a) + int(b))
        continuar = typer.confirm("Deseja continuar?")

# Cria um quarto comando do CLI
@app.command()
def calculadora():
    # realiza lista de perguntas para o usuário
    perguntas = [
        inquirer.List("operacao", message="Qual operação deseja realizar?", choices=["soma", "subtração","multiplicacao","divisao"]),
        inquirer.Text("a", message="Digite o primeiro número"),
        inquirer.Text("b", message="Digite o segundo número")
    ]
    # realiza a leitura das respostas
    respostas = inquirer.prompt(perguntas)
    # apresenta as respostas que o usuário digitou
    print(respostas)
# Executa a aplicação
if __name__ == "__main__":
    app()
