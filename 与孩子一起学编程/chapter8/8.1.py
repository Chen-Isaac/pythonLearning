import easygui
x=int(easygui.enterbox("Which multiplication table would you like?"))
print "Here's your table:"
for i in range(1,11):
    print str(x) + " x " + str(i) + " = " + str(x*i)
