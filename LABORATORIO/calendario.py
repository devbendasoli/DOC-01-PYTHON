


import calendar
from datetime import datetime

# Entrada de dados do utilizador
ano = input("Digite o ano: ").strip()
mes = input("Digite o mês (1-12): ").strip()

try:
    # Converte o texto introduzido para números inteiros
    ano = int(ano)
    mes = int(mes)

    # Valida se o mês está no intervalo de 1 a 12
    if mes < 1 or mes > 12:
        raise ValueError

    # Imprime o cabeçalho visual
    print("\n" + "=" * 55)
    print("                    CALENDÁRIO PYTHON")
    print("=" * 55)

    # Exibe o calendário do mês e ano solicitados
    print(f"\n{calendar.month(ano, mes)}")

    # Obtém a data atual do sistema
    hoje = datetime.now()

    # Se o mês e ano introduzidos forem os atuais, mostra o dia de hoje
    if ano == hoje.year and mes == hoje.month:
        print(f"Hoje: {hoje:%A, %d de %B de %Y}")

    print("=" * 55)

except ValueError:
    # Mensagem exibida caso o utilizador digite letras ou um mês inválido
    print("Por favor, introduza um ano e mês válidos!")
