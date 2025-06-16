import random
listinha = []

qtd = input("Digite quantos numeros randomicos vc quer ")

numero = 0
while (numero < int(qtd)):
    listinha.append(random.randint(0, 40))
    numero += 1

for index, item in enumerate(listinha):
    print(f'{index}: {item}')
