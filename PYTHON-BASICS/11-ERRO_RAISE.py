
#O raise é usado quando queres forçar o programa a dar um erro de propósito sob determinada condição.
#Por que usamos? Às vezes, um valor é um número válido para o Python, mas inválido para a lógica do teu programa.
#Exemplo: O número 13 é um inteiro válido para o Python, mas não existe o mês 13! Usamos o raise para disparar um alarme de erro e interromper a execução normal.

print("-----")
print("Início do programa.")
mes = int(input("Digite um número de mês (1 a 12): "))
print("Você digitou o mês:", mes) 
# simulando o erro - digite um número de mês inválido, 
# como 13 ou 0, para ver o raise em ação
try:
    if mes < 1 or mes > 12:
        raise ValueError("Mês inválido!") 
# Força a ida imediata para o bloco 'except'
except ValueError:
    print("Ocorreu um erro: mês esta fora do intervalo correto.")    
#Quando o Python encontra a linha com raise, ele para imediatamente
#  o bloco try e pula direto para o bloco except correspondente para 
#  tratar a exceção
print("Fim do programa.")
print("-----")
    
    
