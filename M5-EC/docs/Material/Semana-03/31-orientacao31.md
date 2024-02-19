---
sidebar_label: "4 - Encontro de Orientação"
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instrução de Orientação

Planning da Sprint 2	

## 1. Objetivos

- Planejamento da Sprint 2.
- Construção de Sprint Planning e outras cerimônias do framework Scrum.
- Criando Releases no Github.

## 2. Slides do Encontro

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSG6q7EZA2isyGW3V_1pXMM7IJquzznhrFYcQA0ygtI8Nfv7v7SvdBN_jbO2XuOBN3kg1zpmRzti5Om/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }}></iframe>


## 3. Material de Autoestudo

:::danger[Acesse a Adalove!]

Esse material NÃO substitui de forma alguma o uso da Adalove. Você DEVE entrar na Adalove com frequência e REGISTRAR O SEU PROGRESSO. Entendeu? Ainda não? Pera aí que vou desenhar:

<img src={useBaseUrl("/img/memes/aviso-adalove.png")} alt="ACESSE A ADALOVE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />

:::

<Tabs>
  <TabItem value="autoestudos-obrigatorios" label="📘 Autoestudos Obrigatórios" default>
     
     <details> 
        <summary mdxType="summary">	SCRUM O QUE É (de um Jeito BEM Prático)</summary>

        - https://www.youtube.com/watch?v=HlmiVz0SqNQ
    </details> 
    <details> 
        <summary mdxType="summary">	O que é o Scrum?</summary>

        - https://aws.amazon.com/pt/what-is/scrum/
    </details> 
    <details> 
        <summary mdxType="summary">	SCRUM: Esse não é o livro para aprender como aplicar</summary>

        - https://medium.com/@rinaldodev/scrum-esse-n%C3%A3o-%C3%A9-o-livro-para-aprender-como-aplicar-1b2383488e9e
    </details> 
    <details> 
        <summary mdxType="summary">	Atividade Ponderada - Construção de Interface por Linha de Comando (CLI) para Controle do Robô</summary>

        O estudante deverá construir uma interface por linha de comando que deve receber posições para onde o robô deve se deslocar e tratar alguns comandos especiais. Os comandos esperados são: 
            
            - ``home``: faz o robô retornar a sua posição inicial do processo; 
            - ``ligar ferramenta``: faz o robô ligar a ferramenta (atuador); 
            - ``desligar ferramenta``: faz o robô desligar sua ferramenta (atuador); 
            - ``mover x 100``: faz o robô se mover em um eixo (x, y ou z) a distância especificada; 
            - ``atual``: retorna a posição atual do robô. A interface de console deve ser desenvolvida em Python. Pode exisitr uma interface gráfica para o envio dos comandos para o robô. 
        
        Espera-se como padrão de qualidade: 
        
            1. Interface de texto para enviar os comandos para o robô (até 4.0 pontos); 
            2. Robô executando os comandos corretamente (até 4.0 pontos); 
            3. Vídeo demonstrando o funcionamento do sistema (até 1.0 pontos); 
            4. Entrega do projeto pelo Github (até 1.0 ponto); 
            Extra (esses pontos serão utilizados caso a nota máxima, 10, ainda não tenha sido alcançada na atividade): Existe uma interface gráfica para envio dos pontos (até 2.0 pontos). 
            
        A entrega vai acontecer por um link no GitHub. Esse repositório deve ser público. ***Data limite:*** `01/03/2024 (até às 23h59)`.
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
    <details> 
        <summary mdxType="summary">	#Lean Inception - Resumo do livro de Paulo Caroli</summary>

        - https://www.youtube.com/watch?v=2OldFNkGZEs
    </details> 
    <details> 
        <summary mdxType="summary">	Design Sprint Methodology - What Is Design Sprint Process (from Day 1 to Day 5)</summary>

        - https://www.youtube.com/watch?v=WWEJCLkf1D4
    </details> 
    <details> 
        <summary mdxType="summary">	Criando TAGS no GIT e GITHUB!</summary>

        - https://www.youtube.com/watch?v=CqJvlBXgCfc
    </details>     

  </TabItem>
</Tabs>

## 4. Material de Aula


### Metodologia Ágil

Podemos definir a `Metodologia Ágil` como  um conjunto de princípios e práticas para gerenciar e desenvolver projetos de forma flexível, adaptável e colaborativa. Ela surgiu como uma alternativa à metodologia tradicional em cascata, que era considerada rígida e pouco eficiente para lidar com mudanças frequentes nos requisitos e no ambiente de negócios.

Os principais pontos da metodologia ágil são:

- `Valorização da entrega incremental e contínua`: O foco está em entregar funcionalidades do produto final em ciclos curtos e frequentes, permitindo que o cliente avalie o progresso e forneça feedback.
- `Adaptabilidade a mudanças`: A metodologia ágil reconhece que as necessidades do cliente e o ambiente de negócios podem mudar durante o desenvolvimento do projeto, e por isso é importante ser capaz de se adaptar rapidamente a essas mudanças.
- `Colaboração entre todos os stakeholders`: A equipe de desenvolvimento, o cliente e outros stakeholders trabalham juntos de forma colaborativa durante todo o ciclo de vida do projeto.
- `Aprendizagem e melhoria contínua`: A metodologia ágil incentiva a equipe a aprender com seus erros e a buscar constantemente formas de melhorar o processo de desenvolvimento.

Ela pode ser utilizada em diversos tipos de projetos, mas é especialmente adequada para projetos complexos e inovadores, onde a incerteza e a mudança são constantes. Alguns tipos de projetos que podemos utilizar ela:

- `Desenvolvimento de software`: A metodologia ágil é especialmente adequada para o desenvolvimento de software, pois permite que a equipe se adapte rapidamente às mudanças nos requisitos e entregue funcionalidades de forma incremental.
- `Gestão de projetos`: A metodologia ágil pode ser utilizada para gerenciar qualquer tipo de projeto, desde projetos de desenvolvimento de software até projetos de marketing e vendas.
- `Outros tipos de projetos`: A metodologia ágil também pode ser utilizada em outros tipos de projetos, como projetos de design, projetos de construção e projetos de pesquisa.

### Lean Inception

A `Lean Inception` é uma técnica de planejamento e alinhamento de equipes que tem como objetivo definir o escopo e as metas de um projeto de forma colaborativa e eficiente. Ela foi criada por Paulo Caroli e é baseada nos princípios do Lean Startup e do Design Thinking.

Com a `Lean Inception` é possível alinhar a equipe em relação ao escopo e às metas do projeto, definir as funcionalidades mínimas necessárias para lançar o produto no mercado e criar um plano de ação para o desenvolvimento do projeto. As funcionalidades do projeto são entregues de forma incremental, sempre priorizando as mais importantes para o cliente e as que geram mais valor para o negócio.

Podemos definir como principais pontos da `Lean Inception` (adaptado de [Lean Inception](https://www.caroli.org/lean-inception/)):

1. `Visão do produto:` Defina uma visão clara e compartilhada do produto que será desenvolvido. Todos devem compreender o propósito e os objetivos.
2. `É – Não é – Faz – Não faz`: Esclareça as características do produto, identificando o que ele é, o que não é, o que faz e o que não faz. Isso evita ambiguidades e define os limites do escopo. ***FAÇAM ESTÁ ANÁLISE PARA O PROJETO DE VOCÊS!***

3. `Personas`: Desenvolva personas que representem os diferentes perfis de usuários do produto. Compreender suas necessidades e características ajuda a direcionar as decisões.
4. `Jornada de usuários`: Mapeie a jornada que os usuários percorrerão ao interagir com o produto. Identifique etapas, pontos de contato e possíveis desafios.
5. `Brainstorming`: Realize sessões criativas para gerar ideias de funcionalidades e recursos que agreguem valor ao produto.
6. `Revisão Técnica, de UX e de Negócio`: Analise as ideias geradas e avalie sua viabilidade técnica, a experiência do usuário e o impacto no negócio. Ajuste conforme necessário.
7. `Sequenciador`: Priorize as funcionalidades considerando sua importância e valor para os usuários, para o negócio e a viabilidade técnica. Crie uma sequência lógica para o desenvolvimento.
8. `Canvas MVP`: Desenvolva o Canvas do MVP (Minimum Viable Product) para definir os elementos essenciais do produto inicial. Isso ajuda a focar no mínimo necessário para validar o direcionamento do seu negócio.

:::tip[Em relação ao nosso projeto]

Pessoal é importante observar aqui, que após a sprint 1, diversos dos pontos acima já foram realizados. Então, é importante que vocês revisitem esses pontos e vejam o que já foi feito e o que ainda falta ser feito. Vale destacar também para adicionar as observações que os parceiros fizeram sobre o projeto de vocês na sprint review 1.

:::

### Ações para o Projeto

Agora, retomados os pontos acima, é importante que vocês realizem as seguintes ações:

- `Realização das Etapas do Lean Incpetion`: Realizem as etapas do Lean Inception que ainda não foram realizadas. Em especial, a etapa do ***FAZ e NÃO FAZ***, que é muito importante para definir o escopo do projeto e quais as funcionalidades que vocês vão implementar. É muito importante destacar que, características que estão dentro do escopo do ***NÃO FAZ***, não devem ser implementadas nesta versão atual do projeto, mas podem ser adicionadas em um backlog para implementações futuras do projeto.

- `Criação do Release no Github`: Crie um release no Github com as funcionalidades que vocês vão implementar nesta sprint. Isso é importante para que vocês possam acompanhar o progresso do projeto e para que os parceiros possam acompanhar o progresso de vocês. Vamos avaliar um pouco mais sobre o processo de criação de ***releases*** no Github.

- `Realização de Balanceamento das Tarefas`: Pessoal não estou dizendo que vocês devem realizar um planning poker com as tarefas de vocês, mas estou sugerindo que vocês façam uma avaliação crítica quanto ao tempo que vocês vão gastar em cada tarefa. Isso é importante para que vocês possam dimensionar melhor as próximas tarefas e divisão de ações. 

- `Escrevão Padrões de Qualidade`: Além dos baremas, escrevam padrões de qualidade de vocês para definir o que é aceito como uma entrega de qualidade. Isso é importante para que vocês possam ter um norte quanto ao que é esperado de vocês e evita posteriores atritos na equipe quanto a qualidade de entrega de alguma tarefa.

### Criando Tags no Git e no GitHub

Agora, vamos falar um pouco sobre como criar tags no Git e no GitHub. Elas são importantes para marcar versões do seu projeto e para que vocês possam acompanhar o progresso do projeto. Vamos ver um pouco mais sobre isso.

:::tip[Tags no Git]

As tags no Git são referências a pontos específicos na história do seu repositório. Elas são geralmente usadas para marcar versões de lançamento (como v1.0 e v2.0). Ao contrário dos *branches*, as tags não mudam com o tempo. Se você criar uma tag para um commit específico, ela sempre apontará para esse commit, mesmo que você crie novos commits no repositório.

:::

:::danger[Manter o Repositório Atualizado]

É importante que vocês mantenham o repositório de vocês atualizado com as tags. Isso é importante para que vocês possam acompanhar o progresso do projeto e para que os parceiros possam acompanhar o progresso de vocês.

Lembre-se de utiizar o comando `git pull` para manter o repositório de vocês atualizado.

:::

Utilizando o comando `git tag` você pode criar tags no seu repositório. Vamos ver um exemplo de como criar uma tag no Git:

```bash
git tag -a v1.0 -m "Versão 1.0"
```

O que está acontecendo aqui é que estamos criando uma tag chamada `v1.0` com a mensagem `Versão 1.0`. Isso é importante para que vocês possam acompanhar o progresso do projeto e para que os parceiros possam acompanhar o progresso de vocês. O parâmetro `-a` é para criar uma tag anotada, que é uma tag que contém uma mensagem. O parâmetro `-m` é para adicionar uma mensagem à tag.

Por *default*, uma tag é associada ao último commit que você fez. Se você quiser associar a tag a um commit específico, você pode passar o hash do commit como um parâmetro para o comando `git tag`. Por exemplo:

```bash
git tag -a v1.0 9fceb02 -m "Versão 1.0"
```

Onde o `9fceb02` é o hash do commit que você quer associar à tag.

Agora precisamos mandar nossas tags para o repositório remoto. Para fazer isso, utilizamos o comando `git push` com a opção `--tags`. Vamos ver um exemplo de como fazer isso:

```bash
git push origin --tags
```

Desta forma, todas as tags que você criou no seu repositório local serão enviadas para o repositório remoto. Para enviar apenas uma tag específica, utilizar o comando `git push origin v1.0`.

Agora vamos definir o padrão de tags que vamos utilizar. No final de cada sprint, a versão que deve ser entregue, deve estar com a tag `vX.Y`, onde `X` é o número da sprint e `Y` é o número da versão. Por exemplo, a versão que vocês vão entregar no final da sprint 2, deve estar com a tag `v2.0`. As melhorias e correções que forem realizadas na versão que vocês vão entregar no final da sprint 2, devem estar com a tag `v2.1`, e assim por diante.