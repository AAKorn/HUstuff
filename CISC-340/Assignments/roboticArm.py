#I ran out of time and was unable to properly figure out how to move the boxes.
#Will update with the functionality at a later time once I have figured it out.
#I currently suspect that I will need a bunch of if statements to check if a
#move would even be legal.
#Here is a class with some functions for our box objects.
 
class boxes:
    def __init__(self):
        self.box = bool
        self.moved = bool
        self.cords = []

    def setCords(self, xCord, yCord, zCord):
        self.cords.append(xCord)
        self.cords.append(yCord)
        self.cords.append(zCord)

    def getCords(self):
        return self.cords

    def showCords(self):
        return str(self.cords)

    def setMoved(self):
        self.moved = True

    def getMoved(self):
        return self.moved

#This function is here just because I do not feel like moving it outside of 
#the class.
    def setDimensions(self, coordinates):
        n = 5
        cords = [None,None,None]
        for x in xrange(0,n):
            cords[0] = x
            for y in xrange(0,n):
                cords[1] = y
                for z in xrange(0,2):
                    cords[2] = z
                    coordinates[str(cords).replace('[','').replace(']','')] = False    
    
    def updateDimensions(self, coordinates):
        coordinates[str(self.cords).replace('[','').replace(']','')] = True

    def moveBox(self, coordinates):
        a = self.cords
        aNewPlus = [aNewPlus.append(x+1) for x in a]
        aNewMinus = [aNewMinus.append(x-1) for x in a]
        aNew1 = []

        if coordinates[str(aNewPlus)] == False:
            print "your"
        if coordinates[str(aNewMinus)] == False:
            print"your"
        
#dCoords is a dictionary used to keep track of the coordinates and if a box
#is there or not. 
dCoords = {}      

#The main method where to code runs and loops. 
def main(dCoords):
    boxes().setDimensions(dCoords)
    while True:
        findBox(dCoords)
        moveBox(dCoords)

#Used as a fuction to find the box in a picture.
def findBox(dCoords):
    #scan the image and put it into a matrix from getPicture()
    #process the image by running the image against a trained model 
    #that has been taught to identify boxes from a picture.
    #determine where the box is on the x,y coordinate plane
    #where 1 foot serves as a 1 value for an element in the list.
    #measure the depth, again in a 1 foot value, by using a ruler. 
    #(I would suggest something else but I do not have any idea how to measure depth)
    
    box1 = boxes()
    box1.setCords(1,4,0)
    print dCoords
    box1.updateDimensions(dCoords)

def getPicture():
    return processedPicture

#This function is not working because I have not yet figured out a way to make
#it work without making the function complicated, writing a lot of code.
def moveBox(self, coordinates):
    a = self.cords
    aNewPlus = [aNewPlus.append(x+1) for x in a]
    aNewMinus = [aNewMinus.append(x-1) for x in a]
    aNew1 = []

    if coordinates[str(aNewPlus)] == False:
        print "your"
    if coordinates[str(aNewMinus)] == False:
        print"your"

main(dCoords)
