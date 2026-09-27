import random 

gerador = random.randint(1,100)
tentativas = 1
jogador = int(input("Escolha um numero de 1 até 100:\n"))
if jogador < 1 or jogador > 100:
    print("Este numero não está entre os sorteados! Escolha outro.")    
while jogador!=gerador:
    if jogador > gerador:
        print("Numero maior que o sorteado.")
        print(f"{tentativas}/10")
        print()
        tentativas += 1
        jogador = int(input("Tente outro numero!\n"))
    elif jogador < gerador:
        print("Numero menor que o sorteado.")
        print(f"{tentativas}/10")
        print()
        tentativas += 1
        jogador = int(input("Tente outro numero:\n"))
    if tentativas > 10:
        break
    if jogador < 1 or jogador > 100:
     print("Este numero não está entre os sorteados! Escolha outro.")        
if jogador == gerador:
  print("Parabéns, você acertou!")
  print(f"{tentativas}/10")
  print("Encerrando o programa...")
else:
  print("Você perdeu!numero de tentativas atingidas.")
  print()
  print(f"{tentativas}/10")
  print("Encerrando o programa...")
         

    
