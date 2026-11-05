print("------------------")
print("inicio do programa")
resposta = input("Deseja continuar? (Sim/Não): ")

if resposta.lower() == 'sim':
    # lower() transforma a string em minúscula,
    # assim o usuário pode digitar 'sim', 'SIM', 'SiM', etc
    print("Processando...")
else:
    print("Operação cancelada.")

print("------------------")

usuario_cadastrado = "admin"
tentativa = input("Digite seu usuário: ")

if tentativa.lower() == usuario_cadastrado:
    print("Acesso permitido! Bem-vindo.")
else:
    print("Usuário incorreto.")

print("------------------")

cidade = input("Em qual cidade você mora? ")

# Se o usuário digitar "SÃO PAULO" ou
#  "São Paulo", o código padroniza
cidade_padronizada = cidade.lower()
print(f"Cidade registrada: {cidade_padronizada}")

print("------------------")
print("FIM DO PROGRAMA")