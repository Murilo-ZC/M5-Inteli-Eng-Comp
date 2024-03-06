---
sidebar_label: "5 - Encontro de Computação"
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instrução de Orientação	

Eletrônica Analógica com Raspberry Pi Pico	

## 1. Objetivos

- Apresentação dos principais elementos de eletrônica analógica, utilizando o Raspberry Pi Pico como dispositivo auxiliar para desenvolver e validar seus funcionamentos.
- Condicionadores de sinal e drivers de potência mais utilizados para acionamento de cargas com sistemas microcontrolados são abordados neste encontro.
- [***NOVO***] Apresentar como programar o Raspberry Pi Pico em Python.

## 2. Slides do Encontro

<!-- <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSG6q7EZA2isyGW3V_1pXMM7IJquzznhrFYcQA0ygtI8Nfv7v7SvdBN_jbO2XuOBN3kg1zpmRzti5Om/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }}></iframe> -->

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

## 3. Material de Autoestudo

:::danger[Acesse a Adalove!]

Esse material NÃO substitui de forma alguma o uso da Adalove. Você DEVE entrar na Adalove com frequência e REGISTRAR O SEU PROGRESSO. Entendeu? Ainda não? Pera aí que vou desenhar:

<img src={useBaseUrl("/img/memes/aviso-adalove.png")} alt="ACESSE A ADALOVE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />

:::

<Tabs>
  <TabItem value="autoestudos-obrigatorios" label="📘 Autoestudos Obrigatórios" default>
     
    <details> 
        <summary mdxType="summary"> Get started with MicroPython on Raspberry Pi Pico</summary>

        - https://hackspace.raspberrypi.com/books/micropython-pico
    </details> 
    
  </TabItem>
  <TabItem value="autoestudos-opcionais" label="📔 Autoestudos Opcionais">
     
    <details> 
        <summary mdxType="summary"> Amplificadores Operacionais</summary>

        - https://www.youtube.com/watch?v=LW_H29iGxXY&list=PLxI8Can9yAHevRkQnSgviIgnzCH3Nss_Y&index=10
    </details>
    <details> 
        <summary mdxType="summary"> Transistor Bipolar de Junção</summary>

        - https://www.youtube.com/watch?v=sRukbJU834o&list=PLxI8Can9yAHevRkQnSgviIgnzCH3Nss_Y&index=4
    </details>
    <details> 
        <summary mdxType="summary"> Polarização de Transistor Bipolar de Junção</summary>

        - https://www.youtube.com/watch?v=_jIOS7YqdcY&list=PLxI8Can9yAHevRkQnSgviIgnzCH3Nss_Y&index=5
    </details>

  </TabItem>
  <TabItem value="autoestudos-adicionais" label="📓 Autoestudos Adicionais">
    
    <details> 
        <summary mdxType="summary">	Aprenda a dar os primeiros passos em Python na sua Raspberry Pi Pico</summary>

        - https://www.youtube.com/watch?v=suFAItbpNBM
    </details> 

  </TabItem>
</Tabs> 


## 4. Material de Aula

O material do encontro será dividido em algumas partes:
- Apresentação da forma de programar o Raspberry Pi Pico em Python;
- Apresentação dos principais elementos de eletrônica analógica;
- Apresentação dos sensores e atuadores mais utilizados em sistemas microcontrolados;
- [***EM BREVE***] Comunicação com o Raspberry Pi Pico via Wifi.

Os elementos que compoem o kit individual de vocês são os seguintes:

<table class="customTable">
  <thead>
    <tr>
      <th>Quantidade</th>
      <th>Descrição</th>
    </tr>
  </thead>
        <tbody>
            <tr>
                <td>Conteúdo da célula 1</td>
                <td>Conteúdo da célula 2</td>
            </tr>
            <tr>
                <td>Outro conteúdo da célula 1</td>
                <td>Outro conteúdo da célula 2</td>
            </tr>
        </tbody>
</table>

### 4.1 Apresentação da forma de programar o Raspberry Pi Pico em Python

Bem vindo ao incrível mundo de programação de dispositivos embarcados!!! Diversos de vocês já possuem conhecimento sobre este assunto, mas para deixar todos nivelados, vamos passar por alguns conceitos básicos de acordo com a necessidade do assunto.

O microcontrolador que vamos utilizar é a Raspberry Pi Pico. Ela é diferente de uma Raspberry Pi convencional, pois não é um computador completo, mas sim um microcontrolador. A Raspberry Pi Pico é baseada no microcontrolador RP2040, que é um microcontrolador de baixo custo e alto desempenho.

:::tip[Microcontrolador]

Um microcontrolador é um dispositivo compacto, de único chip, que é projetado para executar operações específicas em sistemas embarcados e dispositivos eletrônicos. Ele combina várias funções de um computador tradicional em um pequeno pacote, incluindo uma unidade central de processamento (CPU), memória (tanto RAM quanto ROM), e periféricos de entrada/saída (I/O) em um único circuito integrado.

Microcontroladores são amplamente utilizados em uma variedade de aplicações devido à sua eficiência, baixo custo, e versatilidade. Eles podem ser encontrados em eletrodomésticos, sistemas de controle automotivo, dispositivos médicos, brinquedos, gadgets, e muitos outros produtos que requerem controle automatizado ou interatividade com o usuário.

Diferentemente dos microprocessadores, que são o cérebro de PCs e requerem vários outros chips para fornecer memória e interfaces de I/O, os microcontroladores são projetados para serem autossuficientes e eficientes em termos de energia, o que os torna ideais para aplicações onde o espaço e o consumo de energia são limitados. Eles são programados para realizar tarefas específicas — como coletar dados de sensores, controlar motores, ou operar displays — de maneira autônoma ou como parte de um sistema maior.

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/peLH-HNza44?si=yKpkbm9iWjlN6yxd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

:::

A Raspberry Pi Pico pode ser programa em C/C++ ou em Python. Neste encontro, vamos focar em programação em Python. A Raspberry Pi Pico é programada utilizando um ambiente de desenvolvimento chamado [Thonny](https://thonny.org/). O Thonny é um IDE (Integrated Development Environment) que é utilizado para programar em Python. Como em outros microcontroladores, a Raspberry Pi Pico possui um bootloader que permite que o código seja carregado para o microcontrolador através de uma porta USB.

:::tip[Bootloader]

O bootloader de um microcontrolador é um pequeno programa cuja principal função é permitir a atualização ou a modificação do software (firmware) executado pelo dispositivo, sem a necessidade de um programador de chips externo. Quando um microcontrolador é inicializado ou reinicializado, o bootloader é o primeiro código a ser executado antes de passar o controle para o programa principal (firmware) do dispositivo.

O processo de funcionamento típico de um bootloader começa no momento da inicialização do microcontrolador, onde ele primeiro verifica se há algum comando ou sinal específico (como uma entrada de hardware ou uma mensagem através de uma interface de comunicação) indicando que o firmware deve ser atualizado ou reprogramado. Se tal comando é detectado, o bootloader ativa um modo de programação, onde recebe o novo firmware, geralmente via interfaces como USB, UART, SPI, ou I2C, e o grava na memória flash do microcontrolador. Após a atualização do firmware, ou se nenhum comando de atualização é recebido, o bootloader então passa o controle para o programa principal armazenado na memória do microcontrolador, permitindo que ele execute suas funções designadas.

Bootloaders são essenciais para sistemas embarcados e dispositivos IoT (Internet das Coisas), pois facilitam a atualização remota do firmware, o que é crucial para correção de bugs, atualizações de segurança, ou adição de novas funcionalidades ao dispositivo sem a necessidade de intervenção física direta. Isso contribui significativamente para a flexibilidade, escalabilidade e manutenção de dispositivos embarcados em campo.

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/Jcan8YfLfLs?si=aaLasaabsWi537Rs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/XpFsMB6FoOs?si=6OWflPMeXEbwIG7a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

:::

A programação em Python é feita utilizando a biblioteca MicroPython. MicroPython é uma implementação do Python 3, otimizado para microcontroladores e sistemas embarcados. Ele é um interpretador de Python que roda diretamente no microcontrolador, permitindo que você escreva e execute scripts Python para controlar dispositivos e interagir com o mundo físico.

Primeiro vamos abrir o Thonny e verificar se a Raspberry Pi Pico está conectada. Para isso, conecte a Raspberry Pi Pico na porta USB do seu computador. Abra o Thonny e clique em "Ver" -> "Mostrar Shell". No shell, digite `import os` e pressione Enter. Se a Raspberry Pi Pico estiver conectada, o shell não retornará erro. Caso contrário, verifique se a Raspberry Pi Pico está conectada corretamente e se o Thonny está configurado corretamente.

<img src={useBaseUrl("img/thonny-python/escolhendo-raspberrypipico.png")} alt="Requisição para a rota /echo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

:::danger[Atenção]

Em alguns casos, a Raspberry Pi Pico pode não ser reconhecida pelo Thonny. Neste caso, você pode tentar instalar o driver da Raspberry Pi Pico. O driver pode ser baixado [aqui](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html).

Além disso, pode ser necessário reinstalar o firmware da Raspberry Pi Pico. O firmware pode ser baixado [aqui](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#resetting-flash-memory).

:::

Ok, agora temos nossa Raspberry Pi Pico conectada no nosso computador, podemos iniciar o processo de testar e utilizar o dispositivo 🤖🐶☕!

Na figura abaixo, temos o diagrama chamado de `pinout` da Raspberry Pi Pico regular, modelo sem Wifi.

<img src={useBaseUrl("img/diagramas/pico-regular-pinout.svg")} alt="Raspberry Pi Pico Regular Pinout" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

Já na figura abaixo podemos ver o `pinout` da Raspberry Pi Pico com Wifi, ***Raspberry Pi Pico W***. Este é o modelo que temos no laboratório.

<img src={useBaseUrl("img/diagramas/picow-pinout.svg")} alt="Raspberry Pi Pico Regular Pinout" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.2 Apresentação dos principais elementos de eletrônica analógica

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.3 Apresentação dos sensores e atuadores mais utilizados em sistemas microcontrolados

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.4 Comunicação com o Raspberry Pi Pico via Wifi

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />