from collections import OrderedDict
import binascii
import re

class OSIModel:
	def __init__(self):
		pass

	def applicationLayer(self):
		data = "message"
		size = len(data)
		print 'App Layer data:', data
		print 'size:', size
		print ' '
		return data, size

	def presentationLayer(self, message, size):
		data=[]
		temp=[]
		#converts each character in message to integer representation of ASCII. This can be adapted to fit other encoding formats
		for character in message:
			data.append(ord(character))

		#convert back to original ASCII Chars. This is purely to demonstrate that translation can occur between different syntax's/encodings
		# for i in xrange(0, len(data)):
		# 	data[i] = chr(data[i])

		#Given MIME example header
		data[:0] = '%'
		header = 'MIME-version: 1.0'
		for x in header:
			temp.append(ord(x))
		#	print temp
		data[:0] = temp
		size = len(data)
		print 'Presentation data:', data
		print 'size:', size

		return data, size

	def sessionLayer(self, message, size):

		data=message
		temp=[]

		header = 'SessionHeader'
		for x in header:
			temp.append(ord(x))
		#attach header to beginning of message
		data[:0] = temp
		size = len(data)
		print 'Session data:', data
		print 'size:', size

		return data, size



	def transportLayer(self, message, size):
		data = message
		#following dictionary stores TCP protocol params

		dict = OrderedDict([
		('destPort',self.intToBin(25, 16)),
		('sourcePort',self.intToBin(25, 16)),
		('sequence',self.intToBin(2399401, 32)),
		('ackNumber',self.intToBin(136622, 32)),
		('dataOffset',self.intToBin(4, 4)),
		('reserved',self.intToBin(0, 3)),
		('NS', self.intToBin(0, 1)),
		('URG',self.intToBin(0, 1)),
		('ACK',self.intToBin(1, 1)),
		('PSH',self.intToBin(1, 1)),
		('RST',self.intToBin(0, 1)),
		('SYN',self.intToBin(0, 1)),
		('FIN',self.intToBin(1, 1)),
		('window',self.intToBin(8, 16)),
		('checkSum',self.intToBin(128, 16)),
		('urgPointer',self.intToBin(0, 1))
		])
		#print dict.values()
		data[:0] = list(dict.values())
		size = len(data)
		print 'Transport data:', data
		print 'size:', size

		return data, size


	def networkLayer(self, message, size):
		data = message
 
		IPaddress = "192.168.1.100"
		IP = map(int, IPaddress.split('.'))
		#print IP
		dict = OrderedDict([
		('ip0', self.intToBin(IP[0], 8)),
		('ip1', self.intToBin(IP[1], 8)),
		('ip2', self.intToBin(IP[2], 8)),
		('ip3', self.intToBin(IP[3], 8)),
		])
		data[:0] = list(dict.values())

		size = len(data)
		print 'Transport data:', data
		print 'size:', size
		return data, size

	def dataLinkLayer(self, message, size):
		data = message
		temp = []
		sourceAddr = '01:FF:3C:E4:22:8A'	
		destAddr = '9A:FC:32:54:A8:3E'
		_type = '00'
		#remove : from mac address
		sourceAddr = re.sub(':', '', sourceAddr)
		destAddr = re.sub(':', '', destAddr)
		#convert hex to ascii
		sourceAscii = binascii.unhexlify(sourceAddr)
		destAscii = binascii.unhexlify(destAddr)
		typeAscii = binascii.unhexlify(_type)
		
		#convert ascii to int representation, store in temp list
		for x in sourceAscii:
			temp.append(ord(x))
		for y in destAscii:
			temp.append(ord(y))
		for z in typeAscii:
			temp.append(ord(z))

		data [:0] = temp
		size = len(data)
		print 'DataLink data:', data
		print 'size:', size

		return data, size
	def physicalLayer(self, message, size):
		data = message

		for i in xrange(0, len(data)):
			if type(data[i]) is int:
				data[i] = self.intToBin(data[i], 8)
		transmitted = ''.join(data)
		print 'Transmitted Bits:', transmitted
		print 'size:', size*8

		return transmitted


	def intToBin(self, value, bits):
	#This class converts integer to binary, pads leading 0's to obtain correct length
		number = value
		size = bits
		binary = bin(number)[2:]
		padded = binary.zfill(size)
		return padded


if __name__ == '__main__':
	OSI = OSIModel()
	foo = '00'
	data, size = OSI.applicationLayer()
	data, size = OSI.presentationLayer(data, size)
	data, size = OSI.sessionLayer(data, size)
	data, size = OSI.transportLayer(data, size)
	data, size = OSI.networkLayer(data, size)
	data, size = OSI.dataLinkLayer(data, size)
	global transmittedbits
	transmittedbits = OSI.physicalLayer(data, size)
	
