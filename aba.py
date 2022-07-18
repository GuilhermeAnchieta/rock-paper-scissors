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