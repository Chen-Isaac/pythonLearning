my_file = open("C:\\Users\\Administrator\\Desktop\\BBC.txt", "r")
first_line = my_file.readline()
second_line = my_file.readline()
print "first line =", first_line
print "second line =", second_line
my_file.seek(0)
print "first line =", my_file.readline()
my_file.close