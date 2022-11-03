import pygame 
import sys 
from pygame.locals import *
from mapa import mapa 

mapabusca = mapa

def desenhar():
    
    pygame.init()#inicializa pygame

    #Define a dimensão da tela com display.set_mode()
    tela  = pygame.display.set_mode((500, 300)) #Display

    # Carregue a imagem de fundo aqui. Verifique se o arquivo existe!
    BackGround = pygame.image.load("peacefulwallpaper.jpg")

    pygame.display.set_caption('Algoritmo busca') #Definir a legenda da janela atual


    while True:

        #desenha a imagem nas coordenadas iniciais
        tela.blit(BackGround, (0, 0))

        tela.fill((0, 0, 0)) # Limpa tela (tela preta)

        x, y = pygame.mouse.get_pos()

        for i in mapa:
            print(str (i) + str(mapabusca[i][0].descricao))

            #pygame.draw.rect desenhe um retângulo
            pygame.draw.rect(tela, mapa[i][0].cor, [mapa[i][1]*35, mapa[i][2]*35, 35, 35])
            
        #pygame.draw.rect(tela, (200, 200, 200), [mapa[76][3] * 35, mapa[76][2] * 35, 35, 25])

        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()


        pygame.display.update()


desenhar()
