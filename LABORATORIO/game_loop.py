
print("----------")
print("Controle de Frequência de " \
"Loop (Game Loop / Polling)")
# Controle de Frequência de Loop 
# (Game Loop / Polling)

#Este padrão é muito usado em automações, 
# robótica (IoT) ou jogos para garantir que 
# um ciclo roda exatamente a um intervalo de 
# tempo fixo por segundo, compensando o tempo 
# que a tarefa demora a executar.  

import time

frequencia_alvo = 1.0 
# Executar estritamente a cada 1 segundo
proxima_execucao = time.time() + frequencia_alvo

while True:
    print("Executando tarefa crítica baseada em tempo...")
    
# Simula um código que demora tempos variados 
# para rodar (ex: entre 0.1 e 0.5s)
    time.sleep(0.3)
    
# Calcula exatamente quanto tempo precisa 
# esperar até o próximo ciclo exato
    tempo_restante = proxima_execucao - time.time()
    if tempo_restante > 0:
        time.sleep(tempo_restante)
        
    proxima_execucao += frequencia_alvo
       
#time.time(): Retorna a hora atual do sistema 
# em segundos (timestamp UTC). Serve como 
# relógio base para medir o tempo exato que passou.

#tempo_restante = proxima_execucao - time.time():
#  Subtrai ao momento em que a tarefa devia acontecer
#  o momento atual, descobrindo os segundos de folga 
# para manter a frequência cravada.    

print("Fim do loop de controle de frequência.")    
print("----------")

 
    