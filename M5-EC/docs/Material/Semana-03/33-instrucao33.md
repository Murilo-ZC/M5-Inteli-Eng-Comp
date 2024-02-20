---
sidebar_label: "3 - Encontro de Computação"
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instrução de Computação

Comunicação com o Robô	

# 1. Objetivos

- Desenvolvimento de software de comunicação com o robô. 
- Apresentação da utilização de ferramentas externas e criação de ambientes virtuais utilizando o Python.
- Introdução aos conceitos de comunicação. Navegação em biblioteca externa e documentação do desenvolvedor.
- ***NOVO:*** Utilizar um sistema para construir a interface CLI.

## 2. Slides do Encontro

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSG6q7EZA2isyGW3V_1pXMM7IJquzznhrFYcQA0ygtI8Nfv7v7SvdBN_jbO2XuOBN3kg1zpmRzti5Om/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }}></iframe>


## 3. Material de Autoestudo

:::danger[Acesse a Adalove!]

Esse material NÃO substitui de forma alguma o uso da Adalove. Você DEVE entrar na Adalove com frequência e REGISTRAR O SEU PROGRESSO. Entendeu? Ainda não? Pera aí que vou desenhar:

<img src={useBaseUrl("/img/memes/aviso-adalove.png")} alt="ACESSE A ADALOVE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />

:::

<Tabs>
  <TabItem value="autoestudos-obrigatorios" label="📘 Autoestudos Obrigatórios" default>
     
     <details> 
        <summary mdxType="summary">	virtualenv - Crie ambientes virtuais isolados em Python</summary>

        - https://www.youtube.com/watch?v=ciFdSA8b2qw
    </details> 
    <details> 
        <summary mdxType="summary">	Pacote pydobot</summary>

        - https://pypi.org/project/pydobot/
    </details> 
    
  </TabItem>
  <TabItem value="autoestudos-opcionais" label="📔 Autoestudos Opcionais">
     
        <img class="image-intro" src={useBaseUrl("/img/memes/mash_celebrando.gif")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>

  </TabItem>
  <TabItem value="autoestudos-adicionais" label="📓 Autoestudos Adicionais">
    
    <details> 
        <summary mdxType="summary">	CLI (A "temida" Command Line Interface) // Dicionário do Programador</summary>

        - https://youtu.be/8AgOxHOAV9Y?si=KCqZ1wCncLg--OjU&t=130
    </details> 
    <details> 
        <summary mdxType="summary">	O que é uma aplicação COMMAND-LINE (CLI)?</summary>

        - https://www.youtube.com/watch?v=-CJr6afTy-0
    </details> 
    <details> 
        <summary mdxType="summary">	Professional CLI Applications with Click</summary>

        - https://www.youtube.com/watch?v=vm9tOamPkeQ
    </details> 
    <details> 
        <summary mdxType="summary">	5 Python Libraries for Building Command Line Tools</summary>

        - https://www.youtube.com/watch?v=20Qkq93kwKw
    </details> 
    <details> 
        <summary mdxType="summary">	Criando aplicações de linha de comando (CLIs) com Typer | Live de Python #233</summary>

        - https://www.youtube.com/watch?v=m1_48lmAX-Y
    </details> 

  </TabItem>
</Tabs>

## 4. Material de Aula

Pessoal no material deste encontro vamos trabalhar com alguns pontos que serão relevantes para o desenvolvimento do projeto. Isso vai desde a criação de um ambiente virtual de Python até o desenvolvimento de um sistema com CLI.

### 4.1 Criando um Ambiente Virtual em Python

A estrutura de diretórios que vamos utilizar é a seguinte:

```bash
.
├── .gitignore
├── README.md
├── src
```
Todos estes arquivos podem ser encontrados no diretório [encontro-3-computacao](#). O que cada um destes diretórios e arquivos significam? Vamos avaliar eles em conjunto:

- `.gitignore`: Este arquivo é utilizado para que o git ignore arquivos que não são necessários para o versionamento do projeto. Por exemplo, arquivos de configuração, arquivos de log, arquivos temporários, etc. É importante colocar estes arquivos no `.gitignore` para que o git não fique "poluído" com arquivos que não são necessários.
- `README.md`: Este arquivo é utilizado para que possamos documentar o projeto. É importante que este arquivo seja bem escrito e que contenha todas as informações necessárias para que qualquer pessoa que entre no projeto consiga entender o que está acontecendo. Em especial quando estamos utilizando ambientes virtuais ou alguma outra dependência que não está no projeto, ele deve descrever o que uma pessoal deve fazer para conseguir utilizar nosso projeto.
- `src`: Este diretório é onde vamos colocar o código fonte do nosso projeto. É importante que ele seja bem organizado e que siga as boas práticas de programação.

:::danger[Atenção]

Pessoal deste ponto em diante estou considerando que os comandos para executar nosso ambiente virtual serão executados no terminal do seu sistema operacional. Se você estiver utilizando o Windows, abra o `cmd` (na teoria o `PowerShell` deve funcionar também). Se você estiver utilizando o Linux ou o MacOS, abra o terminal do seu sistema operacional.

Em alguns sistemas operacionais, o comando `python` invoca a versão do Python 2. Se você estiver utilizando o Python 3, você deve utilizar o comando `python3`. Se você não souber qual é a versão do Python que você está utilizando, basta executar o comando `python --version` ou `python3 --version` no terminal. Se você estiver utilizando o Python 3, substitua o comando `python` por `python3` nos comandos a seguir.

Se o terminal do Windows não estiver reconhecendo o comando `python`, você pode tentar adicionar o Python nas variáveis de ambiente do Windows. Se você não souber como fazer isso, você pode seguir [este tutorial](https://docs.python.org/pt-br/3/using/windows.html#excursus-setting-environment-variables).

:::

Agora que temos a estrutura do nosso projeto, vamos criar um ambiente virtual para ele. Para isso, vamos utilizar a ferramenta `venv` que já vem com o Python. Para criar um ambiente virtual, basta executar o seguinte comando:

```bash
python3 -m venv venv
```

Este comando vai criar um ambiente virtual na pasta `venv`. E o que isso significa? Que estamos criando um ambiente dedicado para trabalhar com Python para o nosso projeto. Outras dependências que não estão no Python, como por exemplo, o `pydobot`, não vão ser instaladas no Python global, mas sim no Python do ambiente virtual. Isso é importante para que possamos ter um ambiente isolado e que não interfira em outros projetos.

Após a criação do ambiente virtual, a seguinte estrutura de pasta vai surgir:

```bash
.
├── .gitignore
├── README.md
├── src
├── venv
```

Dentro do diretório `venv` temos a seguinte estrutura:

```bash
.
├── bin
├── include
├── lib
├── pyvenv.cfg
└── share
```

:::tip[Dica]

A estrutura de diretórios do ambiente virtual pode variar de acordo com o sistema operacional que você está utilizando. Por exemplo, no Windows, o diretório `bin` é substituído por `Scripts`. No MacOS, o diretório `lib` é substituído por `libexec`. No Linux, o diretório `lib` é substituído por `lib64`.

:::

Para ativar este ambiente virtual, basta executar o seguinte comando:

```bash
source venv/bin/activate
```

:::tip[Dica]

A forma de ativar o ambiente virtual pode variar de acordo com o sistema operacional que você está utilizando. No Windows, o comando para ativar o ambiente virtual é `venv\Scripts\activate`. No MacOS, o comando para ativar o ambiente virtual é `source venv/bin/activate`. No Linux, o comando para ativar o ambiente virtual é `source venv/bin/activate`.

:::

Após a ativação do ambiente virtual, o terminal vai mostrar o nome do ambiente virtual que está ativo. Por exemplo:

```bash
(venv) $
```

Par verificarmos a instalação do ambiente virtual, podemos executar o seguinte comando:

```bash
which python
```

A saída esperada deste comando é a pasta do ambiente virtual. Por exemplo:

```bash
/home/usuario/projeto/venv/bin/python
```

:::tip[Dica]

A saída deste comando pode variar de acordo com o sistema operacional que você está utilizando. No Windows, a saída deste comando é `C:\caminho\para\o\projeto\venv\Scripts\python.exe`. No MacOS, a saída deste comando é `/caminho/para/o/projeto/venv/bin/python`. No Linux, a saída deste comando é `/caminho/para/o/projeto/venv/bin/python`.

:::

### 4.2 Criando a CLI do Projeto - Versão Pré-Pré-Pré-Alfa

Agora com o nosso ambiente virtual criado, vamos iniciar o processo de criar nossa aplicação 💻🖥️!!
Para isso, vamos iniciar ela com um programa básico que vamos refatorando para adicionar as funcionalidades que desejamos.

Dentro do diretório `src`, vamos criar um arquivo chamado `main.py`. Este arquivo vai ser o ponto de entrada da nossa aplicação. Dentro deste arquivo, vamos adicionar o seguinte código:

```python main.py
# Este é o arquivo ponto de entrada da nossa aplicação
print('Olá, Mundo!')
print(f'Quando este arquivo é executado: {__name__}')
```

Para executar este arquivo, basta executar o seguinte comando:

```bash
python3 src/main.py
```

A saída para a execução deste arquivo é a seguinte:

```bash
Olá, Mundo!
Quando este arquivo é executado: __main__
```

:::warning[Atenção]

<img src={useBaseUrl("/img/memes/chotto-matte.jpeg")} alt="ESPERE UM POUCO" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: 24 }} />

Muito cuidado deste ponto em diante! Em especial, porque neste momento, se você está acompanhando as aulas, deve ter passado em cabeça a seguinte afirmação:

> "Como eu escrevi código e quero manter a rastreabilidade das minhas ações, vou commitar o que eu fiz até agora."

E você ***ESTÁ ABSOLUTAMENTE CERTO***! Mas antes de fazer isso, vamos adicionar no nosso `.gitignore` o diretório `venv` para que ele não seja versionado. Isso é importante para que outras pessoas que baixarem o projeto não tenham que baixar o ambiente virtual também. Para isso, basta adicionar a seguinte linha no arquivo `.gitignore`:

```bash
venv
```

> ***MAS MURILÃO, POR QUE EU NÃO DEVO COMMITAR O AMBIENTE VIRTUAL?***
> Porque o ambiente virtual é uma dependência do projeto. E como dependência, ele não deve ser versionado. Isso porque cada pessoa que baixar o projeto pode ter uma versão diferente do Python, ou mesmo do sistema operacional. E se o ambiente virtual for versionado, pode ser que o projeto não funcione em outras máquinas.

> ***MAS MURILÃO, COMO EU FAÇO PARA QUE OUTRAS PESSOAS POSSAM EXECUTAR O MEU PROJETO?***
> Você deve adicionar um arquivo chamado `requirements.txt` na raiz do projeto. Este arquivo deve conter todas as dependências do projeto. E para que as pessoas consigam instalar estas dependências, basta que elas executem o seguinte comando:

```bash
pip install -r requirements.txt
```

> ***MAS MURILÃO, COMO EU FAÇO PARA CRIAR O ARQUIVO `requirements.txt`?***
> Você pode criar este arquivo manualmente, ou você pode utilizar o seguinte comando:

```bash
pip freeze > requirements.txt
```

Este comando vai criar um arquivo chamado `requirements.txt` com todas as dependências do projeto. 

> ***MAS MURILÃO, EU OLHEI NO SEU GITHUB E VI QUE EM UM COMMIT O SEU VENV FOI ADICIONADO. POR QUE?***
> Como vocês acham que eu lembrei de colocar esse aviso aqui?

:::

Pessoal vamos voltar para o nosso código. Se observarmos ele, o `__name__` apareceu com o valor de `__main__`. Isso acontece porque o Python atribui o valor de `__main__` para o arquivo que está sendo executado. Isso é importante para que possamos saber se o arquivo está sendo executado como um módulo ou como um arquivo principal.

Vamos fazer um teste: criar um outro arquivo e importar o nosso arquivo `main` dentro dele. Vamos chamar este arquivo de `teste_import.py`.

```python
# teste_import.py
import main
print(f'Este é o __name__ do teste_import.py: {__name__}')
```

Agora vamos executar o arquivo `teste_import.py`:

```bash
python3 src/teste_import.py
```

Vamos obter como saída:

```bash
Olá, Mundo!
Quando este arquivo é executado: main
Este é o __name__ do teste_import.py: __main__
```

Podemos reparar que o `__name__` do arquivo `main.py` é `main`, e o `__name__` do arquivo `teste_import.py` é `__main__`. Isso acontece porque o Python atribui o valor de `__main__` para o arquivo que está sendo executado. Para os demais módulo, o valor de `__name__` é o nome do módulo.

:::tip[Dica]

Vale destacar um comportamento aqui: ao importar um módulo, todo o código que está no corpo daquele módulo é executado. Isso é importante para que possamos inicializar variáveis, funções, classes, etc. que são necessárias para o funcionamento do módulo.

:::

Agora vamos iniciar a criação da nossa CLI. Quando estamos executando uma CLI, podemos ter diferentes comportamentos de acordo com os argumentos que são passados para ela. Por exemplo, se executarmos o comando `ls` no terminal, ele vai listar os arquivos e diretórios do diretório atual. Se executarmos o comando `ls -l`, ele vai listar os arquivos e diretórios do diretório atual, mas com mais informações. Se executarmos o comando `ls -a`, ele vai listar os arquivos e diretórios do diretório atual, mas com os arquivos ocultos. E assim por diante.

Vamos focar nesse tipo de solução por hora, onde enviamos os parâmetros para a execução do nosso programa. Vamos iniciar criando um programa que realiza a soma de dois números. Vou alterar nosso programa `main.py`.

```python
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
```

Vamos executar primeiro o nosso script com o comando: `python3 src/main.py`, para obter a seguinte saída na tela:

```bash
Nome do Script: src/main.py
Soma dos elementos fornecidos: 0
```

Vamos executar o script novamente, mas agora fornecendo alguns valores para ele:

```bash
python3 src/main.py 1 2.3 4 5 6
```

A saída que vamos obter agora é:

```bash
Nome do Script: src/main.py
Soma dos elementos fornecidos: 18.3
```



<div class="loader-mario"></div>