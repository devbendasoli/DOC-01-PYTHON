
print("--------")
print("Exemplo de soma com for e sum()")
# loope for e sim())

números = [20, 30, 40]

soma = 0

for n in números:
    soma += n
    
print(soma)

print("--------")

números = [20, 30, 40]
print(sum(números))  # Adicionado o parêntese que faltava no final

#O sum() é uma função nativa (já integrada) do Python que serve para somar todos os números de uma lista de uma só vez.

# exemplo. sum([20, 30, 40]) calcula logo 20 + 30 + 40 e devolve 90.


