from pyStack import Stack

s = Stack()

s.push(5) #5 is added to the last spot in the stack
print s
s.push(3)#3 is added to the last spot in the stack
print s
s.pop()#3 is removed since pop removes the last item in a stack
print s
s.push(2)#2 add back
print s
s.push(8)#8 add back
print s
s.pop()#8 removed
print s
s.pop()#2removed
print s
s.push(9)#9 add back
print s
s.push(1)#1 add back
print s
s.pop()#1 removed
print s
s.push(7)#7 add back
print s
s.push(6)#6 add back
print s
s.pop()#6 removed
print s
s.pop()#7 removed
print s
s.push(4)#4 add back
print s
s.pop()#4 removed
print s
s.pop()#9 removed
print s
#Code output below
'''
[5]
[5, 3]
[5]
[5, 2]
[5, 2, 8]
[5, 2]
[5]
[5, 9]
[5, 9, 1]
[5, 9]
[5, 9, 7]
[5, 9, 7, 6]
[5, 9, 7]
[5, 9]
[5, 9, 4]
[5, 9]
[5]
'''
