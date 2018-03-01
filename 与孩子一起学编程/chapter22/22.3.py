import easygui, pickle

inputList = ["name", "age", "favorite color", "favorite food"]
infoList = []
for item in inputList:
    info = easygui.enterbox(msg = "Enter your " + item, title = "User Info Input")
    infoList.append(info)
pickle_file = open("user_info_list.pkl", "w")
pickle.dump(infoList, pickle_file)
pickle_file.close()

pickle_file = open("user_info_list.pkl", "r")
recovered_list = pickle.load(pickle_file)
pickle_file.close()

print recovered_list
