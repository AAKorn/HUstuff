import random

print "Welcome, the rules are as follows: "
print "Only enter lower-case letters"


n = 6 #max number of attempts

attempt = 0 #attmept counter

#Our list of possible words/phrases
listOfString = ["We are in for it now Scoob", "Defeating a sandwich only makes it tastier", "Harambe", "Cogito Ergo Sum"]

#Randomly choose our word/phrase for the game
string = listOfString[random.randrange(0,len(listOfString))]

#Used only to hold the lower-case string.
lisT = []

#Self explanatory.
obscuredString = []

guesses = []

#Lower case the word/phrase and put it into a list.
for x in string:
    lisT.append(x.lower())

#Obscure the string.
for x in lisT:
    if x == " ":
        obscuredString.append(x)    
    else:
        obscuredString.append(x.replace(x,"_"))

lenObscuredString = [x for x in obscuredString if x !=" "]

#Our main function hangMan
def hangMan(lisT, attempt, n):
    print len(lenObscuredString)
#Drawing for the user begins
    if attempt == 0:
        print"-------"
        print"|   |"
        print"|"
        print"|"
        print"|"
    if attempt == 1:
        print "------"
        print "|  |"
        print "|  O"
        print "|   "
        print "|   "
    if attempt == 2:
        print"-------"
        print"|   |"
        print"|   O"
        print"|   |"
        print"|"
    if attempt == 3:
        print"------"
        print"|   |"
        print"|   O"
        print"|  /|"
        print"|"
    if attempt == 4:
        print"------"
        print"|   |"
        print"|   O"
        print"|  /|\ "
        print"|"
    if attempt == 5:
        print"------"
        print"|   |"
        print"|   O"
        print"|  /|\ "
        print"|  /"
    if attempt == n:
        print"------"
        print"|   |"
        print"|   O"
        print"|  /|\ "
        print"|  / \ "
        print"\n"
        print "GAME OVER"
        return
#Drawing for the user ends.

#Pretty formating for the user.
    obscuredString2 = ','.join(obscuredString)
    print obscuredString2.replace(',',' ')

    guess = raw_input("What letter will you guess?: ")

#If your guess is correct, update the obscuredString list and print it.
    for x in xrange(0,len(lisT)):
        if lisT[x] == guess:
            obscuredString[x] = guess
#Formating so the user has a more pleasant experience. 
            obscuredString3 = ','.join(obscuredString)
            print obscuredString3.replace(',','')

    for x in xrange(0,20):
        print "\n"

#Attempt counter will increase when you have made a wrong guess
    if guess not in lisT:
        attempt+=1
        print "You have:",n - attempt,"attempts left"
        guesses.append(guess)
        print "Wrong Guesses"
        print guesses

#Check if the word has been solved
    if "_" in obscuredString:
        hangMan(lisT, attempt, n)
    else:
        print obscuredString
        print"Congrats you win!"

hangMan(lisT, attempt, n)
