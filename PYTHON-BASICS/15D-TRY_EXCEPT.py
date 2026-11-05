
print("-----------")
print("Bem-vindo ao programa de divisão!")
#Entre dois números inteiros e o programa
while True:
    try:
        # Usamos float() para aceitar centavos (ex: 49.90)
        preco = float(input("Digite o preço do produto (R$): "))
        
        # Garante que o usuário não vai digitar um preço negativo
        if preco < 0:
            print("⚠️ O preço não pode ser negativo. Tente novamente.")
            continue # Volta para o começo do while
            
        break # Se passou por tudo certo, sai do loop
        
    except ValueError:
        print("❌ Erro: Digite um valor numérico válido (ex: 15.50).")

print(f"✅ Preço cadastrado com sucesso: R$ {preco:.2f}")

print("fim do programa de cadastro de preço sem travar o sistema.")
print("-----------")
