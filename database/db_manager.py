import sqlalchemy as sqla
from models import *

class db_manager(object):
	def __init__(self):
		self.engine = create_engine(database, echo=True)
		Base.metadata.bind = engine
		Base.metadata.create_all()
		session = orm.sessionmaker(bind=engine)
		
	def 