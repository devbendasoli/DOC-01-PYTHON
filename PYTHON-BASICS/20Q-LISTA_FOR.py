print("-----")
print("Imicio do COD")
print("=== Percorrendo Listas ===")
nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo", "Fernanda"]
print("Lista de Nomes:", nomes)
print("Tamanho da Lista:", len(nomes))

print("-----")
print("\n# Loop simples lendo cada item")

print("--- Loop Simples ---")
for nome in nomes:
    print("Nome:", nome)
print("-----")

print("# enumerate(): Traz o índice e o valor juntos")
print("\n--- Loop com Enumerate ---")
for posicao, nome in enumerate(nomes):
    print(f"Posição {posicao} -> {nome}")

print("Inicio do COD")
print("-----")    