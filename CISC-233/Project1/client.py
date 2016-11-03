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
