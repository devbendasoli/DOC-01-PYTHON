
print("-----------------------------------")
print("Exemplo de uso de fila com sinalizador" \
" de encerramento (Poison Pill)")
import queue#import queue
import time#import time
import threading#import threading

fila_tarefas = queue.Queue()

def consumidor():
    print("[Consumidor] Iniciado e aguardando tarefas...")
    while True:
# Bloqueia até receber um item. Se receber o 
# sinal "PARAR", o loop encerra.
        tarefa = fila_tarefas.get()
        if tarefa == "PARAR":
            break
            
        print(f"[Consumidor] Processando: {tarefa}")
        time.sleep(1)  # Simula o processamento da tarefa
        fila_tarefas.task_done()
        
    print("[Consumidor] Loop encerrado com segurança.")

# Iniciando a thread consumidora
thread = threading.Thread(target=consumidor)
thread.start()

# Adicionando dados dinamicamente
fila_tarefas.put("Relatório Financeiro")
fila_tarefas.put("Enviar E-mails")

time.sleep(3)
fila_tarefas.put("PARAR") 
# Sinalizador de encerramento (Poison Pill)


print("[Main] Aguardando a thread consumidora finalizar...")
prin("------------------------------------")