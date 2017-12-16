import easygui

fahr = easygui.enterbox("Enter the fahr value your want to convert:")
cel = 5.0/9*(int(fahr)-32)
easygui.msgbox("The corresponding cel is " + str(cel))
