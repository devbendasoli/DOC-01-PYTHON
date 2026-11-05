
print("-----")
print("Inicio do CODE")
print("\nExemplos de compreensão de listas em Python")
# Criar lista com o dobro de cada número
numeros = [1, 2, 3, 4, 5]
dobros = [x * 2 for x in numeros]
print("Dobro dos números:", dobros)

print("-----")

# Criar lista apenas com números pares
pares = [x for x in range(10) if x % 2 == 0]
print("Números pares de 0 a 9:", pares)


print("\nFim do COD")
print("-----")