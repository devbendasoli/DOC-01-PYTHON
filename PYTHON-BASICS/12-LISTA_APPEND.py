print("----------")
print("inicio do programa")
print("Exemplo de lista")
# Lista (coleção ordenada)
numeros = [10, 20, 30, 40]

# Adicionar um numero na lista
novo_numero = int(input("Digite um número para" \
" adicionar ao final da lista: "))
numeros.append(novo_numero)

print(numeros) 
# Saída: [10, 20, 30, 40, (número digitado)]

# Acessa item da lista pelo índice
numero_digitado = int(input(
    "Digite o índice do número que " \
    "deseja acessar (0 a 4): " \
    ""))
print("O número digitado foi: ", numero_digitado)
print("O valor da lista é: ", numeros[numero_digitado]) 
# Saída: do índice digitado    

print("----------")
print("Exemplo de dicionário")
print("----------")

# Dicionário (chave e valor)
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessa o valor da chave "nome"
print(pessoa["nome"])
#saida : Ana
print(pessoa["idade"])  
#saida : 25
print("fim do programa")
print("----------")