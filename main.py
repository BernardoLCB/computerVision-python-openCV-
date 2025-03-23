import cv2
import numpy as np
import sys
import os
from functions import SmoothingFilters, findShapes, assemblingImages, morphologyOperations, figureBackgroundColor

caminho_atual = os.path.dirname(__file__)

print(f"caminho --> {caminho_atual}")

caminho_imagem_exemplos_dados = os.path.join(caminho_atual, "inputs", "chosen")
caminho_imagem_exemplos_criados = os.path.join(caminho_atual, "inputs", "meus_inputs")

print(f"caminho final até a imagem --> {caminho_imagem_exemplos_dados}")
print(f"caminho final até a imagem --> {caminho_imagem_exemplos_criados}")

#=====================================================================#

def nothing(x):
    pass

#=====================================================================#

print("[ 0 ] --> DETECTAR USANDO A CAMERA")
print("[ 1 ] --> DETECTAR UM ARQUIVO DE IMAGEM")

choice = int(input("ESCOLHA UMA DAS OPCOES: "))

if choice == 0:
    cap = cv2.VideoCapture(0)
    frame_time = 100
else:
    frame_time = 300

#=====================================================================#

cv2.namedWindow("CONTROL", cv2.WINDOW_NORMAL)
cv2.namedWindow("IMAGES", cv2.WINDOW_NORMAL)

cv2.createTrackbar("Sm.FT", "CONTROL", 0, 4, nothing)
cv2.createTrackbar("Morph.FT", "CONTROL", 0, 7, nothing)
cv2.createTrackbar("Matrix.Num", "CONTROL", 0, 50, nothing)
cv2.createTrackbar("Threshold", "CONTROL", 0, 255, nothing)
cv2.createTrackbar("Color", "CONTROL", 0, 2, nothing)
cv2.createTrackbar("Ar.Cross", "CONTROL", 2000, 100000, nothing)
cv2.createTrackbar("Ar.Square", "CONTROL", 2000, 100000, nothing)
cv2.createTrackbar("Ar.Circle", "CONTROL", 2000, 100000, nothing)

#=====================================================================#

while (True):
    
    if choice == 0:
        ret, sorce_image = cap.read()

        if sorce_image is None:
            sys.exit("ERROR: COULD NOT FIND CAMERA")

    else:

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/1.jpg") # 0/0/0/120/1/2000/2000/2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/2.jpg") # 2/0/0/128/1/2000/2000/2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/3.jpg") # VALIDAR DEPOIS

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/4.jpg") # 1/0/0/0/1/2000/2000/2000
        
        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/5.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/6.jpg") # VALIDAR DEPOIS

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/7.jpg") # 1/0/0/69/2/2000/2000/+2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/8.jpg") # VALIDAR DEPOIS

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/9.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/10.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/11.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/13.jpg") # 2/0/0/0/1/2000/2000/2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/14.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/15.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/16.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/17.png") # 0/0/0/2/2000/2000/2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/18.png") # 0/0/0/1/2000/2000/2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/19.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/10.jpg") # NÃO SEI SE TEM VALIDAÇÃO
        
        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/21.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/22.jpg") # NÃO SEI SE TEM VALIDAÇÃO

        # sorce_image = cv2.imread(caminho_imagem_exemplos_dados + "/23.jpg") # 1/7/50/112/1/2000/2000/2000

        # #--------------------------------------------------------------------------------------#

        #sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/1.jpg") # 2/0/0/56/2/2000/2000/2000
        
        # sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/2.jpg") # 1/0/0/94/2/2000/2000/2000
        
        # sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/3.jpg") # 0/0/0/62/2/1796/10000/10000/10000 ou 1/0/0/62/1/1796/2000/2000
        
        # sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/4.jpg") # 1/1/4/0/2/2000/2000/2000 ou 1/0/0/0/1/2000/10000/4000
        
        # sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/5.jpg") # 1/0/0/0/1/2000/2000/2000 ou 2/2/3/66/2/2000/2000/2000
        
        # sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/6.jpg") # 1/0/0/0/1/2000/2000/2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/7.jpg") # 1/0/0/29/2/2000/2000/2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/8.jpg") # 1/1/5/15/2/2000/2000/2000

        # sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/9.jpg") # 1/3/14/23/2/2000/2000/2000

        sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/10.jpg") # 2/1/3/52/2/2000/2000/8728
        
        #sorce_image = cv2.imread(caminho_imagem_exemplos_criados + "/11.jpg") # 0/0/0/0/2/2000/2000/2000
    

        if sorce_image is None:
            sys.exit("ERROR: COULD NOT READ THE IMAGE")

    

    sorce_image_copy = sorce_image.copy()

    hsv_sorce_image = cv2.cvtColor(sorce_image, cv2.COLOR_BGR2HSV)
    #-------------------------------------------------------------------------------------------------------#


    #-----------------------------------FUNCIONAMENTO DOS SLIDERS--------------------------------------------#
    sliders1 = cv2.getTrackbarPos("Sm.FT", "CONTROL")               # responsável por aplicar os filtros de suavização
    sliders2 = cv2.getTrackbarPos("Morph.FT", "CONTROL")            # responsável por aplicar os filtros de morfologia
    sliders3 = cv2.getTrackbarPos("Matrix.Num", "CONTROL")          # responsável por definir a dimensão da matriz do elemento estruturante
    sliders5 = cv2.getTrackbarPos("Threshold", "CONTROL")           # responsável por aplicar o número do limiar na imagem
    sliders6 = cv2.getTrackbarPos("Color", "CONTROL")               # responsável por fazer com que somente a cor amarela ou azul seja identificada na imagem
    sliders7 = cv2.getTrackbarPos("Ar.Cross", "CONTROL")            # responsável por exibir as cruzes de acordo com a área definida
    sliders8 = cv2.getTrackbarPos("Ar.Square", "CONTROL")           # responsável por exibir os quadrados de acordo com a área definida
    sliders9 = cv2.getTrackbarPos("Ar.Circle", "CONTROL")           # responsável por exibir os círculos de acordo com a área definida

    #--------------------------------------------------------------------------------------------------------#

    #---------------------REALIZANDO A DETECÇÃO DE COR, ISOLANDO A AMARELA OU AZUL-------------------------------
    gray_image = figureBackgroundColor(sorce_image, hsv_sorce_image, sliders6)
    
    #---------------------APLICANDO FILTROS DE SUAVIZAÇÃO-------------------------------
    gray_image = SmoothingFilters(sliders1, gray_image)                                 
    
    #---------------------APLICANDO FILTROS MORFOLÓGICOS-------------------------------
    gray_image = morphologyOperations(gray_image, sliders2, sliders3)

    #----------------------BINARIZANDO A IMAGEM PARA QUE POSSAMOS UTILIZAR O MÉTODO QUE ENCONTRA OS CONTORNOS-------------------
    _,binarized_image = cv2.threshold(gray_image, sliders5, 255, cv2.THRESH_BINARY) 

    #----------------------ENCONTRANDO OS CONTORNOS NA IMAGEM BINARIZADA----------------------
    contours,hierarquia = cv2.findContours(binarized_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #----------------------TRAÇANDO OS CONTORNOS ENCONTRADOS NA IMAGEM BINARIZADA----------------------
    gray_image_copy = gray_image.copy()
    gray_image_copy = np.stack((gray_image_copy,)*3, axis=-1)
    
    findShapes(contours, gray_image_copy, hierarquia, sliders7, sliders8, sliders9)
    
    #----------------------ESTRUTURANDO AS IMAGENS DE MODO QUE POSSAM SER USADAS EM UMA PILHA DE EXIBIÇÃO----------------------
    img_stack = assemblingImages(gray_image, binarized_image, gray_image_copy ,sorce_image_copy, sliders1, sliders2)
    cv2.imshow("IMAGES", img_stack)
    
    
    cv2.waitKey(frame_time) 