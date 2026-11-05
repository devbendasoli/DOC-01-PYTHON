
print("-----")
print("\n-----Funções em Python-----")

print("# Definindo uma função simples")
def saudar(nome):
    return f"Olá, {nome}!"

print("# Chamando a função")
mensagem = saudar("Maria")
print(mensagem)

print("-----")
print("\n# Função com múltiplos parâmetros")
def calcular_area(largura, altura):
    return largura * altura
print("# Chamando a função")
area = calcular_area(5, 10)
print(f"A área é: {area}")

print("-----")
print("\n# Função com valor padrão para um parâmetro")
def cumprimentar(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"
print("# Chamando a função com o valor padrão")
mensagem = cumprimentar("João")
print(mensagem)
print("-----")
print("# Chamando a função com um valor diferente para o parâmetro")
mensagem = cumprimentar("João", "Oi")
print(mensagem)

print("-----")
def somar(a, b):
    return a + b

resultado = somar(10, 15)
print(resultado)  # Output: 25

print("Fim do código de funções em Python.")
print("-----")

