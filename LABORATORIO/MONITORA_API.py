print("----------")
print("Exemplo de uso do loop while com asyncio" \
" para monitorar uma API e executar outra tarefa em paralelo.")
import asyncio
#importando a biblioteca asyncio para trabalhar 
#com programação assíncrona

async def monitorar_api():
    tentativas = 0
    while tentativas < 5:
        tentativas += 1
        print(f"Verificando status do servidor... Tentativa {tentativas}")
        
# async do asyncio simula uma requisição de 
# rede sem travar a aplicação
        await asyncio.sleep(2)
        
# Simulação de sucesso em uma resposta
        if tentativas == 3:
            print("Conectado com sucesso!")
            break

async def outra_tarefa():
    for i in range(3):
        print(f"  [Outra Tarefa] Rodando em paralelo {i}")
        await asyncio.sleep(1)

async def main():
    # Executa o loop do while e outra tarefa simultaneamente
    await asyncio.gather(monitorar_api(), outra_tarefa())

asyncio.run(main())



#Explicação dos Conceitos e Argumentos Principais:
#1. async def (Corrotinas)
#Em vez de usar a palavra def normal, usa-se async 
#def para definir funções assíncronas. Isto diz ao 
# Python que esta função pode ser pausada e retomada
#a meio da execução, permitindo multitarefa cooperativa.

#2. await
#O comando await é usado dentro de funções assíncronas 
#para pausar a função atual enquanto espera que uma 
#tarefa demorada (como uma consulta a uma API ou base
#de dados) termine. Em vez de congelar o programa todo,
#o Python aproveita para executar outras tarefas nesse intervalo.

#3. asyncio.sleep(2)
#Simula uma pausa ou espera de 2 segundos (por exemplo, 
#o tempo de resposta de uma rede) de forma assíncrona, 
#sem bloquear os outros processos que estejam a correr 
#ao mesmo tempo.

#4. asyncio.gather(...)
#Esta função junta e executa várias tarefas assíncronas 
#em simultâneo (em paralelo). No exemplo, faz com que a 
#função de monitorizar a API e a outra_tarefa corram ao 
#mesmo tempo.

print("fim do exemplo de uso do loop while com asyncio.")
print("\n----------")

