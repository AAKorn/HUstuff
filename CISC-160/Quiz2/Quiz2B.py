from pyStack import Stack
import random 

s = Stack()

def pushAndReverse(s):
	
	for i in xrange(0,10):
		x = random.randrange(0,10)
		s.push(x)
		if i == 9:
			print s	
	s.reverse()
	print s

pushAndReverse(s)
#Code output below
'''
[4, 6, 9, 5, 2, 4, 1, 6, 4, 0]
[0, 4, 6, 1, 4, 2, 5, 9, 6, 4]
'''
