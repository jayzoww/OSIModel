from collections import OrderedDict
import Part1
import binascii
import re

class CRC:
	def __init__(self):
		pass

	def generate(self, message, polynomial):
		data = message
		poly =  polynomial
		data = re.sub('%', '', data)
		dataPadded = data.ljust(len(data)+len(poly)-1, '0')
		print 'Padded Data: ', dataPadded
		#convert both polynomial and data to decimal
		polyInt = int(poly, 2)
		dataInt = int(dataPadded, 2)

		print 'Polynomial to int:', polyInt
		print 'Padded to integer:', dataInt

		remain = dataInt%polyInt
		print 'remainder:', remain

		remainBin = bin(remain)[2:].zfill(15)
		print 'Remainder in Bin:', remainBin

		dataEncoded = data+remainBin
		print 'Encoded Data:', dataEncoded
		print 'Encoded in int', int(dataEncoded, 2)

		return dataEncoded
	def verify(self, message, polynomial):
		dataCheck = message
		polyCheck = polynomial

		print 'Data to be decoded: ', dataCheck
		print 'polynomial: ', polyCheck

		polyCheckInt = int(polyCheck, 2)
		dataCheckInt = int(dataCheck, 2)
		print 'Polynomial to int:', polyCheckInt
		print 'data to integer:', dataCheckInt
		remain = dataCheckInt%polyCheckInt


		if remain == 0:
			return 'Correct'
		else: 
			return 'Altered'

	def alter(self, message, bit):
		dataToAlter = message
		position = int(bit) - 1
		temp = []
		alteredData = ''
		for i in dataToAlter:
			temp.append(i)
		#print temp

		if temp[position] == '0':
			temp[position] == '1'
		else:
			temp[position] == '0'
		#print temp

		for i in xrange(0, len(temp)):
			alteredData = alteredData+temp[i]
		return alteredData

if __name__ == '__main__':
	CRC = CRC()
	transmittedBits = '111111111111111111111111'
	polynomial = '1100000000000101'
	bit = 8
	EncodedMessage = CRC.generate(transmittedBits, polynomial)
	#print EncodedMessage
	AlteredMessage = CRC.alter(EncodedMessage, bit)
	verifyData = CRC.verify(AlteredMessage, polynomial)
	#print verifyData
	#print Part1.transmittedbits




