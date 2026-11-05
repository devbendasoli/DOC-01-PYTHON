
print("-----------")
print("Bem-vindo ao programa!")
while True:
    try:
        # Tenta converter o input para número inteiro
        idade = int(input("Digite a sua idade: "))
        
        # Se deu tudo certo, o break encerra o loop
        break
        
    except ValueError:
        # Se a pessoa digitar uma letra ou valor inválido, 
        # cai aqui sem fechar o programa
        print("❌ Digite apenas números.")

# Quando sair do loop, o programa continua normalmente 
# com o dado validado
print(f"✅ Idade registrada com sucesso: {idade} anos.")

print("fim do programa sem travar o sistema.")
print("-----------")


