import pygame
from pygame.locals import *

def desenhar():
    
    pygame.init()#inicializa pygame

    clock = pygame.time.Clock()

    #Define a dimensão da tela com display.set_mode()
    tela = pygame.display.set_mode((1280, 720)) 

    # Carregue a imagem de fundo aqui. Verifique se o arquivo existe!
    BackGround = pygame.image.load("peacefulwallpaper.jpg")

    pygame.display.set_caption('Algoritmo busca') #Definir a legenda da janela atual


    while True:

        clock.tick(60)

        tela.blit(BackGround, (0, 0))

        x, y = pygame.mouse.get_pos()


        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()


        pygame.display.update()


desenhar()
