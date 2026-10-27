 # fazendo um jogo
 # vamos encontrar algo
 
nome = input("Digite seu nome: ")
encontrar = input("O que você quer encontrar? ")

if encontrar in nome:
    print(f"Você encontrou '{encontrar}' em '{nome}'!")
else:
    print(f"'{encontrar}' não está em '{nome}'.")
           