# Sprint 2

Os entregaveis esperados para está Sprint estão descritos abaixo.

## 1. Mapeamento do Fluxo de Utilização da Solução

No artefato da Sprint 1 você realizou o mapeamento das Jornadas de Usuário e das User Stories referentes às Personas que utilizarão a solução que você pretende desenvolver. Depois de validar essas Jornadas com o parceiro e realizar os devidos ajustes, no presente mapeamento você desenvolverá um mapeamento que leva em consideração componentes e telas da sua solução. 

### 1.1 Padrão de entrega

Para informações detalhadas das requisições deste artefato, acesse: [link](https://drive.google.com/file/d/1kALlRapte63KtoKdta9Eu_0C8csGGKoc/view?usp=sharing).

### 1.2 Padrão de qualidade

Para informações detalhadas dos critérios de qualidade deste artefato, acesse: [link](https://drive.google.com/file/d/1kALlRapte63KtoKdta9Eu_0C8csGGKoc/view?usp=sharing).

## 2. Sistema de Automação (Antigo: Sistema Robótico)

Este artefato contempla o desenvolvimento de um sistema básico de automação. Neste entregável, este sistema será implementado pelo robô manipulador e sua integração com o software desenvolvido pelo grupo.

O grupo deve desenvolver um software que consiga trocar informações com o robô, com ele conectado localmente no computador. O software tem que ser capaz de enviar comandos para o robô, que por sua vez, deve ser capaz de executar esses comandos. A biblioteca que deve ser utilizada é a [pydobot](https://github.com/luismesas/pydobot).

Recomenda-se criar um ambiente virtual para a execução do projeto. Para isso, utilize o comando abaixo:

```bash
python3 -m venv venv
```

O comando deve ser executado dentro do diretório do projeto. Para ativar o ambiente virtual, utilize o comando abaixo:

```bash
# No Linux ou MacOS
source venv/bin/activate
# No Windows
venv\Scripts\activate
```

O sistema criado deve ser utilizado por linha de comando. Este tipo de interface também é chamado de `CLI` (*Command Line Interface*).

:::tip[Interface por Linha de Comando]

Para saber mais sobre este tipo de interface:
- [CLI (A "temida" Command Line Interface) // Dicionário do Programador](https://youtu.be/8AgOxHOAV9Y?si=KCqZ1wCncLg--OjU&t=130)
- [O que é uma aplicação COMMAND-LINE (CLI)?](https://www.youtube.com/watch?v=-CJr6afTy-0)
- [Professional CLI Applications with Click](https://www.youtube.com/watch?v=vm9tOamPkeQ)
- [5 Python Libraries for Building Command Line Tools](https://www.youtube.com/watch?v=20Qkq93kwKw)
- [Criando aplicações de linha de comando (CLIs) com Typer | Live de Python #233](https://www.youtube.com/watch?v=m1_48lmAX-Y)

:::

Sistema robótico que interage com um programa no computador. 

### 2.1 Padrão de entrega

O sistema deve ser capaz de movimentar o robô para um conjunto pré-definido de pontos.
O sistema de pontos deve ser programável. A interface para controlar o robô deve ser construída utilizando alguma ferramenta previamente conhecida pela equipe de desenvolvimento.

Espera-se que para esta entrega, o usuário possa interagir com o sistema, por alguma interface definida pelo grupo. O robô deve ser capaz de navegar para um conjunto de pontos previamente definidos. Esses arquivos podem ser carregados de um arquivo de referência (CSV, JSON, por exemplo).

ATENÇÃO: Não espera-se que neste momento do projeto, um banco de dados seja implementado. Ele pode, e deve, ser considerado como um elemento que deve estar presente na solução final. 

### 2.2 Padrão de qualidade

1. Sistema robótico controlado pelo software desenvolvido pelo grupo (até 2.0 pontos);
2. Interface desenvolvido pela equipe que permite manipular o robô de forma programática (até 2.0 pontos);
3. Carregamento de pontos pré-definidos para o robô (até 2,0 pontos);
4. Navegação do robô para os pontos pré-definidos (até 2.0 pontos);
5. Vídeo de funcionamento do sistema até o momento (até 2.0 pontos).

## 3. Documentação

Este artefato deve ser responsável por apresentar toda a documentação realizada ao longo da Sprint.

### 3.1 Padrão de entrega

Ela deve conter a descrição e documentação dos demais artefatos, bem como apresentações, vídeos de demonstrações e instruções para executar o projeto até o momento desta entrega. Deve ser realizada também um "RELEASE" do repositório, destacando a documentação que foi entregue referente a sprint que passou. 

É importante destacar que na documentação deve existir um log com o registro da evolução das tarefas do projeto, bem como a quantidade de tempo que foi investido em cada tarefa que foi desenvolvida durante a sprint. Todos os artefatos de documentação devem ser elaborados utilizando o Docusaurus (https://docusaurus.io/). Ela deve estar disponível no GitHub Pages da equipe e deve seguir os padrões definidos na orientação. Espera-se também neste artefato que os estudantes construam o pipeline de automação do GitHub para que a documentação construída com o Docusaurus possa ser visualizada no GitHub Pages do repositório da equipe. 

Toda a documentação é viva, ela deve ser atualizada refletindo o que você trouxeram de novo para o projeto. As atualizações devem ser registradas no log de evolução do projeto. Vocês podem, ***E DEVEM***, chamar partes que já foram documentadas, como atualizações de arquitetura.

Outro ponto bastante importante, o repositório de vocês não vai mais conter apenas a documentação do projeto, ele também vai conter o código do projeto. Vocês devem criar um diretório chamado `src` e colocar todo o código do projeto lá. A documentação do projeto deve ser feita utilizando o Docusaurus e deve estar disponível no GitHub Pages da equipe.

:::tip[Diretório do Código Fonte do Projeto]

Dentro do diretório `src`, vocês devem criar um arquivo `README.md` que contenha as instruções para executar o projeto. Este arquivo deve ser o ponto de partida para quem for executar o projeto. Ele deve explicar a diferença que existe entre os pontos que vocês desenvolveram, como o sistema que controla o robô, o backend e o frontend, por exemplo.

:::

### 3.2 Padrão de qualidade

1. A documentação traz os passos necessários para executar a versão atual da sprint (até 3.0 pontos);
2. A documentação contém todos os arquivos de mídia utilizados pela equipe (apresentações e vídeos) (até 2.0 pontos);
3. A documentação atende os requisitos apresentados pelo escritório de projetos para entrega ao parceiro (até 2.0 pontos);
4. A documentação foi atualizada para refletir as mudanças e aprimoramentos (até 3.0 pontos).

