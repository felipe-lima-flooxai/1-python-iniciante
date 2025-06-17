salas = [
    ["Maria", "Helena"],
    ["Elaine"],
    ["Luiz", "João", "Eduarda"]
]

print(salas[0])
print(salas[0][1])


for sala in salas:
    for aluno in sala:
        print(aluno)