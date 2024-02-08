---
sidebar_label: "1 - Encontro de Instrução Computação"
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instrução de Computação

Apresentação das ferramentas utilizadas no desenvolvimento de projetos. Git, Github, Python, VSCode, Robô, Raspberry Pi Pico  e Docusaurus. Nivelamento do uso das ferramentas de software ao longo do módulo.	

Apresentação das ferramentas do módulo e a forma como elas serão utilizadas ao longo do módulo. Retomada das ferramentas e das técnicas para utilização e desenvolvimento de software. Setup de ferramentas de desenvolvimento.

## 1. Objetivos

- Conhecer algumas das ferramentas de software que serão utilizadas ao longo do módulo.
- Realizar *refresher* das ferramentas que serão utilizadas.


## 2. Slides do Encontro

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQC61sHirw6wd5a4nbJOWEQvGZs7_GG3khZlPLGNNXL9i-Xzf9fFJyU23jUXFXW68onGUswG9UkHLty/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }} ></iframe>

## 3. Material de Autoestudo

:::danger[Acesse a Adalove!]

Esse material NÃO substitui de forma alguma o uso da Adalove. Você DEVE entrar na Adalove com frequência e REGISTRAR O SEU PROGRESSO. Entendeu? Ainda não? Pera aí que vou desenhar:

<img src={useBaseUrl("/img/memes/aviso-adalove.png")} alt="ACESSE A ADALOVE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />

:::

<Tabs>
  <TabItem value="autoestudos-obrigatorios" label="📘 Autoestudos Obrigatórios" default>
     <details> 
        <summary mdxType="summary">	Software de controle de versão Git</summary>

        - https://git-scm.com/download/win
    </details> 

    <details> 
        <summary mdxType="summary">Ambiente de Programação Visual Studio Code</summary>

        - https://code.visualstudio.com/
    </details> 

    <details> 
        <summary mdxType="summary">Criando uma conta no GitHub</summary>

        - https://git-scm.com/book/pt-br/v2/GitHub-Configurando-uma-conta
    </details> 

    <details> 
        <summary mdxType="summary">	Thonny Python IDE</summary>

        - https://thonny.org/
    </details> 

    <details> 
        <summary mdxType="summary">	Docusaurus </summary>

        - https://docusaurus.io/
    </details> 

    <details> 
        <summary mdxType="summary">	NodeJS </summary>

        - https://nodejs.org/en
    </details> 

    <details> 
        <summary mdxType="summary">	Build Stunning Documentation With React & Docusaurus (Complete Guide) </summary>

        - https://www.youtube.com/watch?v=xKOhIJQi84w
    </details> 
  </TabItem>
  <TabItem value="autoestudos-opcionais" label="📔 Autoestudos Opcionais">
     
        <img class="image-intro" src={useBaseUrl("/img/memes/mash_celebrando.gif")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>

  </TabItem>
  <TabItem value="autoestudos-adicionais" label="📓 Autoestudos Adicionais">
        <img class="image-intro" src={useBaseUrl("/img/memes/mash_celebrando.gif")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>
  </TabItem>
</Tabs>

## 4. Material de Aula

### Utilizando o Git 

O Git é um software utiilzado para controlar versões. Isso significa que ele monitora mudanças no código e permite que você volte para versões anteriores do código. O Git é uma ferramenta muito utilizada por desenvolvedores de software. Ele é utilizado para controlar versões de código, mas também pode ser utilizado para controlar versões de documentos e de qualquer tipo de arquivo.

Para utilizar o `Git`, primeiro é necessário instalar o software. O Git pode ser baixado no site oficial do projeto: [Git](https://git-scm.com/download/win). Após a instalação, é necessário configurar o Git. Isso pode ser feito utilizando o comando `git config`. 

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@mail.com"
```

Após a configuração, é possível utilizar o Git para controlar versões de código. O Git é utilizado através do terminal. O terminal é uma interface de linha de comando que permite que comandos sejam executados no computador. O terminal do Git é chamado de `Git Bash`. Ele é uma interface de linha de comando que permite que comandos do Git sejam executados. Além disso, o `Git Bash` possibilita utilizar alguns comandos do Linux no Windows.

Para iniciar o controle de versão em um repositório, é necessário inicializar o repositório. Isso pode ser feito utilizando o comando `git init`. O comando `git init` cria um repositório Git vazio. O repositório é criado na pasta onde o comando é executado. 

```bash
git init
```

Após a inicialização do repositório, é possível adicionar arquivos ao repositório. Isso pode ser feito utilizando o comando `git add`. O comando `git add` adiciona arquivos ao repositório. O comando `git add` pode ser utilizado para adicionar um arquivo específico ou todos os arquivos de uma vez. 

```bash
# Adiciona um arquivo por vez
git add arquivo1.txt
# Adiciona todos os arquivos
git add .
```

Após adicionar os arquivos ao repositório, é necessário realizar um commit. O commit é uma forma de salvar as mudanças no repositório. O commit é realizado utilizando o comando `git commit`. O comando `git commit` salva as mudanças no repositório. O commit deve ser acompanhado de uma mensagem que descreve as mudanças realizadas. 

```bash
git commit -m "Mensagem do commit"
```

Após realizar o commit, é possível enviar as mudanças para um repositório remoto. Isso pode ser feito utilizando o comando `git push`. O comando `git push` envia as mudanças para um repositório remoto. O repositório remoto é um repositório que está em um servidor. O servidor pode ser o Github, o Gitlab ou qualquer outro servidor que utilize o Git. 

```bash
git push
```

Para realizar o download das mudanças de um repositório remoto, é possível utilizar o comando `git pull`. O comando `git pull` realiza o download das mudanças de um repositório remoto para a sua versão local. 

```bash
git pull
```

Quando desejamos acompanhar o status do repositório, podemos utilizar o comando `git status`. O comando `git status` mostra o status do repositório. Ele mostra quais arquivos foram modificados, quais arquivos foram adicionados e quais arquivos foram removidos. 

```bash
git status
```

A utilização do `Git` pode ser extendida para a utilização de branches, que são ramificações do código principal. A utilização de branches permite que diferentes versões do código sejam desenvolvidas ao mesmo tempo. A utilização de branches é muito útil para o desenvolvimento de software.

Para criar uma branch, é necessário utilizar o comando `git branch`. O comando `git branch` cria uma nova branch. 

```bash
git branch nome-da-branch
```

Após criar a branch, é necessário mudar para a branch. Isso pode ser feito utilizando o comando `git checkout`. O comando `git checkout` muda para a branch desejada. 

```bash
git checkout nome-da-branch
```

Após realizar as mudanças na branch, é necessário realizar um merge. O merge é uma forma de unir duas branches. O merge é realizado utilizando o comando `git merge`. O `git merge` deve ser realizado na branch que receberá as mudanças. 

```bash
# Mudando para a branch que receberá as mudanças
git checkout nome-da-branch-que-recebera-mudancas
# Realizando o merge
git merge nome-da-branch
```

Para saber mais sobre a utilização do Git, recomendo fortemente assistir:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ts-H3W1uLMM?si=HLi3X2eQju5IKMc3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display:"block", marginLeft:"auto", marginRight:"auto", marginBottom:"24px"}}></iframe>



:::danger[Conteúdo Avançado]

Quer conhecer um pouco mais sobre o controle de versão e a história da criação do Git? Recomendo assistir:

<iframe width="560" height="315" src="https://www.youtube.com/embed/6Czd1Yetaac?si=GQpEYzp_o2nt0L9o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display:"block", marginLeft:"auto", marginRight:"auto", marginBottom:"8px"}}></iframe>

> NÃO É UM TUTORIAL, MAS UMA HISTÓRIA SOBRE O GIT.
:::

- 

#### Utilizando o Github

<div class="loader-mario"></div>

#### Utilizando o VSCode

O `VSCode` é um editor de código muito utilizado por desenvolvedores de software. Ele é um editor de código gratuito e de código aberto.  Ele possui diversas extensões que podem ser utilizadas para aumentar a sua produtividade. 

O `VSCode` pode ser baixado no site oficial do projeto: [VSCode](https://code.visualstudio.com/). Após a instalação, é possível utilizar o o comando `code` no terminal para abrir o `VSCode` na pasta que deseja. Para iniciar o `VSCode` no diretório atual, basta utilizar o comando `code .` no terminal.

Algumas extensões que podem ser utilizadas para aumentar a produtividade são:

- Python: Extensão para desenvolvimento em Python.
- GitLens: Extensão para visualizar informações do Git.
- Live Share: Extensão para compartilhar o ambiente de desenvolvimento com outras pessoas.
- Remote - SSH: Extensão para desenvolvimento remoto com SSH.
- Git Graph: Extensão para visualizar o grafo do Git.
- Thunder Client: Extensão para realizar requisições HTTP.

Algumas configurações que podem ser realizadas para aumentar a produtividade são:

- Zoom com o mouse: Utilize o comando `Ctrl` + `Scroll` para aumentar ou diminuir o zoom.
- Word Wrap: Utilize o comando `Alt` + `Z` para ativar ou desativar o Word Wrap.
- Terminal: Utilize o comando `Ctrl` + ` para abrir o terminal.
- Atalhos: Utilize o comando `Ctrl` + `Shift` + `P` para abrir o painel de comandos.

:::tip[Como deixar o VSCode mais bonito?]

<iframe width="560" height="315" src="https://www.youtube.com/embed/u1Pu_hKVYa8?si=zZFgbncKWIXvhPGV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display:"block", marginLeft:"auto", marginRight:"auto", marginBottom:"8px"}}></iframe>

:::


### Utilizando o Python

O Python é uma linguagem de programação que ganha mais relevancia a cada momento. O Python pode ser utilizado em diversas áreas, desde a criação de scripts para automação de tarefas até a criação de aplicações web.

Ao longo desta seção vamos avaliar diversas aplicações de Python para refenciar o uso da linguagem ao longo do módulo.

### Configuração do Ambiente e Ambiente Virtual

O Python pode ser instalado de diversas formas diferentes no nosso sistema operacional. Ele pode ser utilizado em servidores Web também. Para o desenvolvimento ao longo do módulo, vamos utilizar o Python de forma local.

Você pode baixar o Python no site oficial da linguagem: [Python](https://www.python.org/downloads/). Escolher a versão específica de acordo com o seu sistema operacional.

:::tip[Ajuda em forma de vídeo]

Quando o Python é instalado no Windows, é necessário adicionar ele no PATH do sistema. Essa configuração é necessária para permitir que o comando `python` possa ser utilizado no terminal mesmo fora do diretório de instalação. O vídeo a seguir mostra como fazer isso:

    <iframe width="560" height="315" src="https://www.youtube.com/embed/0pG4NrucQR4?si=fY4fPJYo8uJdUCw3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" style={{display:"block", marginLeft:"auto", marginRight:"auto"}} allowfullscreen></iframe>
:::

:::warning[Ambientes Virtuais]

Quando diversas bibliotecas vão sendo instaladas em nossa instalação de Python, podemos ter incomptabilidades entre suas diferentes versões e dependências (outras bibliotecas e pacotes). Para evitar isso, é recomendado a utilização de ambientes virtuais.

Primeiro criando um ambiente virtual para o projeto:

- No Windows🪟:

```bash 
python -m venv .
# Navegando para ativar o env - No Windows
cd Scripts
# Ativando o env
activate
# Voltando para a pasta raiz
cd ..
```

- No Linux🐧:

```bash
python3 -m venv .
# Ativando o env
source bin/activate
```

- No MacOS🍏:

```bash
python3 -m venv .
# Ativando o env
source bin/activate
```
:::

### Escrevendo um Script em Python

O Python é uma linguagem de programação que é muito fácil de ser utilizada. A linguagem é muito legível e possui uma sintaxe muito simples. Podemos criar um script em Python para realizar diversas tarefas. Vamos iniciar criando um arquivo chamado `ola.py` com o seguinte conteúdo:

```python
print("Olá, Mundo!")
```

Para executar o script, basta abrir o terminal e digitar:

```bash
python ola.py
```

A saída experada para o comando acima é:

```bash
Olá, Mundo!
```

Agora criando um script um pouco mais complexo, pode ser chamado de `calculaMedia.py`:

```python showLineNumbers
# Script para calcular a média de notas
notas = [10, 9, 8, 7, 6]
media = sum(notas) / len(notas)
print(f"A média das notas é: {media}")
```

Para executar o script:

```bash
python calculaMedia.py
```

Ao avaliar o código acima, podemos notar que várias coisas estão acontecendo:

- A linha 2 cria uma lista de notas;
- A linha 3 calcula a média das notas, ela realiza isso somando (`sum`) todas as notas e dividindo pelo número de notas (`len`);
- A linha 4 imprime a média das notas.

### Trabalhando com Sets

Um Set em Python é equivalente a uma lista, mas nenhum de seus valores pode ser duplicado. Vamos criar um script chamado `trabalhandoComSets.py`:

```python showLineNumbers
# Script para trabalhar com sets
notas = {10, 9, 8, 7, 6, 6, 7, 8, 9, 10}
print(f"O conjunto de notas é: {notas}")
```
No código acima, podemos notar que a lista de notas possui valores duplicados. No entanto, ao executar o script, podemos notar que a saída é:

```bash
O conjunto de notas é: {6, 7, 8, 9, 10}
```

Os Sets não armazenam valores duplicados e nem a ordem que os valores foram inseridos. Quando um set for iniciado sem nenhum valor, devemos utilizar a função `Set()`. Vamos avaliar algumas operações que podem ser realizadas com Sets.

```python
# Exemplo para trabalhar com sets

amigos = {'João', 'Maria', 'José', 'Ana', 'João', 'Maria'}
amigos_fora = {'José', 'Ana', 'João'}

# Diferença entre sets
print("Diferença:" ,amigos.difference(amigos_fora))

# Total de elementos distintos - União dos sets
print("União:", amigos.union(amigos_fora))

# Interseção
print("Interseção:", amigos.intersection(amigos_fora))
```

Sets podem  ser utilizados para acelerar comparações entre listas, por exemplo.

> ***Nota:*** Sets não possuem ordem, então não é possível acessar um elemento pelo seu índice.

Mais operações com sets: [Documentação sobre Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).

### List Comprehension

O operador `in` pode ser utilizado para verificar se um elemento está contido em um set, uma lista ou um dicionário. Uma forma de trabalhar com listas é utilizando um recursos chamado *list comprehension*.

```python
# Utilizando o recurso de list comprehensions:

# Lista base
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Criando uma lista de quadrados
## Estrutura: [expressão for item in lista]
quadrados = [x * x for x in lista]
print(quadrados)
```

O objetivo do *list comprehension* é criar uma nova lista a partir de uma lista existente, aplicando uma expressão a cada elemento da lista. A estrutura dela é a seguinte:
- Primeiro a operação que deve ser realizada com cada elemento da lista;
- Segundo o elemento que será utilizado para realizar a operação. Ele também será o responsável por interar sobre a lista;
- Terceiro a lista que será utilizada para realizar a operação.

Em geral, as operações com list comprehensions são escritas em uma única linha. Manter a operação concisa é uma boa prática. Quando a operação não deve ser aplicada a todos os elementos da lista, é possível utilizar um `if` para filtrar os elementos que devem ser utilizados. Ele deve ser implementado no final da expressão.

```python
# Utilizando o recurso de list comprehensions:

# Lista base
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Criando uma lista de pares
pares = [x for x in lista if x % 2 == 0]
print(pares)
```

> ***Nota:*** Quando uma lista é criada utilizando o recurso de list comprehension, ela é criada em memória. Se a lista for muito grande, pode ser que o computador não consiga processar a operação. Nesse caso, é possível utilizar um gerador, que é um objeto que gera os elementos da lista sob demanda. 

### Desempacotamento de Sequência

Com Python é possível realizar uma operação chamada Desempacotamento de Sequência. Ela permite que uma lista seja desempacotada em variáveis individuais.

```python
# Desempacotamento de Sequência
pessoas = ['João', 'Maria', 'José', 'Ana']
pessoa1, pessoa2, pessoa3, pessoa4 = pessoas
# Para ignorar um elemento da lista, basta utilizar um underline
pessoa1, pessoa2, _, pessoa4 = pessoas
# Para pegar todos os elementos restantes, basta utilizar um asterisco
pessoa1, pessoa2, *restante = pessoas
```

> ***Nota:*** O desempacotamento de sequência pode ser utilizado com qualquer tipo de sequência, como listas, sets, tuplas e strings.

### Funções e Lambdas

Funções são blocos de código que podem ser chamados para realizar uma tarefa específica. Em Python, funções são definidas utilizando a palavra-chave `def`. Funções podem receber parâmetros e retornar valores. 

```python
# Função para calcular a média
def calcula_media(notas):
    return sum(notas) / len(notas)

# Chamando a função
notas = [10, 9, 8, 7, 6]
media = calcula_media(notas)
print(f"A média das notas é: {media}")
```

Funções podem receber valores para seus parâmetros. Em Python, os parâmetros podem ser passados por posição ou por nome, podem ainda possuir valores padrões, que a função assume se nenhum outro valor for passado para ele. 

```python
# Função para calcular a média
def calcula_media(notas, peso1=1, peso2=1, peso3=1, peso4=1, peso5=1):
    return (notas[0] * peso1 + notas[1] * peso2 + notas[2] * peso3 + notas[3] * peso4 + notas[4] * peso5) / (peso1 + peso2 + peso3 + peso4 + peso5)

# Chamando a função
notas = [10, 9, 8, 7, 6]
media = calcula_media(notas, peso1=2, peso2=2, peso3=2, peso4=2, peso5=2)
print(f"A média das notas é: {media}")

nova_media= calcula_media(notas)
print(f"A média das notas é: {nova_media}")
```

No caso do bloco de código acima, os parâmetros `peso1`, `peso2`, `peso3`, `peso4` e `peso5` possuem valores padrões. Se nenhum valor for passado para eles, a função assume o valor padrão. Na primeira chamada a função `calcula_media` é chamada com valores específicos para os pesos. Na segunda chamada, a função é chamada sem passar valores para os pesos, então a função assume os valores padrões.

Funções podem retornar valores. Em Python, funções podem retornar mais de um valor. Quando uma função retorna mais de um valor, ela retorna uma tupla.

```python
# Função para calcular a média e a soma de notas
def calcula_media_soma(notas):
    return sum(notas)/len(notas), sum(notas)

# Chamando a função
notas = [10, 9, 8, 7, 6]
media, soma = calcula_media_soma(notas)
print(f"A média das notas é: {media}")
print(f"A soma das notas é: {soma}")
```

> ***IMPORTANTE:*** Quando utilizando funções, se uma variável local de uma função tiver o mesmo indicador de nome de uma variável global, a variável local terá prioridade sobre a variável global. Para utilizar a variável global, é necessário utilizar o comando `global` antes de declarar a variável local. Se a variável global for alterada dentro da função, ela será alterada também fora da função. Se a variável global for sobreescrita dentro da função, ela será criada como uma variável local.


Existe um tipo especial de função chamada ***lambda***. Elas foram desenvolvidas para processar dados de entrada e retornar um conjunto de dados de saída. Em geral, elas não são utilizadas para realizar ações diferentes deste tipo de processamento.


As funções lambda são escritas em uma única linha e não possuem nome. Elas são utilizadas para realizar operações simples e não devem ser utilizadas para realizar operações complexas. Sua sintaxe é a seguinte:

> *lambda argumento: expressão*

Para utilizar as funções lambdas em um local diferente de onde elas foram criadas, é necessário atribuí-las a uma variável. Uma utilização bastante comum das funções do tipo lambda são em list comprehensions. Elas permitem que uma operação seja realizada em cada elemento de uma lista.

```python
# Sintaxe de uma função lambda
# lambda argumento: expressão
variavel_para_lambda = lambda x,y : x+ y

print(variavel_para_lambda(2,3))

# Utilizando um list comprehension com uma função lambda
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrado = lambda x: x * x
# Pode ser utilizado de qualquer uma das duas formas:
# Forma 1:
quadrados = [(lambda x: x * x)(x) for x in lista]
# Forma 2:
quadrados = map(quadrado, lista)

```

O uso da sintaxe da função ***map()*** é comum em outras linguagens de programação. Ela permite que uma função seja aplicada a cada elemento de uma lista. O resultado é uma lista com os elementos alterados.


Os parênteses ao redor da função lambda são necessários para que a função seja executada como um bloco. Além de **list comprehensions**, podemos utilizar os dictionaries comprehensions. Eles são utilizados para criar dicionários a partir de uma lista.

```python
# Exemplo de como utilizar dictionary compreenhencion
usuarios = [
    (0, "Murilo", "Professor"),
    (1, "Mojang", "Desenvolvedora"),
    (0, "Midoria", "Estudante")
]

# Gera um novo dicionário com os registros
novo_dict = {usuario[1]:usuario for usuario in usuarios}

print(novo_dict)
```

Quando a quantidade de argumentos que será enviado para uma função não é conhecida, é possível utilizar o operador `*` para indicar que a função deve receber uma quantidade variável de argumentos. Os argumentos serão recebidos como uma tupla.


```python
# Exemplo de como utilizar o operador * para receber uma quantidade variável de argumentos
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
print(soma(1,2))
print(soma(1,2,4,5,7,8))

```

É possível utilizar parâmetros nomeados e o operador `**` para receber uma quantidade variável de argumentos nomeados. Os argumentos serão recebidos como um dicionário. Utilizando o apenas o operador `*` os argumentos serão recebidos como uma tupla.


```python
# Exemplo de como utilizar o operador ** para receber uma quantidade variável de argumentos nomeados
def soma(**kwargs):
    total = 0
    for numero in kwargs.values():
        total += numero
    return total
print(soma(a=1,b=2))
print(soma(a=1,b=2,c=4,d=5,e=7,f=8))

```  

### Um Pouco de Orientação a Objetos

Quando temos um método definido em uma classe, podemos mandar uma instância da classe como argumento para o método. Quando fazemos isso, o método recebe a instância como primeiro argumento. Esse argumento é chamado de `self` e é utilizado para acessar os atributos e métodos da classe.


```python
# Exemplo de como utilizar o operador ** para receber uma quantidade variável de argumentos nomeados
class ClasseExemplo:
    def __init__(self, nome):
        self.nome = nome
    def imprimir_nome(self):
        print(self.nome)

instancia = ClasseExemplo("Murilo")
# Chamada do método imprimir_nome
instancia.imprimir_nome()

# Chamada do método imprimir_nome utilizando a classe
ClasseExemplo.imprimir_nome(instancia)

```

:::note[Definição de uma classe]
> ***ATENÇÃO:*** Uma classe é um modelo para criar objetos. Um objeto é uma instância de uma classe. Quando uma classe é instanciada, é criado um objeto. Um objeto é uma instância de uma classe.
:::

Existem alguns métodos que são especiais nas classes. Eles são invocados de forma automática em algumas situações específicas. Um exemplo é o método `__init__`. Ele é invocado quando uma classe é instanciada. Ele é utilizado para inicializar os atributos da classe.

```python
# Exemplo de como utilizar o método __init__ para inicializar os atributos da classe
class ClasseExemplo:
    def __init__(self, nome):
        self.nome = nome
    def imprimir_nome(self):
        print(self.nome)

instancia = ClasseExemplo("Murilo")
# Chamada do método imprimir_nome
instancia.imprimir_nome()
```

O método `__str__` é utilizado para retornar uma representação em string de um objeto. Ele é invocado quando utilizamos a função `print()` para imprimir um objeto, por exemplo.

O método `__repr__` é utilizado para retornar uma representação em string do conteúdo do objeto. Ele é invocado quando utilizamos a função `repr()` para imprimir um objeto, por exemplo. Ele é chamado de forma automática quando utilizamos o interpretador do Python para debugar um código.

Em geral, o método `__str__` é utilizado para retornar uma representação mais amigável do objeto, enquanto o método `__repr__` é utilizado para retornar uma representação mais precisa do objeto.

Podemos definir valores constantes dentro de uma classe. Para isso, basta definir um atributo da classe e atribuir um valor a ele. Para acessar o valor de um atributo de classe, basta utilizar o nome da classe e o nome do atributo.

```python
# Exemplo de como utilizar o método __init__ para inicializar os atributos da classe
class ClasseExemplo:
    # Atributo de classe
    VALOR_CONSTANTE = 10
    def __init__(self, nome):
        self.nome = nome
    def imprimir_nome(self):
        print(self.nome)

instancia = ClasseExemplo("Murilo")
# Chamada do método imprimir_nome
instancia.imprimir_nome()
# Acessando o atributo de classe
print(ClasseExemplo.VALOR_CONSTANTE)
```

:::note[Atributo de classe]
> ***IMPORTANTE:*** Quando um atributo de classe é alterado, ele é alterado para todas as instâncias da classe. Quando um atributo de instância é alterado, ele é alterado apenas para a instância que foi alterada.
:::


Assim como podemos definir atributos para a classe, podemos definir métodos para a classe. Para isso, basta definir uma função dentro da classe. Para acessar um método de uma classe, basta utilizar o nome da classe e o nome do método.

```python
# Exemplo de como utilizar o método __init__ para inicializar os atributos da classe
class ClasseExemplo:
    # Atributo de classe
    VALOR_CONSTANTE = 10
    def __init__(self, nome):
        self.nome = nome
    def imprimir_nome(self):
        print(self.nome)
    # Método de classe
    @classmethod
    def imprimir_valor_constante(cls):
        # A referência cls indica a própria classe
        print(cls.VALOR_CONSTANTE)

ClasseExemplo.imprimir_valor_constante()
```

Métodos de classe podem ter acesso a classe, mas não podem ter acesso a instância. Para isso, é necessário utilizar o decorador `@classmethod` antes da definição do método. Esses métodos podem ser utilizados para criar objetos com uma variação de atributos, por exemplo.

:::danger[Existe diferença entre métodos de classe e métodos estáticos]

Definição: "*Class methods can access and modify class-level attributes. They have access to the class object and can modify class variables or create new instances of the class. Static methods, on the other hand, do not have access to the class object and cannot modify any class-level attributes.*"

- https://www.linkedin.com/pulse/exploring-differences-between-class-methods-static-python/
- https://realpython.com/instance-class-and-static-methods-demystified/
- https://www.geeksforgeeks.org/class-method-vs-static-method-python/
:::

Utilizamos o conceito de herança quando queremos criar uma classe que herda os atributos e métodos de outra classe. Para isso, basta passar a classe que será herdada como argumento da classe que será criada.

```python
# Exemplo de como utilizar o método __init__ para inicializar os atributos da classe
class ClasseExemplo:
    # Atributo de classe
    VALOR_CONSTANTE = 10
    def __init__(self, nome):
        self.nome = nome
    def imprimir_nome(self):
        print(self.nome)
    # Método de classe
    @classmethod
    def imprimir_valor_constante(cls):
        # A referência cls indica a própria classe
        print(cls.VALOR_CONSTANTE)

# Classe que herda os atributos e métodos da classe ClasseExemplo
class ClasseExemplo2(ClasseExemplo):
    pass

instancia = ClasseExemplo2("Murilo")
instancia.imprimir_nome()
```

Quando uma classe herda os atributos e métodos de outra classe, ela pode sobrescrever os atributos e métodos da classe que está herdando. Para isso, basta definir o atributo ou método com o mesmo nome da classe que está herdando.

```python
# Exemplo de como utilizar o método __init__ para inicializar os atributos da classe
class ClasseExemplo:
    # Atributo de classe
    VALOR_CONSTANTE = 10
    def __init__(self, nome):
        self.nome = nome
    def imprimir_nome(self):
        print(self.nome)
    # Método de classe
    @classmethod
    def imprimir_valor_constante(cls):
        # A referência cls indica a própria classe
        print(cls.VALOR_CONSTANTE)

# Classe que herda os atributos e métodos da classe ClasseExemplo
class ClasseExemplo2(ClasseExemplo):
    # Quando desejamos chamar o construtor da classe que está herdando, utilizamos o método super()
    def __init__(self, nome):
        super().__init__(nome)
    # Sobrescrevendo o método imprimir_nome
    def imprimir_nome(self):
        print("Sobrescrevendo o método imprimir_nome")

instancia = ClasseExemplo2("Murilo")
instancia.imprimir_nome()
```

Em geral, em Python a composição é mais utilizada do que a herança. A composição é utilizada quando queremos que uma classe tenha uma instância de outra classe como atributo. Para isso, basta criar um atributo da classe que será utilizada como composição.

Com a composição, podemos escrever classes menores e mais específicas, permitindo que elas sejam reutilizadas em outras classes e possuam uma melhor organização.

Do ponto de vista conceitual, a herança cria uma ligação do tipo `é um` entre as classes. Já a composição cria uma ligação do tipo `tem um` entre as classes.


### Type Hinting


A partir do Python 3.5, é possível utilizar o Type Hinting para indicar o tipo de um argumento de uma função ou método. Isso é útil para indicar o tipo de dado que deve ser passado para uma função ou método. O Type Hinting não é obrigatório, mas é uma boa prática utilizá-lo.

Quando utilizamos o Type Hinting, o Python não faz nenhuma validação do tipo de dado que está sendo passado para a função ou método. Ele apenas indica o tipo de dado que deve ser passado. CONTUDO, se estivermos utilizando algum linter, ele pode fazer a validação do tipo de dado que está sendo passado.

```python
# Importando o tipo lista para retorno
from typing import List

# Cria uma função que retorna a soma dos valores informados em uma lista
def soma_lista(dados:List) -> float:
    return sum(dados)

entrada = [1,2,3,4]
print(soma_lista(entrada))
```

Podemos especificar que um tipo de dado é uma classe utilizando o nome da classe. Podemos especificar que um tipo de dado é uma lista de um determinado tipo de dado utilizando o nome da classe entre colchetes. Podemos especificar que um tipo de dado é uma tupla de um determinado tipo de dado utilizando o nome da classe entre parênteses.

### Exercícios

Pessoal aqui vão existir alguns exercícios para auxiliar vocês a fixar alguns dos conteúdos apresentados. Lembrando, eles não valem nota ou precisam ser entregues, servem apenas para práticar a utilização do Python.

1. Construa um programa que permita que o usuário informe os 3 lados de um triângulo, A, B e C. Apresente para ele o valor da área do triângulo utilizando a fórmula de [Hierão](https://pt.khanacademy.org/math/geometry-home/geometry-volume-surface-area/heron-formula-tutorial/v/heron-s-formula#:~:text=a%20%2B%20b%20%2B%20c%20dividido%20por,fórmula%20de%20Herão%2C%20esta%20combinação.). ATENÇÃO: Para o calculo do semiperimetro (s) e da Área, elabore uma função.

2. Elabore um programa capaz de converter a temperatura monitorada em graus C, informada por um usuário, para graus K e F. OBRIGATÓRIAMENTE: utilize duas funções, uma para converter a temperatura para graus K e outra para graus F.

3. Elabore um programa que armazene os dados do usuário (nome, idade e cpf) em strings diferentes. Utilize uma função para realizar a leitura dos dados do usuário e uma função de exibição para mostrar todas as informações lidas. 

4. Elabore um programa que possibilite o usuário inserir 15 medições de tempo. Determine quais foram os tempos máximo, mínimo e médio. Considere que os valores de tempo informado estão todos em segundos, apenas valores interiores são fornecidos e cada uma das funcionalidades deve ser implementada em uma função distinta. 

5. Existem diversas maneiras de se resolver algumas equações. Dentre elas, algumas abordagens são bastantes conhecidas na literatura, como o Algoritmo de Euclides para calcular o Máximo Divisor Comum. Elabore uma função que realize sua implementação.

6. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

  - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
  - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
  - A mensagem "Aprovado com Distinção", se a média for igual a 10. 
  (Retirado de https://wiki.python.org.br/EstruturaDeDecisao).

7. Faça um Programa que leia três números e mostre o maior e o menor deles. (Retirado de https://wiki.python.org.br/EstruturaDeDecisao).

8.  Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
  - Para homens: (72.7*h) - 58
  - Para mulheres: (62.1*h) - 44.7
  Lembre-se de realizar a leitura do sexo da pessoa. (Adaptado de https://wiki.python.org.br/EstruturaDeDecisao).

9. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. (Retirado de https://wiki.python.org.br/EstruturaDeDecisao).