def longestPalindrome(dna):

    dnaStack = []
    palindromeBuffer = []
    dnaList = list(dna)
    newDnaDictionary = {}
    count = 0

    for x in xrange(0,len(dnaList)):

        dnaStack.append(dnaList[x])

        if palindromeBuffer == []:
            palindromeBuffer.append(dnaList[x])

        if 0 <= x+1 < len(dnaList):
	    palindromeBuffer.append(dnaList[x+1]) 
        
        print palindromeBuffer 

        if isReverse(palindromeBuffer):
            print "PALINDROME FOUND"
	    print palindromeBuffer
            newDnaDictionary[''.join(palindromeBuffer)] = True
            palindromeBuffer = []

def isReverse(palindromeBuffer):
    listString = palindromeBuffer
    newListString = []
    for x in xrange(0,len(listString)):
        newListString.insert(0, listString[x])
    if ''.join(listString) == ''.join(newListString):
        return True
    else:
	return False









dna = "CACAATTCCCATGGGTTGTGGAG"
longestPalindrome(dna)
