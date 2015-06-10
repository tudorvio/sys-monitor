import pika
from sys-monitor import conf

class Controller(object):
	def __init__(self):
		self.server_conn = pika.BlockingConnection(pika.ConnectionParameters(controller_addr))
		self.channel = self.server_conn.channel()
		self.channel.queue_declare(queue=status_queue)
		
	def callback(ch, method, properties, body):
		self.sys_status = json.loads(body)
	
	def monitor(self):
		self.channel.basic_consume(callback, queue = status_queue, no_ack = True)
		self.channel.start_consuming()