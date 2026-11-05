
print('-----')
print("Inicio do COD")

import itertools

tamanhos = ["P", "M"]
cores = ["Azul", "Vermelho"]

# Cruza cada tamanho com cada cor
print(list(itertools.product(tamanhos, cores)))
# Resultado: [('P', 'Azul'), ('P', 'Vermelho'),
# ('M', 'Azul'), ('M', 'Vermelho')]

print('Fim do COD')
print('-----')
