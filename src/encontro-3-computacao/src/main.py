# main.py
import typer

# Vamos configurar está função main() para ser executada apenas quando o script for o ponto de entrada da aplicação
def main(valor1: float, valor2: float):
    # Somando os demais elementos do script
    soma = valor1 + valor2
    print(f'Soma dos elementos fornecidos: {soma}')

if __name__ == "__main__":
    typer.run(main)