#--------------------aba contem logicas dos botoes------------------------#
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