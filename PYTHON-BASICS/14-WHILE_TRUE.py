print("------------------")
print("Programa iniciado")
while True:
    resposta = input("Digite 'sair' para encerrar o programa: ")
    if resposta.lower() == 'sair':
#lower() transforma a string em minúscula,
# assim o usuário pode digitar 'sair', 'SAIR', 'SaiR', etc.
        print("Programa encerrado")
        break
print("Você digitou: ", resposta)
    
print("-----------------")  