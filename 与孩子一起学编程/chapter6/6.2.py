import easygui

name = easygui.enterbox("Enter your name:")
room = easygui.enterbox("Enter your address:")
province = easygui.enterbox("Enter your province:")
zipcode = easygui.enterbox("Enter your zipcode:")
easygui.msgbox(name +"\n" +room +"\n"+ province +"\n"+ zipcode+"\n")
