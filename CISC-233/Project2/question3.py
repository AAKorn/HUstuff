import urllib2
from pyStack import Stack
response = urllib2.urlopen('http://google.com/')
html = response.read()

def htmlChecker(string):
    s = Stack()
    openCount = 0    
    closeCount = 0
    
    for x in string:
        if x == "<":
            openCount+=1

    for y in string:
        if y == ">":
            closeCount+=1

    if openCount != closeCount:
        print "You already failed."
        print "Ensure your opening and closing tags have the proper syntax."

    else:
        print "Ok, the fun starts here!" 
        for z in string:
            s.push(z)
        
        newClose = 0        

        for i in xrange(0, s.size()):
            if s.returnIndexElement(i) == "<" and s.returnIndexElement(i+1) == "/":
                newClose+=1 
            
        if openCount - newClose == newClose:
            print "Congrats, at least your html tags have proper opening and closing syntax."
        else:
            print "Well at least you tried."
            print "Try checking to make sure you have '/' , minus the single quotes, after the ls in closing tag."

htmlChecker(html)
