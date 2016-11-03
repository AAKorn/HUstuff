from pyQueue import ArrayQueue

print "If you want to buy type b . If you want to sell type s ."


def buy(numShares, price):
    return numShares * (price * -1)

def sell(numShares, price):
    return numShares * price

FIFO = ArrayQueue()

days = input("How many days are you calculating for?: ")

for x in xrange(days):

    print "Day = " + str(x+1)

    OR = raw_input("Buy or sell?: ")

    if OR == 'b':
        FIFO.enqueue(buy(input("Buy: How many shares?: "), input("At how much?: ")))

    if OR == 's':
        FIFO.enqueue(sell(input("Sell: How many shares?: "), input("At how much?: ")))
    
capitalList = []

for x in xrange(days):
    capitalList.append(FIFO.dequeue())

profit = sum(capitalList)

if profit < 0:
    print "You have lost a total of: $" + str(profit) + " capital."

else:
    print "You have gained a total of: $" + str(profit) + " capital."

