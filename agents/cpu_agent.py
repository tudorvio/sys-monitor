import wmi

class cpu_agent(object):
	def __init__(self):
		self.interface = wmi.WMI()				
		self.cpu = self.interface.Win32_Processor()[0]
		self.cores = self.cpu.NumberOfCores
		self.description = self.cpu.Name
		self.data = {}

	def getUsage(self):
		return self.cpu.LoadPercentage

	def getCores(self):
		return self.cores

	def getDescription(self):
		return self.description

	def getData(self):
		self.data['Name'] = self.getDescription()
		self.data['Cores'] = self.getCores()
		self.data['Usage'] = self.getUsage()
		return self.data