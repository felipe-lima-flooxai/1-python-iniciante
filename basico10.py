#desestruturação em python

nomes = ["Maria", 'Helena', "Luiz"]

nome1, nome2, nome3 = nomes
print(nome1)
print(nome2)
print(nome3)

fruta1, *resto = ["Abacaxi", "Banana", "Cereja"]
print(fruta1)
print(resto)