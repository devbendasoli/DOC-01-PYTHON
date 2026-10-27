
while True:
    resposta = input(" Digite 'sair' para encerrar o programa ")
    if resposta.lower() == 'sair':
        print("Programa encerrado")
        break
        
        
print("------------------")    
  
  
cont = 0
while cont < 5:
    cont += 1
    if cont == 3:
        print("pulando o 3")  # Colocado ANTES do continue
        continue 
    print(cont)