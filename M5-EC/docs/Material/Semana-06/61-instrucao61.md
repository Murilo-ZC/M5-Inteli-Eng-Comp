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

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ7QzRtfMVdi-wrkWaq9PZ4Y3oGru0cpbvgBsrnknn_vCZuVsFOC5hwQ-5a55L42Jni79Z7chUSYp4E/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }}></iframe>


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
pinoC = Pin(19, Pin.IN, Pin.PULL_UP)
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
pinoC = Pin(19, Pin.IN, Pin.PULL_UP)
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

<img src={useBaseUrl("/img/diagramas/circuito-material-combinacional.png")} alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

Avaliando o circuito acima, podemos descrever o seu comportamento utilizando uma expressão booleana. A saída do circuito é dada por:

> S = ((A AND B) OR C) AND (NOT D)

Essa mesma expressão pode ser reescrita utilizando uma notação matemática:

> S = ((A . B) + C) . (!D)

Portanto, podemos verificar o seguinte:
- `Operação AND`: Utilizar o operador `.`
- `Operação OR`: Utilizar o operador `+`
- `Operação NOT`: Utilizar o operador `!`

Agora, para descrever o comportamento deste circuito com a Pico:

```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoA = Pin(21, Pin.IN, Pin.PULL_UP)
pinoB = Pin(20, Pin.IN, Pin.PULL_UP)
pinoC = Pin(19, Pin.IN, Pin.PULL_UP)
pinoD = Pin(18, Pin.IN, Pin.PULL_UP)
pinoSaida = Pin(10, Pin.OUT)

# Função lógica que desejamos implementar
def comportamento(a,b,c,d):
    return ((a and b) or c) and (not d)

while True:
  a = pinoA.value() == VERDADERO
  b = pinoB.value() == VERDADERO
  c = pinoC.value() == VERDADERO
  d = pinoD.value() == VERDADERO

  saida.value(comportamento(a,b,c,d))
```

Podemos fazer o processo inverso, ou seja, a partir de uma expressão booleana, podemos criar um circuito combinacional. Vamos analisar a expressão a seguir:

> S = (!A . B) . (C + D)

Qual será o circuito que implementa essa expressão e o código para ela?

<details> 
  <summary mdxType="summary"> Proposta de Solução - Circuito [NÃO ABRIR ANTES DE TENTAR!!]</summary>
<img src={useBaseUrl("/img/diagramas/circuito-combinacional-2-material.png")} alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />
</details> 

<details> 
  <summary mdxType="summary"> Proposta de Solução - Código [NÃO ABRIR ANTES DE TENTAR!!]</summary>

```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoA = Pin(21, Pin.IN, Pin.PULL_UP)
pinoB = Pin(20, Pin.IN, Pin.PULL_UP)
pinoC = Pin(19, Pin.IN, Pin.PULL_UP)
pinoD = Pin(18, Pin.IN, Pin.PULL_UP)
pinoSaida = Pin(10, Pin.OUT)

# Função lógica que desejamos implementar
def comportamento(a,b,c,d):
    return ((not a) and b) and (c or d)

while True:
  a = pinoA.value() == VERDADERO
  b = pinoB.value() == VERDADERO
  c = pinoC.value() == VERDADERO
  d = pinoD.value() == VERDADERO

  saida.value(comportamento(a,b,c,d))
```

</details> 

Existem outras funções lógicas que valem a pena ser descritas:
- `NAND`: A função `NAND` retorna 0 quando todas as entradas são 1.
- `NOR`: A função `NOR` retorna 0 quando pelo menos uma das entradas é 1.
- `XOR`: A função `XOR` retorna 1 quando as entradas são diferentes. 
- `XNOR`: A função `XNOR` retorna 1 quando as entradas são iguais.

:::tip[Simplificação de Circuitos e Mapas de Karnaugh]

Quando os circuitos eram construídos apenas com componentes discretos, era necessário simplificar as expressões booleanas para que o circuito fosse mais eficiente. Para isso, era utilizado o mapa de Karnaugh. O mapa de Karnaugh é uma ferramenta que permite simplificar expressões booleanas de forma visual.

Para saber mais sobre mapas de Karnough, assista o vídeo a seguir:

<iframe width="560" height="315" src="https://www.youtube.com/embed/RO5alU6PpSU?si=Iujpjs99j6z54c1x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::


### 4.3 Lógica Sequencial

Até esse momento, avaliamos circuitos que realizam operações lógicas com base nas entradas e retornam um resultado. Esses circuitos são chamados de circuitos combinacionais. Agora, vamos avaliar circuitos que possuem memória, ou seja, circuitos que armazenam informações. Esses circuitos são chamados de circuitos sequenciais.

Diferente dos circuitos combinacionais, os circuitos sequenciais possuem um estado interno que é alterado com base nas entradas e no estado atual. Vamos implementar um circuito sequencial utilizando o Raspberry Pi Pico.

Os flip-flops são os elementos básicos dos circuitos sequenciais. Eles são circuitos que possuem dois estados: 0 e 1. Eles possuem uma entrada chamada de `clock` que é responsável por alterar o estado do flip-flop. Existem vários tipos de flip-flops, mas os mais comuns são o flip-flop RS, o flip-flop D, o flip-flop JK e o flip-flop T.

:::tip[Resumo do Funcionamento dos Flip-Flop]

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hi7rK0hZnfc?si=_jRayjt83IrkrtOP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

O Flip-Flop do tipo RS é o elemento mais simples. Ele possui duas entradas: `R` e `S`. Quando `R` é 1 e `S` é 0, o flip-flop é resetado. Quando `R` é 0 e `S` é 1, o flip-flop é setado. Quando `R` e `S` são 0, o flip-flop mantém o seu estado. Vamos implementar um flip-flop RS utilizando o Raspberry Pi Pico.

<img src="https://www.newtoncbraga.com.br/images/stories/artigo2019/cur5006_0005.gif" alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />
<p align="center">Retirado de https://www.newtoncbraga.com.br/images/stories/artigo2019/cur5006_0005.gif</p>

```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoR = Pin(20, Pin.IN, Pin.PULL_UP)
pinoS = Pin(21, Pin.IN, Pin.PULL_UP)
pinoQ = Pin(10, Pin.OUT)
pinoQ_ = Pin(11, Pin.OUT)

# Função lógica que desejamos implementar
def flipflop_rs(r,s):
    if r and not s:
        return 0, 1
    elif not r and s:
        return 1, 0
    else:
        return 0, 0

while True:
  r = pinoR.value() == VERDADERO
  s = pinoS.value() == VERDADERO

  q, q_ = flipflop_rs(r,s)
  pinoQ.value(q)
  pinoQ_.value(q_)

```

Agora vamos adicionar o comportamento de um sinal de `CLOCK` no nosso sistema. O `CLOCK` tem como objetivo alterar o estado do flip-flop. Vamos implementar um flip-flop RS com `CLOCK` utilizando o Raspberry Pi Pico.

```py
from machine import Pin

VERDADERO = 0

# Configuração dos pinos
pinoR = Pin(20, Pin.IN, Pin.PULL_UP)
pinoS = Pin(21, Pin.IN, Pin.PULL_UP)
pinoClock = Pin(19, Pin.IN, Pin.PULL_UP)
pinoQ = Pin(10, Pin.OUT)
pinoQ_ = Pin(11, Pin.OUT)

# Função lógica que desejamos implementar
def flipflop_rs(r,s,clk):
    if clk:
        if r and not s:
            return 0, 1
        elif not r and s:
            return 1, 0
        else:
            return 0, 0
    else:
        return q, q_

while True:
  r = pinoR.value() == VERDADERO
  s = pinoS.value() == VERDADERO
  clk = pinoClock.value() == VERDADERO

  q, q_ = flipflop_rs(r,s,clk)
  pinoQ.value(q)
  pinoQ_.value(q_)

```



<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.4 Material Adicional

Pessoal vamos analisar algumas coisas aqui:

- Como construir diagramas elétricos/eletrônicos utilizando o KiCad
- Como integrar um sensor da Pico com um banco de dados

:::tip[Utilizando o KiCAD]

Pessoal assistam até o minoto 14:00 do vídeo a seguir, para entender como utilizar o KiCAD para criar diagramas elétricos e eletrônicos:

<iframe width="560" height="315" src="https://www.youtube.com/embed/2DAExiW40qM?si=OmpZfE4un_7RcJ5i" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

Vamos utilizar o KiCAD para criar um diagrama elétrico para o nosso projeto. O diagrama elétrico é uma representação gráfica dos componentes e das conexões do circuito. Ele é utilizado para documentar o projeto e para facilitar a montagem do circuito.

Utilizando o KiCAD, vamos criar um diagrama elétrico para ligar as saídas em nosso projeto. Vamos desenvolver um diagrama elétrico para o circuito a seguir:

<img src={useBaseUrl("/img/diagramas/criando-projeto-kicad.png")} alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

Ao selecionar um novo projeto, podemos editar o esquemático. Vamos adicionar os componentes e as conexões do circuito.

<img src={useBaseUrl("/img/diagramas/tela-inicial-kicad.png")} alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

Para adicionar os componentes, vamos selecionar a opção `Adicionar Símbolo`. Vamos adicionar os componentes do nosso circuito. A princípio vamos adicionar um resistor e um LED.

<img src={useBaseUrl("/img/diagramas/adicionar-componentes.png")} alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

Após adicionar os componentes, vamos adicionar as conexões. Para isso, vamos selecionar a opção `Adicionar Fio` e vamos conectar os componentes.

<img src={useBaseUrl("/img/diagramas/circuito-montado.png")} alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

Beleza, agora vamos verificar um outro comportamento do nosso sistema. Vamos integrar um sensor com o nosso banco de dados. Vamos utilizar o TinyDB para armazenar as informações do sensor.

<img src={useBaseUrl("/img/diagramas/pico-adc.png")} alt="Simbologia porta AND" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

Nosso programa vai utilizar o conversor ADC da Pico. Ele é responsável por converter um sinal analógico em um sinal digital. Vamos utilizar o ADC para ler a tensão de um sensor e vamos armazenar essa informação no TinyDB. Nosso sensor vai ser simulado por um potenciômetro.

:::tip[Conversor ADC Raspberry Pi Pico]

Para conhecer mais sobre o conversor ADC.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4XPDyKujcxI?si=cmhnAeSq9FRBP9Pk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

Agora vamos analisar o código para a leitura do sensor.

```py

from machine import ADC, Pin
import time

# Configuração do ADC
adc = ADC(Pin(26))

# Loop principal
while True:
    # Leitura do ADC
    valor = adc.read_u16()

    # Armazenamento do valor no banco de dados
    print({'valor': valor, 'data': time.time()})

    # Aguarda 1 segundo
    time.sleep(1)

```

Vamos compreender esse código:
- `adc = ADC(Pin(26))`: Configura o pino 26 como um pino de entrada analógica.
- `valor = adc.read_u16()`: Realiza a leitura do valor do sensor. Considerando que o sensor é um potenciômetro, o valor lido será um número entre 0 e 65535. Onde o valor 0 representa 0V e o valor 65535 representa 3.3V.

Agora vamos configurar o nosso servidor para fazer a recepção desses dados e armazenar eles no TinyDB. Primeiro vamos criar o ambiente virtual e instalar as bibliotecas necessárias.

```sh
python3 -m venv venv
source venv/bin/activate
pip install flask tinydb
```

```py
from flask import Flask, render_template, request, redirect, json
from tinydb import TinyDB, Query
import time

app = Flask(__name__)
db_data = TinyDB('db.json')

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

@app.route('/', methods=['GET', 'POST'])
def index():
    dados = db_data.all()
    return (dados)

@app.route('/add', methods=['POST'])
def add():
    dados = json.loads(request.json)
    dado = dados['dado']
    ip_send = dados['ip_send']
    timestamp = time.time()
    db_data.insert({'dado': dado, 'ip_send': ip_send, 'timestamp': timestamp})
    return {"status": "ok"}


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
```

Explicando esse código:

- `app = Flask(__name__)`: Cria uma instância do servidor.
- `db_data = TinyDB('db.json')`: Cria um banco de dados para armazenar os dados do sensor.
- `@app.route('/ping', methods=['GET'])`: Cria uma rota para verificar se o servidor está ativo.
- `@app.route('/', methods=['GET', 'POST'])`: Cria uma rota para visualizar os dados do sensor.
- `@app.route('/add', methods=['POST'])`: Cria uma rota para adicionar os dados do sensor no banco de dados.
- `dados = json.loads(request.json)`: Lê os dados enviados pelo sensor.
- `db_data.insert({'dado': dado, 'ip_send': ip_send, 'timestamp': timestamp})`: Armazena os dados no banco de dados.

Vamos explorar esse código durante nossa interação!
