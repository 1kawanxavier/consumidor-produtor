import pika
import threading

# Configuração da conexão RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Função consumidor
def consumidor():
    def callback(ch, method, properties, body):
        print(f'Recebido: {body.decode()}')

    channel.basic_consume(queue='fila', on_message_callback=callback, auto_ack=True)
    print('Aguardando mensagens...')
    channel.start_consuming()

# Thread para consumidor
thread_consumidor = threading.Thread(target=consumidor)

# Iniciar a thread
thread_consumidor.start()
