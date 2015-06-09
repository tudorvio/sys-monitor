import wmi

class disk_agent(object):
	def __init__(self):
		self.interface = wmi.WMI()
		self.disk = self.interface.Win32_PerfRawData_PerfDisk_PhysicalDisk()[0]
		self.bytes_read = self.disk.DiskReadBytesPerSec
		self.bytes_written = self.disk.DiskWriteBytesPerSec
		
	def getRead(self):
		return self.bytes_read
		
	def getWritten(self):
		return self.bytes_written
