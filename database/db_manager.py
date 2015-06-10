import sqlalchemy as sqla
import models

class db_manager(object):
	def __init__(self):
		self.engine = create_engine(database, echo=True)
		Base.metadata.bind = engine
		Base.metadata.create_all()
		session = orm.sessionmaker(bind=engine)
		conn = self.engine.connect()
		
		self.cpu_table = models.CPU()
		self.mem_table = models.Memory()
		self.net_table = models.Network()
		self.disk_table = models.Disk()

	def update(self, sys_info):
		for device in sys_info: 
			if device == 'CPU':
				ins = cpu_table.insert().values(name = device[name], cores = device[cores], usage = device[usage])
			elif device == 'Memory':
				ins = mem_table.insert().values(free_mem = device[free_mem], used_mem = device[used_mem])
			elif device == 'Network':
				ins = net_table.insert().values(sent_bytes = device[sent_bytes], received_bytes = device[received_bytes])
			elif device == 'Disk':
				ins = disk_table.insert().values(bytes_read = device[bytes_read], bytes_written = device[bytes_written])
			else: print 'Unknown device.'
			conn.execute(ins)