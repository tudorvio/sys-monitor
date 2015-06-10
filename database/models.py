from sqlalchemy.ext import declarative
from sys-monitor.agents import cpu_agent

Base = declarative.declarative_base()

class CPU(Base):
	__tablename__ = 'CPU'
	name = Column(String(32))
	cores = Column(Integer(2))
	usage = Column(Integer(4))
	
class Network(Base):
	__tablename__ = 'Network'
	sent_bytes = Column(String(32))
	received_bytes = Column(String(32))
	
class Disk(Base):
	__tablename__ = 'Disk'
	bytes_read = Column(String(32))
	bytes_written = Column(String(32))
	
class Memory(Base):
	__tablename__ = 'Memory'
	free_mem = Column(String(32))
	used_mem = Column(String(32))