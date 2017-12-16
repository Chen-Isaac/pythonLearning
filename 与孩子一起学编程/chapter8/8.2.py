
import easygui
x = int(easygui.enterbox("Which multiplication table would you like?"))
print "Here's your table:"
i = 1;
while i <= 10:
    print x," x ",i," = ",x*i
    i += 1
