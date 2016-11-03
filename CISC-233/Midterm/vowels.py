import random

#Begin generating a random string

nums = [random.randrange(1,26) for x in range(10)]

letters = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

newList = [letters[x] for x in nums]

string = ''.join(newList) 

#End generating a random string

counter = -1
numVowels = 0
numConsonants = 0

def moreVowels(s, counter, numVowels, numConsonants):

    vowels = ['a','e','i','o','u', 'y']

    listString = list(s)

    counter = counter + 1

    if counter == len(listString):

        if numVowels > numConsonants:
            print s
            print "This string has more vowels than consonants: "
            print "Number of vowels: " + str(numVowels)
            print "Number of consonants: " + str(numConsonants)
            return

        elif numVowels == numConsonants:
            print s
            print "This string has an even numver of vowels and consonants: " 
            print "Number of vowels: " + str(numVowels)
            print "Number of consonants: " + str(numConsonants)
            return

        else:
            print s
            print "This string has more consonants than vowels: " 
            print "Number of vowels: " + str(numVowels)
            print "Number of consonants: " + str(numConsonants)
            return

    if listString[counter] in vowels:
        numVowels = numVowels + 1

    else:
        numConsonants = numConsonants + 1
 
    moreVowels(s, counter, numVowels, numConsonants)

moreVowels(string, counter, numVowels, numConsonants)
    
