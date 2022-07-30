#//////////iniciando variaveis e importaçoes////////////#

# implementação da bibliotecas
import pygame
from pygame.locals import *
from random import randint
# importando outras abas 
import aba
# inicia janela do pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('PedraPapelTesoura')

# jogada e vida do player e bot
player = 0 
bot = 0 
playerVida = 200
botVida = 200

# estado do jogo, pra definir quando pode clicar ou nao
modoJogo = True
Menu = True
# chave pra deixar bot escolher
chave = True
chaveA = 0
botKey = False
vidaKey = False
Fim = False
# posição pra animar mao
py = 150
pv = 2.5
by = 150
tv = 0.1
#animacao de titulo
textMuve = 20
textMove = 600
textMoveKey = False
TextRotate = 0
textGrau = 0.01
# bloqueador de opção
blockPedra = 1
blockPapel = 1
blockTesoura = 1
# som On/off
som = True

# importa todas as imagens do jogo 
fundo, fundoMenu, nomejogador, pedra, papel, tesoura, nomebot, bot0, botPedra, botPapel , botTesoura, bigPedra, bigPapel, bigTesoura, perde, ganha, again, playBtn, goToMenu, quadrado1, quadrado2, quadrado3, sound_on, sound_off = aba.imagens()

# tamanho das imagens
pedra = pygame.transform.scale(pedra, (200, 205))
papel = pygame.transform.scale(papel, (200, 205))
tesoura = pygame.transform.scale(tesoura, (200, 205))
bigPedra = pygame.transform.scale(bigPedra, (150, 150))
bigTesoura = pygame.transform.scale(bigTesoura, (200, 150))
bigPapel = pygame.transform.scale(bigPapel, (200, 150))
bot0 = pygame.transform.scale(bot0, (150, 150))
botPedra = pygame.transform.scale(botPedra, (150, 150))
botPapel = pygame.transform.scale(botPapel, (150, 150))
botTesoura = pygame.transform.scale(botTesoura, (150, 150))
sound_on = pygame.transform.scale(sound_on, (50, 50))
sound_off = pygame.transform.scale(sound_off, (50, 50))


#iniciando textos 
pygame.font.init()
cor_branca = (255, 255, 255)
font = pygame.font.get_default_font()
cont = pygame.font.SysFont(font, 45)

# iniciando musicas 
pygame.mixer.init()

# musicas e sons 
trilha = pygame.mixer.Sound(r'audio/trilha-game.wav')
Menu_music = pygame.mixer.Sound(r'audio/menu musica.wav')
button = pygame.mixer.Sound(r'audio/botão click.wav')

#Volume
pygame.mixer.Sound.set_volume(trilha, 0.4) #trilha 
pygame.mixer.Sound.set_volume(Menu_music, 0.1) # Menu
pygame.mixer.Sound.set_volume(button, 0.2) # button

#//////////loop principal do jogo, e utilização de todas variaveis////////////#

# loop principal
while True:
    # para imput de botoes e clicks
        # pega posição do mouse
    x, y = pygame.mouse.get_pos()
    #print ("y: ", y)

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # erro: criar variavel de rodada para ficar duas e não só uma
        if event.type == pygame.MOUSEBUTTONUP:
            # som do jogo 
            if  x > 552 and  x < 597 and y > 552 and y < 595:
                if som == True:
                    som = False
                    Menu_music.stop()
                    trilha.stop()
                elif som == False:
                    som = True
                    if Menu == True:
                        Menu_music.play(-1)
                    elif Menu == False:
                        trilha.play(-1)

            #botao menu
            if Menu == True and x > 240 and x < 360 and y > 250 and y < 366:
                Menu = False
                #inicia musica 
                Menu_music.stop()
                if som == True:
                    trilha.play(-1)
            if Menu == True and textMoveKey == False and x > 550 and y > 290 and y < 340:
                textMoveKey = True
            elif Menu == True and textMoveKey == True and x > 550 and y > 290 and y < 340:
                textMoveKey = False
            #logica dos botoes
            if modoJogo == True:
                if x < 190 and x > 80 and y > 440 and y < 580 and blockPedra < 3:
                    button.play()
                    blockPedra, blockPapel, blockTesoura, player, modoJogo, chave = aba.OpPedra(blockPedra, blockPapel, blockTesoura, player, modoJogo, chave)
                    
                elif x < 340 and x > 250 and y > 440 and y < 580 and blockPapel < 3:
                    button.play()
                    blockPedra, blockPapel, blockTesoura, player, modoJogo, chave = aba.OpPapel(blockPedra, blockPapel, blockTesoura, player, modoJogo, chave)
                    
                elif x < 490 and x > 390 and y > 440 and y < 580 and blockTesoura < 3:
                    button.play()
                    blockPedra, blockPapel, blockTesoura, player, modoJogo, chave = aba.OpTesoura(blockPedra, blockPapel, blockTesoura, player, modoJogo, chave)
                        
            # reset do jogo
            if Fim == True:
                #voltar pro menu
                if x < 428 and x > 313 and y > 300 and y < 415:
                    trilha.stop()
                    Menu,player,bot,blockPedra,blockPapel,blockTesoura,playerVida,botVida,modoJogo,chave,chaveA,botKey,vidaKey,Fim,py,pv,by = aba.OpVoltaMenu(Menu,player,bot,blockPedra,blockPapel,blockTesoura,playerVida,botVida,modoJogo,chave,chaveA,botKey,vidaKey,Fim,py,pv,by)
                # jogar de novo 
                if x < 286 and x > 170 and y > 300 and y < 415:
                    player,bot,blockPedra,blockPapel,blockTesoura,playerVida,botVida,modoJogo,chave,chaveA,botKey,vidaKey,Fim,py,pv,by = aba.OpReplay(player,bot,blockPedra,blockPapel,blockTesoura,playerVida,botVida,modoJogo,chave,chaveA,botKey,vidaKey,Fim,py,pv,by) 
                           
    # reloading da tela
    screen.fill((0, 0, 0))
    
    #menu
    if Menu == True:
        if som == True:
            Menu_music.play(-1)
        #fundo
        screen.blit(fundoMenu, (0, 0))
        screen.blit(playBtn, (240, 250))
        #titulp
        font = pygame.font.SysFont(None, 80)
        text = font.render('Rock Paper Scissors', True, (10,25,55))
        text = pygame.transform.rotate(text, TextRotate)
        screen.blit(text, (20, textMuve))
        textMuve += tv
        TextRotate+=textGrau
        if TextRotate > 10 or TextRotate < -10:
            textGrau*=-1
        if textMuve > 150 or textMuve < 5:
            tv *= -1
        #devs
        font = pygame.font.SysFont(None, 30)
        img = font.render('SuperDevs: GuilhermeAnchieta and JoaoBRBR', True, (50,50,50))
        screen.blit(img, (20, 580))
        #area de como jogar
        font = pygame.font.SysFont(None, 30)
        img = font.render('Texto de Exemplo', True, (10,10,50))
        screen.blit(img, (textMove, 240))
        img = font.render('Texto de Exemplo', True, (10,10,50))
        screen.blit(img, (textMove, 270))
        img = font.render('Texto de Exemplo', True, (10,10,50))
        screen.blit(img, (textMove, 300))
        img = font.render('Texto de Exemplo', True, (10,10,50))
        screen.blit(img, (textMove, 330))
        if textMoveKey:
            if textMove > 370:
                textMove-=1
        elif textMove < 600:
            textMove+=1
        font = pygame.font.SysFont(None, 80)
        if textMoveKey:
            img = font.render('>', True, (200,0,0))
            screen.blit(img, (570, 280))
        else:
            img = font.render('<', True, (0,200,0))
            screen.blit(img, (570, 280))
    #jogo
    elif Menu == False:
        screen.blit(fundo, (0, 0))
        # quadrado preto
        screen.blit(quadrado1, (90, 435))
        screen.blit(quadrado2, (230, 435))
        screen.blit(quadrado3, (370, 435))
        # botoes
        screen.blit(pedra, (70, 4113))
        screen.blit(papel, (205, 400))
        screen.blit(tesoura, (350, 400))

        # mostra imagem player e animação da mao
        if player == 0:
            screen.blit(bigPedra, (50, py))
        if chave == False:
            screen.blit(bigPedra, (50, py))
            bot = 0
            py -= pv
            if py < 100 or py >= 150:
                pv *= -1
                chaveA += 1
            if chaveA >= 6:
                chaveA = 0
                chave = True
                botKey = True

        if chave == True:
            if player == 1:
                screen.blit(bigPedra, (50, 150))
            elif player == 2:
                screen.blit(bigPapel, (50, 150))
            elif player == 3:
                screen.blit(bigTesoura, (50, 150))
            modoJogo = True
        # quadrado preto
        if blockPedra < 3:
            screen.blit(quadrado1, (90, 435))
        if blockPapel < 3:
            screen.blit(quadrado2, (230, 435))
        if blockTesoura < 3:
            screen.blit(quadrado3, (370, 435))
        # botoes
        screen.blit(pedra, (70, 412))
        if blockPedra > 2:
            screen.blit(quadrado1, (90, 435))
        screen.blit(papel, (205, 405))
        if blockPapel > 2:
            screen.blit(quadrado2, (230, 435))
        screen.blit(tesoura, (350, 400))
        if blockTesoura > 2:
            screen.blit(quadrado3, (370, 435))

        # contador dos botões 
        text = cont.render(f'{blockPedra}', True, cor_branca)
        screen.blit(text, (90,435))
        text = cont.render(f'{blockPapel}', True, cor_branca)
        screen.blit(text, (230,435))
        text = cont.render(f'{blockTesoura}', True, cor_branca)
        screen.blit(text, (370,435))

        # escolha do bot,
        if botKey == True:
            vidaKey = True
            bot = randint(1, 3)
            botKey = False
        # mostra imagem bot
        if bot == 0:
            screen.blit(bot0, (400, by))
        elif bot == 1:
            screen.blit(botPedra, (400, 150))
        elif bot == 2:
            screen.blit(botPapel, (400, 150))
        elif bot == 3:
            screen.blit(botTesoura, (400, 150))

        # vidas
        ajuste = 200-botVida
        pygame.draw.rect(screen, (80, 0, 0), [50, 50, 200, 20], 0)
        pygame.draw.rect(screen, (80, 0, 0), [350, 50, 200, 20], 0)
        pygame.draw.rect(screen, (250, 0, 0), [50, 50, playerVida, 20], 0)
        pygame.draw.rect(screen, (250, 0, 0), [350+ajuste, 50, botVida, 20], 0)

        # nome do jogador e do bot
        screen.blit(nomejogador, (10, 49))
        screen.blit(nomebot, (453, 49))

        # logica de ganha/perde
        if vidaKey == True:
            vidaKey = False
            if player == bot:
                playerVida -= 5
                botVida -= 5
            elif (player == 1 and bot == 3) or (player == 2 and bot == 1) or (player == 3 and bot == 2):
                if player == 1:
                    botVida -= 20
                elif player == 2:
                    botVida -= 10
                elif player == 3:
                    botVida -= 30
            else:
                if bot == 1:
                    playerVida -= 20
                elif bot == 2:
                    playerVida -= 10
                elif bot == 3:
                    playerVida -= 30

        # caso ganhe ou perca
        if playerVida <= 0:
            if py < 600:
                py += 3
                modoJogo = False
            player = 0
            Fim = True
            screen.blit(perde, (50, 150))
        if botVida <= 0:
            if by < 600:
                by += 3
                modoJogo = False
            bot = 0
            Fim = True
            screen.blit(ganha, (350, 150))

        # para jogar novamente
        if Fim == True:
            screen.blit(again, (170, 300))
            screen.blit(goToMenu, (310, 300))
    # Imagens som on/off
    if som == True:
        screen.blit(sound_on, (549, 550))
    else:
        screen.blit(sound_off, (549, 550))

    # refresh da tela
    pygame.display.update()
