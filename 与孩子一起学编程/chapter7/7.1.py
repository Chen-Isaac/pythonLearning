import easygui

x = float(easygui.enterbox("Enter a price:"))

if x <= 10:
    easygui.msgbox("The discount is 10%. The final price is "+ str(x*0.9))
else:
    easygui.msgbox("The discount is 20%. The final price is "+ str(x*0.8))
