

# Exemplo 1: Convertendo String para Inteiro (int)
print("--exemp 1--")

texto_numero = "42"
numero_inteiro = int(texto_numero)
 
print(type(numero_inteiro))
print(numero_inteiro)  

print("-----")
print("--exemp 2--")
# Exemplo 2: Convertendo String ou Inteiro para Float (float)

texto_preco = "19.99"
preco_decimal = float(texto_preco)

print(type(preco_decimal)) 
print(preco_decimal)

print("-----")
print("--exemp 3--")


# Exemplo 3: Convertendo Número ou Booleano para String (str)
# Útil para juntar textos (concatenação)
idade = 44
mensagem = "Minha idade é " + str(idade) + " anos."

print(type(str(idade)))  
# Saída: <class 'str'>
print(mensagem)  
# Saída: Minha idade é 44 anos.
print("-----")
print("--exemp 4--")


# Exemplo 4: Convertendo Valores para Booleano (bool)
# Em Python, números zero, strings vazias e estruturas vazias viram False.
# O restante costuma virar True.

nome = "Python" 
# String preenchida = True
numero_zero = 0  
# Zero = False

print(bool(nome))  # Saída: True
print(bool(numero_zero))  # Saída: False


print("---fim---")


#print(True % False) erro
