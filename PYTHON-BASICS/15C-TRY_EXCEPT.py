
print("-----------")
print("Bem-vindo ao programa de tarefas!")

while True:
    print("\n--- MENU DE TAREFAS ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")
    
    try:
        # Tenta pegar a opção como número inteiro
        opcao = int(input("Escolha uma opção (1-3): "))
        
        # Valida se está dentro do intervalo correto do menu
        if opcao == 1:
            print("📝 Você escolheu: Adicionar tarefa.")
            # Aqui iria o código de adicionar...
        elif opcao == 2:
            print("📋 Você escolheu: Ver tarefas.")
            # Aqui iria o código de listar...
        elif opcao == 3:
            print("👋 Saindo do programa. Até logo!")
            break  # Sai do loop while e encerra o programa
        else:
            print("⚠️ Opção inválida! Digite um número entre 1 e 3.")
            
    except ValueError:
        # Captura se o usuário digitar letras ou símbolos (ex: "abc" ou "1.5")
        print("❌ Erro: Digite apenas números inteiros válidos para o menu.")

print("fim do programa de tarefas.")
print("-----------")