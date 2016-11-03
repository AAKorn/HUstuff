from pyStack import Stack

def parChecker(sS):
    s = Stack()
    balanced = True
    index = 0
    while index < len(sS) and balanced:
        symbol = sS[index]

        if symbol == "(":
            s.push(symbol)

        elif s.isEmpty():
            balanced = False

        else:
            s.pop()

        index +=1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print parChecker('((()))')
print parChecker('(()')

