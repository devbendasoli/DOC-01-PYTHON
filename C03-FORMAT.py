
# Exemplos com a função .format()
# A função .format() insere os valores dentro das chaves {} na ordem em que são passados ou através de índices/nomes.

nome = "Ana"
profissao = "desenvolvedora"

# As chaves {} recebem os valores na ordem dos argumentos do .format()
mensagem = "Olá, meu nome é {} e eu trabalho como {}.".format(nome, profissao)

print(mensagem)
# Saída: Olá, meu nome é Ana e eu trabalho como desenvolvedora.



print(10 * "-")



preco = 45.5678

# O ':.2f' formata o número para ter apenas 2 casas decimais
texto = "O valor total da compra é R$ {:.2f}".format(preco)

print(texto)
# Saída: O valor total da compra é R$ 45.57

print("fim")