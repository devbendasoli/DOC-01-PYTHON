



# 6. FILE HANDLING (MANIPULAÇÃO DE FICHEIROS)
print("\n--- 6. Ficheiros ---")
with open("teste.txt", "w") as f:
    f.write("Olá Ficheiro!")
with open("teste.txt", "r") as f:
    print(f"Lido do ficheiro: {f.read()}")