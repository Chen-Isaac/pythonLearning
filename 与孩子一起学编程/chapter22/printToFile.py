my_file = open("new_file.txt", "w")
print >> my_file, "Hello there, neighbor!"  #if the file is not existed, no content will be written into the file.
my_file.close