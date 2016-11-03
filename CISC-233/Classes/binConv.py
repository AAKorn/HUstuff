from pyStack import Stack

def binaryConversion(n):
    s = Stack()

    while n > 0:
        remainder = n % 2
        newN = n / 2    

        if newN < 1:
            s.push(remainder)
            s.reverse()
            print s
            break

        else:
            s.push(remainder)
            n = newN

inputNum = int(raw_input("What number will you convert?: "))

binaryConversion(inputNum)
