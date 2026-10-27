from functools import reduce

print("=== 1. ENTRADA E SAÍDA ===")
print("Olá! Exemplo de saída com print().")

print("\n=== 2. CONVERSÃO DE TIPOS ===")
num_str = "10"
num_int = int(num_str)
num_float = float(num_str)
lista = list((1, 2, 3))
print(f"Texto '{num_str}' -> Inteiro: {num_int}, Float: {num_float}, Lista: {lista}")

print("\n=== 3. FUNÇÕES MATEMÁTICAS ===")
numeros = [-5, 3, 12, 1]
print(f"Lista: {numeros}")
print(f"abs(-5): {abs(-5)} | pow(2, 3): {pow(2, 3)} | round(3.75): {round(3.75)}")
print(f"min: {min(numeros)} | max: {max(numeros)} | soma: {sum(numeros)}")

print("\n=== 4. SEQUÊNCIAS ===")
frutas = ["Maçã", "Banana", "Laranja"]
print(f"Tamanho (len): {len(frutas)}")
print(f"Ordenada (sorted): {sorted(frutas)}")
for i, item in enumerate(frutas):
    print(f"Índice {i}: {item}")

print("\n=== 5. STRINGS ===")
letra = "A"
print(f"Código Unicode de '{letra}' (ord): {ord(letra)}")
print(f"Caractere do código 65 (chr): {chr(65)}")

print("\n=== 6. VERIFICAÇÃO DE TIPOS ===")
x = 42
print(f"Tipo de x (type): {type(x)}")
print(f"x é do tipo int (isinstance)? {isinstance(x, int)}")

print("\n=== 7. MEMÓRIA E REPRESENTAÇÃO ===")
print(f"ID na memória de x (id): {id(x)}")
print(f"Binário de 10 (bin): {bin(10)} | Hexadecimal (hex): {hex(10)}")

print("\n=== 8. PROGRAMAÇÃO FUNCIONAL ===")
nums = [1, 2, 3, 4, 5]
dobros = list(map(lambda n: n * 2, nums))
pares = list(filter(lambda n: n % 2 == 0, nums))
soma_total = reduce(lambda a, b: a + b, nums)
print(f"Dobros (map): {dobros}")
print(f"Pares (filter): {pares}")
print(f"Soma acumulada (reduce): {soma_total}")

print("\n=== 9. ITERADORES E RANGE ===")
meu_range = range(1, 4)
iterador = iter(meu_range)
print(f"Primeiro elemento (next): {next(iterador)}")
print(f"Segundo elemento (next): {next(iterador)}")


print("----------------------------")



