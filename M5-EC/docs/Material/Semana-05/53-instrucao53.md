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
                <td>1x</td>
                <td>Mini Protoboard</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>Cabo Micro USB</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>Raspberry Pi Pico W</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>Sensor Ultrassônico</td>
            </tr>
            <tr>
                <td>2x</td>
                <td>TCRT5000</td>
            </tr>
            <tr>
                <td>4x</td>
                <td>Botões tipo Microswitch</td>
            </tr>
            <tr>
                <td>4x</td>
                <td>LEDs (Vermelho, Azul, Verde e Amarelo)</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>Módulo Relé</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>Buzzer</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>LDR</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>Transistor BC558</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>Potênciometro</td>
            </tr>
            <tr>
                <td>1x</td>
                <td>LED RGB</td>
            </tr>
            <tr>
                <td>8x</td>
                <td>Resistores de 10k Ohms</td>
            </tr>
            <tr>
                <td>8x</td>
                <td>Resistores de 330 Ohms</td>
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


:::tip[MicroPython]

Pessoal alguns Raspberry Pi Pico vem sem o MicroPython instalado. Se vocês tiverem problemas para rodar o código, vocês podem instalar o MicroPython na Raspberry Pi Pico. O processo de instalação do MicroPython na Raspberry Pi Pico pode ser encontrado [aqui](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython).
<img src="https://www.raspberrypi.com/documentation/microcontrollers/images/MicroPython-640x360-v2.gif" alt="processo de reset e gravacao micropython" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />
<p align="center"> Fonte: https://www.raspberrypi.com/</p>

:::

Na figura abaixo, temos o diagrama chamado de `pinout` da Raspberry Pi Pico regular, modelo sem Wifi.

<img src={useBaseUrl("img/diagramas/pico-regular-pinout.svg")} alt="Raspberry Pi Pico Regular Pinout" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

Já na figura abaixo podemos ver o `pinout` da Raspberry Pi Pico com Wifi, ***Raspberry Pi Pico W***. Este é o modelo que temos no laboratório.

<img src={useBaseUrl("img/diagramas/picow-pinout.svg")} alt="Raspberry Pi Pico Regular Pinout" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

Pronto, agora que temos a Pico conectada e o Thonny configurado, podemos começar a programar a Raspberry Pi Pico em Python. Vamos começar com um exemplo simples, acender um LED. Para isso, conecte um LED no pino 25 da Raspberry Pi Pico. Abra o Thonny e digite o código abaixo:

```python
from machine import Pin
import time

led = Pin(25, Pin.OUT)

led.value(1)
time.sleep(1)
led.value(0)
time.sleep(1)
```

Após digitar o código, clique em "Executar" e veja o LED acender e apagar. Parabéns, você acabou de programar a Raspberry Pi Pico em Python 🎉🎉🎉!

Vamos avaliar algumas coisas no nosso código:

- `from machine import Pin`: Importa a classe `Pin` do módulo `machine`. A classe `Pin` é utilizada para controlar os pinos da Raspberry Pi Pico. ***IMPORTANTE***: Utilizar o pino informado é do `GP` e não o número do pino!
- `led = Pin(25, Pin.OUT)`: Cria um objeto `led` que representa o GP25 da Raspberry Pi Pico. O segundo argumento `Pin.OUT` informa que o pino será utilizado como saída.
- `led.value(1)`: Define o valor do GP25 como 1, ou seja, liga o LED.
- `time.sleep(1)`: Espera 1 segundo.
- `led.value(0)`: Define o valor do GP25 como 0, ou seja, desliga o LED.
- `time.sleep(1)`: Espera 1 segundo.

Agora que vocês já sabem como programar a Raspberry Pi Pico em Python, vamos para alguns pontos de avaliação:

- Como vocês podem alterar o código para que ele fique rodando de forma indefinida?
- Como corrigir o erro que aparece quando o código é interrompido?
- Como controlar um outro LED externo?

Esses são alguns problemas iniciais ineressantes para iniciar o processo de desenvolvimento com a Pico.
Agora vamos avaliar alguns conceitos sobre eletrônica e eletricidade.

### 4.2 Apresentação dos principais elementos de eletrônica analógica

Enquanto estamos trabalhando com alguns conceitos importantes da eletrônica analógica, vamos primeiro definir o que é eletrônica analógica.
A eletrônica analógica é um ramo da eletrônica que lida com a manipulação e processamento de sinais analógicos. Os sinais analógicos são contínuos por natureza, o que significa que podem assumir infinitos valores dentro de um determinado intervalo. A eletrônica analógica utiliza componentes eletrônicos básicos, como resistores, capacitores, indutores, diodos e transistores, para projetar e construir circuitos que possam processar, amplificar, filtrar ou converter esses sinais.

O diodo é um componente eletrônico que permite a passagem de corrente elétrica em apenas um sentido. O diodo é um componente que possui dois terminais, chamados de ânodo e cátodo. O ânodo é o terminal positivo e o cátodo é o terminal negativo. A figura abaixo mostra o símbolo do diodo. Ele é utilizado para retificar sinais, ou seja, converter sinais alternados em sinais contínuos. Também pode ser utilizado como um componente de proteção contra inversão de polaridade.
Para que o diodo possa conduzir corrente, a tensão no ânodo deve ser maior que a tensão no cátodo. A tensão necessária para que o diodo comece a conduzir corrente é chamada de tensão de condução. A tensão de condução de um diodo de silício é de aproximadamente 0.7V.

<img src="https://dam-assets.fluke.com/s3fs-public/6004284b-dmm-how-to-diode-715x360-2.jpg" alt="Diodo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />
<p align="center"> Fonte: https://dam-assets.fluke.com/s3fs-public/6004284b-dmm-how-to-diode-715x360-2.jpg</p>

:::tip[Diodos]

<iframe width="560" height="315" src="https://www.youtube.com/embed/-SSkjWuUri4?si=OqKHbWRTCzDLKizC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

O LED é um tipo de diodo que emite luz quando conduz corrente. O LED é um componente que possui dois terminais, chamados de ânodo e cátodo. O ânodo é o terminal positivo e o cátodo é o terminal negativo. A figura abaixo mostra o símbolo do LED. O LED é utilizado para indicar o estado de um circuito, como por exemplo, se um circuito está ligado ou desligado.
Para emiti luz, a tensão no ânodo deve ser maior que a tensão no cátodo. A tensão necessária para que o LED comece a emitir luz é chamada de tensão de condução. A tensão de condução de um LED de silício é de aproximadamente 1.7V. Em geral, para LED's pequenos de 5mm, a corrente necessária para que ele conduza é de 10 mA.

<img src="https://lh3.googleusercontent.com/proxy/GLhp3kzclprKBOJmbBn6xRYy5POMLa-OKHeTGXzrTYTjuGYIvEjUBA5Uif4rg2wVWiln-y6luK02M5cVgfO2bHlfEQ2r_p7bq9U" alt="Diodo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />
<p align="center"> Fonte: https://lh3.googleusercontent.com/proxy/GLhp3kzclprKBOJmbBn6xRYy5POMLa-OKHeTGXzrTYTjuGYIvEjUBA5Uif4rg2wVWiln-y6luK02M5cVgfO2bHlfEQ2r_p7bq9U</p>

:::tip[LED]

<iframe width="560" height="315" src="https://www.youtube.com/embed/otyFC5sJI-E?si=F7jYBrDAv8pOEhWv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

O transistor é um componente eletrônico que pode ser utilizado para amplificar sinais ou para controlar a passagem de corrente. O transistor é um componente que possui três terminais, chamados de emissor, base e coletor. A figura abaixo mostra o símbolo do transistor. O transistor é utilizado para amplificar sinais, ou seja, aumentar a amplitude de um sinal. O transistor também pode ser utilizado para controlar a passagem de corrente, ou seja, ligar ou desligar um circuito.
Em geral, existem dois tipos de transistores: o transistor bipolar de junção (BJT) e o transistor de efeito de campo (FET). O transistor BJT é um tipo de transistor que é controlado pela corrente que passa pela base. O transistor FET é um tipo de transistor que é controlado pela tensão aplicada no gate.
Para os BJT, a corrente que passa pela base controla a corrente que passa pelo coletor. A corrente que passa pela base é multiplicada por um fator chamado de ganho de corrente. O ganho de corrente é um valor que varia de acordo com o transistor e com a corrente que passa pela base. Em geral, o ganho de corrente de um transistor BJT é da ordem de 100.

<img src="https://upload.wikimedia.org/wikipedia/commons/f/f8/Transistor-photo.JPG" alt="Diodo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />
<p align="center"> Fonte: https://upload.wikimedia.org/wikipedia/commons/f/f8/Transistor-photo.JPG</p>

Os transistores BJT podem ser do tipo NPN ou PNP. O transistor BJT NPN é um tipo de transistor que é formado por duas junções PN, sendo que a junção do meio é do tipo P e as junções das extremidades são do tipo N. O transistor BJT PNP é um tipo de transistor que é formado por duas junções PN, sendo que a junção do meio é do tipo N e as junções das extremidades são do tipo P. A figura abaixo mostra o símbolo do transistor BJT NPN e do transistor BJT PNP.

<img src="https://i0.wp.com/eltgeral.com.br/wp-content/uploads/2021/09/Transistor_Junction.png?resize=575%2C335&ssl=1" alt="Diodo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />
<p align="center"> Fonte: https://i0.wp.com/eltgeral.com.br/wp-content/uploads/2021/09/Transistor_Junction.png?resize=575%2C335&ssl=1</p>

:::tip[Transistores]

<iframe width="560" height="315" src="https://www.youtube.com/embed/R0Uy4EL4xWs?si=xvjpzdQ_ywAeKWpC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/wNiXUZIHQLw?si=LIuqKy_to24wfDfs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

O amplificador operacional é um componente eletrônico que pode ser utilizado para amplificar sinais ou para realizar operações matemáticas. O amplificador operacional é um componente que possui dois terminais de entrada, chamados de terminal inversor e terminal não inversor, e um terminal de saída. A figura abaixo mostra o símbolo do amplificador operacional. O amplificador operacional é utilizado para amplificar sinais, ou seja, aumentar a amplitude de um sinal. O amplificador operacional também pode ser utilizado para realizar operações matemáticas, como por exemplo, somar, subtrair, multiplicar e dividir sinais.

<img src="https://www.manualdaeletronica.com.br/y/432/Amplificador-operacional.jpg" alt="Diodo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />
<p align="center"> Fonte: https://www.manualdaeletronica.com.br/y/432/Amplificador-operacional.jpg</p>

:::tip[Amplificador Operacional]

Para saber mais sobre amplificadores operacionais:

<iframe width="560" height="315" src="https://www.youtube.com/embed/kbVqTMy8HMg?si=PsMKpRHzoTuppQUg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

### 4.3 Apresentação dos sensores e atuadores mais utilizados em sistemas microcontrolados

Nesta seção vamos discultir os principais sensores que podem ser utilizados em sistemas microcontrolados e como alguns deles podem ser ligados junto da Pico. Vale destacar que os códigos aqui apresentados tem por objetivo auxiliar no processo de criação e desenvolvimento de sistemas embarcados. Eles podem e devem ser melhorados para atender as necessidades do projeto.

#### 4.3.1 Chave de Botão

A chave de botão é um dos componentes mais simples e mais utilizados em sistemas microcontrolados. Ela é utilizada para acionar um sinal digital quando pressionada. A chave de botão é um componente que possui 4 terminais, sendo que dois deles são conectados internamente. Quando a chave é pressionada, os terminais que estão conectados internamente são conectados com os terminais que estão soltos. A figura abaixo mostra o símbolo da chave de botão.
Vamos avaliar o código abaixo:

```python
from machine import Pin
import time

botao = Pin(25, Pin.IN, Pin.PULL_UP)

while True:
    if botao.value() == 0:
        print("Botão pressionado")
    else:
        print("Botão solto")
    time.sleep(1)
```

Vamos analisar o código anterior:
- `from machine import Pin`: Importa a classe `Pin` do módulo `machine`. A classe `Pin` é utilizada para controlar os pinos da Raspberry Pi Pico.
- `botao = Pin(25, Pin.IN, Pin.PULL_UP)`: Cria um objeto `botao` que representa o GP25 da Raspberry Pi Pico. O segundo argumento `Pin.IN` informa que o pino será utilizado como entrada. O terceiro argumento `Pin.PULL_UP` informa que o pino está configurado como `PULL_UP`, ou seja, ele está configurado para receber um sinal de 0V quando acionado.
- `while True:`: Loop infinito.
- `if botao.value() == 0:`: Verifica se o GP25 está com o valor 0. Se sim, imprime "Botão pressionado". Se não, imprime "Botão solto".
- `time.sleep(1)`: Espera 1 segundo.

#### 4.3.2 Sensor de Luz - LDR

O LDR (Light Dependent Resistor) é um sensor que varia sua resistência de acordo com a luz que incide sobre ele. Quanto mais luz incide sobre o LDR, menor é a sua resistência. O LDR é um componente que possui 2 terminais.
Em geral, para ler os sinais de um LDR, nós devemos construir um divisor de tensão com um resistor, em geral de 10k Ohms. A figura abaixo mostra o símbolo do LDR e o circuito que deve ser montado para ler o sinal do LDR.

<img src="https://www.facom.ufu.br/~jamil/eletronica/divisores_tensao/15_05_04.gif" alt="Divisor de Tensão com LDR" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />
<p align="center"> Fonte: https://www.facom.ufu.br/~jamil/eletronica/divisores_tensao/15_05_04.gif</p>

O divisor de tensão é um circuito que é utilizado para dividir a tensão de um sinal. O circuito é composto por dois resistores, um deles é o LDR. A tensão de saída do divisor de tensão é dada pela fórmula:

V_out = V_in * (R_2)/(R_1 + R_2)

:::tip[Divisor de Tensão]

Para saber mais sobre divisores de tensão, acesse o link [aqui](https://embarcados.com.br/divisor-de-tensao/).

:::

Vamos avaliar o código abaixo:

```python
from machine import Pin, ADC
import time

ldr = ADC(Pin(26))

while True:
    print(ldr.read_u16())
    time.sleep(1)
```

Vamos analisar o código anterior:

- `from machine import Pin, ADC`: Importa as classes `Pin` e `ADC` do módulo `machine`. A classe `Pin` é utilizada para controlar os pinos da Raspberry Pi Pico. A classe `ADC` é utilizada para ler sinais analógicos.
- `ldr = ADC(Pin(26))`: Cria um objeto `ldr` que representa o GP26 da Raspberry Pi Pico. O objeto `ldr` é um objeto da classe `ADC` que é utilizado para ler sinais analógicos.
- `while True:`: Loop infinito.
- `print(ldr.read_u16())`: Lê o sinal analógico do GP26 e imprime o valor lido.
- `time.sleep(1)`: Espera 1 segundo.

Entrada analógica é uma entrada especial que pode ler sinais de tensão entre 0V e 3.3V. A entrada analógica da Raspberry Pi Pico é de 12 bits, ou seja, ela pode ler sinais de tensão entre 0V e 3.3V e converter esses sinais em valores entre 0 e 4095.
Cada bit a mais em um conversor analógico-digital dobra a resolução do conversor. A resolução é a menor diferença de tensão que o conversor pode detectar. A resolução de um conversor analógico-digital de 12 bits é de 3.3V/4096 = 0.0008V = 0.8mV.

:::tip[Conversor ADC]

Para saber mais sobre os conversores ADC, acesse o link [aqui](https://embarcados.com.br/conversor-a-d/).

:::


### 4.4 Comunicação com o Raspberry Pi Pico via Wifi

Vamos trabalhar com nossa Pico se conectando em uma rede específica e depois consultando algumas API's para buscar informações.
Primeiro, vamos conectar a Pico na rede Wifi. Para isso, vamos utilizar o código abaixo:

```python
import network
import time
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NOME_DA_REDE', 'SENHA_DA_REDE')
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

print(wlan.ifconfig())

```

Este primeiro programa tem por objetivo conectar a Pico em uma rede Wifi conhecida. Para isso, utilizamos a biblioteca `network` e a classe `WLAN`. A classe `WLAN` possui um método chamado `connect` que recebe como argumento o nome da rede e a senha. Após a conexão, o método `ifconfig` retorna o IP da Pico na rede.
Desta forma, já temos nossa Pico conectada na rede Wifi. Agora podemos fazer requisições HTTP para buscar informações.

```python
import urequests
import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NOME_DA_REDE', 'SENHA_DA_REDE')
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
  
response = urequests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(response.json())
```

Nessa versão do nosso código, primeiro conectamos a Pico na rede Wifi. Após a conexão, utilizamos a biblioteca `urequests` para fazer uma requisição HTTP para a API do Coindesk. A API do Coindesk retorna o preço do Bitcoin em dólares. O método `get` da classe `urequests` recebe como argumento a URL da API. O método `json` retorna o JSON retornado pela API.
Podemos utilizar uma integração da requisição em conjunto com uma ação do usuário, como o acionamento de um sensor, por exemplo. 

```python
import network
import urequests
import time
from machine import Pin

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NOME_DA_REDE', 'SENHA_DA_REDE')
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

entrada = Pin(25,Pin.IN, Pin.PULL_UP)

try:
    if entrada.value() == 0:
        response = urequests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature')
        print(response.json())
        time.sleep(4)
except:
    print("Programa Encerrado")

```

Vamos avaliar os pontos de atenção do código:

- Primeiro fazemos que nosso código se conecte na rede Wifi;
- Depois, definimos que a variável `entrada` é o GP25 da Pico, que será utilizado como entrada. ***IMPORTANTE***: essa entrada é configurada como `PULL_UP`, ou seja, ela está configurada para receber um sinal de 0V quando acionada;
- A estrutura `try-except` é utilizada para que se algum erro acontecer ou ainda se o programa for interrompido, o programa não pare de funcionar;
- Dentro do bloco `try`, verificamos se o GP25 está com o valor 0. Se sim, fazemos uma requisição para a API do Open Meteo para buscar a temperatura atual em Berlim.

Desta forma já conseguimos realizar requisições HTTP com a Pico. Agora, vamos avaliar algumas coisas:

- Como fazer a Pico se conectar em uma rede Wifi desconhecida?
- Como fazer a Pico enviar dados em uma rede local?
- É possível realizar requisições HTTPS com a Pico?
- É possível realizar requisições POST com a Pico?

### 4.5 Hardware Adicional para Instrução de Eletrônica Digital

Para a instrução de eletrônica digital, vamos utilizar o seguinte hardware adicional:

<img src={useBaseUrl("/img/diagrama-montagem-digital.png")} alt="ACESSE A ADALOVE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />

O que temos montado aqui:

- 4 entradas digitais, que serão ligadas utilizando o GP18 à GP21;
- 4 saídas digitais, que serão ligadas utilizando o GP10 à GP13.

Esse é o hardware mínimo para nosso encontro de eletrônica digital. Tentem trazer todos os componentes montados para o encontro!

Quem tiver alguma dificuldade, pode entrar em contato comigo para que possamos resolver o problema durante o autoestudo.

Para testar se todo o hardware está funcionando corretamente, vamos utilizar o código abaixo:

```python
from machine import Pin

entrada1 = Pin(18, Pin.IN, Pin.PULL_UP)
entrada2 = Pin(19, Pin.IN, Pin.PULL_UP)
entrada3 = Pin(20, Pin.IN, Pin.PULL_UP)
entrada4 = Pin(21, Pin.IN, Pin.PULL_UP)

saida1 = Pin(10, Pin.OUT)
saida2 = Pin(11, Pin.OUT)
saida3 = Pin(12, Pin.OUT)
saida4 = Pin(13, Pin.OUT)

while True:
    saida1.value(not entrada1.value())
    saida2.value(not entrada1.value())
    saida3.value(not entrada1.value())
    saida4.value(not entrada1.value())
```