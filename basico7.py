#for elemento in iterável:
#elemento é uma variável que recebe cada item do iteravel

for i in range(5):
    print(i)




frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")


nomes = ["Ana", "João"]
idades = [25, 30]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")


print("Numeros de 2 em 2, a partir do 5, até o 20")
for num in range(5, 20, 2):
    print(num)

