
print("----------")
print("Algoritmo de Busca Dinâmica (Árvores e Grafos)")

#Algoritmo de Busca Dinâmica (Árvores e Grafos)
#Usa um ciclo while e uma lista para percorrer 
# estruturas hierárquicas (como diretórios de 
# pastas ou redes), removendo os nós à medida 
# que são visitados até a lista esvaziar.  

# Estrutura de exemplo: Um sistema de pastas simplificado
sistema_arquivos = {
    "root": ["documentos", "fotos"],
    "documentos": ["relatorio.pdf", "notas.txt"],
    "fotos": ["familia.png"],
}

# Algoritmo de Busca em Largura (BFS) usando while
fila_de_busca = ["root"]

while fila_de_busca:
    pasta_atual = fila_de_busca.pop(0)  
# Remove o primeiro item da lista
    print(f"Explorando: {pasta_atual}")
    print(f"Fila de busca atual: {fila_de_busca}")
    print("-----------")
# Se a pasta tiver subpastas, adiciona 
# elas na fila para continuar a busca
    if pasta_atual in sistema_arquivos:
        fila_de_busca.extend(sistema_arquivos[pasta_atual])
        
        
#.pop(0): Remove e retorna o elemento que está 
# na posição 0 (o primeiro da lista). No contexto
# de filas, isto garante que processamos os 
# elementos pela ordem de chegada (FIFO).

#.extend(...): Adiciona múltiplos elementos de
# uma só vez ao final da lista atual (neste caso,
# insere as subpastas encontradas dentro da fila 
# de pendentes).        

print("Fim da busca dinâmica") 
print("----------")       
#    *COD FICOU BEM CONFUSO- VOLTAR AQUI DEPOIS*        
        
        
        
        
        