# Slicing: you can slice the characters in a string using a square bracket ([]) and even specify a range of characters using colons ([:]).

name = input("Enter a word longer than 5 letters: ")
print (name[0], "is the first indexed character.")
print (name[1], "is the second indexed character.")
print (name[2:4], "is the range of third to fifth carachter.")
print (name[-1], " is the last character.")
print (name[-2], "is the second to last character")

# String concatenation
name = "Peter"
print (name)
name = name[0:4] + " Pan"
print (name)

# String repetition (use the asterisk oprator to create new strings, use "," to add a space or "+" no space)
string1 = "Hello"
string2 = "World"
string3 = "!"
print ("string1 * 3 + string3 = ", string1 * 3 + string3)
print ("string1 + string2 = ", string1 + string2)
print ("string1, string2 = ", string1, string2)
print ("string1, string2 + string3 =", string1, string2 + string3)
