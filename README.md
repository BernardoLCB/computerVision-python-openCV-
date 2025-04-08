# 🛬 Detecção de Base de Pouso para Drones
Um sistema em Python utilizando OpenCV para detectar formas geométricas específicas (quadrados, círculos e cruzes) em imagens ou via câmera, com suporte à filtragem de cores (amarelo e azul). O principal objetivo é integrar essa funcionalidade a um drone, permitindo a identificação precisa de bases de pouso.

- [Base de pouso 1](https://github.com/BernardoLCB/Projects/blob/main/computerVision-python(openCV)/inputs/Base_de_Takeoff.png)
  
- [Base de pouso 2](https://github.com/BernardoLCB/Projects/blob/main/computerVision-python(openCV)/inputs/Base_de_Takeoff(2).png)

## 📌 Descrição
Este projeto utiliza processamento de imagem e visão computacional para detectar padrões específicos que representam uma base de pouso. Ele pode ser usado tanto com imagens estáticas quanto com transmissões ao vivo de uma câmera.

## 🛠️ Funcionalidades


- **Detecção de Formas Geométricas**: Detecta quadrados, círculos e cruzes em imagens.
  
- **Filtragem de Cores**: Suporte para filtrar as cores amarelo e azul nas imagens.
  
- **Integração com Drone**: Permite que a detecção de formas seja usada para guiar o drone em direção às bases de pouso.
  
- **Trabalho com Imagens Estáticas ou Ao Vivo**: Permite trabalhar tanto com imagens estáticas (carregadas do disco) quanto com transmissões ao vivo (via câmera), proporcionando flexibilidade no uso do sistema em diferentes cenários.
  
- **Sliders**: Permitem a alteração em tempo real de diversos parâmetros dentro do programa, como:
    - Aplicar filtros de suavização na imagem.
    - Aplicar filtros de morfologia na imagem.
    - Ajustar a dimensão da matriz do elemento estruturante (referente aos filtros de morfologia).
    - Ajustar o brilho da imagem.
    - Aplicar limiarização (threshold) na imagem.
    - Filtrar para detectar somente a cor amarela ou azul na imagem.
    - Controlar a detecção das formas com base em um valor de área.
 

## 📖 História do Projeto

O presente sistema foi desenvolvido como parte do Projeto Prático de Controle e Sistemas Embarcados, no contexto do processo de treinamento para ingressar na Equipe de Robótica Aérea (EDRA) da Universidade de Brasília (UnB). O objetivo principal é adquirir a experiência necessária e se preparar para atuar na área de Controle e Sistemas Embarcados (C&SE), buscando a vaga e a oportunidade de contribuir com inovações e soluções tecnológicas no campo.

A escolha de trabalhar com o tema de Visão Computacional foi motivada pela relevância crescente dessa área na atualidade, que tem se tornado fundamental em diversas aplicações, desde a automação industrial até sistemas de segurança, veículos autônomos, e drones. Embora o projeto não integre diretamente inteligência artificial avançada, como o YOLO (You Only Look Once), ele se baseia em técnicas de processamento de imagem e análise visual, com o objetivo de detectar, interpretar e responder a informações visuais de maneira eficiente.


## 🗂️ Fontes de Pesquisa
Este projeto foi desenvolvido com base em diversas fontes de pesquisa, sendo principalmente fundamentado na leitura da documentação oficial da biblioteca OpenCV, além de fóruns de ajuda e vídeos tutoriais disponíveis no YouTube. Essas fontes foram essenciais para adquirir o conhecimento necessário e garantir a aplicação adequada das ferramentas e técnicas utilizadas no desenvolvimento do sistema.

## 🚀 Como Executar o Projeto

### Pré-requisitos
Antes de começar, certifique-se de que você tem os seguintes itens instalados:

- Python 3.7+
- OpenCV 4.11.0
- NumPy 2.2.3

### Passo a Passo
  
  1. Clone esse repositório
```bash 
git clone https://github.com/BernardoLCB/Projects.git
cd Projects/computerVision-python(openCV)
```
2. Instale as dependências
   
👉 Download [Python](https://www.python.org/downloads/)
```bash
pip install numpy  # Para instalar o NumPy
pip install opencv-python  # Para instalar o OpenCV
```
3. Execute o código
```bash
python main.py
```

## Valores dos Sliders para os Inputs
Segue abaixo os valores necessários para ajustar os sliders de cada entrada, garantindo que o resultado seja validado.
        
1. INPUTS DADOS:
   
   1.jpg # 0/0/0/120/1/2000/2000/2000

   2.jpg # 2/0/0/128/1/2000/2000/2000

   3.jpg # VALIDAR DEPOIS

   4.jpg # 1/0/0/0/1/2000/2000/2000

   5.jpg # NÃO SEI SE TEM VALIDAÇÃO

   6.jpg # VALIDAR DEPOIS

   7.jpg # 1/0/0/69/2/2000/2000/+2000

   8.jpg") # VALIDAR DEPOIS

   9.jpg") # NÃO SEI SE TEM VALIDAÇÃO

   10.jpg # NÃO SEI SE TEM VALIDAÇÃO

   11.jpg # NÃO SEI SE TEM VALIDAÇÃO

   13.jpg # 2/0/0/0/1/2000/2000/2000

   14.jpg # NÃO SEI SE TEM VALIDAÇÃO

   15.jpg # NÃO SEI SE TEM VALIDAÇÃO

   16.jpg # NÃO SEI SE TEM VALIDAÇÃO

   17.png # 0/0/0/2/2000/2000/2000

   18.png # 0/0/0/1/2000/2000/2000

   19.jpg # NÃO SEI SE TEM VALIDAÇÃO

   10.jpg # NÃO SEI SE TEM VALIDAÇÃO

   21.jpg # NÃO SEI SE TEM VALIDAÇÃO

   22.jpg # NÃO SEI SE TEM VALIDAÇÃO

   23.jpg # 1/7/50/112/1/2000/2000/2000
  
3. INPUTS CRIADOS:
   
    1.jpg # 2/0/0/56/2/2000/2000/2000
    
    2.jpg # 1/0/0/94/2/2000/2000/2000
    
    3.jpg # 0/0/0/62/2/1796/10000/10000/10000 ou 1/0/0/62/1/1796/2000/2000/2000
    
    4.jpg # 1/1/4/0/2/2000/2000/2000 ou 1/0/0/0/1/2000/10000/4000
    
    5.jpg # 1/0/0/0/1/2000/2000/2000 ou 2/2/3/66/2/2000/2000/2000
    
    6.jpg # 1/0/0/0/1/2000/2000/2000
    
    7.jpg # 1/0/0/29/2/2000/2000/2000
    
    8.jpg # 1/1/5/15/2/2000/2000/2000
    
    9.jpg # 1/3/14/23/2/2000/2000/2000
    
    10.jpg # 2/1/3/52/2/2000/2000/8728
    
    11.jpg # 0/0/0/0/2/2000/2000/2000

## 📧 Contato
Se tiver alguma dúvida ou sugestão, entre em contato via email: bernardoleinig@gmail.com.
