


# 2. TYPE CONVERSION (CONVERSÃO DE TIPOS)

print("\n--- 2. Conversão de Tipos ---")

texto = "10"

print(f"int('10'): {int(texto)}")
print(f"float('10'): {float(texto)}")
print(f"str(10): {str(10)}")
print(f"bool(1): {bool(1)}")

print("-----")


#1. list() — Quando você precisa de uma lista que pode ser alterada

produtos_iniciais = ("Arroz", "Feijão")

# Transformamos em lista para poder adicionar mais itens com .append()
cesta_compras = list(produtos_iniciais)
cesta_compras.append("Macarrão")

print(cesta_compras)  # Saída: ['Arroz', 'Feijão', 'Macarrão']

print("------")

#2. tuple() — Quando você quer proteger seusdados para não mudarem por engano

# Sua lista de configurações mutáveis
configuracoes_usuario = ["modo_escuro", "notificacoes_ativadas"]

# Transformamos em tupla para "congelar" a segurança dos dados
configuracoes_seguras = tuple(configuracoes_usuario)

print(configuracoes_seguras)  # Saída: ('modo_escuro', 'notificacoes_ativadas')
# Se tentar alterar algum item aqui depois, o Python vai dar erro de propósito para te proteger.

print("-----")
#3. set() — Quando você precisa tirar itens duplicados

# Lista com cidades repetidas que os usuários digitaram
cidades_digitadas = [
    "São Paulo",
    "Rio de Janeiro",
    "São Paulo",
    "Curitiba",
    "Rio de Janeiro",
]

# Transformamos em set para limpar e manter apenas os valores únicos
cidades_unicas = set(cidades_digitadas)

print(cidades_unicas)  # Saída: {'Curitiba', 'São Paulo', 'Rio de Janeiro'} (a ordem pode variar e os repetidos somem)

print("-----")

#4. dict() — Quando você precisa buscar um valor através de uma chave (como um dicionário de verdade)

# Lista de pares (Código do produto e Preço)
dados_produto = [("codigo_01", 150.00), ("codigo_02", 45.50)]

# Transformamos em dicionário para facilitar a busca pelo código
tabela_precos = dict(dados_produto)

print(tabela_precos)  # Saída: {'codigo_01': 150.0, 'codigo_02': 45.5}
print(
    tabela_precos["codigo_01"]
)  # Saída: 150.0 (você acha o preço direto pela chave!)

