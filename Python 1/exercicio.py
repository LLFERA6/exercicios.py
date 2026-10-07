# 1 - peca o nome e idade e mostre: "____, daqui ha 10 anos vc tera X anos"
# 2 - peca uma temperatura em celcius e converta para faherenheit (F = C * 9/5 + 32)
# 3 - peca a base e a altura de um retangulo e mostre a area e o perimetro
# 4 - peca 3 notas e mostre a media
# 5 - refacaa calculadora IMC, colocando o seguite:
# Menor que 18,5: abaixo do peso
# 18,5 a 24,9: peso normal ou adequado
# 25,0 a 29,9: sobrepeso
# 30,0 a 34,9: obesidade grau I
# 35,0 a 34,9: obesidade grau II
#40,0 ou mais: obesidade grau III (grave)

print(" exercicio 1 ")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

idade_futura = idade + 10

print(f"{nome}, daqui a 10 anos você terá {idade_futura} anos.")

print("\n exercico 2 ")

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius:.1f}°C equivalem a {fahrenheit:.1f}°F.")

print("\n exercicio 3 ")

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

print("\n exercicio 4 ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.2f}")

print("\n exercicio 5 ")

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")

elif imc < 25.0:
    print("Classificação: Peso normal ou adequado")

elif imc < 30.0:
    print("Classificação: Sobrepeso")

elif imc < 35.0:
    print("Classificação: Obesidade grau I")

elif imc < 40.0:
    print("Classificação: Obesidade grau II")

else:
    print("Classificação: Obesidade grau III (grave)")