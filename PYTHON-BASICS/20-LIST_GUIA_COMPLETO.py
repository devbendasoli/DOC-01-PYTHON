
print('-----')
print("Inicio dos COD'S")
# ============================================================
# GUIA COMPLETO DE ESTRUTURAS E MÉTODOS DE LISTAS EM PYTHON
# ============================================================

# --- 1. CRIAÇÃO DE LISTAS ---
print("\nCRIAÇÃO DE LISTAS")
print("1.1-Lista vazia: sem elementos iniciais.")
# Lista vazia: Cria uma estrutura sem elementos iniciais.
lista_vazia = []
print("Lista vazia:", lista_vazia)  # Resultado: []
print("-----")

print("1.2-Lista com elementos: Armazena múltiplos valores de qualquer tipo de dados.")
# Lista com elementos: Armazena múltiplos valores de qualquer tipo de dados.
numeros = [10, 20, 30, 40, 50]
print("Lista de números:", numeros)  # Resultado: [10, 20, 30, 40, 50]
print("-----")

print("1.3-Lista heterogênea: Permite misturar diferentes tipos de dados em uma única lista.")
# Função list(): Converte outros iteráveis (como strings, tuplas ou ranges) em uma lista.
letras = list("Python")  # Resultado: ['P', 'y', 't', 'h', 'o', 'n']
print("Lista de letras:", letras)
print("-----")

# --- 2. ACESSO E FATIAMENTO (SLICING) ---
print("\n2. ACESSO E FATIAMENTO (SLICING)")
print("Lista de números:", numeros)
print("2.1-Acesso por índice positivo (começando do zero).")
# Acesso por índice positivo: Obtém o elemento em uma posição específica (começando do zero).
primeiro = numeros[0]  # Resultado: 10
print("Primeiro elemento:", primeiro)
print("-----")

print("2.2-Acesso por índice negativo (começando do final).")
# Acesso por índice negativo: Obtém elementos contando a partir do final da lista.
ultimo = numeros[-1]  # Resultado: 50
print("Último elemento:", ultimo)
print("-----")

print("2.3-Fatiamento básico [inicio:fim]")
# Fatiamento básico [inicio:fim]: Extrai uma sublista do índice de início até antes do índice de fim.
sublista = numeros[1:4]  # Resultado: [20, 30, 40]
print("Sublista (índices 1 a 3):", sublista)
print("-----")

print("2.4-Fatiamento com passo [inicio:fim:passo]")
# Fatiamento com passo [inicio:fim:passo]: Seleciona elementos pulando posições conforme o valor do passo.
pares = numeros[::2]  # Resultado: [10, 30, 50]
print("Elementos em posições pares:", pares)
print("-----")

print("2.5-Fatiamento com passo negativo [inicio:fim:passo]")
# Inversão de lista com slicing: Inverte a ordem de todos os elementos da lista.
invertida = numeros[::-1]  # Resultado: [50, 40, 30, 20, 10]
print("Lista invertida:", invertida)
print("-----")

# --- 3. ADIÇÃO DE ELEMENTOS ---
print("\n3. ADIÇÃO DE ELEMENTOS")
print("3.1-append(valor): Adiciona um novo elemento ao final da lista.")
# append(valor): Adiciona um novo elemento ao final da lista.
numeros.append(60)  # [10, 20, 30, 40, 50, 60]
print("Lista após append(60):", numeros)
print("-----")

print("3.2-insert(indice, valor): Insere um elemento em uma posição específica, deslocando os demais.")
# insert(indice, valor): Insere um elemento em uma posição específica, deslocando os demais.
numeros.insert(1, 15)  # Insere 15 na posição 1
print("Lista após insert(1, 15):", numeros)
print("-----")

print("3.3-extend(iteravel): Adiciona todos os elementos de outra lista/coleção ao final da lista atual.")
# extend(iteravel): Adiciona todos os elementos de outra lista/coleção ao final da lista atual.
numeros.extend([70, 80])  # Adiciona 70 e 80 no final
print("Lista após extend([70, 80]):", numeros)
print("-----")

# --- 4. REMOÇÃO DE ELEMENTOS ---
print("\n4. REMOÇÃO DE ELEMENTOS")
print("4.1-remove(valor): Remove a primeira ocorrência do valor especificado (gera erro se não existir).")
# remove(valor): Remove a primeira ocorrência do valor especificado (gera erro se não existir).
numeros.remove(15)  # Remove o valor 15
print("Lista após remove(15):", numeros)
print("-----")

print("4.2-pop(indice): Remove e retorna o elemento na posição informada (se não informar o índice, remove o último).")
# pop(indice): Remove e retorna o elemento na posição informada (se não informar o índice, remove o último).
removido = numeros.pop()  # Remove e devolve o último item
print("Elemento removido com pop():", removido)
print("Lista após pop():", numeros)
print("-----")

print("4.3-clear(): Apaga todos os elementos da lista, deixando-a totalmente vazia.")
# clear(): Apaga todos os elementos da lista, deixando-a totalmente vazia.
copia_temp = [1, 2, 3]
copia_temp.clear()  # Resultado: []
print("Lista após clear():", copia_temp)
print("-----")

print("4.4-del lista[indice]: Apaga um elemento em um índice específico ou apaga uma fatia inteira.")
# Comando del: Apaga um elemento em um índice específico ou apaga uma fatia inteira.
del numeros[0]  # Apaga o primeiro elemento
print("Lista após del numeros[0]:", numeros)
print("-----")

# --- 5. CONSULTA E PESQUISA ---
print("\n5. CONSULTA E PESQUISA")
print("5.1-index(valor): Retorna o índice da primeira ocorrência do valor pesquisado na lista.")    
# index(valor): Retorna o índice da primeira ocorrência do valor pesquisado na lista.
posicao = numeros.index(30)
print("Índice do valor 30:", posicao)  # Resultado: 2
print("-----")

print("5.2-count(valor): Conta quantas vezes um determinado valor aparece dentro da lista.")
# count(valor): Conta quantas vezes um determinado valor aparece dentro da lista.
quantidade = numeros.count(20)
print("Quantidade de vezes que 20 aparece:", quantidade)  # Resultado: 1
print("-----")

print("5.3-Verificação de existência com operador 'in'.")
# Operador in: Verifica se um elemento existe dentro da lista (retorna True ou False).
existe = 40 in numeros  # Resultado: True
print("O valor 40 existe na lista?", existe)
print("-----")

# --- 6. ORDENAÇÃO E INVERSÃO ---
print("\n6. ORDENAÇÃO E INVERSÃO")
print("6.1-sort(): Ordena a própria lista em ordem crescente (modifica a lista original).")
# sort(): Ordena a própria lista em ordem crescente (modifica a lista original).
numeros.sort()
print("Lista após sort():", numeros)
print("-----")

print("6.2-sort(reverse=True): Ordena a própria lista em ordem decrescente.")
# sort(reverse=True): Ordena a própria lista em ordem decrescente.
numeros.sort(reverse=True)
print("Lista após sort(reverse=True):", numeros)
print("-----")

print("6.3-sorted(lista): Retorna uma nova lista ordenada sem alterar a lista original.")
# sorted(lista): Retorna uma nova lista ordenada sem alterar a lista original.
nova_ordenada = sorted(numeros)
print("Nova lista ordenada com sorted():", nova_ordenada)
print("Lista original após sorted():", numeros)
print("-----")

print("6.4-reverse(): Inverte a ordem atual dos elementos na própria lista.")
# reverse(): Inverte a ordem atual dos elementos na própria lista.
numeros.reverse()
print("Lista após reverse():", numeros)
print("-----")

# --- 7. CÓPIA DE LISTAS ---
print("\n7. CÓPIA DE LISTAS")
print("7.1-Atribuição direta: Cria uma referência à lista original (não é uma cópia).")
# copy(): Cria uma cópia rasa (shallow copy) da lista para evitar alterar a original.
lista_copiada = numeros.copy()
print("Lista copiada com copy():", lista_copiada)
print("Alterando a lista copiada não afeta a original.")
lista_copiada.append(100)
print("Lista copiada após append(100):", lista_copiada)
print("Lista original permanece inalterada:", numeros)  
print("-----")

# --- 8. FUNÇÕES NATIVAS ÚTEIS COM LISTAS ---
print("\n8. FUNÇÕES NATIVAS ÚTEIS COM LISTAS")
print("8.1-len(lista): Retorna a quantidade total de elementos presentes na lista.")
# len(lista): Retorna a quantidade total de elementos presentes na lista.
tamanho = len(numeros)
print("tamanho:", tamanho)
print("-----")

print("8.2-sum(lista): Retorna o somatório de todos os valores numéricos contidos na lista.")
# sum(lista): Somatório de todos os valores numéricos contidos na lista.
total_soma = sum([20, 30, 40])  # Resultado: 90
print("Soma de [20, 30, 40]:", total_soma)
print("-----")

print("8.3-min(lista) e max(lista): Encontra o menor e o maior valor dentro da lista, respectivamente.")
# min(lista) e max(lista): Encontra o menor e o maior valor dentro da lista, respectivamente.
menor = min(numeros)
maior = max(numeros)
print("Menor valor:", menor)
print("Maior valor:", maior)
print("-----")

# --- 9. ITERAÇÃO E LAÇOS ---
print("\n9. ITERAÇÃO E LAÇOS")
print("9.1-Loop for com range(len(lista)): Percorre a lista usando índices para acessar cada elemento.")
# Loop for simples: Percorre diretamente cada valor contido na lista.
for item in numeros:
    print(f"Elemento: {item}")

print("-----")

print("9.2-Loop for com enumerate(lista): Percorre a lista retornando tanto o índice quanto o valor em cada volta do loop.")
# enumerate(lista): Percorre a lista retornando tanto o índice quanto o valor em cada volta do loop.
for indice, valor in enumerate(numeros):
    print(f"Índice {indice}: {valor}")

print("-----")

# --- 10. COMPREENSÃO DE LISTAS (LIST COMPREHENSION) ---
print("\n10. COMPREENSÃO DE LISTAS (LIST COMPREHENSION)")
print("10.1-List Comprehension básica: Sintaxe curta para criar novas listas baseadas em iteráveis.")
range_exemplo = range(5)  # Gera números de 0 a 4
# List Comprehension básica: Sintaxe curta para criar novas listas baseadas em iteráveis.
quadrados = [x ** 2 for x in range(5)]  # Resultado: [0, 1, 4, 9, 16]
print("Lista de quadrados de 0 a 4:", quadrados)
print("-----")

print("10.2-List Comprehension com múltiplas condições (if/else): Permite criar listas com base em condições específicas.")
# List Comprehension com filtro (if): Cria uma lista filtrando apenas elementos que atendem a uma condição.
pares_filtrados = [x for x in range(10) if x % 2 == 0]  # Resultado: [0, 2, 4, 6, 8]
print("Lista de números pares de 0 a 9:", pares_filtrados)
print("-----")
print("Finalizando os exemplos de List Comprehension.")
print("-----")