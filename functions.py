import cv2
import numpy as np

#==================================================================================================#

'''Função responsável por aplicar filtros a uma imagem de entrada.'''

def SmoothingFilters(value,img):

    #FILTRO DE GAUSS
    if value == 1:
        mask = (5,5)
        smoothing = 0
        img = cv2.GaussianBlur(img, mask, smoothing)
    
    #FILTRO DE MÉDIA
    elif value == 2:
        mask = (5,5)
        img = cv2.blur(img, mask)
    
    #FILTRO DE MEDIANA
    elif value == 3:
        smoothing = 5
        img = cv2.medianBlur(img,smoothing)
    
    #FILTRO DE CANNY
    elif value == 4:
        thresold1 = 30    
        thresold2 = 120 
        maskSobel = 3 #valor padrão             
        img = cv2.Canny(img, thresold1, thresold2, maskSobel)
    
    return img

#==================================================================================================#

'''Função responsável por determinar a forma geométrica com base no contorno já encontrado.'''

def findShapes(contours, img, hierarquia, sl7, sl8, sl9):
    
    for i, contour in enumerate(contours):
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

        child = hierarquia[0][i][2]

        x, y, w, h = cv2.boundingRect(approx)
        
        #inicializa a variável para armazenar as coordenadas do centro do objeto
        centro_x = None
        centro_y = None

        #verifica a existência do objeto com base na quantidade de pixels que possui 
        M = cv2.moments(contour)
        if M["m00"] != 0:   # Evita divisão por zero
            centro_x = int(M["m10"] / M["m00"])
            centro_y = int(M["m01"] / M["m00"])
    
        
        #o seguinte bloco é responsável por verificar a quantidade de lados do objeto detectado e se o objeto detectado atende a um requisito mínimo de área. Segue a seguinte lógica:
        # 4 lados  --> quadrado
        # 12 lados  -> cruz
        # +12 lados -> círculo
    #---------------------------------------------------------------------------------------------------#
        if (len(approx) == 4 and (w*h >= sl8)):
            
            #verifica se existe dentro do quadrado outra forma (contorno); se não, faz o traçado do quadrado em vermelho; se sim, traça o contorno do quadrado em laranja.
            if child == -1: 
                cv2.drawContours(img, [approx], -1, (0, 0, 255), 2)
            
            else:
                cv2.drawContours(img, [approx], -1, (0, 127, 255), 2)
                cv2.putText(img, "Square", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 127, 255))

                if (centro_x != None) and (centro_y != None):
                    cv2.circle(img,(centro_x, centro_y), 5,(0, 127, 255),-1)

            
        elif (len(approx) == 12 and (((2*w*h) - w**2) >= sl7)):
            cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)
            cv2.putText(img, "Cross", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            cv2.circle(img,(centro_x, centro_y), 5,(0, 255, 0),-1)


        elif len(approx) > 12:
            area_contour = cv2.contourArea(contour)
            (x1, y1), raio = cv2.minEnclosingCircle(contour)
            area_circular = np.pi * (raio**2)
            
            #tolerância de 20%
            if (((area_contour - area_circular) / area_circular < 0.1) and (area_contour >=sl9)):
                    cv2.drawContours(img, [approx], -1, (255, 0, 255), 2)
                    cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255))

                    if (centro_x != None) and (centro_y != None):
                        cv2.circle(img,(centro_x, centro_y), 5,(255, 0, 255),-1)
    #---------------------------------------------------------------------------------------------------#



#==================================================================================================#

'''Função responsável por aplicar operações morfológicas na imagem.'''

def morphologyOperations(img, value, value_matrix):

    x = 100
    y = 100
    
    if value_matrix != 0:

        #erosão: remove ruídos e pequenas estruturas, reduzindo o tamanho dos objetos brancos na imagem.
        if value == 1:
            element_estr = cv2.getStructuringElement(cv2.MORPH_RECT, (value_matrix, value_matrix))
            img = cv2.erode(img, element_estr, iterations = 2)
        
        #dilatação: expande as regiões brancas da imagem, preenchendo pequenos buracos.
        elif value == 2:
            element_estr = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (value_matrix, value_matrix))
            img = cv2.dilate(img, element_estr, iterations=2)

        #abertura: realiza erosão seguida de dilatação, útil para remover pequenos ruídos.
        elif value == 3:
            element_estr = cv2.getStructuringElement(cv2.MORPH_RECT, (value_matrix, value_matrix))
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, element_estr)
        
        #fechamento: realiza dilatação seguida de erosão, útil para fechar buracos em objetos.
        elif value == 4:
            element_estr = cv2.getStructuringElement(cv2.MORPH_RECT, (value_matrix, value_matrix))
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, element_estr)

        #gradiente: obtém o contorno dos objetos ao calcular a diferença entre a dilatação e a erosão.
        elif value == 5:
            element_estr = cv2.getStructuringElement(cv2.MORPH_RECT, (value_matrix, value_matrix))
            img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, element_estr)
        
        #top-hat: realça detalhes menores e variações de intensidade na imagem.
        elif value == 6:
            element_estr = cv2.getStructuringElement(cv2.MORPH_RECT, (value_matrix, value_matrix))
            img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, element_estr)
            
        #black-Hat: destaca regiões escuras em fundos claros.
        elif value == 7:
            element_estr = cv2.getStructuringElement(cv2.MORPH_RECT, (value_matrix, value_matrix))
            img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, element_estr)


    return img
        
#==================================================================================================#

'''Função responsável por filtrar na imagem a cor amarela ou azul. '''

def figureBackgroundColor(img, hsv_img,sl6):

    if sl6 == 0: #converte a imagem original para escala de cinza sem aplicar filtros de cor
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img
    
    elif sl6 == 1: #filtra a cor amarela na imagem
        lower_limit = np.array([20,100,100])
        upper_limit = np.array([40,255,255]) #100 , 255, 255
        mask = cv2.inRange(hsv_img, lower_limit, upper_limit)
        result = cv2.bitwise_and(img, img, mask=mask)
        img = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        return img


    elif sl6 == 2: #filtra a cor azul na imagem
        lower_limit = np.array([100, 100, 100])
        upper_limit = np.array([140, 255, 255])
        mask = cv2.inRange(hsv_img, lower_limit, upper_limit)
        result = cv2.bitwise_and(img, img, mask=mask)
        img = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        return img
    


#==================================================================================================#

'''Função responsável por garantir que imagens com menos ou mais de 3 canais possam ser agrupadas e exibidas em uma única janela.'''

def assemblingImages(img1, img2, img3, img4, sl1, sl2):

    img1 = np.stack((img1,)*3, axis=-1)
    img2 = np.stack((img2,)*3, axis=-1)

    #-------------------------------------------------------------------------------------------------------------#
    
    # Exibe na imagem o nome do filtro selecionado pelo usuário na seção "smoothing filters"
    if sl1 == 0:
        cv2.putText(img1, "NormalImage", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    elif sl1 == 1:
        cv2.putText(img1, "GaussFilter", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    
    elif sl1 == 2:
        cv2.putText(img1, "BluerFilter", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    
    elif sl1 == 3:
        cv2.putText(img1, "MedianFilter", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    elif sl1 == 4:
        cv2.putText(img1, "CannyFilter", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    #-------------------------------------------------------------------------------------------------------------#

    # Exibe na imagem o nome do filtro selecionado pelo usuário na seção "morphology filters"
    if sl2 == 0:
         cv2.putText(img1, "NormalImage", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    elif sl2 == 1:
        cv2.putText(img1, "Erosion", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    elif sl2 == 2:
        cv2.putText(img1, "Dilation", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    elif sl2 == 3:
        cv2.putText(img1, "Open", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    elif sl2 == 4:
        cv2.putText(img1, "Close", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    
    elif sl2 == 5:
        cv2.putText(img1, "Gradiente", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    elif sl2 == 6:
        cv2.putText(img1, "Top-Hat", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    elif sl2 == 7:
        cv2.putText(img1, "Black-Hat", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

     #-------------------------------------------------------------------------------------------------------------#

    images = [img4, img1, img2 ,img3]
    img_stack = np.hstack(images)
    return img_stack