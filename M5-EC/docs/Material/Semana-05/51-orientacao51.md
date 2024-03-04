---
sidebar_label: "7 - Encontro de Orientação"
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instrução de Orientação	

Planning da Sprint 3

## 1. Objetivos

- Planejamento da Sprint 3. 
- Retomada dos conceitos de eletricidade básica.
- [***NOVO***] Leitura de QrCode com Python.

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
        <summary mdxType="summary"> Arduino Course for Beginners - Open-Source Electronics Platform - Seção 2 - Fundamentos de Eletrônica</summary>

        - https://youtu.be/zJ-LqeX_fLU?si=CpTMczJxrdBgDSZY&t=81
    </details> 
    <details> 
        <summary mdxType="summary"> Arduino Course for Beginners - Open-Source Electronics Platform - Seção 5 - Como utilizar protoboards</summary>

        - https://youtu.be/zJ-LqeX_fLU?si=Dt_dK0tO9jopPN7z&t=2794
    </details> 

  </TabItem>
  <TabItem value="autoestudos-opcionais" label="📔 Autoestudos Opcionais">
     
        <img class="image-intro" src={useBaseUrl("/img/memes/mash_celebrando.gif")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>

  </TabItem>
  <TabItem value="autoestudos-adicionais" label="📓 Autoestudos Adicionais">

    <img class="image-intro" src={useBaseUrl("/img/memes/mash_celebrando.gif")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>

    <!-- <details> 
        <summary mdxType="summary">	Lean Inception em 15 Minutos | 📎 Zup Clipes ✂️</summary>

        - https://www.youtube.com/watch?v=8BI6jFwmVPA
    </details>  -->

  </TabItem>
</Tabs> 

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

## 4. Material de Aula

### 4.1 Eletricidade Básica	

<img src="https://i.redd.it/q0dd3k02unqb1.gif" alt="Boot process" style={{ display: 'block', marginLeft: 'auto', maxHeight: '30vh', marginRight: 'auto' }} />

### 4.2 Leitura de QrCode com Python

Pessoal, devido a demanda bastante alta em utilizar a leitura e acompanhamento de QrCode, vamos fazer um encontro de orientação para que vocês possam entender como fazer isso.

:::warning[CUIDADO]

Todo o material desenvolvido pode ser utilizado para realizar a leitura de códigos QrCode e teoricamente de códigos de barras. Entretanto, a utilização de códigos de barras não foi testada com exito. Sugiro que vocês utilizem o material e adicionem uma consideração de utilizar, para a ***PoC***, apenas códigos QrCode criados por vocês.

:::

#### 4.2.1 Instalação e Utilização da Biblioteca QReader

Existem diversas bibliotecas que podem ser utilizadas para realizar a leitura de QrCode. Entretanto, a que vamos utilizar é a `QReader`, que é uma forma encapsulada de utilizar o `pyzbar`.

Detalhes sobre a forma que a biblioteca utiliza as ferramentas internas serão adicionadas posteriormente.

Para utilizar o `QReader` vocês precisam instalar a biblioteca. Para isso, utilizem o comando:

```bash
pip install qreader
```

:::tip[Instalação]

O documentação da biblioteca pode ser acessada no [`link`](https://pypi.org/project/qreader/). Durante a instalação vocês podem encontrar problemas com alguma dependência. No caso do Windows, foi necessário realizar a instalação do [`vcredist_x64.exe`](https://www.microsoft.com/en-gb/download/details.aspx?id=40784).

Para o MacOS, foi necessário realizar a instalação do [`zbar`](http://zbar.sourceforge.net/download.html). Utilizar o comando:

```bash
brew install zbar
```

:::

Agora que vocês já instalaram a biblioteca, vamos realizar a leitura de um QrCode. Para isso, utilizem o código abaixo:

```python
# Teste QReader
from qreader import QReader
import cv2

# Create a QReader instance
qreader = QReader(
    model_size = 'l', min_confidence = 0.5
)

# Get the image that contains the QR code
image = cv2.cvtColor(cv2.imread("image.png"), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text = qreader.detect_and_decode(image=image)

# Print the decoded text
print(decoded_text)

```

Os modelos que podem ser utilizados para o sistema são:

> QReader(model_size = 's', min_confidence = 0.5, reencode_to = 'shift-jis')
This is the main class of the library. Please, try to instantiate it just once to avoid loading the model every time you need to detect a QR code.
> `model_size`: str. The size of the model to use. It can be 'n' (nano), 's' (small), 'm' (medium) or 'l' (large). Larger models are more accurate but slower. Default: 's'.
> `min_confidence`: float. The minimum confidence of the QR detection to be considered valid. Values closer to 0.0 can get more False Positives, while values closer to 1.0 can lose difficult QRs. Default (and recommended): 0.5.
> `reencode_to`: str | None. The encoding to reencode the utf-8 decoded QR string. If None, it won't re-encode. If you find some characters being decoded incorrectly, try to set a Code Page that matches your specific charset. Recommendations that have been found useful: 'shift-jis' for Germanic languages and 'cp65001' for Asian languages (Thanks to @nguyen-viet-hung for the suggestion)

#### 4.2.2 Utilização da Biblioteca QReader em conjunto com a Webcam

Agora que conseguimos fazer a leitura do QrCode, vamos fazer a leitura de um QrCode utilizando a webcam. Essa leitura pode ser realizada utilizando a biblioteca `opencv-python`. Ela permite a manipulação de imagens e vídeos.

Vamos avaliar o código abaixo:

```python
# import the opencv library 
import cv2 

# QReader
from qreader import QReader

# Create a QReader instance
qreader = QReader(
    model_size = 'l', min_confidence = 0.5
)  
  
# define a video capture object 
vid = cv2.VideoCapture(1) 
      
# Capture the video frame 
# by frame 

print("Capturando imagem...")
ret, frame = vid.read() 

# Save the frame into an image file
print("Salvando imagem...")
cv2.imwrite('image.png', frame) 
      
# After the loop release the cap object 
vid.release() 

# Realiza a leitura do QRCode
print("Processando imagem...")
image = cv2.cvtColor(cv2.imread("image.png"), cv2.COLOR_BGR2RGB)
# image = cv2.cvtColor(cv2.imread("teste-barcode-2.jpg"), cv2.COLOR_BGR2RGB)

# Utilizando o QReader
# Use the detect_and_decode function to get the decoded QR data
decoded_text = qreader.detect_and_decode(image=image)

# Print the decoded text
print(decoded_text)
```

Pontos mais relevantes do código acima:

- A linha `qreader = QReader(model_size = 'l', min_confidence = 0.5)  ` cria uma instância do QReader, utilizando o modelo de tamanho `l` e a confiança mínima de `0.5`.

- A linha `vid = cv2.VideoCapture(1)` define que a captura de imagem será realizada pela webcam. Caso você tenha mais de uma webcam, você pode alterar o valor do parâmetro para `0` ou `2`.

- A linha `ret, frame = vid.read()` realiza a captura da imagem.

- A linha `cv2.imwrite('image.png', frame)` salva a imagem capturada em um arquivo.

- A linha `image = cv2.cvtColor(cv2.imread("image.png"), cv2.COLOR_BGR2RGB)` realiza a leitura da imagem e a transforma em um array de pixels.

- A linha `decoded_text = qreader.detect_and_decode(image=image)` realiza a leitura do QrCode.

