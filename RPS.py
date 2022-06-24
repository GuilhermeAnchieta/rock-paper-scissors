from random import randint
from time import sleep
#implementação da logica simples, pode mudar como quiser


#variaveis que guardam jogada do player e bot
player = 0
#escolhe um numero entre 1 e 3 
bot = randint(1,3)

titulo = "Pedra Papel Tesoura"
#pergunta se vai querer continuar vazia
again = ' '


#essse print embaixo faz criar uma linha sempre do tamanho do titulo 
print('\n\n')
print(f"{'=' * (len(titulo)+6)}")
print(f"   {titulo}")
print(f"{'=' * (len(titulo)+6)}")

while again not in 'não':
  print("\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\n")

  # caso coloque outra opção 
  try:
    player = int(input("Faça sua escolha: "))
    if (player != 1) and (player != 2) and (player != 3):
      print('\nERRO!!\n\n')
      continue
    #trata o erro de digitar letras 
  except ValueError:
    print("\nERRO! Digite uma opção válida\n\n")
    continue

  #biblioteca o "f" serve pra fazer o print formatado 
  ops = {1:"Pedra", 2:"Papel", 3:"Tesoura"}

  print(f"\nVocê escolheu: {ops[player]}\nmaquina escolheu: {ops[bot]}")
  #empate
  if player == bot:
    print("\nUAU!!! Aconteceu um empate!")

  #casos de que o jogador vence  
  elif (player == 1 and bot == 3) or (player == 2 and bot == 1) or (player == 3 and bot == 2):
    print("\nPARABÉNS!!! Você ganhou!\n\n")
  else:
    print("\nNÂOOOO!!! Você perdeu!\n\n")
  
  #só prosegue quando o jogar escreve certo 
  while True:
    again = input("\nVocê deseja jogar de novo [sim] ou [não]: ").strip().lower()[0]
    if again not in 'sn':
      print("Opa, essa opção não é válida.\n")
    else:
      break 


    
 