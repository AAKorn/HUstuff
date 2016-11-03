def remDuplicates(string):
    listString = list(string)
    print "".join(listString)
    for x in listString:
        count = 0
        for y in listString:
            if x == y:
                count +=1
                if count >=2:
                    listString.remove(y)     
                    print "".join(listString)

string = "MMom your"
remDuplicates(string)
