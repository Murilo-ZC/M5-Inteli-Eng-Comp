---
title: Semana 07
---

# Apresentação da Semana 7

Nesta seção vocês poderão encontrar todo o material do módulo de Orientação e Computação da `Semana`.
As apresentações, por motivos de confidencialidade, serão disponibilizadas apenas como link para versão do Google Apresentações.

:::tip[Correções, Melhorias e Atualizações no Material]
Encontrou algum erro ou alguma coisa que possa melhorar no material? `bug🐞`? Abra uma issue no [repositório do módulo](https://github.com/Murilo-ZC/M5-Inteli-Eng-Comp).
:::

Está semana teremos os seguintes encontros:

- [Encontro de Computação](/docs/Material/Semana-07/71-orientacao71.md): Décimo encontro de computação.
- [Encontro de Computação](#): Oitavo encontro de computação.
- [Encontro de Orientação](/docs/Material/Semana-07/75-orientacao75.md): Décimo-primeiro encontro de orientação.

## Atividade Ponderada

Pessoal vou adicionar algumas informaçoes sobre a atividade ponderada: `Atividade Ponderada - Projeto em Flask com interface de controle do robô`.

### Data de Entrega

Pessoal a atividade fica com prazo de entrega até o dia 31/03/2024, as 23h59.
A entrega deve toda ser realizada pelo Github, logo, o link para o repositório do projeto deve ser enviado para no card do Adalove.
Commits fora do prazo nao serao considerados.

:::danger[Faltam `ã`]

No momento da escrita deste material, estou utilizando um setup provisório. Assim que ele estiver finalizado, vou corrigir as acentuaçoes.

:::

### Descrição da Atividade

Esta atividade tem por objetivo realizar uma integração do sistema construído com Flask e o robô físico. O estudante deverá construir um sistema que realiza o log dos comandos enviados por uma interface gráfica construída com HTMX e servida com Flask em um servidor local. Neste servidor, o robô físico deve estar conectado. Quando o robô não estiver conectado, apenas as funcionalidades de visualização do log devem estar disponíveis no sistema. 

A forma como a interface do sistema será construída fica a critério do estudante, desde que contemple no mínimo: 

- Uma interface no estilo de dashboard para visualizar os logs do sistema; 
- Uma interface que permita controlar o robô. 

O banco de dados utilizado deve ser o TinyDB. Entende-se aqui por log do sistema, a capacidade de visualizar os comandos que foram enviados para o robô. Por exemplo, se o usuário do sistema pediu para o robô se deslocar em X por 50 mm, o log deve registrar este comando e o momento que ele aconteceu. A sua interface deve possuir duas páginas principas para realizar a exibiç±ao destas informaçoes. Para o projeto, o uso das ferramentas Flask e HTMX NAO É OPCIONAL.

Como barema, espera-se encontrar: 

> 1. Backend construído em Flask conectado ao banco de dados TinyDB (até 2.0 pontos); 

Onde:

- [0.0 até 1.0] - Foi construído um backend em Flask, mas não está conectado ao banco de dados TinyDB. 
- [1.0 até 1.5] - Foi construído um backend em Flask e está conectado ao banco de dados TinyDB, mas nao implementa o CRUD complemente, mesmo que todas as rotas do CRUD nao sejam utilizadas.
- [1.5 até 2.0] - Foi construído um backend em Flask e está conectado ao banco de dados TinyDB, além disso, o CRUD está complementamente implementado.


> 2. Frontend construído com HTMX (até 2.0 pontos); 

Onde:

- [0.0 até 1.0] - Foi construído um frontend com HTMX, mas não está conectado ao backend. 
- [1.0 até 1.5] - Foi construído um frontend com HTMX e está conectado ao backend, mas não implementa as funcionalidades corretamente. 
- [1.5 até 2.0] - Foi construído um frontend com HTMX e está conectado ao backend, além disso, implementa as funcionalidades corretamente.

> 3. O sistema verifica se o robô está conectado e exibe as interfaces corretamente (até 2.0 pontos); 

Onde:
    
- [0.0 até 1.0] - O sistema não verifica se o robô está conectado e não exibe as interfaces corretamente. 
- [1.0 até 1.5] - O sistema verifica se o robô está conectado, mas não exibe as interfaces corretamente. 
- [1.5 até 2.0] - O sistema verifica se o robô está conectado e exibe as interfaces corretamente.

> 4. Existe uma página funcional de controle do robô (até 2.0 pontos); 

Onde:
    
- [0.0 até 1.5] - Existe uma página de controle do robô, mas ela não é totalmente funcional. 
- [1.5 até 2.0] - Existe uma página de controle do robô e ela é funcional.

> 5. Existe uma página funcional de exibição de logs do sistema (até 2.0 pontos).

Onde:

- [0.0 até 1.5] - Existe uma página de exibição de logs do sistema, mas ela não é está integrada corretamente ao sistema. 
- [1.5 até 2.0] - Existe uma página de exibição de logs do sistema e ela é funcional.