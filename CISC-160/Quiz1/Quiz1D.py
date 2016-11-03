class Horse:
    def __init__(self,_name,_weight,_color,_speed,_jumpHeight):
        self.name = _name
        self.weight = _weight
        self.color = _color
        self.speed = _speed
        self.jumpHeight = _jumpHeight

    def run(self):
        if self.weight > 1200:
            self.setTopSpeed(55)
        else:
            self.setTopSpeed(60)

    def jump(self):
        if self.weight > 1200:
            self.setPeakJumpHeight(8)
        else:
            self.setPeakJumpHeight(10)


    def setTopSpeed(self, speed):
        self.speed = speed
                
    def getTopSpeed(self):
        return self.speed

    def setPeakJumpHeight(self, jumpHeight):
        self.jumpHeight = jumpHeight

    def getPeakJumpHeight(self):
        return self.jumpHeight



James = Horse("James", 1300,"black",None,None)

James.run()

print"James' top speed is", James.getTopSpeed(),"mph"

James.jump()

print"James' peak jump height is", James.getPeakJumpHeight(),"feet"

