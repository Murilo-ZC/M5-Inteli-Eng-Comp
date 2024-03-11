---
sidebar_label: "6 - Encontro de Computação"
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instrução de Orientação	

Eletrônica Digital com Raspberry Pi Pico	

## 1. Objetivos

- Apresentação dos principais conceitos de eletrônica digital utilizando o Raspberry Pi Pico como hardware auxiliar. 
- As lógicas combinacionais e sequênciais são apresentadas neste contexto.
- A interface destes elementos versos sua utilização com circuitos discretos também será abordada.

## 2. Slides do Encontro

<!-- <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSG6q7EZA2isyGW3V_1pXMM7IJquzznhrFYcQA0ygtI8Nfv7v7SvdBN_jbO2XuOBN3kg1zpmRzti5Om/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }}></iframe> -->

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

## 3. Material de Autoestudo

:::danger[Acesse a Adalove!]

Esse material NÃO substitui de forma alguma o uso da Adalove. Você DEVE entrar na Adalove com frequência e REGISTRAR O SEU PROGRESSO. Entendeu? Ainda não? Pera aí que vou desenhar:

<img src={useBaseUrl("/img/memes/aviso-adalove.png")} alt="ACESSE A ADALOVE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />

:::

<!-- <Tabs>
  <TabItem value="autoestudos-obrigatorios" label="📘 Autoestudos Obrigatórios" default>
     
    <details> 
        <summary mdxType="summary"> Python TinyDB: base de dados em arquivos JSON</summary>

        - https://www.youtube.com/watch?v=99Vm0c9eNOA
    </details> 
    
  </TabItem>
  <TabItem value="autoestudos-opcionais" label="📔 Autoestudos Opcionais">
     
        <img class="image-intro" src={useBaseUrl("/img/memes/mash_celebrando.gif")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>

  </TabItem>
  <TabItem value="autoestudos-adicionais" label="📓 Autoestudos Adicionais">
    
    <details> 
        <summary mdxType="summary">	Lean Inception em 15 Minutos | 📎 Zup Clipes ✂️</summary>

        - https://www.youtube.com/watch?v=8BI6jFwmVPA
    </details> 

  </TabItem>
</Tabs> -->

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

## 4. Material de Aula

Ao longo do material, vamos discutir os principais conceitos de eletrônica digital e como eles se aplicam ao Raspberry Pi Pico.
Nosso material de referência de hardware, será o mesmo apresentado (aqui)[/docs/Material/Semana-05/53-instrucao53.md], na seção 4.5.

### 4.1 Eletrônica Digital

A eletrônica digital é a base de todos os sistemas computacionais. Ela é responsável por representar informações de forma binária, ou seja, utilizando apenas dois estados: 0 e 1. 
Quando utilizamos essa primeira definição, temos diante de nós uma nova base numérica, a base 2. Essa base é bastante importante para a computação, pois é a base utilizada para representar informações em sistemas digitais.

:::tip[Gerge Boole e o Sistema de Base 2]

O matemático George Boole, em 1854, publicou um livro chamado "An Investigation of the Laws of Thought". Neste livro, Boole apresentou um sistema de lógica que hoje é conhecido como álgebra de Boole. A álgebra de Boole é a base da eletrônica digital e da computação moderna.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xNuqxH4aH4c?si=RLsgOpANethJnQHB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

O sistema de base 2, ou binário, é a base numérica que utiliza apenas dois dígitos: 0 e 1, como dito anteriormente. Mais sobre este sistema pode ser visto em:

<iframe width="560" height="315" src="https://www.youtube.com/embed/eD56zn5kYfU?si=3uw3z2HP2Zry8tmo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

Para realizarmos operações com os números binários, utilizamos a álgebra de Boole. A álgebra de Boole é uma álgebra que trabalha com variáveis lógicas e operadores lógicos. Vamos estudar mais sobre esses elementos a seguir.

### 4.2 Álgebra de Boole e Lógica Combinacional

A álgebra de Boole nos permite realizar operações com variáveis lógicas. Ela pode ser implementada utilizando portas lógicas, que são dispositivos eletrônicos que realizam operações lógicas. As portas lógicas são a base de todos os sistemas digitais.

:::tip[Portas Lógicas]

<iframe width="560" height="315" src="https://www.youtube.com/embed/gI-qXk7XojA?si=Odk2LA0eMGVkurAu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

#### 4.2.1 Funções Lógicas

As funções lógicas são funções que recebem variáveis lógicas como entrada e retornam uma variável lógica como saída. As funções lógicas mais comuns são a função AND, a função OR e a função NOT. Em geral, o comportamento dessas funções é descrito por meio de tabelas verdade. Vamos implementar essas funções lógicas utilizando nosso Raspberry Pi Pico. 

Primeiro vamos analisar o comportamento da funções lógica `AND`. Essa função tem como tabela verdade a seguir e a sua simbologia é apresentada na figura abaixo

| A | B | A AND B |
|---|---|---------|
| 0 | 0 |   0     |
| 0 | 1 |   0     |
| 1 | 0 |   0     |
| 1 | 1 |   1     |

<img src={useBaseUrl("/img/diagramas/and-gate.png")} alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

A função `AND` retorna 1 apenas quando ambas as entradas são 1. Vamos implementar essa função utilizando o Raspberry Pi Pico.

```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoA = Pin(20, Pin.IN, Pin.PULL_UP)
pinoB = Pin(21, Pin.IN, Pin.PULL_UP)
pinoSaida = Pin(10, Pin.OUT)

# Função lógica AND
def AND(a, b):
    return a and b

# Loop principal
while True:
    # Leitura dos pinos
    a = pinoA.value() == VERDADERO
    b = pinoB.value() == VERDADERO

    # Cálculo da função lógica
    saida = AND(a, b)

    # Atualização da saída
    pinoSaida.value(saida)

```
Importante destacar o seguinte, a função `AND` pode ser implementada com mais elementos de entrada. Neste caso, a função `AND` retorna 1 apenas quando todas as entradas são 1. Modifique o programa anterior para trabalhar com 3 entradas no lugar de duas e verifique o comportamento do sistema.

<details> 
  <summary mdxType="summary"> Proposta de Solução [NÃO ABRIR ANTES DE TENTAR!!]</summary>
```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoA = Pin(20, Pin.IN, Pin.PULL_UP)
pinoB = Pin(21, Pin.IN, Pin.PULL_UP)
pinoC = Pin(22, Pin.IN, Pin.PULL_UP)
pinoSaida = Pin(10, Pin.OUT)

# Função lógica AND
def AND(a, b, c):
    return a and b and c

# Loop principal
while True:
    # Leitura dos pinos
    a = pinoA.value() == VERDADERO
    b = pinoB.value() == VERDADERO
    c = pinoC.value() == VERDADERO

    # Cálculo da função lógica
    saida = AND(a, b, c)

    # Atualização da saída
    pinoSaida.value(saida)
```
</details> 

Agora vamos analisar o comportamento da função lógica `OR`. Essa função tem como tabela verdade a descrita a seguir e sua simbologia pode ser vista na figura a seguir.

| A | B | A OR B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

<img src={useBaseUrl("/img/diagramas/or-gate.png")} alt="Simbologia porta OR" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

Podemos observar um comportamento diferente aqui. A função `OR` retorna 1 quando pelo menos uma das entradas é 1. Vamos implementar essa função utilizando o Raspberry Pi Pico.

```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoA = Pin(20, Pin.IN, Pin.PULL_UP)
pinoB = Pin(21, Pin.IN, Pin.PULL_UP)
pinoSaida = Pin(10, Pin.OUT)

# Função lógica OR
def OR(a, b):
    return a or b

# Loop principal
while True:
    # Leitura dos pinos
    a = pinoA.value() == VERDADERO
    b = pinoB.value() == VERDADERO

    # Cálculo da função lógica
    saida = OR(a, b)

    # Atualização da saída
    pinoSaida.value(saida)
```

Assim como a função lógica `AND`, a função `OR` pode ser aplicada em mais entradas, tendo sua saída como verdadeira quando ao menos uma delas for verdadeira. Modifique o programa anterior para implementar a lógica com 3 entradas.

<details> 
  <summary mdxType="summary"> Proposta de Solução [NÃO ABRIR ANTES DE TENTAR!!]</summary>
```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoA = Pin(20, Pin.IN, Pin.PULL_UP)
pinoB = Pin(21, Pin.IN, Pin.PULL_UP)
pinoC = Pin(22, Pin.IN, Pin.PULL_UP)
pinoSaida = Pin(10, Pin.OUT)

# Função lógica AND
def OR(a, b, c):
    return a or b or c

# Loop principal
while True:
    # Leitura dos pinos
    a = pinoA.value() == VERDADERO
    b = pinoB.value() == VERDADERO
    c = pinoC.value() == VERDADERO

    # Cálculo da função lógica
    saida = OR(a, b, c)

    # Atualização da saída
    pinoSaida.value(saida)
```
</details> 

Uma última função lógica que vamos implementar é a função `NOT`. Essa função tem como tabela verdade e simbologia os elementos a seguir:

| A | NOT A |
|---|-------|
| 0 |   1   |
| 1 |   0   |

<img src={useBaseUrl("/img/diagramas/not-gate.png")} alt="Simbologia porta NOT" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

A função `NOT` tem por comportamento inverter o estado de uma entrada. Vamos implementar essa função utilizando o Raspberry Pi Pico.

```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoA = Pin(20, Pin.IN, Pin.PULL_UP)
pinoSaida = Pin(10, Pin.OUT)

# Função lógica OR
def NOT(a):
    return not a

# Loop principal
while True:
    # Leitura dos pinos
    a = pinoA.value() == VERDADERO

    # Cálculo da função lógica
    saida = NOT(a)

    # Atualização da saída
    pinoSaida.value(saida)
```

A função `NOT` pode ser utilizada para inverter o estado de mais elementos. Ela pode ser utilizada em combinação com mais elementos lógicos para criar expressões mais complexas.

:::tip[Portas Lógicas Discretas]

Além do comportamento por software, existem as portas lógicas implementas em circuitos eletrônicos. Eles são chamados de componentes discretos e podem ser utilizados na construção de soluções digitais. Assim como nosso microcontrolador, esses dispositivos possuem seus manuais de referência (também chamados de *datasheets*), que descrevem o que cada circuito faz.

Quando eles vão ser comprados no mercado, eles são identificados por um código, que pode ser consultado no datasheet. Por exemplo, a porta lógica `AND` é identificada pelo código `7408`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/cdMJvFT-Afc?si=Hpm3OF4eNTMbfCJI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

Podemos utilizar os circuitos de forma combinada. Esses circuitos são chamados de circuitos combinacionais. Eles são circuitos que realizam operações lógicas com base nas entradas e retornam um resultado. Vamos implementar um circuito combinacional utilizando o Raspberry Pi Pico.
Analise o circuito a seguir:



<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />