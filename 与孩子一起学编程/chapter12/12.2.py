print "Enter 5 names:"
names = []
for i in range(5):
    names.insert(i, raw_input())
print "The names are ",names
namesSorted = names[:]
namesSorted.sort()
print "The sorted names are ",namesSorted
    
