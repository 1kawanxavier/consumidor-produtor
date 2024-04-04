import pika
import time
import threading
import sys

# Configuração da conexão RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='fila')

# Lock para proteger o acesso ao canal
lock = threading.Lock()

# Função produtor
def produtor(mensagem):
    with lock:
        channel.basic_publish(exchange='', routing_key='fila', body=mensagem)
        print(f'Produzido: {mensagem}')

# Thread para produtor
thread_produtor = threading.Thread(target=produtor, args=(sys.argv[1],))

# Iniciar a thread
thread_produtor.start()
