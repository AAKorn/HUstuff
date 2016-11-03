class BankAccount:
    
    def __init__(self, ammount, username, password):
        self.ammount = ammount
        self.balance = ammount
        self.username = username
        self.password = password
        self.type = raw_input("What type of account are you opening today?: Savings or Checking? ")
        
    def checkBalance(self):
        return self.balance

    def deposit(self, ammount):
        self.balance = self.balance + ammount
        print "You deposited: " + str(ammount)
        return self.balance

    def withdraw(self, ammount):
        self.balance = self.balance - ammount
        print "You withdrew: " + str(ammount)
        return self.balance

    def login(self, username, password):
        if username != self.username:
            print "Username for this account is incorrect."

        if password != self.password:
            print "Password for this account is incorrect."
        
        if username == self.username and password == self.password:
            print "Login successful."



korn = BankAccount(100, "bigchiefmaiz", 1234)
