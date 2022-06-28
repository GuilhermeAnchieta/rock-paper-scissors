#implementação da bibliotecas
import pygame
from pygame.locals import *
from random import randint

#inicia janela do pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('PedraPapelTesoura')

#jogada e vida do player e bot
player = 0
bot = 0
playerVida = 200
botVida = 200

#randint(1,3)
#estado do jogo, pra definir quando pode clicar ou nao
modoJogo = True
#chave pra deixar bot escolher
chave = True
chaveA = 0
botKey = False
vidaKey = False
Fim = False
#posição pra animar mao
py = 150
pv = 2.5
by = 150

#carregando imagens
fundo = pygame.image.load(r'images/fundoa.png')

#jogador
nomejogador = pygame.image.load(r'images/PLAYER/JOGADOR.png')
pedra = pygame.image.load(r'images/PLAYER/Pedra.png')
papel = pygame.image.load(r'images/PLAYER/Papel.png')
tesoura = pygame.image.load(r'images/PLAYER/Tesoura.png')
#bot
nomebot = pygame.image.load(r'images/BOT/BOT.png')
bot0 = pygame.image.load(r'images/BOT/bot0.png')
botPedra = pygame.image.load(r'images/BOT/botPedra.png')
botPapel = pygame.image.load(r'images/BOT/botPapel.png')
botTesoura = pygame.image.load(r'images/BOT/botTesoura.png')
#mãobig
bigPedra = pygame.image.load(r'images/bigmão/bigPedra.png')
bigPapel = pygame.image.load(r'images/bigmão/bigPapel.png')
bigTesoura = pygame.image.load(r'images/bigmão/bigTesoura.png')
#outros
perde = pygame.image.load(r'images/perde.png')
ganha = pygame.image.load(r'images/ganha.png')
again = pygame.image.load(r'images/again.png')

#tamanho das imagens
pedra = pygame.transform.scale(pedra, (200,205))
papel = pygame.transform.scale(papel, (200,205))
tesoura = pygame.transform.scale(tesoura, (200,205))
bigPedra = pygame.transform.scale(bigPedra, (150,150))
bigTesoura = pygame.transform.scale(bigTesoura, (200,150))
bigPapel = pygame.transform.scale(bigPapel, (200,150))
bot0 = pygame.transform.scale(bot0, (150,150))
botPedra = pygame.transform.scale(botPedra, (150,150))
botPapel = pygame.transform.scale(botPapel, (150,150))
botTesoura = pygame.transform.scale(botTesoura, (150,150))

#loop principal
while True:

    #pega posição do mouse
    x, y = pygame.mouse.get_pos()

    #para imput de botoes e clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if modoJogo == True:
                if x < 190 and x > 80 and y > 440 and y < 580:
                    player = 1
                    modoJogo = False
                    chave = False
                elif x < 340 and x > 250 and y > 440 and y < 580:
                    player = 2
                    modoJogo = False
                    chave = False
                elif x < 490 and x > 390 and y > 440 and y < 580:
                    player = 3
                    modoJogo = False
                    chave = False
            #reset do jogo
            if Fim == True:
                if x < 360 and x > 240 and y > 300 and y < 415:
                    print ("hi")
                    player = 0
                    bot = 0
                    playerVida = 200
                    botVida = 200
                    modoJogo = True
                    chave = True
                    chaveA = 0
                    botKey = False
                    vidaKey = False
                    Fim = False
                    py = 150
                    pv = 3
                    by = 150

    #reloading da tela
    screen.fill((0,0,0))
    
    #fundo
    screen.blit(fundo, (0, 0))

    #botoes
    screen.blit(pedra, (70,417))
    screen.blit(papel, (205,405))
    screen.blit(tesoura, (350,400))

    #mostra imagem player e animação da mao
    if player == 0:
        screen.blit(bigPedra, (50,py))  
    if chave == False:
        screen.blit(bigPedra, (50,py))
        bot = 0
        py -= pv
        if py < 100 or py >= 150:
            pv *= -1
            chaveA +=1
        if chaveA >= 6:
            chaveA = 0
            chave = True
            botKey = True
        
    if chave == True:
        if player == 1:
            screen.blit(bigPedra, (50,150))
        elif player == 2:
            screen.blit(bigPapel, (50,150))
        elif player == 3:
            screen.blit(bigTesoura, (50,150))
        modoJogo = True

    #escolha do bot,
    if botKey == True:
        vidaKey = True
        bot = randint(1,3)
        botKey = False
    #mostra imagem bot
    if bot == 0:
        screen.blit(bot0, (400,by))
    elif bot == 1:
        screen.blit(botPedra, (400,150))
    elif bot == 2:
        screen.blit(botPapel, (400,150))
    elif bot == 3:
        screen.blit(botTesoura, (400,150))

    #logica de ganha/perde
    if vidaKey == True:
        vidaKey = False
        if player == bot:
            playerVida -= 5
            botVida -= 5
        elif (player == 1 and bot == 3) or (player == 2 and bot == 1) or (player == 3 and bot == 2):
            botVida -= 20
        else:
            playerVida -= 20

    #vidas
    ajuste = 200-botVida
    pygame.draw.rect(screen, (80,0,0), [50,50,200,20], 0)
    pygame.draw.rect(screen, (80,0,0), [350,50,200,20], 0)
    pygame.draw.rect(screen, (250,0,0), [50,50,playerVida,20], 0)
    pygame.draw.rect(screen, (250,0,0), [350+ajuste,50,botVida,20], 0)

    #nome do jogador e do bot
    screen.blit(nomejogador, (10, 49))
    screen.blit(nomebot, (453, 49))
    
    #caso ganhe ou perca
    if playerVida <= 0:
        if py < 600:
            py+=3
            modoJogo = False
        player = 0
        Fim = True
        screen.blit(perde, (50,150))
    if botVida <= 0:
        if by < 600:
            by+=3
            modoJogo = False
        bot = 0
        Fim = True
        screen.blit(ganha, (350,150))

    #para jogar novamente
    if Fim == True:
        screen.blit(again, (240,300))
    #refresh da tela
    pygame.display.update()