#interpolação de strings

nome = "Luiz"
preco= 1000.4546321
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

#existem:
#f strings
#format()
#interpolação


palavrona = "Incostitucionalissimamente"
print(palavrona[0])
print(palavrona[0:5])
print(palavrona[7:13])
print(palavrona[-7:-2]) #nao inverte o resultado, aparentemente
print(palavrona[:10])
print(palavrona[10:])
print(palavrona[1:14:2])
print(palavrona[::-1])