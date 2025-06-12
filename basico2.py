nome = "Zoe"
surname ="Deusa"
age = 10000000000
birthDay = -10000002025
height = 1.45
isAdult = age >= 18
print("Nome:", nome)
print("Sobrenome:", surname)
print("Idade:", age)
print("Ano de nascimento:", birthDay)
print("Maior de Idade?:", isAdult)
print("Altura em metros:", height)

#imc = peso /(altura x altura)
height = 1.7
weight = 150
imc = weight / height ** 2
print("imc", imc)

# f" Esse é o {imc:.2f}"
a = "A"
b = "B"
c = "C"
formato = "a={} b={} c={}".format(a, b, c)
print(formato)