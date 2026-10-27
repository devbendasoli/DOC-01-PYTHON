

# 1. CADASTRO
print("=== CADASTRO DE SENHA ===")
senha_nu = input("Digite sua senha numérica para cadastro: ")
senha_le = input("Digite suas letras para cadastro: ")
print("\nCadastro realizado com sucesso!\n")

# 2. PRIMEIRO TENTATIVA DE LOGIN
print("=== LOGIN ===")
senha_nu_add = input("Digite sua senha numérica: ")
senha_le_add = input("Digite as letras de sua senha: ")

# Controle de tentativas
tentativas = 1
max_tentativas = 3

# 3. VERIFICAÇÃO E REPETIÇÃO
# Enquanto a senha estiver incorreta E ainda houver tentativas restantes:
while (senha_nu != senha_nu_add or senha_le != senha_le_add) and tentativas < max_tentativas:
    tentativas += 1
    print(f"\nSenha errada! Tentativa {tentativas} de {max_tentativas}.")
    
    senha_nu_add = input("Digite sua senha numérica novamente: ")
    senha_le_add = input("Digite as letras de sua senha novamente: ")

# 4. RESULTADO FINAL
if senha_nu == senha_nu_add and senha_le == senha_le_add:
    print("\nSenha correta! Acesso concedido.")
else:
    print("\nSenha incorreta!")
    print("Acesso BLOQUEADO devido a 3 tentativas incorretas.")
    
    
    
    
    
    
    
    
    