# Open and read the entire contents of 'days.txt' file
my_text = open("/Coding/Projects py/days.txt")
print(my_text.read())

# Read the content of a file using the method readline()
print(my_text.readline())

# Use method readlines(): output-> list of lines in the file, each item represents one line  
print(my_text.readlines())
# Use close() method to close the file 
my_text.close()

# Write to a file
my_text1 = open ("/Users/licetullmann/Library/CloudStorage/OneDrive-Personal/Coding/Projects py/seasons.txt", "w")
my_text1.write("Seasons of the year:\n")
my_text1.write("Spring\n")
my_text1.write("Summer\n")
my_text1.write("Autum\n")
my_text1.write("Winter\n")

# Use close() method to close the file to free up the memory and processing resources used 
my_text1.close() 

# Open and write a file with "with"
with open("/Users/licetullmann/Library/CloudStorage/OneDrive-Personal/Coding/Projects py/seasons1.txt", "w") as f:
    f.write("Seasons of the year:\n")
    f.write("Spring\n")
    f.write("Summer\n")
    f.write("Autum\n")
    f.write("Winter\n")

