import wmi

class disk_agent(object):
	def __init__(self):
		self.interface = wmi.WMI()
		self.disk = self.interface.Win32_PerfRawData_PerfDisk_PhysicalDisk()[0]
		self.bytes_read = self.disk.DiskReadBytesPerSec
		self.bytes_written = self.disk.DiskWriteBytesPerSec
		self.data = {}

	def getRead(self):
		return self.bytes_read

	def getWritten(self):
		return self.bytes_written

	def getData(self):
		self.data['bytes_read'] = self.getRead()
		self.data['bytes_written'] = self.getWritten()
		return self.data