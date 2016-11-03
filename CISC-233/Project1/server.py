##########################################################Server
import socket
import sys

HOST = '10.2.105.156' 
PORT = 8890
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'socket created'

try:
	s.bind((HOST, PORT))

except socket.error as err:
	print 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1]
	sys.exit()

print 'Socket Bind Success!'

s.listen(10)
print 'Socket is now listening'

choice = raw_input("Do you wish to continue?: ")

if choice == "n":
	s.close()

conn, addr = s.accept()

while True:
	print 'Connect with ' + addr[0] + ':' + str(addr[1])
	data = conn.recv(1024)
	if data == "q":
		print "goodbye!"
		break

	for shift in xrange(1,27):
    		dencryptedList = [chr(ord(x)-shift) for x in data]
    		dencryptedMessage = ''.join(dencryptedList)
    		print dencryptedMessage
	

s.close()


