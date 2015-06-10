import sqlalchemy as sqla
from sqlalchemy.ext import declarative
from agents import cpu_agent

Base = declarative.declarative_base()

class CPU(Base):
	__tablename__ = 'CPU'
	name = sqla.Column(sqla.String(32))
	cores = sqla.Column(sqla.Integer(2))
	usage = sqla.Column(sqla.Integer(4))

class Network(Base):
	__tablename__ = 'Network'
	sent_bytes = sqla.Column(sqla.String(32))
	received_bytes = sqla.Column(sqla.String(32))

class Disk(Base):
	__tablename__ = 'Disk'
	bytes_read = sqla.Column(sqla.String(32))
	bytes_written = sqla.Column(sqla.String(32))

class Memory(Base):
	__tablename__ = 'Memory'
	free_mem = sqla.Column(sqla.String(32))
	used_mem = sqla.Column(sqla.String(32))