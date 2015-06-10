import wmi

class mem_agent(object):
	def __init__(self):
		self.interface = wmi.WMI()
		self.total = self.interface.Win32_OperatingSystem()[0].TotalVisibleMemorySize
		self.data = {}

	def getFreeMem(self):
		return self.interface.Win32_OperatingSystem()[0].FreePhysicalMemory

	def getUsedMem(self):
		free = self.getFreeMem()
		return int(self.total) - int(free)
		
	def getData(self):
		self.data['Free memory'] = self.getFreeMem()
		self.data['Used memory'] = self.getUsedMem()
		return self.data