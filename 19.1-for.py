
#for range contas os números 
for i in range(10):
    if i == 3:
        print('  i é 3, pulando...')
        #print(i)
        continue

    if i == 7:
        print('  i é 7, então break seu else não executará')
        break

    for j in range(1, 4):
       # print(j, i)
       print(f" {j} coluna e {i} linha")
        
else:
    print('For completo com sucesso!')
print("FIM DE COD")    
print(" ---")
