
#gerar uma sequência de números
#Ela aceita até três argumentos: range(início, fim, passo).
print("----------")
print("inicio do programa")
print("1. Apenas o valor final: range(fim)")
for i in range(5):
#saida gera os números de 0 a 4
    print(i)
    
print(" ")
print("----------")
print(" ")

print ("2. Início e fim: range(início, fim)")
for i in range(4, 9):
#Saida gera os números de 4 a 8
    print(i)
    
print(" ")
print("----------")
print(" ")

print("3. Início, fim e passo (incremento):")
for i in range(0, 10, 2):
# Números pares de 0 a 8
    print(i)
    

print(" ")
print("---------")
print(" ")

print("4. Ordem decrescente (passo negativo)")
for i in range(5, 0, -1):
#Saida Números de 5 a 1
    print(i)
    
print(" ")
print("-----------")
print(" ")    
    
print ("5. Convertendo para uma Lista") 
numeros = list(range(1, 6))
print(numeros)  # [1, 2, 3, 4, 5]


print("-----------")
print("fim do programa")





    
    
    




    
    
    
    
    
    