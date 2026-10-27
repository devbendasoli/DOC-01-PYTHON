#capiture senha 
print("Digite sua senha numérica pra cadrastro")
senha_nu = input("Digite senha cadrastro" )
print(" ")
print("Digite uma senha com letras para cadrastro" )
senha_le = input(" Digitar letras pra cadrastro" )
print(" ")
senha_nu_add = int(input("Digite sua senha" ))
print(" ")
senha_le_add = input("Digite as 3 letras de sua senha" )
print(" ")

if senha_nu == senha_nu_add and senha_le == senha_le_add:
    print("Senha correta")
    
elif senha_nu != senha_nu_add and senha_le != senha_le_add:
    
senha_nu_add  = 0
while senha_nu_add < 3:
    print(f"senha_nu_add: {senha_nu_add}")
    senha_nu_add += 1
    
    
    print("senha errada, digite novamente")
    senha_nu_add = int(input("Digite sua senha"))
    senha_le_add = input("Digite as 3 letras de sua senha")
    else:
        print("Senha incorreta")
        print("senha bloqueado")
        
        
     
     
        
    
    



