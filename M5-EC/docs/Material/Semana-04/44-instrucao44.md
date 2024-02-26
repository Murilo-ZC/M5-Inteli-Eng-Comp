---
sidebar_label: "4 - Encontro de Computação"
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instrução de Computação	

Flask e sistema de requisições para controlar o robô

## 1. Objetivos

- Apresentação do microframework Flask e como ele pode ser utilizado para construir uma aplicação Web. 
- Apresentação do conceito de servidor e aplicação Web.
- Desenvolvimento integrado ao robô utilizando Flask e Python.
- Deploy com as ferramentas de teste, no momento.

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
        <summary mdxType="summary"> Web Programming with Flask - Intro to Computer Science - Harvard`s CS50 (2018)</summary>

        - https://www.youtube.com/watch?v=zdgYw-3tzfI
    </details> 
    
  </TabItem>
  <TabItem value="autoestudos-opcionais" label="📔 Autoestudos Opcionais">
     
     <details> 
        <summary mdxType="summary"> Documentação Oficial Flask - Tutorial</summary>

        - https://flask.palletsprojects.com/en/3.0.x/tutorial/
    </details> 

  </TabItem>
  <TabItem value="autoestudos-adicionais" label="📓 Autoestudos Adicionais">
    
    <details> 
        <summary mdxType="summary">	API REST - Live de Python #175</summary>

        - https://www.youtube.com/watch?v=1_nQ5A2HcgU
    </details> 
    <details> 
        <summary mdxType="summary">	Create A Python API in 12 Minutes</summary>

        - https://www.youtube.com/watch?v=zsYIw6RXjfM
    </details> 
    <details> 
        <summary mdxType="summary">	Build APIs with Flask (the right way)</summary>

        - https://www.youtube.com/watch?v=mt-0F_5KvQw
    </details> 
    <details> 
        <summary mdxType="summary">	Blueprints - Flask Tutorial (Part 12)</summary>

        - https://www.youtube.com/watch?v=6Hmo5XabUro
    </details> 
    <details> 
        <summary mdxType="summary">	Organizando nossa Aplicação com Flask Blueprints</summary>

        - https://www.youtube.com/watch?v=EML_F6W_zrU
    </details> 

  </TabItem>
</Tabs>

<!-- <img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} /> -->

## 4. Material de Aula

Pessoal ao longo deste encontro vamos compreender alguns conceitos importantes para o desenvolvimento dos nossos projetos: como construir soluções que possam ser acessadas via web, como criar um servidor e como integrar o robô com a aplicação web. Para isso, vamos passar por alguns conceitos fundamentais para depois iniciarmos a construção da nossa aplicação web, utilizando o microframework Flask.

### 4.1 Conceitos Fundamentais de Aplicações Web

Antes de qualquer outro avanço, vamos fazer um nivelamento sobre aplicações web, o que são, o que comem, como vivem e como podemos construir uma. Primeiro precisamos entender quais são as partes de uma aplicação e sua importância.

Existem diversos tipos de aplicação Web, um dos tipos mais conhecidos são os websites, que são acessados por meio de um navegador. Outros tipos de aplicações web são as APIs, que são acessadas por meio de requisições HTTP e retornam dados em formato JSON ou XML. As aplicações Web são programas que podem ser acessados através de um navegador da web, como o Google Chrome, Mozilla Firefox ou Microsoft Edge. Elas são compostas por diversos elementos que trabalham juntos para fornecer uma experiência interativa ao usuário.

<img src="https://www.appventurez.com/wp-content/uploads/2020/07/web-application-architecture-infographic.jpg" alt="Arquitetura de uma aplicação web simplificada" style={{ display: 'block', marginLeft: 'auto', maxHeight: '60vh', marginRight: 'auto' }} />

Avaliando alguns destes elementos, podemos destacar:

- `Cliente`: O navegador do usuário.
- `Servidor`: O computador que armazena os arquivos da aplicação e processa os pedidos.
- `HTTP`: O protocolo usado para comunicação entre o cliente e o servidor.
- `HTML, CSS e JavaScript`: Linguagens usadas para desenvolver a interface da aplicação, a lógica da aplicação e a interatividade.
- `Banco de dados`: Armazena informações sobre produtos, usuários, pedidos, para citar algumas aplicações.
- `Interface do usuário`: Páginas da aplicação que o usuário visualiza, como a página inicial, a página de produtos e a página de checkout.
- `Lógica da aplicação`: Código que define como a aplicação responde às ações do usuário, como adicionar um produto ao carrinho ou realizar um pedido.
- `Camada de acesso a dados`: Código que interage com o banco de dados para armazenar, recuperar e atualizar informações sobre produtos, usuários e pedidos.

Diferentes aplicações podem ter diferentes arquiteturas, mas a maioria das aplicações web modernas segue uma arquitetura de três camadas, que divide a aplicação em três partes principais: a interface do usuário, a lógica da aplicação e a camada de acesso a dados. Um exemplo de aplicação mais completa pode ser vista na imagem abaixo. Uma explicação mais detalhada sobre a arquitetura de três camadas pode ser vista [aqui](https://www.aalpha.net/blog/web-application-architecture/).

<img src="https://cdn-cjmik.nitrocdn.com/UjszoEMIGzQLBmRYICliaPmdTnvQlovN/assets/images/optimized/rev-22ebbc4/www.aalpha.net/wp-content/uploads/2023/01/Components-of-Web-Application-Architecture.webp" alt="Arquitetura de uma aplicação Web mais completa" style={{ display: 'block', marginLeft: 'auto', maxHeight: '60vh', marginRight: 'auto' }} />

E um resumo sobre a aplicação pode ser vista em:

<iframe width="560" height="315" max-width="724" max-height="600" src="https://www.youtube.com/embed/Sfzo4xm5eX8?si=OHnK6KcQ5OKR6UqP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', marginBottom: '24px'}}></iframe>

:::tip[Diferentes Arquiteturas]

Para conhecer mais sobre diferentes arquiteturas de aplicações:

<iframe width="560" height="315" max-width="724" max-height="600" src="https://www.youtube.com/embed/i53Gi_K3o7I?si=JHwYo3FC_G0gf903" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', marginBottom: '24px'}}></iframe>

:::

Frente a esses conceitos, vamos entender como podemos construir uma aplicação web com Flask, um microframework para Python.

### 4.2 Python Flask

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.3 Construção de uma API com Flask

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.4 Construção de uma aplicação web com Flask

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.5 Deploy da aplicação web

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.6 Integrando aplicação web com banco de dados

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.7 Utilizando *blueprints* para organizar a aplicação

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.8 Integração com o Robô

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />