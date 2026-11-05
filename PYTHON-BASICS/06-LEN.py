print("-----")
print("\nInicio do COD")
#com len
print("-----LEN-----")
n1 = [1.5, 2.5, 3, 5]
n2 = [10, 20, 30]
n3 = ["ABC", 'D', 'E']
print("Contando quantos valor á na chaves: ", n1,",", n2, " e ", n3)
print(len(n1+n2+n3))# len calcula
print("-----FIM-----")

print(" ")

print("-----LEN-----")
string1 = "Marcelo"
string2 = "Enzo"
print("Contando quantas letra a em: ", string1, " e ", string2)
print(len(string1+string2))
print("-----FIM-----")

print(" ")

print("-----LEM-----")
string1 = string3 = "pedra"
#string1 recebe string3 e agora com novo valor
print(string1, "tem", len(string1), "Letras")
print("-----FIM-----")

print(" ")

print("-----FOR-----")
n1 = [20, 30, 30.5, 6]
n4 = 4  # Quantas vai repetir

for i1 in range(n4):  # range(4) vai gerar: 0, 1, 2, 3
       for i2 in n1:
        print(i1, i2)
        
print("-----FIM-----")

print("\nUsando um metodo diferente " \
"pra ficar com a saida mais organizada sem repetição ")

print(" 1° -----FOR-----")
lista = [20, 30, 30.5, 6]

for i, valor in enumerate(lista):
    print(i, valor)
    
print("-----FIM-----")

print("\nDessa forma, o loop roda " \
"exatamente 4 vezes em sequência, " \
"sem repetições indesejadas, ")

print(" 2° -----FOR-----")
lista = [20, 30, 30.5, 6]
n4 = len(lista)  # 4

for i in range(n4):
    print(i, lista[i])
    
print("-----FIM-----")

print("-----")        
        
