        
print("-----------")    
print("Inicio do programa")  
  
cont = 0
while cont < 5:
    cont += 1
    if cont == 3:
        print("pulando o 3")  # Colocado ANTES do continue
        continue #Aqui ele pula e continua para a
# próxima iteração do loop, sem executar o print abaixo
    print(cont)

print("fim do programa")
print("----------")    