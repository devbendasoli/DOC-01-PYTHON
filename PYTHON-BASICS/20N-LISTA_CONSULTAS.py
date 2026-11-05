
print("-----")
print("\nInicio do COD")

print("Exemplo de consulta em listas")
#              0          1       2        3
linguagens = ["Python", "Java", "C++", "Python"]
print("Lista de linguagens:", linguagens)

print("------")
print("# index(): Mostra em qual posição está o elemento")
posicao = linguagens.index("Java")
print("Posição do Java:", posicao)

print("------")
print("# count(): Conta quantas vezes aparece na lista")
qtd = linguagens.count("Python")
print("Quantas vezes Python aparece:", qtd)

print("------")
print("# operador in: Verifica se existe (retorna True ou False)")
existe = "C++" in linguagens
print("C++ está na lista?", existe)

print("\nFim do COD")
print("-----")