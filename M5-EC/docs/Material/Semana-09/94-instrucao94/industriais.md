---
title: Redes Industriais
sidebar_position: 3
sidebar_class_name: opcional
slug: /industriais
---

import Admonition from '@theme/Admonition';

# Introdução a redes industriais

## 1. Fieldbus

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
        src="https://www.youtube.com/embed/ndc6at_d7uQ" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

- **Camadas OSI:** Aplica-se principalmente às camadas física (1) e de enlace
  de dados (2).
- **Funcionamento:** É um sistema de rede usado para comunicações digitais
  entre controladores e dispositivos de campo, como sensores e atuadores.
  Utiliza um único cabo para transmitir sinais de controle, alimentação e
  dados.
- **Vantagens:** Reduz a fiação e custos associados, permite diagnósticos
  avançados e integração de dispositivos.
- **Desvantagens:** Pode ser complexo de implementar e requer hardware
  específico.

## 2. DeviceNet

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
        src="https://www.youtube.com/embed/acnpobFi5qg" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

- **Camadas OSI:** Opera nas camadas física (1) e de enlace de dados (2).
- **Funcionamento:** É uma rede baseada em CAN (Controller Area Network)
  projetada para automação industrial, conectando dispositivos como sensores,
  atuadores e controladores.
- **Vantagens:** Facilita a comunicação entre dispositivos de diferentes
  fabricantes, é robusto e confiável.
- **Desvantagens:** Tem limitações de distância e velocidade em comparação com
  outras redes.

## 3. Modbus

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
        src="https://www.youtube.com/embed/txi2p5_OjKU" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

- **Camadas OSI:** Principalmente nas camadas de aplicação (7), apresentação
  (6) e sessão (5).
- **Funcionamento:** É um protocolo de comunicação serial que permite a troca
  de dados entre dispositivos, comumente usado em sistemas de controle e
  monitoramento.
- **Vantagens:** Simples, fácil de implementar e amplamente suportado.
- **Desvantagens:** Limitado em termos de velocidade e distância, sem suporte
  nativo para segurança.

## 4. Profibus

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
        src="https://www.youtube.com/embed/zJDsEqCyTqc" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

- **Camadas OSI:** Atua nas camadas física (1) e de enlace de dados (2).
- **Funcionamento:** É um padrão de rede de campo para automação industrial que
  conecta dispositivos como PLCs, sensores e atuadores.
- **Vantagens:** Alta velocidade de transmissão, suporte a uma ampla gama de
  dispositivos e diagnósticos avançados.
- **Desvantagens:** Requer hardware específico e pode ser complexo de
  configurar.

## 5. Profinet

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
        src="https://www.youtube.com/embed/YxF9QgRAx8A" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

- **Camadas OSI:** Opera em todas as sete camadas do modelo OSI.
- **Funcionamento:** É uma rede Ethernet industrial que permite a integração de
  automação e TI, oferecendo comunicação em tempo real entre dispositivos.
- **Vantagens:** Alta velocidade, flexibilidade, integração com sistemas de TI
  e diagnósticos detalhados.
- **Desvantagens:** Pode ser mais caro e complexo de implementar do que outras
  soluções.

## 6. RS-485

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
        src="https://www.youtube.com/embed/3wgKcUDlHuM" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

- **Camadas OSI:** Aplica-se principalmente às camadas física (1) e de enlace
  de dados (2).
- **Funcionamento:** É um padrão de comunicação serial que suporta redes de
  dispositivos em longas distâncias e em ambientes ruidosos.
- **Vantagens:** Permite comunicação em longas distâncias, suporta múltiplos
  dispositivos e é resistente a interferências.
- **Desvantagens:** Limitado a baixas taxas de transmissão e requer terminação
  correta da rede.

## 7. HART

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
        src="https://www.youtube.com/embed/pXkun-PEiY0" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

- **Camadas OSI:** Principalmente nas camadas física (1) e de enlace de dados (2).
- **Funcionamento:** É um protocolo de comunicação que combina comunicação
  digital com sinalização analógica 4-20 mA, usado para conectar dispositivos
  de campo com sistemas de controle.
- **Vantagens:** Compatível com sistemas analógicos existentes, permite
  diagnósticos avançados e fácil integração.
- **Desvantagens:** Limitado em termos de velocidade de transmissão de dados e
  requer equipamentos compatíveis.

## 8. RS-232

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
        src="https://www.youtube.com/embed/eo9dbnrpspM" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

- **Camadas OSI:** Aplica-se principalmente às camadas física (1) e de enlace
  de dados (2).
- **Funcionamento:** É um padrão de comunicação serial para troca de dados
  entre dispositivos, como computadores e periféricos.
- **Vantagens:** Simples e fácil de implementar, amplamente utilizado em
  dispositivos legados.
- **Desvantagens:** Limitado em distância e velocidade, não é adequado para
  ambientes ruidosos ou redes de dispositivos.
