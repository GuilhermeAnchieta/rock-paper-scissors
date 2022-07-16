import pygame
from Jogo import Menu_music
from Jogo import button
def botoes():
    # pega posição do mouse
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # erro: criar variavel de rodada para ficar duas e não só uma
        if event.type == pygame.MOUSEBUTTONUP:
            if Menu == True and x > 240 and x < 360 and y > 250 and y < 366:
                Menu = False
                #inicia musica 
                Menu_music.stop()
                pygame.mixer.music.play(-1)

            if modoJogo == True:
                    
                if x < 190 and x > 80 and y > 440 and y < 580 and blockPedra < 3:
                    button.play()
                    blockPedra += 1
                    if blockPapel == 2:
                        blockPapel -= 1
                    if blockTesoura == 2:
                        blockTesoura -= 1
                    player = 1
                    modoJogo = False
                    chave = False
                    if blockTesoura == 3:
                        blockTesoura += 1
                    elif blockTesoura == 4:
                        blockTesoura = 1
                    if blockPapel == 3:
                        blockPapel += 1
                    elif blockPapel == 4:
                        blockPapel = 1
                            
                elif x < 340 and x > 250 and y > 440 and y < 580 and blockPapel < 3:
                    button.play()
                    blockPapel += 1
                    if blockPedra == 2:
                        blockPedra -= 1
                    if blockTesoura == 2:
                        blockTesoura -= 1
                    player = 2
                    modoJogo = False
                    chave = False
                    if blockPedra == 3:
                        blockPedra += 1
                    elif blockPedra == 4:
                        blockPedra = 1
                    if blockTesoura == 3:
                        blockTesoura += 1
                    elif blockTesoura == 4:
                        blockTesoura = 1
                    
                elif x < 490 and x > 390 and y > 440 and y < 580 and blockTesoura < 3:
                    button.play()
                    blockTesoura += 1
                    if blockPedra == 2:
                        blockPedra -= 1
                    if blockPapel == 2:
                        blockPapel -= 1
                    player = 3
                    modoJogo = False
                    chave = False
                    if blockPedra == 3:
                        blockPedra += 1
                    elif blockPedra == 4:
                        blockPedra = 1
                    if blockPapel == 3:
                        blockPapel += 1
                    elif blockPapel == 4:
                        blockPapel = 1
                        
            # reset do jogo
            if Fim == True:
                #voltar pro menu
                if x < 428 and x > 313 and y > 300 and y < 415:
                    Menu = True
                    pygame.mixer.music.stop()
                    player = 0
                    bot = 0
                    blockPedra = 1
                    blockPapel = 1
                    blockTesoura = 1
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
                # jogar de novo 
                if x < 286 and x > 170 and y > 300 and y < 415:
                    player = 0
                    bot = 0
                    blockPedra = 1
                    blockPapel = 1
                    blockTesoura = 1
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