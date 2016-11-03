class creditCard:
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def getBalance(self):
		return self.balance

	def getName(self):
		return self.name

	def showCustomerInfo(self):
		print "Name: ","'", self.name,"'", "Balance: ", self.balance

	def spend(self, cost):
		self.balance = self.balance + cost
		print self.balance

	def payment(self, cost):
		self.balance = self.balance - cost
		print self.balance


James = creditCard("James", 0)

James.showCustomerInfo()
James.spend(500)



