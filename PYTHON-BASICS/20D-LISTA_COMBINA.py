
print("-----")
print('Inicio do COD')
# 2. permutations (Permutações)
# O que faz: Aqui a ordem importa! 
# Se mudares a ordem dos elementos, 
# conta como uma combinação nova. 
# (Ideal para criar senhas, anagramas ou caminhos de rota).

import itertools #quando se quer usar funções de combinatória

letras = ["A", "B", "C"]
print(list(itertools.permutations(letras, 2)))
# Resultado: [('A', 'B'), ('A', 'C'), ('B', 'A'), 
# ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Repara que ('A', 'B') e ('B', 'A') 
# são diferentes, porque a ordem importa.
print(list(itertools.permutations(letras, 3)))
print("Fim do COD")
print("-----")