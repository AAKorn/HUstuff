class Flower:
    
    def __init__(self, name, numPetals, price):
        self._name = str(name)
        self._numPetals = int(numPetals)
        self._price = float(price)

    def setName(self, name):
        self._name = str(name)
    
    def setNumPetals(self, numPetals):
        self._numPetals = int(numPetals)

    def setPrice(self, price):
        self._price = float(price)
    
    def getName(self):
        return self._name
    
    def getNumPetals(self):
        return self._numPetals

    def getPrice(self):
        return self._price
