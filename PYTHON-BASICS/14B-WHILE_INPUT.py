print("-----------")
print("Programa iniciado. Digite 's' " \
"para sair a qualquer momento.")
while True:
    sair = input("Deseja sair? (s/n): ")
    if sair.lower() == 's':
#Que isso faz, lower() é um método de string que 
# converte todos os caracteres da string para
# minúsculas. Isso é útil que o 
# usuário digitar 's' ou 'S'.
        print("Saindo do programa...")
        break #Aqui, o break é usado para sair do loop  
print("Programa encerrado.")
print("-----------")




