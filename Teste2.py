#implementação da bibliotecas
import pygame
from pygame.locals import *
from random import randint
from time import sleep

#inicia janela do pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('RPS')

#variaveis que guardam jogada do player e bot
player = 0 
bot = randint(1,3)

#carregando imagens
fundo = pygame.image.load(r'images/fundo.png')
pedra = pygame.image.load(r'images/Pedra.png')
papel = pygame.image.load(r'images/Papel.png')
tesoura = pygame.image.load(r'images/Tesoura.png')
#tamanho
pedra = pygame.transform.scale(pedra, (200,200))
papel = pygame.transform.scale(papel, (200,200))
tesoura = pygame.transform.scale(tesoura, (200,200))
while True:

    #para fechar janela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    #reloading da tela
    screen.fill((0,0,0))

    #fundo
    screen.blit(fundo, (0, 0))
    
    #botoes
    screen.blit(pedra, (50,400))
    screen.blit(papel, (200,400))
    screen.blit(tesoura, (350,400))



    #refresh da tela
    pygame.display.update()