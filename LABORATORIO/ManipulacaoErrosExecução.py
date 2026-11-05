

# =========================================================
# FUNÇÕES DE EXECUÇÃO E MANIPULAÇÃO DE CÓDIGO
# =========================================================

# 1. eval(): Avalia e executa uma expressão matemática ou lógica simples
print("--- 1. Função eval() ---")
expressao = "5 * 4 + 10"
resultado_eval = eval(expressao)
print(f"Expressão: '{expressao}'")
print(f"Resultado com eval(): {resultado_eval}")

# 2. exec(): Executa blocos de código Python dinâmicos (várias linhas)
print("\n--- 2. Função exec() ---")
codigo_dinamico = """
nome = 'Python'
versao = 3.12
mensagem = f'Linguagem: {nome} v{versao}'
print(mensagem)
"""
print("Executando bloco de código com exec():")
exec(codigo_dinamico)

# 3. compile(): Compila código em um objeto de código executável
print("\n--- 3. Função compile() ---")
codigo_fonte = "x = 100 * 2"
# Compilando a string de código para modo 'exec'
codigo_compilado = compile(codigo_fonte, '<string>', 'exec')

# Executando o código compilado com exec()
ambiente = {}
exec(codigo_compilado, ambiente)
print(f"Valor da variável 'x' após compilar e executar: {ambiente['x']}")


# ==========================================
# SAÍDA ESPERADA NO TERMINAL (VISUALIZAÇÃO):
# ==========================================
# --- 1. Função eval() ---
# Expressão: '5 * 4 + 10'
# Resultado com eval(): 30
#
# --- 2. Função exec() ---
# Executando bloco de código com exec():
# Linguagem: Python v3.12
#
# --- 3. Função compile() ---
# Valor da variável 'x' após compilar e executar: 200