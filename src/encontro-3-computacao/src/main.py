# main.py
import sys

# Vamos configurar está função main() para ser executada apenas quando o script for o ponto de entrada da aplicação
def main():
    # Nome do script
    print(f'Nome do Script: {sys.argv[0]}')

    # Somando os demais elementos do script
    soma = 0
    for elemento in sys.argv[1:]:
        soma += float(elemento)
    print(f'Soma dos elementos fornecidos: {soma}')

if __name__ == "__main__":
    main()