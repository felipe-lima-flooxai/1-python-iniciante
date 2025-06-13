nome = input("Digite seu nome ")
idade = input('Qual sua idade ')

texto = f"Seu nome é {nome} e sua idade é {idade}"

print(texto)

senha = input("Senha: ") or "Sem senha"
print("senha ", senha)

#funciona tb tipo false or 0 or "Joaquim" or "Jamal" => imprime joaquim, pq é o primeiro valor true