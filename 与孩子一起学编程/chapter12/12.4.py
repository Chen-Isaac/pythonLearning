nameList = []
print "Enter 5 names:"
for i in range(5):
    nameList.append(raw_input())
print "The names are ",nameList
repIndex = int(raw_input("Replace one name. Which one?(1-5):")) - 1
newName = raw_input("New name:")
del nameList[repIndex]
nameList.insert(repIndex,newName)
print "The names are ",nameList
