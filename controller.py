import pika
from sys-monitor import conf

class Controller(object):
	def __init__(self):
		self.server_conn = pika.BlockingConnection(pika.ConnectionParameters(controller_addr))
		self.channel = self.server_conn.channel()
		self.channel.queue_declare(queue=status_queue)
		
	def callback(ch, method, properties, body):
		# TO DO: convert the received dict to JSON and load it into an SQLAlchemy db.
		# Not sure if it's the way to go, I'm still researching this.
	
	def monitor(self):
		self.channel.basic_consume(callback, queue = status_queue, no_ack = True)
		self.channel.start_consuming()