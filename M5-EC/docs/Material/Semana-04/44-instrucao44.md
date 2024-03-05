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

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT4K4qOqIDmGUqZRqKL3DsPLIZMmw7dulqaaeAO2O0O-D6BN3WcS4C4TgRzep0Oun_2WTLRIkIrsdfC/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }}></iframe>

<!-- <img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} /> -->

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

Para construir uma aplicação web, precisamos de um servidor que possa receber requisições e retornar respostas. O Flask é um microframework para Python que nos permite construir aplicações web de forma rápida e fácil. Ele é um dos frameworks mais populares para construção de aplicações web em Python, e é utilizado por empresas como Netflix, Reddit, Lyft, entre outras.

O Python em conjunto com nossa aplicação Flask é executada no servidor, que é um computador que armazena os arquivos da aplicação e processa os pedidos. O servidor é responsável por receber as requisições dos clientes, processar essas requisições e retornar respostas. O servidor é um programa que executa continuamente, aguardando por requisições e respondendo a elas.

O Flask é um microframework, o que significa que ele é um framework minimalista que fornece apenas o essencial para construir uma aplicação web. Ele é fácil de aprender e usar, e é uma ótima opção para construir aplicações web pequenas e médias. O Flask é extensível, o que significa que podemos adicionar funcionalidades adicionais através de extensões, que são pacotes de código que estendem as funcionalidades do Flask. Para conhecer mais sobre o Flask, acesse a [documentação oficial](https://flask.palletsprojects.com/en/latest/).

Para utilizarmos o Flask, vamos primeiro criar um ambiente virtual para nossa aplicação. Os arquivos de uma aplicação Flask são organizados de forma que possamos separar a lógica da aplicação em diferentes arquivos. Todo nosso código será desenvolvido em [`src/encontro-4-computacao`](#).

Primeiro vamos instalar o Flask em nosso ambiente virtual. Para isso, vamos utilizar o comando `pip install flask`. Após a instalação, vamos criar um arquivo chamado `src/encontro-4-computacao/ola-flask.py` e adicionar o seguinte código:

```python
# ola-flask.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Ola Mundo!!</p>"
```

Agora com nossa aplicação salva, vamos executar nossa aplicação: `python3 -m flask --app ola-flask run`. Vamos obter a seguinte saída no terminal:

```bash
 * Serving Flask app 'ola-flask'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Ao acessar o endereço apresentado no terminal, vamos conseguir ver a imagem "Ola Mundo!!" no navegador. Com isso, conseguimos criar nossa primeira aplicação web com Flask.

:::danger[Atenção]

Até aqui pessoal, fizemos bastante coisa, mas vamos passar por cada um dos passos para compreender o que aconteceu. Se você está com dúvidas, não se preocupe, vamos passar por cada um dos passos para compreender o que aconteceu.

<img src="https://media1.tenor.com/m/WgoifA87r5AAAAAC/mashle-mash-burnedead.gif" alt="Mashle Confused" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto', marginBottom: '24px'}} />

:::

Agora vamos compreender o que aconteceu aqui!

Primeiro, nosso arquivo fonte. O arquivo `ola-flask.py` é um arquivo Python que contém o código da nossa aplicação. Neste arquivo, importamos a classe `Flask` do módulo `flask` e criamos uma instância da classe `Flask` chamada `app`. A instância da classe `Flask` representa a nossa aplicação web. Em seguida, utilizamos o decorador `@app.route("/")` para associar a função `hello_world` com a rota `/`. O decorador `@app.route("/")` é uma forma de associar uma função com uma rota. Quando um cliente acessa a rota `/`, a função `hello_world` é executada e retorna a string "Ola Mundo!!".

O objeto `app` é um objeto especial nas aplicações Python. Ele é responsável por configurar a aplicação e gerenciar as requisições e respostas. O objeto `app` possui diversos métodos e atributos que nos permitem configurar a aplicação e adicionar funcionalidades adicionais. O método `app.run()` é utilizado para executar a aplicação. Ele inicia um servidor de desenvolvimento que aguarda por requisições e responde a elas. Outra características bastante importante é que o `app` de Flask é um singleton, ou seja, ele é único e compartilhado por toda a aplicação. Para conhecer mais sobre o padrão Singleton, acesse [aqui](https://refactoring.guru/pt-br/design-patterns/singleton).

Agora para executar nossa aplicação, utilizamos o comando `python3 -m flask --app ola-flask run`. O comando `python3 -m flask` é utilizado para executar o Flask. O argumento `--app ola-flask` é utilizado para especificar o nome do arquivo que contém a aplicação. O argumento `run` é utilizado para iniciar o servidor de desenvolvimento. O servidor de desenvolvimento é um servidor que aguarda por requisições e responde a elas. Ele é utilizado para testar a aplicação durante o desenvolvimento. O servidor de desenvolvimento é executado no endereço `http://120.0.0.0:5000`.

:::tip[Modo de Desenvolvimento]

Podemos alterar a porta onde o servidor de desenvolvimento é executado utilizando o argumento `--port`. Por exemplo, para executar o servidor de desenvolvimento na porta 8000, utilizamos o comando `python3 -m flask --app ola-flask run --port 8000`.

Podemos também expor a aplicação para os outros elementos da rede, utilizando o argumento `--host`. Por exemplo, para expor a aplicação para os outros elementos da rede, utilizamos o comando `python3 -m flask --app ola-flask run --host 0.0.0.0`.

:::

Quando nosso servidor recebeu a requisição, ele executou a função `hello_world` e retornou a string "Ola Mundo!!". O servidor de desenvolvimento é um servidor que aguarda por requisições e responde a elas. 

:::danger[APENAS PARA DESENVOLVIMENTO]

Cuidado pessoal, o servidor de desenvolvimento é utilizado apenas para testar a aplicação durante o desenvolvimento. Ele não é adequado para uso em produção. Para implantar a aplicação em produção, utilizamos um servidor WSGI, como o Gunicorn ou o uWSGI. Para conhecer mais sobre o Gunicorn, acesse [aqui](https://gunicorn.org/).

Dizemos que uma aplicação vai para `produção`, quando ela está pronta para ser utilizada por usuários finais. A aplicação em produção é executada em um servidor de produção, que é um servidor que está configurado para executar a aplicação de forma segura e eficiente. O servidor de produção é utilizado para atender as requisições dos usuários finais e fornecer uma experiência interativa ao usuário.

:::

Agora vamos ajustar nossa aplicação para que ela se comporte como uma API, ou seja, que ela possa receber requisições e retornar respostas em formato padronizado.

### 4.3 Construção de uma API com Flask

Uma API Web, ou API RESTful, é um conjunto de definições e protocolos que permitem a comunicação entre diferentes sistemas através da web. Ela funciona como um intermediário, possibilitando que um sistema (cliente) solicite dados ou execute ações em outro sistema (servidor) de forma padronizada e segura.

1. `O cliente faz uma requisição`: O cliente envia uma requisição para a API, geralmente através do protocolo HTTP. A requisição especifica o método desejado (GET, POST, PUT, DELETE), o endpoint da API e os dados da requisição.
2. `A API processa a requisição`: A API recebe a requisição e a processa de acordo com o método especificado. Ela pode acessar um banco de dados, executar um script ou realizar qualquer outra operação necessária.
3. `A API retorna uma resposta`: A API retorna uma resposta para o cliente, geralmente em formato JSON ou XML. A resposta pode conter dados, mensagens de erro ou outros resultados da operação.

Agora vamos ajustar nossa aplicação para que ela se comporte como uma API. Para isso, vamos criar um novo arquivo chamado `src/encontro-4-computacao/ola-flask-api.py` e adicionar o seguinte código:

```python
# ola-flask-api.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong"

@app.route('/echo', methods=['POST'])
def echo():
   return jsonify(request.json)

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})

@app.route("/subtracao/<int:a>/<int:b>")
def subtracao(a, b):
    return jsonify({"resultado": a - b})

@app.route("/multiplicacao")
def multiplicacao():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify({"resultado": a * b})

@app.route("/divisao", methods=["POST"])
def divisao():
    dados = request.json
    a = int(dados.get("a"))
    b = int(dados.get("b"))
    return jsonify({"resultado": a / b})

```

Nesse ponto, podemos executar nossa aplicação com o comando: `python3 -m flask --app ola-flask-api run --host 0.0.0.0 --port 8000`. Um ponto diferente aqui é que nossa aplicação agora possui rotas que podem receber requisições e retornar respostas. Ele não é uma aplicação web tradicional, mas sim uma API, que pode ser acessada por outros sistemas através de requisições HTTP.

> ***IMPORTANTE:*** Uma aplicação pode possuir rotas de API e rotas de aplicação web. As rotas de API são utilizadas para fornecer dados e funcionalidades para outros sistemas, enquanto as rotas de aplicação web são utilizadas para fornecer uma interface interativa para o usuário.

Para testar a nossa aplicação, vamos utilizar o Thunder Client, uma extensão do Visual Studio Code que nos permite fazer requisições HTTP. Para instalar o Thunder Client, acesse [aqui](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client).

Agora vamos fazer algumas requisições para a nossa aplicação. Primeiro, vamos fazer uma requisição GET para a rota `/ping`. Em seguida, vamos fazer uma requisição POST para a rota `/echo` com o corpo `{"mensagem": "Ola Mundo!!"}`. Por fim, vamos fazer requisições para as rotas `/soma`, `/subtracao`, `/multiplicacao` e `/divisao` com os parâmetros e corpo especificados.

Agora vamos verificar como realizar essas requisições utilizando o `Thunder Client`. Primeiro, vamos instalar a extensão no Visual Studio Code. Em seguida, iniciar nossas requisições. Com a a extensão aberta no Visual Studio Code, vamos selecionar a opção `Nova Requisição`.

<img src={useBaseUrl("img/thunder-client/inicio.png")} alt="Iniciando uma requisição no Thunder Client" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto' }} />

Agora devemos configurar nossa requisição, em especial para qual rota vamos fazer ela. Além da , vale destacar que também devemos configurar outros parâmetros para nossa requisição, como o método HTTP que vamos utilizar, se algum cabeçalho ou corpo da mensagem serão enviados. Vamos testar primeiro a rota `/ping`.

<img src={useBaseUrl("img/thunder-client/requisicao-ping.png")} alt="Requisição para a rota /ping" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

Vale observar aqui alguns pontos importantes:

- As requisições realizadas ficam listadas no menu da esquerda, sendo possível repetir alguma delas e at;e mesmo realizar elas novamente com diferentes parâmetros;
- O método HTTP que foi utilizado foi o `GET`, a requisição foi realizada para a rota `http://localhost:8000/ping`.
- O servidor respondeu essa requisição com o a mensagem `pong` e com **status code** 200, indicando que ela foi bem sucedida. Para mais mensagens de status do protocolo HTTP, verificar este [link😺](https://http.cat/), ou este [link🐶](https://http.dog/) ou este último por fim [link🛜](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

Se modificarmos está requisição para tentar acessar a rota `/echo`, vamos obter o seguinte comportamento:

<img src={useBaseUrl("img/thunder-client/erro-metodo-echo.png")} alt="Requisição para a rota /echo - erro de método" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

Este erro indica para nós que a rota `/echo` não aceita requisições com o método que nós fizemos, neste caso, ela não trabalha com requisições do tipo `GET`. Ao trocar o tipo da requisição para `POST`, vamos ter o seguinte comportamento:

<img src={useBaseUrl("img/thunder-client/erro-corpo-echo.png")} alt="Requisição para a rota /echo - erro de conteúdo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

O método chato 🌋!! Na verdade ele está apenas indicando para nós que nossa requisição não tem os parâmetros que ele precisa para conseguir ser realizado com sucesso. Vamos ajustar nossa requisição para que ela possa trazer em seu corpo um mensagem como a rota espera. Para isso, vamos adicionar um `Body` a requisição. O corpo das requisições `POST` não é enviado como os argumentos passados como parâmetros de uma requisição `GET`, por exemplo.

<img src={useBaseUrl("img/thunder-client/echo-correto.png")} alt="Requisição para a rota /echo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

:::danger[Corpo da Requisição]

Mesmo que o conteúdo da requisição seja um JSON, ele não é enviado como um parâmetro da requisição, mas sim como um corpo da requisição. Isso é importante para que o servidor consiga interpretar corretamente a requisição e retornar a resposta esperada. Devemos configurar o `Content-Type` da requisição para `application/json` e o corpo da requisição deve ser um JSON válido.

Ainda assim, isso não faz com que os dados enviados na requisição estejam protegidos por algum tipo de criptográfia, por exemplo. Para isso, devemos utilizar o protocolo HTTPS, que é uma versão segura do protocolo HTTP. Mesmo assim, diversas aplicações ainda utilizando algum algoritmo de criptografia para proteger os dados enviados e recebidos.

Para estudar mais sobre o protocolo HTTP:

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/aumDleTg_UQ?si=S_8iCnSvNKEqwAcD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/iYM2zFP3Zn0?si=-2uDhm_PhEKsB0Wk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

:::


Continuando com os testes das nossas rotas, os métodos `soma` e `subtracao` são rotas que recebem parâmetros na URL. Já os métodos `multiplicacao` e `divisao` recebem parâmetros no corpo da requisição. Vamos testar cada uma delas. Primeiro os métodos `soma` e `subtracao`:

<img src={useBaseUrl("img/thunder-client/soma-subtracao.png")} alt="Requisição para a rota /echo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

Podemos observar que os parâmetros para essas rotas são passados diretamente na URL. Já para a rota `multiplicacao`, os parâmetros devem ser passados como `Query String`, ou seja, como parâmetros passados na URL, mas que não fazem parte da rota. Vamos passar a `Query String` para a rota `multiplicacao`, enviando eles depois da rota, separados por `?` e `&`.
Vale destacar que o Thunder Client nos permite configurar esses parâmetros de forma mais fácil, mas é importante entender como eles são passados para a aplicação.

<img src={useBaseUrl("img/thunder-client/multiplicacao.png")} alt="Requisição para a rota /echo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />

Por fim, a rota `divisao` recebe os parâmetros no corpo da requisição, como um JSON. Vamos configurar a requisição para que ela possa ser realizada com sucesso.

<img src={useBaseUrl("img/thunder-client/divisao.png")} alt="Requisição para a rota /echo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px' }} />


Pessoal, desta forma abordamos diferentes aspectos de uma aplicação web, como ela pode ser construída e como podemos testar ela. Vamos continuar com a construção da nossa aplicação, mas antes, vamos fazer uma pausa para o café ☕☕. Na sequencia, vamos continuar com a construção da nossa aplicação web.

### 4.4 Construção de uma aplicação web com Flask

Agora, vamos construir nossa aplicação Web utilizando um outro recurso do Flask, os *templates*. Os *templates* são arquivos HTML que contém o código HTML da interface da aplicação. Elas são utilizadas para criar páginas da aplicação que o usuário visualiza, como a página inicial, a página de produtos e a página de checkout. Os *templates* permitem que possamos criar páginas dinâmicas, que podem exibir diferentes conteúdos com base nos dados da aplicação.

Agora, vamos criar o projeto em `src/encontro-4-computacao/projeto-web`. Dentro dele, vamos criar o diretório `templates` e o arquivo `app.py`. Em seguida, vamos adicionar o seguinte código ao arquivo `app.py`:

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

Dentro do diretório `templates`, vamos criar o arquivo `index.html` e adicionar o seguinte código:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Minha Aplicação Web</title>
</head>
<body>
    <h1>Ola Mundo!!</h1>
</body>
</html>
```

Como modificamos nosso arquivo `app.py`, vamos executar nossa aplicação com o comando: `python projeto-web/app.py`, considerando que o terminal está no repositório `encontro-4-computacao`. Agora, ao acessar a rota `http://localhost:8000`, vamos ver a página `index.html` sendo exibida no navegador.

Mais arquivos e outras rotas podem ser adicionados a aplicação. Vamos adicionar mais uma rota e um arquivo HTML para ela. Vamos criar o arquivo `sobre.html` e adicionar o seguinte código:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sobre</title>
</head>
<body>
    <h1>Sobre</h1>
    <p>Esta é a página sobre a minha aplicação web.</p>
</body>
</html>
```

E adicionar a rota para a página `sobre.html` no arquivo `app.py`:

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

Agora, ao acessar a rota `http://localhost:8000/sobre`, vamos ver a página `sobre.html` sendo exibida no navegador.

> "Mas Murilão, e se eu quisar passar informações para a página, como eu faço?". Podemos preparar nossa aplicação para receber informações e passar elas para a página. Vamos adicionar um parâmetro para a rota `sobre` e passar ele para a página `sobre.html`. Vamos adicionar o seguinte código ao arquivo `app.py`:

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre/<nome>")
def sobre(nome):
    return render_template("sobre.html", nome=nome)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)	
```

Aqui estamos passando um parâmetro para a rota `sobre` e passando ele para a página `sobre.html`. Agora, ao acessar a rota `http://localhost:8000/sobre/Murilão`, vamos ver a página `sobre.html` sendo exibida no navegador com as mensagens: 

> Esta é a página sobre a minha aplicação web.
> Ola Murilão!!

Para isso, é necessário editar o arquivo `sobre.html`. Vamos adicionar o seguinte código:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sobre</title>
</head>
<body>
    <h1>Sobre</h1>
    <p>Esta é a página sobre a minha aplicação web.</p>
    <p>Ola {{ nome }}!!</p>
</body>
</html>
```

> "Calma lá Murilão! Que aconteceu aqui? Tem umas coisas nesse código que não são HTML!" Isso mesmo pessoal, o código que está entre `{{` e `}}` é um código Python que é executado pelo Flask. Esse código é utilizado para passar informações da aplicação para a página. O código `{{ nome }}` é utilizado para exibir o valor da variável `nome` na página. O Flask substitui o código `{{ nome }}` pelo valor da variável `nome` antes de enviar a página para o navegador. Esse tipo de código é chamado de *template tag* e é utilizado para criar páginas dinâmicas com o Flask. Quem quiser saber mais sobre *template tags*, acesse [aqui](https://flask.palletsprojects.com/en/latest/templating/). A biblioteca utilizada para isso é a Jinja2, que é uma biblioteca de *template* para Python. Para conhecer mais sobre a Jinja2, acesse [aqui](https://jinja.palletsprojects.com/en/latest/).

Legal, agora conseguimos ajustar nossa aplicação para que ela possa enviar informações de uma página para outra. Vamos utilizar um `form` para enviar informações da página para a aplicação. Na rota `\`, vamos adicionar um formulário que envia informações para a rota `/sobre`. Vamos adicionar o seguinte código ao arquivo `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Minha Aplicação Web</title>
</head>
<body>
    <h1>Ola Mundo!!</h1>
    <form action="/sobre" method="post">
        <input type="text" name="nome" placeholder="Digite o seu nome">
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```
Se apenas fizermos está modificação, não vamos conseguir enviar as informações para a rota `/sobre`. Isso porque a rota `/sobre` está configurada para receber apenas requisições do tipo `GET`. Vamos ajustar a rota `/sobre` para que ela possa receber requisições do tipo `POST` também. Não vamos deixar de receber requisições do tipo `GET`, mas vamos adicionar a possibilidade de receber requisições do tipo `POST`. Vamos adicionar o seguinte código ao arquivo `app.py`:

```python
# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre", methods=["GET", "POST"])
def sobre(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
    return render_template("sobre.html", nome=nome)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

Aqui tem algumas coisas que valem a pena observar:
- A função `sobre` agora recebe um parâmetro `nome` com o valor padrão `None`. Isso é feito para que a função possa ser chamada com ou sem o parâmetro `nome`.
- A função `sobre` verifica o método da requisição utilizando `request.method`. Se o método da requisição for `POST`, a função obtém o valor do campo `nome` do formulário utilizando `request.form.get("nome")`. Se o método da requisição for `GET`, a função utiliza o valor padrão `None` para o parâmetro `nome`.
- Quando a função `sobre` recebe uma requisição do tipo `GET` apenas, ela retorna a página `sobre.html` com o valor padrão `None` para o parâmetro `nome`.



<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />


### 4.5 Integrando aplicação web com banco de dados

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.6 Utilizando *blueprints* para organizar a aplicação

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.7 Deploy da aplicação web

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.8 Integração com o Robô

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />