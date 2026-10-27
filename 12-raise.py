
#O raise é usado quando queres forçar o programa a dar um erro de propósito sob determinada condição.
#Por que usamos? Às vezes, um valor é um número válido para o Python, mas inválido para a lógica do teu programa.
#Exemplo: O número 13 é um inteiro válido para o Python, mas não existe o mês 13! Usamos o raise para disparar um alarme de erro e interromper a execução normal.


mes = 13 # simulando o erro


try:
    if mes < 1 or mes > 12:
        raise ValueError("Mês inválido!")  # Força a ida imediata para o bloco 'except'
except ValueError:
    print("Ocorreu um erro: mês fora do intervalo correto.")
    
#Quando o Python encontra a linha com raise, ele para imediatamente o bloco try e pula direto para o bloco except correspondente para tratar a exceção

    
    
