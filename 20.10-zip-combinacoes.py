

alunos = ["Ana", "Bruno", "Carla"]
notas = [8.5, 9.0, 7.5]

# zip() junta as duas listas par a par
combinadas = list(zip(alunos, notas))
print("Listas combinadas:", combinadas)

# Podemos percorrer essa combinação num loop
print("\n--- Relatório de Notas ---")
for aluno, nota in zip(alunos, notas):
    print(f"O(a) aluno(a) {aluno} tirou {nota}")
    
    
 # Juntar e Combinar Listas (Com o zip)
# Se tens duas listas separadas (por #exemplo, uma com nomes e outra com notas) e queres combiná-las linha a linha, usas a função zip().   




