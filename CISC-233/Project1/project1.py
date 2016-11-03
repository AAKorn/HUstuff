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

#######################################################################Client
import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.2.105.156', 8890))

message = "Hello, my name is Alexander Korn. The ladies call me bigchiefmaiz. What is yours?"

shift = random.randrange(1,26)

while message != "q":
	if len(message) >= 64:
		encryptedList = [chr(ord(x)+shift) for x in message]
        	encryptedMessage = ''.join(encryptedList)
        	print encryptedMessage
		s.send(encryptedMessage)
	else:
		print "Message either not long enough or there isn't one."

	message = raw_input("->")

if message =="q":
	s.send("q")

s.close()
print 'goodbye!'
