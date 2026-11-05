print("-----------")
print("Bem-vindo ao programa de divisão!")
#Entre dois números inteiros e o programa 
# tentará dividi-los, lidando com possíveis erros.
try:
    # O usuário digita os dois números 
    # (pode gerar ValueError se digitar letras)
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))

    # Tenta fazer a divisão (pode gerar
    #  ZeroDivisionError se b for 0)
    resultado = a / b
    print(f"O resultado da divisão é: {resultado}")

# Se o usuário digitar uma letra em vez de número
except ValueError:
    print("Erro: Digite apenas números inteiros válidos.")

# Se o usuário tentar dividir por zero
except ZeroDivisionError:
    print("Erro: Não é possível dividir um número por zero.")

# Bônus: Capturando o erro original do Python usando 'as erro'
except Exception as erro:
    # Esse bloco pega qualquer outro erro inesperado que 
    # não seja os anteriores
    print(f"Ocorreu um erro inesperado: {erro}")

    print("Detalhes do erro:")
    # Mostra o tipo do erro e a mensagem original
    print(f"Tipo do erro: {type(erro).__name__}")
    print(f"Mensagem do erro: {erro}")
    print("fim do programa com erro inesperado.")
    print("-----------")
    #AQUI TERMINA O PROGRAMA COM ERRO, MAS SEM TRAVAR O SISTEMA