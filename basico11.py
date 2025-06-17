#split e join
frase = "Olha só, isso é uma frase"
frase_split = frase.split()
print(frase_split)
frase_split2 = frase.split(",")
print(frase_split2)
frase_junta = ", ".join(frase_split2)
print(frase_junta)