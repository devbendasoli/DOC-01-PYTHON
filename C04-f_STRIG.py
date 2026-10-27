

#As f-strings (introduzidas no Python 3.6) permitem colocar as variáveis diretamente dentro das chaves {} colocando a letra f antes das aspas, o que deixa o código mais limpo e fácil de ler.

linguagem = "Python"
nivel = "intermediário"

# As variáveis são colocadas diretamente dentro das chaves
mensagem = f"Estou estudando {linguagem} e estou no nível {nivel}."

print(mensagem)
# Saída: Estou estudando Python e estou no nível intermediário.

print("-----")

nome = "marcelo"
pontos = 1500

# Você pode rodar métodos de string ou contas matemáticas direto nas chaves
mensagem = f"Parabéns, {nome.capitalize()}! Sua pontuação é de {pontos * 2} pontos no ranking."

print(mensagem)
# Saída: Parabéns, Marcelo! Sua pontuação é de 3000 pontos no ranking.


print("fim")