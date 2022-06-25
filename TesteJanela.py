# importando coisas
import pygame
from pygame.locals import *

#iniciando janela
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('testando')

#carregando imagens
image = pygame.image.load(r'maoTodas.jpg')

#variaveis posiciones e movimento
y = 50
v = 0.1

while True:

    #sobe e desce
    y += v
    if y < 20 or y > 80:
        v = v * -1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    #coisas na tela:
    screen.fill((0,255,0))
    
    screen.blit(image, (0, y))
    
    pygame.display.update()
