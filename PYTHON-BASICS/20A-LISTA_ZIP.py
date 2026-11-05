
print("-----")
print("Inicio do COD")
alunos = ["Ana", "Bruno", "Carla"]
notas = [8.5, 9.0, 7.5]

print("Lista de alunos: ", alunos)
print("Lista de notas: ", notas)

print("\n-----")

print("Combinação de listas com zip()")
combinadas = list(zip(alunos, notas))
print("Listas combinadas:", combinadas)

print("\n-----")
print("Podemos percorrer essa combinação num loop") 
print("\n--- Relatório de Notas ---")
for aluno, nota in zip(alunos, notas):
    print(f"O(a) aluno(a) {aluno} tirou {nota}")
    
    
 # Juntar e Combinar Listas (Com o zip)
# Se tens duas listas separadas (por #exemplo,
# uma com nomes e outra com notas) e queres 
# combiná-las linha a linha, usas a função zip().   

print("\n-----")
print("Fim do COD")


