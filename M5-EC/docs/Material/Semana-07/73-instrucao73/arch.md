---
title: Arquitetura de CPUs
sidebar_position: 1
sidebar_class_name: autoestudo
slug: /arch
---

import Admonition from '@theme/Admonition';

# Introdução à arquitetura de CPUs

## 1. Como uma CPU funciona?

<Admonition 
    type="info" 
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/Z5JC9Ve1sfI" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

O ciclo de fetch-execute é o processo fundamental pelo qual uma unidade central
de processamento (CPU) executa instruções em um programa de computador. Esse
ciclo é também conhecido como o ciclo de instrução e é a base para a operação
de qualquer CPU. O ciclo pode ser dividido em várias etapas, que são repetidas
continuamente enquanto o computador está ligado.

### 1.1. Etapas do Ciclo de Fetch-Execute

1. **Fetch (Busca):** Durante esta etapa, a CPU busca a próxima instrução a ser
   executada da memória. A instrução é identificada pelo contador de programa
   (PC), que armazena o endereço da próxima instrução. A instrução é então
   carregada no registrador de instrução (IR) da CPU.

2. **Decode (Decodificação):** Nesta etapa, a CPU decodifica a instrução no IR
   para determinar qual operação deve ser realizada. Isso geralmente envolve a
   análise do opcode (código de operação) da instrução e de quaisquer operandos
   necessários para a execução.

3. **Execute (Execução):** Após a decodificação, a CPU executa a instrução.
   Isso pode envolver uma variedade de operações, como cálculos aritméticos,
   manipulação de dados, controle de fluxo do programa, entre outros.
   Dependendo da instrução, a execução pode envolver o uso de unidades lógicas
   e aritméticas (ALUs), registradores e outras partes da CPU.

4. **Writeback (Escrita):** Em algumas arquiteturas de CPU, após a execução da
   instrução, os resultados são escritos de volta na memória ou em
   registradores. Esta etapa é essencial para atualizar o estado do programa e
   preparar a CPU para a próxima instrução.

### 1.2. Importância do Ciclo de Fetch-Execute

O ciclo de fetch-execute é fundamental para o funcionamento de qualquer
computador moderno. Ele permite que a CPU execute uma sequência de instruções,
o que é a base para a execução de programas e o funcionamento de sistemas
operacionais. A eficiência deste ciclo é crucial para o desempenho geral do
computador, pois determina a velocidade com que as instruções podem ser
processadas.

### 1.3. Otimizações

Com o avanço da tecnologia, várias técnicas de otimização foram desenvolvidas
para melhorar a eficiência do ciclo de fetch-execute. Isso inclui:

- **Pipelining:** Permite que várias instruções sejam processadas
  simultaneamente em diferentes estágios do ciclo, aumentando a taxa de
  execução das instruções.
- **Superscalaridade:** Permite que várias instruções sejam executadas em
  paralelo dentro de um único ciclo de clock.
- **Predição de desvio:** Melhora a eficiência do ciclo ao prever o resultado
  de instruções condicionais e preparar a execução de acordo com essa previsão.

## 2. Modelo Von Neumann

<Admonition 
    type="info" 
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/Ml3-kVYLNr8" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

A arquitetura de Von Neumann é um modelo de design de computador baseado em um
conceito proposto pelo matemático e físico John von Neumann em 1945. Essa
arquitetura é também conhecida como modelo de Von Neumann ou arquitetura de
Princeton. Ela se tornou a base para a maioria dos computadores modernos e se
caracteriza por uma estrutura onde a unidade de processamento e a memória estão
separadas, mas interconectadas.

### 2.1. Características Principais

1. **Memória Única:** Na arquitetura de Von Neumann, tanto os dados quanto as
   instruções do programa são armazenados na mesma memória. Isso contrasta com
   a arquitetura de Harvard, onde a memória de dados e a memória de instruções
   são separadas.

2. **Processamento Sequencial:** As instruções são executadas uma após a outra
   em uma sequência linear. Esse processo é conhecido como o ciclo de
   fetch-execute, que é o coração do funcionamento de uma CPU baseada em Von
   Neumann.

3. **Unidade Central de Processamento (CPU):** A CPU é a principal componente
   do sistema e é responsável pela execução das instruções do programa. Ela
       geralmente inclui uma unidade de controle (UC), uma unidade lógica e
       aritmética (ALU) e um conjunto de registradores.

4. **Barramento de Sistema:** É o meio pelo qual os dados, as instruções e os
   sinais de controle são transferidos entre a CPU, a memória e os dispositivos
   de entrada/saída.

### 2.2. Vantagens da Arquitetura de Von Neumann

- **Simplicidade:** A arquitetura é relativamente simples e fácil de
  implementar, o que facilitou a construção dos primeiros computadores.
- **Flexibilidade:** Os programas podem ser facilmente alterados sem a
  necessidade de modificar o hardware, pois as instruções e os dados são
  armazenados na mesma memória.
- **Universalidade:** A arquitetura é capaz de executar qualquer algoritmo
  computável, desde que haja memória suficiente para armazenar o programa e os
  dados.

### 2.3. Desvantagens da Arquitetura de Von Neumann

- **Gargalo de Von Neumann:** A utilização de uma única memória para dados e
  instruções pode levar a um gargalo, pois a CPU precisa esperar pela leitura
  das instruções e dos dados. Esse problema é agravado pelo fato de que a
  velocidade de acesso à memória é geralmente mais lenta do que a velocidade da
  CPU.
- **Vulnerabilidade a ataques:** Como os dados e as instruções são armazenados
  juntos, há um risco maior de ataques que podem modificar o código do
  programa.


## 3. CISC vs RISC

<Admonition 
    type="info" 
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/g16wZWKcao4" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

RISC (Reduced Instruction Set Computing) e CISC (Complex Instruction Set
Computing) são dois tipos de arquiteturas de processadores que têm abordagens
diferentes na execução de instruções de computador. Cada arquitetura tem suas
próprias vantagens e desvantagens, e a escolha entre elas depende das
necessidades específicas de um sistema computacional.

### 3.1. RISC (Reduced Instruction Set Computing)

RISC é uma arquitetura de processador que utiliza um conjunto reduzido de
instruções simples e de tamanho fixo. As características principais da
arquitetura RISC incluem:

- **Conjunto de instruções simplificado:** RISC tem um número limitado de
  instruções, que são projetadas para serem executadas rapidamente.
- **Instruções de tamanho fixo:** Todas as instruções têm o mesmo tamanho, o
  que simplifica o design do pipeline de execução e melhora a eficiência do
  cache de instruções.
- **Execução em um único ciclo de clock:** A maioria das instruções é projetada
  para ser executada em um único ciclo de clock, o que resulta em um desempenho
  previsível e rápido.
- **Uso intensivo de registradores:** RISC utiliza um grande número de
  registradores para reduzir os acessos à memória, o que aumenta a velocidade
  de execução.

Exemplos de processadores RISC incluem ARM, MIPS e SPARC.

### 3.2. CISC (Complex Instruction Set Computing)

CISC é uma arquitetura de processador que utiliza um conjunto complexo de
instruções, que podem variar em tamanho e número de ciclos de clock necessários
para a execução. As características principais da arquitetura CISC incluem:

- **Conjunto de instruções extenso:** CISC tem um grande número de instruções,
  incluindo instruções complexas que podem realizar várias operações em um
  único comando.
- **Instruções de tamanho variável:** As instruções podem ter tamanhos
  diferentes, o que permite uma maior flexibilidade, mas também complica o
  design do pipeline de execução.
- **Execução em múltiplos ciclos de clock:** Algumas instruções complexas podem
  levar vários ciclos de clock para serem executadas.
- **Menor número de registradores:** CISC geralmente utiliza menos
  registradores, dependendo mais de operações de memória.

Exemplos de processadores CISC incluem a família de processadores Intel x86.

### 3.3. RISC vs CISC: Comparação

- **Desempenho:** RISC geralmente oferece um desempenho mais previsível e
  rápido devido ao seu conjunto simplificado de instruções e execução em um
  único ciclo de clock. CISC pode ter um desempenho superior em certas
  situações devido à sua capacidade de executar operações complexas em uma
  única instrução.
- **Complexidade:** CISC tende a ser mais complexo em termos de design de
  hardware e implementação de software devido ao seu conjunto extenso de
  instruções. RISC é mais simples e mais fácil de implementar.
- **Uso de memória:** RISC pode exigir mais espaço de memória para armazenar
  código devido ao seu conjunto simplificado de instruções, enquanto CISC pode
  ser mais eficiente em termos de uso de memória devido à sua capacidade de
  realizar mais operações por instrução.
- **Aplicações:** RISC é comumente usado em dispositivos móveis e sistemas
  embarcados, onde a eficiência energética e a simplicidade são cruciais. CISC
  é frequentemente usado em computadores de propósito geral, onde a
  flexibilidade e a compatibilidade com software existente são importantes.

## 4. Exemplo: M3 vs i9

<Admonition 
    type="info" 
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/vqs_0W-MSB0" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>
