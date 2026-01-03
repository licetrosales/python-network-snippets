# Open and read the entire contents of 'days.txt' file
my_text = open("/Coding/Projects py/days.txt")
print(my_text.read())

# Read the content of a file using the method readline()
print(my_text.readline())

# Use method readlines(): output-> list of lines in the file, each item represents one line  
print(my_text.readlines())
my_text.close()

