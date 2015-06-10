import pika
import time

from cpu_agent import *
from mem_agent import *
from net_agent import *
from disk_agent import *

from sys-monitor import conf

class AgentDeployer(object):
	def __init__(self):
		# Initialize agents.
		self.cpu = cpu_agent()
		self.mem = mem_agent()
		self.net = net_agent()
		self.disk = disk_agent()
		# The information will be passed as a dictionary.
		sys_status = {}

	# Get data from the agents and send it to the controller node.
	def run(self):	
		# Connect to controller node. See `conf.py` for controller_addr and status_queue.
		self.server_conn = pika.BlockingConnection(pika.ConnectionParameters(controller_addr))
		self.channel = self.server_conn.channel()
		self.channel.queue_declare(queue=status_queue)
		
		while (True):
			# Get info from agents and pass it using the aforementioned dict.
			sys_status['CPU'] = self.cpu.getData()
			sys_status['Disk'] = self.disk.getData()
			sys_status['Memory'] = self.mem.getData()
			sys_status['Network'] = self.net.getData()
			channel.basic_publish(exchange = '', routing_key = status_queue, body = sys_status)
			# Sleep until next update. See `conf.py` for monitor_interval.
			time.sleep(monitor_interval)

deployed_agents = AgentDeployer()
deployed_agents.run()