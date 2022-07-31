#--------------------aba contem logicas dos botoes------------------------#
import pygame
#logica botao pedra
def OpPedra(blockPedra, blockPapel, blockTesoura, player, modoJogo, chave):
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
    return blockPedra, blockPapel, blockTesoura, player, modoJogo, chave
#logica botao papel
def OpPapel(blockPedra, blockPapel, blockTesoura, player, modoJogo, chave):
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
    return blockPedra, blockPapel, blockTesoura, player, modoJogo, chave
#logica botao tesoura
def OpTesoura(blockPedra, blockPapel, blockTesoura, player, modoJogo, chave):
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
    return blockPedra, blockPapel, blockTesoura, player, modoJogo, chave
#logica botao volar para menu
def OpVoltaMenu(Menu,player,bot,blockPedra,blockPapel,blockTesoura,playerVida,botVida,modoJogo,chave,chaveA,botKey,vidaKey,Fim,py,pv,by):
    Menu = True
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
    return Menu,player,bot,blockPedra,blockPapel,blockTesoura,playerVida,botVida,modoJogo,chave,chaveA,botKey,vidaKey,Fim,py,pv,by
#logica botao jogar novamente
def OpReplay(player,bot,blockPedra,blockPapel,blockTesoura,playerVida,botVida,modoJogo,chave,chaveA,botKey,vidaKey,Fim,py,pv,by):
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
    return player,bot,blockPedra,blockPapel,blockTesoura,playerVida,botVida,modoJogo,chave,chaveA,botKey,vidaKey,Fim,py,pv,by

# todas as imagens do jogo
def imagens():
    # carregando imagens
    fundo = pygame.image.load(r'images/cenário/fundo mk.png')
    fundoMenu = pygame.image.load(r'images/cenário/menu-fogov2.png')
    # jogador
    nomejogador = pygame.image.load(r'images/PLAYER/JOGADOR.png')
    pedra = pygame.image.load(r'images/PLAYER/Pedra.png')
    papel = pygame.image.load(r'images/PLAYER/Papel.png')
    tesoura = pygame.image.load(r'images/PLAYER/Tesoura.png')
    # bot
    nomebot = pygame.image.load(r'images/BOT/BOT.png')
    bot0 = pygame.image.load(r'images/BOT/bot0.png')
    botPedra = pygame.image.load(r'images/BOT/botPedra.png')
    botPapel = pygame.image.load(r'images/BOT/botPapel.png')
    botTesoura = pygame.image.load(r'images/BOT/botTesoura.png')
    # mãobig
    bigPedra = pygame.image.load(r'images/bigmão/bigPedra.png')
    bigPapel = pygame.image.load(r'images/bigmão/bigPapel.png')    
    bigTesoura = pygame.image.load(r'images/bigmão/bigTesoura.png')
    # outros
    perde = pygame.image.load(r'images/cenário/perde.png')
    ganha = pygame.image.load(r'images/cenário/ganha.png')
    again = pygame.image.load(r'images/cenário/again.png')
    playBtn = pygame.image.load(r'images/cenário/playBtn.png')
    goToMenu = pygame.image.load(r'images/cenário/goToMenu.png')
    quadrado1 = pygame.image.load(r'images/cenário/quadrados.png')
    quadrado2 = pygame.image.load(r'images/cenário/quadrados.png')
    quadrado3 = pygame.image.load(r'images/cenário/quadrados.png')
    regras = pygame.image.load(r'rules.png')
    setared = pygame.image.load(r'seta vermelha.png')
    setagreen = pygame.image.load(r'seta verde.png')
    # som
    sound_on = pygame.image.load(r'images/cenário/som ligado.png')
    sound_off = pygame.image.load(r'images/cenário/som desligado.png')
    
    


    return fundo, fundoMenu, nomejogador, pedra, papel, tesoura, nomebot, bot0, botPedra, botPapel , botTesoura, bigPedra, bigPapel, bigTesoura, perde, ganha, again, playBtn, goToMenu, quadrado1, quadrado2, quadrado3, regras, setared, setagreen, sound_on, sound_off