import wmi

class net_agent(object):
	def __init__(self):
		self.interface = wmi.WMI()
		self.net = self.interface.Win32_PerfRawData_Tcpip_NetworkInterface()[0]
		self.bytes_sent = self.net.BytesSentPerSec
		self.bytes_received = self.net.BytesReceivedPerSec
		
	def getSent(self):
		return self.bytes_sent
		
	def getReceived(self):
		return self.bytes_received
