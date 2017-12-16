import easygui

userIn = easygui.enterbox("Enter the password:")

if userIn == "fuck you!":
    easygui.msgbox("You're in!")
else:
    easygui.msgbox("Wrong!")
