# Atalhos e Macros

Aqui serão adicionados atalhos e macros que podem ser utilizados ao longo do módulo.

## Integração Slack e Github

### Inscrição em um repositório

O primeiro passo da integração é ligar o Slack ao Github. Realizar isso pelas instruções do [Github](https://slack.github.com/).

Antes de realizar a inscrição é necessário adicionar o bot `github` ao canal do Slack: `/invite @github`.

Para inscrever-se em um repositório, utilizar a sintaxe: `/github subscribe <owner>/<repo>`.

Exemplo de inscrição no repositório `Inteli-College/2024-T0008-EC05-G01`: `/github subscribe Inteli-College/2024-T0008-EC05-G01`.

### Comandos do Bot: criando uma issue

Para criar uma issue no repositório, utilizar a sintaxe: `/github issue create <owner>/<repo> <title> <body>`.
Exemplo de criação de uma issue no repositório `Inteli-College/2024-T0008-EC05-G01`: 

```bash
/github issue create Inteli-College/2024-T0008-EC05-G01 "Título da Issue" "Corpo da Issue"`
```

## Utilizando o Docusaurus

Material desenvolvido com o professor Nicola.

- [Link](https://rmnicola.github.io/m9-ec-encontros/docusaurus)

## Deploy com o Github Actions

Material desenvolvido com o professor Nicola.

- [Link](https://rmnicola.github.io/m9-ec-encontros/actions)