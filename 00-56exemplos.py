
# ============================================================
# GUIA COMPLETO DAS 56 FUNÇÕES NATIVAS DO PYTHON (1 ao 56)
# ============================================================

print("--- NÍVEL 1: INICIANTE (BEGINNER) ---")

# 1. print() - Exibe dados/saída na tela.
print("\n[1] print():")
print("Olá, mundo!")
# Saída no Terminal: Olá, mundo!

# 2. input() - Aceita entrada/dados digitados pelo utilizador.
print("\n[2] input():")
# nome = input("Qual o seu nome? ")
print("Exemplo: le o texto digitado pelo utilizador no terminal.")

# 3. len() - Retorna o número de itens de um objeto (tamanho).
print("\n[3] len():")
frutas = ["Maçã", "Banana", "Uva"]
print(len(frutas))
# Saída no Terminal: 3

# 4. type() - Retorna o tipo de dado de um objeto.
print("\n[4] type():")
numero = 10
print(type(numero))
# Saída no Terminal: <class 'int'>

# 5. int() - Converte um valor para o tipo número inteiro.
print("\n[5] int():")
texto = "25"
num = int(texto)
print(num + 5)
# Saída no Terminal: 30

# 6. float() - Converte um valor para número decimal (ponto flutuante).
print("\n[6] float():")
valor = float("10.5")
print(valor)
# Saída no Terminal: 10.5

# 7. str() - Converte um valor para o tipo texto (string).
print("\n[7] str():")
idade = 20
print("Idade: " + str(idade))
# Saída no Terminal: Idade: 20

# 8. bool() - Converte um valor para Verdadeiro (True) ou Falso (False).
print("\n[8] bool():")
print(bool(1))
print(bool(0))
# Saída no Terminal:
# True
# False

# 9. list() - Cria/converte um iterável numa lista.
print("\n[9] list():")
palavra = "Python"
print(list(palavra))
# Saída no Terminal: ['P', 'y', 't', 'h', 'o', 'n']

# 10. tuple() - Cria uma tupla imutável (lista que não pode ser alterada).
print("\n[10] tuple():")
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)
# Saída no Terminal: (1, 2, 3)

# 11. set() - Cria um conjunto de valores únicos (sem elementos duplicados).
print("\n[11] set():")
numeros = [1, 2, 2, 3, 3, 4]
conjunto = set(numeros)
print(conjunto)
# Saída no Terminal: {1, 2, 3, 4}

# 12. dict() - Cria um dicionário (estrutura de chave e valor).
print("\n[12] dict():")
pessoa = dict(nome="Ana", idade=25)
print(pessoa)
# Saída no Terminal: {'nome': 'Ana', 'idade': 25}

# 13. range() - Gera uma sequência numérica.
print("\n[13] range():")
print(list(range(5)))
# Saída no Terminal: [0, 1, 2, 3, 4]

# 14. abs() - Retorna o valor absoluto (módulo) de um número (sempre positivo).
print("\n[14] abs():")
print(abs(-15))
# Saída no Terminal: 15

# 15. round() - Arredonda um número para o valor mais próximo ou casas decimais.
print("\n[15] round():")
print(round(3.756, 2))
# Saída no Terminal: 3.76

# 16. max() - Retorna o maior item de um iterável ou entre vários argumentos.
print("\n[16] max():")
print(max([10, 50, 20]))
# Saída no Terminal: 50

# 17. min() - Retorna o menor item de um iterável.
print("\n[17] min():")
print(min([10, 50, 20]))
# Saída no Terminal: 10

# 18. sum() - Soma todos os itens de um iterável.
print("\n[18] sum():")
print(sum([10, 20, 30]))
# Saída no Terminal: 60

# 19. sorted() - Retorna uma nova lista ordenada a partir de qualquer iterável.
print("\n[19] sorted():")
nums = [4, 1, 3, 2]
print(sorted(nums))
# Saída no Terminal: [1, 2, 3, 4]

# 20. reversed() - Retorna um iterador com os elementos na ordem inversa.
print("\n[20] reversed():")
letras = ['a', 'b', 'c']
print(list(reversed(letras)))
# Saída no Terminal: ['c', 'b', 'a']


print("\n------------------------------------------------------------")
print("--- NÍVEL 2: INTERMEDIÁRIO (INTERMEDIATE) ---")
print("------------------------------------------------------------")

# 21. enumerate() - Adiciona um índice/contador aos itens durante a iteração.
print("\n[21] enumerate():")
nomes = ["Ana", "Beto"]
for i, nome in enumerate(nomes):
    print(i, nome)
# Saída no Terminal:
# 0 Ana
# 1 Beto

# 22. zip() - Combina múltiplos iteráveis elemento por elemento.
print("\n[22] zip():")
alunos = ["Ana", "Beto"]
notas = [9.0, 7.5]
print(list(zip(alunos, notas)))
# Saída no Terminal: [('Ana', 9.0), ('Beto', 7.5)]

# 23. map() - Aplica uma função a cada item de um iterável.
print("\n[23] map():")
nums = [1, 2, 3]
dobros = list(map(lambda x: x * 2, nums))
print(dobros)
# Saída no Terminal: [2, 4, 6]

# 24. filter() - Filtra itens de um iterável com base numa condição True/False.
print("\n[24] filter():")
nums = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, nums))
print(pares)
# Saída no Terminal: [2, 4, 6]

# 25. any() - Retorna True se pelo menos um item do iterável for verdadeiro.
print("\n[25] any():")
valores = [False, False, True]
print(any(valores))
# Saída no Terminal: True

# 26. all() - Retorna True apenas se TODOS os itens do iterável forem verdadeiros.
print("\n[26] all():")
valores = [True, True, True]
print(all(valores))
# Saída no Terminal: True

# 27. pow() - Calcula a potência de um número (base elevada ao expoente).
print("\n[27] pow():")
print(pow(2, 3))  # 2³
# Saída no Terminal: 8

# 28. divmod() - Retorna uma tupla com o quociente e o resto da divisão.
print("\n[28] divmod():")
quociente, resto = divmod(10, 3)
print(f"Quociente: {quociente}, Resto: {resto}")
# Saída no Terminal: Quociente: 3, Resto: 1

# 29. isinstance() - Verifica se um objeto é de um determinado tipo de dado.
print("\n[29] isinstance():")
x = 10
print(isinstance(x, int))
# Saída no Terminal: True

# 30. issubclass() - Verifica se uma classe herda de outra classe.
print("\n[30] issubclass():")
class Animal: pass
class Cachorro(Animal): pass
print(issubclass(Cachorro, Animal))
# Saída no Terminal: True

# 31. callable() - Verifica se um objeto pode ser chamado como uma função.
print("\n[31] callable():")
def minha_funcao(): pass
x = 10
print(callable(minha_funcao))
print(callable(x))
# Saída no Terminal:
# True
# False

# 32. id() - Retorna o identificador único na memória de um objeto.
print("\n[32] id():")
a = [1, 2, 3]
print(id(a))
# Saída no Terminal: (exemplo de número de memória: 1402392819283)

# 33. dir() - Lista os atributos e métodos disponíveis num objeto.
print("\n[33] dir():")
texto = "olá"
print(dir(texto)[:3])  # Mostra apenas os 3 primeiros métodos
# Saída no Terminal: ['__add__', '__class__', '__contains__']

# 34. vars() - Retorna o dicionário de atributos de um objeto.
print("\n[34] vars():")
class Pessoa:
    def __init__(self):
        self.nome = "Ana"
p = Pessoa()
print(vars(p))
# Saída no Terminal: {'nome': 'Ana'}

# 35. globals() - Retorna um dicionário com as variáveis globais atuais.
print("\n[35] globals():")
minha_var_global = 100
print("minha_var_global" in globals())
# Saída no Terminal: True

# 36. locals() - Retorna um dicionário com as variáveis locais do escopo atual.
print("\n[36] locals():")
def teste():
    a = 10
    print(locals())
teste()
# Saída no Terminal: {'a': 10}

# 37. iter() - Cria um iterador a partir de um objeto iterável.
print("\n[37] iter():")
lista = [10, 20]
meu_iter = iter(lista)
print(meu_iter)
# Saída no Terminal: <list_iterator object at ...>

# 38. next() - Retorna o próximo item de um iterador.
print("\n[38] next():")
lista = [10, 20]
meu_iter = iter(lista)
print(next(meu_iter))
print(next(meu_iter))
# Saída no Terminal:
# 10
# 20

# 39. slice() - Cria um objeto de fatiamento configurável.
print("\n[39] slice():")
fatia = slice(1, 4)
numeros = [0, 10, 20, 30, 40, 50]
print(numeros[fatia])
# Saída no Terminal: [10, 20, 30]

# 40. format() - Formata um valor numa representação específica.
print("\n[40] format():")
print(format(0.5, ".0%"))
# Saída no Terminal: 50%

# 41. chr() - Retorna o caractere correspondente ao código Unicode enviado.
print("\n[41] chr():")
print(chr(65))
# Saída no Terminal: A

# 42. ord() - Retorna o código Unicode numérico de um caractere.
print("\n[42] ord():")
print(ord("A"))
# Saída no Terminal: 65

# 43. bin() - Converte um número inteiro para string em formato binário.
print("\n[43] bin():")
print(bin(10))
# Saída no Terminal: 0b1010

# 44. hex() - Converte um número inteiro para string em formato hexadecimal.
print("\n[44] hex():")
print(hex(255))
# Saída no Terminal: 0xff

# 45. oct() - Converte um número inteiro para string em formato octal.
print("\n[45] oct():")
print(oct(8))
# Saída no Terminal: 0o10

# 46. repr() - Retorna uma representação em string legível de um objeto.
print("\n[46] repr():")
texto = "Olá\nMundo"
print(repr(texto))
# Saída no Terminal: 'Olá\nMundo'


print("\n------------------------------------------------------------")
print("--- NÍVEL 3: AVANÇADO (ADVANCED) ---")
print("------------------------------------------------------------")

# 47. open() - Abre um ficheiro para leitura, escrita ou alteração.
print("\n[47] open():")
# f = open("arquivo.txt", "w")
# f.write("Olá")
# f.close()
print("Exemplo: abre ficheiros no sistema de arquivos.")

# 48. eval() - Avalia/executa uma expressão Python em string e retorna o resultado.
print("\n[48] eval():")
resultado = eval("10 + 5")
print(resultado)
# Saída no Terminal: 15

# 49. exec() - Executa dinamicamente blocos completos de código Python.
print("\n[49] exec():")
exec("x = 5\nprint(x * 2)")
# Saída no Terminal: 10

# 50. compile() - Compila código em string para código executável Python.
print("\n[50] compile():")
codigo = compile("print('Código compilado!')", "<string>", "exec")
exec(codigo)
# Saída no Terminal: Código compilado!

# 51. super() - Acessa métodos da classe pai (superclasse) na herança.
print("\n[51] super():")
class Pai:
    def falar(self):
        return "Olá do Pai!"

class Filho(Pai):
    def falar(self):
        return super().falar() + " E Olá do Filho!"

f = Filho()
print(f.falar())
# Saída no Terminal: Olá do Pai! E Olá do Filho!

# 52. property() - Cria atributos gerenciados por getters/setters em classes.
print("\n[52] property():")
class Conta:
    def __init__(self):
        self._saldo = 100
    def get_saldo(self):
        return self._saldo
    saldo = property(get_saldo)

c = Conta()
print(c.saldo)
# Saída no Terminal: 100

# 53. staticmethod() - Converte um método em método estático (não recebe self).
print("\n[53] staticmethod():")
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(5, 5))
# Saída no Terminal: 10

# 54. classmethod() - Converte um método em método de classe (recebe cls em vez de self).
print("\n[54] classmethod():")
class Robo:
    quantidade = 0
    @classmethod
    def criar_robo(cls):
        cls.quantidade += 1
        return f"Robôs criados: {cls.quantidade}"

print(Robo.criar_robo())
# Saída no Terminal: Robôs criados: 1

# 55. hasattr() - Verifica se um objeto possui um determinado atributo/método.
print("\n[55] hasattr():")
class Carro:
    cor = "Vermelho"

c = Carro()
print(hasattr(c, "cor"))
print(hasattr(c, "velocidade"))
# Saída no Terminal:
# True
# False

# 56. getattr() - Obtém o valor de um atributo de um objeto pelo seu nome em string.
print("\n[56] getattr():")
class Carro:
    cor = "Azul"

c = Carro()
valor = getattr(c, "cor")
print(valor)
# Saída no Terminal: Azul

print("\n============================================================")
print("FIM DO GUIA COMPLETO")
print("============================================================")
