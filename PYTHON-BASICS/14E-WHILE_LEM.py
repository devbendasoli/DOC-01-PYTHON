
print("-----------")
print("Programa iniciado.")
#Interando string comwhile

#------012345678910
nome = input("Digite seu nome: ") #interavel
#------1110987654321
#Cria uma string vazia e acumula dentro da outra 
indice = 0
novo_nome = ""
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f"*{letra}"
    indice += 1
novo_nome += "*"
print(novo_nome)
print("fim do while")
print("-----------")