import easygui

sex = easygui.enterbox("Enter your gender:")
if sex == "male":
    easygui.msgbox("You can't join the club.")
else:
    age = int(easygui.enterbox("Enter your age:"))
    if 10 <= age <= 12:
        easygui.msgbox("Welcome to our soccer club.")
    else:
        easygui.msgbox("Your age doesn't meet our requirement.")
