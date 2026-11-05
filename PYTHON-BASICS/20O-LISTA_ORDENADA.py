
print("-----")
print("Inicio do programa")
print("\nExemplo de ordenação e inversão de listas em Python")

numeros = [40, 10, 50, 20, 30]
print("Lista original:", numeros)

print("-----")
print("# sort(): Ordena em ordem crescente")
print("Lista original:", numeros)
numeros.sort()
print("Ordem crescente com sort():", numeros)

print("-----")
print("# sort(reverse=True): Ordena em ordem decrescente")
print("Lista original:", numeros)
numeros.sort(reverse=True)
print("Ordem decrescente com sort():", numeros)

print("-----")
print("# reverse(): Apenas inverte a ordem atual")
numeros = [1, 5, 2, 6, 3, 4, 8, 7]
print("Lista original:", numeros)
numeros.reverse()
print("Apenas invertida com reverse():", numeros, 'sem ordenação')

print("-----")
print("# sorted(): Retorna uma nova lista ordenada")
print("Lista original:", numeros)
nova_lista = sorted(numeros)
print("Nova lista ordenada com sorted():", nova_lista)  

print("-----")
print("# sorted(reverse=True): Retorna uma nova lista ordenada em ordem decrescente")
print("Lista original:", numeros)
nova_lista_decrescente = sorted(numeros, reverse=True)
print("Nova lista ordenada em ordem decrescente com sorted(reverse=True):", nova_lista_decrescente) 

print("\nFim do programa")
print("-----")