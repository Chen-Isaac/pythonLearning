import easygui
x= int(easygui.enterbox("Which multiplication table would you like?"))
n= int(easygui.enterbox("How high do you want to go?"))
print "Here's your table:"
for i in range (1,n+1):
    print x," x ",i," = ",x*i
