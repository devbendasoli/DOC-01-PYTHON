print("-----")
print("Inicio do COD")

import itertools

frutas = ["Maçã", "Banana", "Uva"]

print("Lista de frutas:", frutas)
# Gerar todas as combinações de 2 em 2 itens
combinacoes = list(itertools.combinations(frutas, 2))
print("Todas as combinações possíveis (grupos de 2):", combinacoes)


# Combinações Matemáticas (Com o módulo itertools)
# Imagina que tens uma lista de ingredientes ou 
# cores e queres saber todas as duplas possíveis
# que podes formar, sem repetir a ordem (ou seja, 
# "Maçã e Banana" é o mesmo que "Banana e Maçã"). 
# Para isto, o Python tem uma ferramenta nativa 
# chamada itertools.
print("Fim do COD")
print("\n-----")