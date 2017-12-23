class BankAccount:
    def __init__(self):
        self.accountName = ""
        self.accountNum = ""
        self.balance = 0.0

    def showBalance(self):
        print "The balance is",self.balance

    def showDeposit(self,depositMoney):
        self.balance = self.balance + depositMoney
        print "The deposit money is",depositMoney
        print "The balance is",self.balance

    def showWithdraw(self,withdrawMoney):
        if (self.balance >= withdrawMoney):
            self.balance = self.balance - withdrawMoney
            print "The withdraw money is",withdrawMoney
            print "The balance is",self.balance
        else:
            print "The balance is",self.balance,"<",withdrawMoney,
            print "The withdraw operation is not allowed."
