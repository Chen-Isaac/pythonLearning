import easygui

tank = float(easygui.enterbox("Enter the size of tank:"))
per = float(easygui.enterbox("Enter the percent full:"))
kmPerLiter = float(easygui.enterbox("Enter km per liter:"))

length = tank * per / 100 * kmPerLiter

easygui.msgbox("You can go another " + str(length) + "km." + "\n" + "The next gas station is 200 km away.")

if length >= 200 + 5:
    easygui.msgbox("You can wait for the next station.")
else:
    easygui.msgbox("Get gas now!")

