

# ============================================================
# GUIA COMPLETO DE ESTRUTURAS E MÉTODOS DE LISTAS EM PYTHON
# ============================================================

# --- 1. CRIAÇÃO DE LISTAS ---

# Lista vazia: Cria uma estrutura sem elementos iniciais.
lista_vazia = []

# Lista com elementos: Armazena múltiplos valores de qualquer tipo de dados.
numeros = [10, 20, 30, 40, 50]

# Função list(): Converte outros iteráveis (como strings, tuplas ou ranges) em uma lista.
letras = list("Python")  # Resultado: ['P', 'y', 't', 'h', 'o', 'n']


# --- 2. ACESSO E FATIAMENTO (SLICING) ---

# Acesso por índice positivo: Obtém o elemento em uma posição específica (começando do zero).
primeiro = numeros[0]  # Resultado: 10

# Acesso por índice negativo: Obtém elementos contando a partir do final da lista.
ultimo = numeros[-1]  # Resultado: 50

# Fatiamento básico [inicio:fim]: Extrai uma sublista do índice de início'' até antes do índice de fim.
sublista = numeros[1:4]  # Resultado: [20, 30, 40]

# Fatiamento com passo [inicio:fim:passo]: Seleciona elementos pulando posições conforme o valor do passo.
pares = numeros[::2]  # Resultado: [10, 30, 50]

# Inversão de lista com slicing: Inverte a ordem de todos os elementos da lista.
invertida = numeros[::-1]  # Resultado: [50, 40, 30, 20, 10]


# --- 3. ADIÇÃO DE ELEMENTOS ---

# append(valor): Adiciona um novo elemento ao final da lista.
numeros.append(60)  # [10, 20, 30, 40, 50, 60]

# insert(indice, valor): Insere um elemento em uma posição específica, deslocando os demais.
numeros.insert(1, 15)  # Insere 15 na posição 1

# extend(iteravel): Adiciona todos os elementos de outra lista/coleção ao final da lista atual.
numeros.extend([70, 80])  # Adiciona 70 e 80 no final


# --- 4. REMOÇÃO DE ELEMENTOS ---

# remove(valor): Remove a primeira ocorrência do valor especificado (gera erro se não existir).
numeros.remove(15)  # Remove o valor 15

# pop(indice): Remove e retorna o elemento na posição informada (se não informar o índice, remove o último).
removido = numeros.pop()  # Remove e devolve o último item

# clear(): Apaga todos os elementos da lista, deixando-a totalmente vazia.
copia_temp = [1, 2, 3]
copia_temp.clear()  # Resultado: []

# Comando del: Apaga um elemento em um índice específico ou apaga uma fatia inteira.
del numeros[0]  # Apaga o primeiro elemento


# --- 5. CONSULTA E PESQUISA ---

# index(valor): Retorna o índice da primeira ocorrência do valor pesquisado na lista.
posicao = numeros.index(30)

# count(valor): Conta quantas vezes um determinado valor aparece dentro da lista.
quantidade = numeros.count(20)

# Operador in: Verifica se um elemento existe dentro da lista (retorna True ou False).
existe = 40 in numeros  # Resultado: True


# --- 6. ORDENAÇÃO E INVERSÃO ---

# sort(): Ordena a própria lista em ordem crescente (modifica a lista original).
numeros.sort()

# sort(reverse=True): Ordena a própria lista em ordem decrescente.
numeros.sort(reverse=True)

# sorted(lista): Retorna uma nova lista ordenada sem alterar a lista original.
nova_ordenada = sorted(numeros)

# reverse(): Inverte a ordem atual dos elementos na própria lista.
numeros.reverse()


# --- 7. CÓPIA DE LISTAS ---

# copy(): Cria uma cópia rasa (shallow copy) da lista para evitar alterar a original.
lista_copiada = numeros.copy()


# --- 8. FUNÇÕES NATIVAS ÚTEIS COM LISTAS ---

# len(lista): Retorna a quantidade total de elementos presentes na lista.
tamanho = len(numeros)

# sum(lista): Somatório de todos os valores numéricos contidos na lista.
total_soma = sum([20, 30, 40])  # Resultado: 90

# min(lista) e max(lista): Encontra o menor e o maior valor dentro da lista, respectivamente.
menor = min(numeros)
maior = max(numeros)


# --- 9. ITERAÇÃO E LAÇOS ---

# Loop for simples: Percorre diretamente cada valor contido na lista.
for item in numeros:
    print(f"Elemento: {item}")

# enumerate(lista): Percorre a lista retornando tanto o índice quanto o valor em cada volta do loop.
for indice, valor in enumerate(numeros):
    print(f"Índice {indice}: {valor}")


# --- 10. COMPREENSÃO DE LISTAS (LIST COMPREHENSION) ---

# List Comprehension básica: Sintaxe curta para criar novas listas baseadas em iteráveis.
quadrados = [x ** 2 for x in range(5)]  # Resultado: [0, 1, 4, 9, 16]

# List Comprehension com filtro (if): Cria uma lista filtrando apenas elementos que atendem a uma condição.
pares_filtrados = [x for x in range(10) if x % 2 == 0]  # Resultado: [0, 2, 4, 6, 8]









