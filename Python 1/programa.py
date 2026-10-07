nome = "Leonardo"
idade = 16
altura = 1.75
print(f'Meu nome é {nome}, tenho {idade} anos e {altura}, de altura')

nome = input('Digite seu nome: ')
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / altura ** 2
print(f"Meu nome {nome}, tenho {idade} anos, {altura} de altura e {peso}, IMC: {imc:.2f}")

