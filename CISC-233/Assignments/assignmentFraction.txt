from __future__ import division

class Fraction:

	def __init__(self, name, top, bottom):
		self.name = name
		if isinstance(top, int):
			self.num = top
		else:
			print self.name,"Error, numerator must be of type int! \n" 

		if isinstance(bottom, int):
			self.den = bottom
		else:
			print self.name,"Error, denominator must be of type int! \n"

	def getDen(self):
		return self.den;


	def getNum(self):
		return self.num;

	def show(self):
		print self.num,"/",self.den

	def __add__(self, oF):
		newNum = self.num * oF.den + self.den * oF.num
		newDen = self.den * oF.den
		return Fraction("newFraction", newNum, newDen)
	def __sub__(self, oF):
		newNum = self.num * oF.den - self.den * oF.num
		newDen = self.den * oF.den
		return Fraction("newFraction", newNum, newDen)
	def __mul__(self, oF):
		newNum = self.num * oF.num
		newDen = self.den * oF.den
		return Fraction("newFraction", newNum, newDen)

	def __truediv__(self, oF):
		newNum = self.num * oF.den
		newDen = self.den * oF.num

		return Fraction("newFraction", newNum, newDen)

	def __gt__(self, oF):
		newSelf = self.num / float(self.den)
		
		newoF = oF.num / float(oF.den)
		
		if newSelf > newoF:
			print str(self.num), "/", str(self.den)," is greater than ", str(oF.num),"/",str(oF.den)

		elif newSelf <= newoF:
			print str(self.num), "/", str(self.den)," is not greater than ", str(oF.num),"/",str(oF.den) 

		else:
			print "Unknown Error"
	def __ge__(self, oF):
		newSelf = self.num / float(self.den)
		
		newoF = oF.num / float(oF.den)

		if newSelf >= newoF:
			print str(self.num), "/", str(self.den)," is greater than or equal to ", str(oF.num),"/",str(oF.den)

		elif newSelf < newoF:
			print str(self.num), "/", str(self.den)," is not greater than or equal to ", str(oF.num),"/",str(oF.den)

		else:
			print "Unknown Error"	

	def __lt__(self, oF):
		newSelf = self.num / float(self.den)
		
		newoF = oF.num / float(oF.den)
		
		if newSelf < newoF:
			print str(self.num), "/", str(self.den)," is less than ", str(oF.num),"/",str(oF.den)

		elif newSelf >= newoF:
			print str(self.num), "/", str(self.den)," is not less than ", str(oF.num),"/",str(oF.den)

		else:
			print "Unknown Error"
	
	def __le__(self, oF):
		newSelf = self.num / float(self.den)
		
		newoF = oF.num / float(oF.den)
		
		if newSelf <= newoF:
			print str(self.num), "/", str(self.den)," is less than or equal to ", str(oF.num),"/",str(oF.den)

		elif newSelf > newoF:
			print str(self.num), "/", str(self.den)," is not less than or equal to ", str(oF.num),"/",str(oF.den)

		else:
			print "Unknown Error"

	def __ne__(self, oF):
		newSelf = self.num / float(self.den)
		
		newoF = oF.num / float(oF.den)

		if newSelf != newoF:
			print str(self.num), "/", str(self.den)," is not equal to ", str(oF.num),"/",str(oF.den)

		elif newSelf == newoF:
			print str(self.num), "/", str(self.den)," is equal to ", str(oF.num),"/",str(oF.den)

		else:
			print "Unknown Error"

# __repr__ returns the formal, readable for the python interpreter, python representation of a string object while __str__ returns the informal, readable for humans, representation of a string.
# the difference is that "'Hello World'" is the __repr__ representation of a string object and 'Hello World' is the __str__ representation of a string object. 
	def __repr__(self, oF):
		return 'Fraction(num=%s, den=%s)' % (self.num, self.den)		

f1 = Fraction("Fraction 1",2,7)
f2 = Fraction("Fraction 2", 3,11)

add = f1 + f2
sub = f1 - f2
mul = f1 * f2
div = f1 / f2

add.show()
sub.show()
mul.show()
div.show()

f2 > f1
f2 < f1
f2 >= f1
f2 <= f1
f2 != f1

f2 < f2
f2 <= f2
f2 > f2
f2 >= f2
