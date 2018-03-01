import easygui

userInfo = open("userInfo.txt", "w")
inputList = ["name", "age", "favorite color", "favorite food"]
for item in inputList:
    info = easygui.enterbox(msg = "Enter your " + item, title = "User Info Input")
    userInfo.write(info + "\n")
userInfo.close()


