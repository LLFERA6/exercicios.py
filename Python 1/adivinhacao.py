import random

# numero_secreto = 11
# chute = int(input('Escolha um numero entre 1 e 10: '))

# if chute > numero_secreto:
#     print('Voçe errou !! Tente um Numero menor. ')
# elif chute < numero_secreto: 
#     print('Voçe errou !! Tente um Numero Maior. ')
# else:
#     print('Voçe acertou')

numero_secreto = random.randint(1, 20)
# tentativas = 0

print('Tente adivinhar o número que estou pensando... Entre 1 e 20 ')

for tentativa in range (1, 6):
    chute = int (input("Seu palpites: "))

    if chute < numero_secreto:
     print('Voce errou tente um numero maior')
    elif chute > numero_secreto:
     print("Voçe errou tente um numero menor ")
    else:
     print(f"Acertou em {tentativa} tentativa(s)")
     break 

else: 
  print("Voce no acertou. o numero era {numero_secreto} ")  



# while True:
#     chute = int(input('Seu palpite: '))
#     tentativas += 1

#     if chute < numero_secreto:
#         print('Voce errou! Tente um numero maior ')
#     elif chute > numero_secreto:
#         print('Voçe errou! Tente um menor ')
#     else:
#         print(f'Voçe acertou em {tentativas} tentativa(s)! ')
#         break

