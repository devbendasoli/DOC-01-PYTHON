

texto_original = "PYTHON É MUITO BOM!"
texto_minusculo = texto_original.lower()

print(texto_minusculo)
# Saída: python é muito bom!

print("-----")

resposta = input("Você deseja continuar? (Sim/Não): ")

# Transformamos tudo em minúsculo para comparar com segurança
if resposta.lower() == "sim":
  print("Continuando o programa...")
else:
  print("Operação cancelada.")
  
