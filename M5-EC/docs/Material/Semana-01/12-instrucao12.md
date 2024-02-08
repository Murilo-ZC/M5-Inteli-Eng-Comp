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

#### Utilizando o Git 

<div class="loader-mario"></div>

#### Utilizando o Github

<div class="loader-mario"></div>

#### Utilizando o VSCode

<div class="loader-mario"></div>

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