# Sprint 4

Os entregaveis esperados para está Sprint estão descritos abaixo.

## 1. Interface Navegável

Para esta entrega é esperada a apresentação de um protótipo em alta fidelidade navegável ou da interface funcional já implementada à plataforma da solução proposta. Aqui, estamos considerando o conceito de "Responsive Design" como a adaptabilidade da solução nas diversas telas dos dispositivos nos quais a plataforma deverá ser acessada. 

### 1.1 Padrão de entrega

Para informações detalhadas das requisições deste artefato, acesse: [link](https://drive.google.com/file/d/10v1eyResfv_89G39XV8kjJA25ZtnLyW9/view?usp=sharing)

### 1.2 Padrão de qualidade

Para informações detalhadas dos critérios de qualidade deste artefato, acesse: [link](https://drive.google.com/file/d/10v1eyResfv_89G39XV8kjJA25ZtnLyW9/view?usp=sharing)

## 2. Interface frontend e backend do sistema

A interface para o usuário final deve ser elaborada nesta sprint. Este artefato tem por objetivo permitir que os usuários possam interagir com o nosso sistema de forma muito semelhante ou idêntica ao que será entregue ao final do projeto.

Até o momento, já possuimos oficialmente uma interface por linha de comando (***CLI***) do nosso projeto. Esta interface é utilizada para a comunicação com o robô e para a visualização dos logs e registros do sistema. Contudo, agora vamos entregar uma interface para que todos os usuários do sistema possam interagir com ele.

Para este momento do projeto, recomendo fortemente que vocês façam uma visita cuidadosa ao `backlog do projeto` e que verifiquem se todas as funcionalidades que foram propostas para o sistema estão contempladas nesta interface. Está visita tem por objetivo mapear o que já foi implementado e o que ainda precisa de atenção para o desenvolvimento ao longo da sprint.

É esperado que a interface do usuário que vocês desenvolvam permita que o usuário final possa realizar algumas funcionalidades básicas, como:

- Carregar/Escolher um conjunto de itens/layouts para o robô;
- Visualizar os logs e registros do sistema;
- Carregar/Escolher outro conjunto de itens/layouts para o robô.

Deixo aqui como sugestão deixar claro quem é responsável por cada uma das funcionalidades que estão sendo entregues. O que deve ser realizado pelo backend e o que deve ser realizado pelo frontend da aplicação. É importante destacar que a recomendação para o desenvolvimento da interface é utilizar o framework `Flask` para o backend e `páginas renderizadas de template` para o frontend.

Recomendo também que vocês utilizam alguma ferramenta para estilização da interface, como o `Bootstrap` ou `Bulma`. Estilos personalizados podem ser criados, mas sugiro que vocês utilizem um framework para agilizar o desenvolvimento. Sugiro que vocês assistam a está playlist do canal [`Thi Code`](https://www.youtube.com/@thi_code), onde o autor apresenta um tutorial de como criar um sistema de cadastro de usuários utilizando o `Flask` e o `Bootstrap`. O link para a playlist é: [link](https://www.youtube.com/watch?v=pzsBEuiZ2I4&list=PLR8JXremim5DU70e3x_rYhClgMTzTyv4m&index=1)

<iframe width="560" height="315" src="https://www.youtube.com/embed/pzsBEuiZ2I4?si=jtd9y0VTwlZNCFxz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### 2.1 Padrão de entrega

Aqui o sistema deve contemplar uma forma intuitiva e de baixa fricção para os usuários. Um sistema que possibilite visualizar os logs e registros do sistema também deve ser desenvolvido. O sistema do usuário deve permitir o carregamento de outro conjunto de pontos também.

O backend da aplicação, deve possuir essencialmente o acesso ao armazenamento dos dados. Outras funcionalidades podem ser adicionadas ao backend, caso o grupo considere que esta abordagem é pertinente 

### 2.2 Padrão de qualidade

1. Carregamento de um conjunto diferente de pontos para o robô (até 2.0 pontos);
2. Frontend do sistema de interface com o usuário (até 2.0 pontos);
3. Backend do sistema de interface com o usuário responsável por realizar a comunicação com os bancos de dados e gerenciar as regras de negócio do sistema (até 4.0 pontos);
4. Integração entre o sistema de backend e o frontend da aplicação (até 2.0 pontos).

## 3. Documentação

Este artefato deve ser responsável por apresentar toda a documentação realizada ao longo da Sprint. Nas sprints depois da primeira, espera-se que a documentação esteja mais robusta e que ela possa refletir as mudanças e aprimoramentos que foram realizados no projeto.

A documentação também deve apresentar as evidências que os requisitos funcionais e não funcionais foram atendidos. Além disso, espera-se que eventuais demandas para executar o projeto ou partes dele, como programas em Python ou a própria documentação localmente, também constem na documentação e no *README* do repositório.

É muito importante que a documentação também apresente as mídias do projeto. Vídeos de demonstração e as apresentações das sprints devem estar refletidos nela.

### 3.1 Padrão de entrega

Ela deve conter a descrição e documentação dos demais artefatos, bem como apresentações, vídeos de demonstrações e instruções para executar o projeto até o momento desta entrega. Deve ser realizada também um "RELEASE" do repositório, destacando a documentação que foi entregue referente a sprint que passou. 

É importante destacar que na documentação deve existir um log com o registro da evolução das tarefas do projeto, bem como a quantidade de tempo que foi investido em cada tarefa que foi desenvolvida durante a sprint. Todos os artefatos de documentação devem ser elaborados utilizando o Docusaurus (https://docusaurus.io/). 

Ela deve estar disponível no GitHub Pages da equipe e deve seguir os padrões definidos na orientação. Espera-se também neste artefato que os estudantes construam o pipeline de automação do GitHub para que a documentação construída com o Docusaurus possa ser visualizada no GitHub Pages do repositório da equipe. 

### 3.2 Padrão de qualidade

1. A documentação traz os passos necessários para executar a versão atual da sprint (até 3.0 pontos);
2. A documentação contém todos os arquivos de mídia utilizados pela equipe (apresentações e vídeos) (até 2.0 pontos);
3. A documentação atende os requisitos apresentados pelo escritório de projetos para entrega ao parceiro (até 2.0 pontos);
4. A documentação foi atualizada para refletir as mudanças e aprimoramentos (até 3.0 pontos).