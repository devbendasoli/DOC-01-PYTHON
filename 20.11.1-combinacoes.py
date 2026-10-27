

import itertools

letras = ["A", "B", "C"]
print(list(itertools.combinations(letras, 2)))
# Resultado: [('A', 'B'), ('A', 'C'), ('B', 'C')]


# O que faz: Cria combinações onde a ordem não interessa e não há repetição de itens (ex: ('Maçã', 'Banana') é igual a ('Banana', 'Maçã'), por isso só aparece uma vez).
