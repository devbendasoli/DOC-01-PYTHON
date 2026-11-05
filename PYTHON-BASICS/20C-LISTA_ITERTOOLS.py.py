
print('-----')
print("\nInicio do COD")

import itertools

letras = ["A", "B", "C"]
print("Lista de letras: ", letras)
print(list(itertools.product(letras, repeat=2)))
# Resultado: [('A', 'A'), ('A', 'B'), ('A', 'C'), 
# ('B', 'A'), ('B', 'B'), ('B', 'C'),
# ('C', 'A'), ('C', 'B'), ('C', 'C')
print("\n-----")    
print(list(itertools.permutations(letras, 2)))
# Resultado: [('A', 'B'), ('A', 'C'), ('B', 'A'), 
# ('B', 'C'), ('C', 'A'), ('C', 'B')]
print("\n-----")
print(list(itertools.combinations(letras, 2)))
# Resultado: [('A', 'B'), ('A', 'C'), ('B', 'C')]


# O que faz: Cria combinações onde a ordem não 
# interessa e não há repetição de itens (ex: 
# ('Maçã', 'Banana') é igual a ('Banana', 'Maçã'),
# por isso só aparece uma vez).

print('\nFim do COD')
print('-----')