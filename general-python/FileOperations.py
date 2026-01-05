# Open and read the entire contents of 'days.txt' file
my_text = open("/Coding/Projects py/days.txt")
print(my_text.read())

# Read the content of a file using the method readline()
print(my_text.readline())

# Use method readlines(): output-> list of lines in the file, each item represents one line  
print(my_text.readlines())
my_text.close()

# Write to a file
my_text1 = open ("/Users/licetullmann/Library/CloudStorage/OneDrive-Personal/Coding/Projects py/seasons.txt", "w")
