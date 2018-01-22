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

myAccount = BankAccount("Isaac","6222021202013751855",0)
myAccount.showBalance()
myAccount.deposit(100000)
myAccount.withdraw(10000)
