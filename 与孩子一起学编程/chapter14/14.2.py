class BankAccount:
    def __init__(self,accountName,accountNum,balance):
        self.accountName = accountName
        self.accountNum = accountNum
        self.balance = balance

    def showBalance(self):
        print "The balance is",self.balance

    def deposit(self,depositMoney):
        self.balance = self.balance + depositMoney
        print "The deposit money is",depositMoney
        print "The balance is",self.balance

    def withdraw(self,withdrawMoney):
        if (self.balance >= withdrawMoney):
            self.balance = self.balance - withdrawMoney
            print "The withdraw money is",withdrawMoney
            print "The balance is",self.balance
        else:
            print "The balance is",self.balance,"<",withdrawMoney,
            print "The withdraw operation is not allowed."

class InterestAccount(BankAccount):
    def __init__(self, accountName,accountNum,balance,interest):
        BankAccount.__init__(self, accountName,accountNum,balance)
        self.interest = interest
        
    def addInterest(self,year):
        self.balance = self.balance * (1 + self.interest) ** year
        print "The balance is",self.balance,"after",year,"years."
        
        
myAccount = InterestAccount("Isaac","6222021202013751855",0,0.5)
myAccount.owner = "Isaac Chen" #try to add one more property
myAccount.showBalance()
myAccount.deposit(100000)
myAccount.withdraw(10000)
myAccount.addInterest(7)
print "The account's owner is",myAccount.owner
        
        