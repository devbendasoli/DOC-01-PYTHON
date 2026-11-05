

print("-----------")
print("Programa iniciado.")

while True:
    sair = input("Deseja sair? (s)im: ")
# sair é a palavra que o usuário digita para sair do programa.
    sair = sair.lower()
# converte a entrada para minúsculas
    sair = sair.startswith('s')
# verifica se a entrada começa com 's'

    print(sair)
    if sair:
        print("Saindo do programa...")
    break
print("Programa encerrado.")
print("-----------")

#Tudo isso é feito em uma única linha
while True:
    sair = input("Deseja sair? (s)im: ").lower().startswith('s')
    print(sair)
    if sair:
        print("Saindo do programa...")
        break

print("Programa encerrado.")
print("-----------")



