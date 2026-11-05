
print("-----")
print("Inicio do COD")
numeros = [10, 20, 30, 40, 50]
print("Lista com numeros", numeros)

print("------")
print("# remove(): Apaga pelo valor")
print("Lista", numeros)
numeros.remove(20)
print("Após remove(20):", numeros)

print("------")
print("# pop(): Apaga pelo índice (posição -1)")
print("Lista", numeros)
removido = numeros.pop()
print("Item removido com pop():", removido)
print("Lista após pop():", numeros)

print("------")
print("# del: Apaga pelo índice (posição 0)")
print("Lista", numeros)
del numeros[0]
print("Após del numeros[0]:", numeros)

print("------")
print("# clear(): Apaga tudo")
print("Lista", numeros)
numeros.clear()
print("Após clear():", numeros)
print("Lista vazia")

print("\nFim do COD")
print("-----")

