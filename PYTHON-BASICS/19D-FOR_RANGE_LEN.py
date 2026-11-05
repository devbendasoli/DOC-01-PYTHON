
print("-----")
print("FOR")
"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    
    
print ("-----")


nomes = ['maria', 'luiz', 'rose']
n = [1, 2, 3]

for i in nomes:
    for numeros in n:  
        print(f"{numeros} - {i}")

      
        
print("Fim do FOR")        
print("-----")        
        
        
        
        
    