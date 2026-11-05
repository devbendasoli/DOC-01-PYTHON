
#or
print("or -> Ou uma ou outra vai ser valida")
entrada = input('[E]ntrar [S]air ')
senha_digitada = input("senha ")
senha_permitida = "1234"

if(entrada == "E" or entrada == "e" ) and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

#=============================== 
print(20 * "#")    
#===============================

#and
 print("and -> as duas são verdadeira - true ")   
# Entradas do usuário
dig_senha = input("Digite a senha numérica: ")
dig_letra = input("Digite as letras: ")

# Valores esperados
senha_correta = '12345'
letra_correta = 'ABC'

# O 'and' exige que as DUAS comparações sejam verdadeiras ao mesmo tempo
if dig_senha == senha_correta and dig_letra == letra_correta:
    print("Acesso permitido!")
else:
    print("SENHA ERRADA")
    
    
    
        