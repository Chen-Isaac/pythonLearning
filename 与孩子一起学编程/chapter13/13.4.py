def calTotalVal (money):
    money[3] = int(raw_input("quarters:"))
    money[2] = int(raw_input("dimes:"))
    money[1] = int(raw_input("nickels:"))
    money[0] = int(raw_input("pennies:"))
    return 0.25*money[3]+0.1*money[2]+0.05*money[1]+0.01*money[0]

money = [0,0,0,0]
val = calTotalVal(money)
print "total is $",val
