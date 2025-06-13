#operadores in e not in
#strings e outros trem em py são iteraveis

string = "otávio"
contador1 = 0
contador2 = 0

print(string[0])

for c in string:
    print(c)

#bom saber que for var in var só funciona se for var e não pode ter literal
#for "o" in string:
#    contador1 += 1

#for "o" not in string:
#    contador2 += 1

#print("Existem {contador1} 'o's na string")
#print("Existem {contador} que não são 'o's na string")


print("o" in string)
print("e" not in string)
print("o" not in string)

#em py, bool or bool retorna bool
#porém obj1 or obj2 vai retornar um fucking objeto, não bool
print( 1 or 0)