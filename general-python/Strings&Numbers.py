# Strings and numbers

# Slicing: slice the characters in a string using a square bracket ([]) and/or specify a range of characters using colons ([:]).
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

# String escape sequence
print("I am sorry,\" he said, \"the 'Transformers' toys are out of stock\"." )
print('"I am sorry, " he said, "the \'Transformers\' toys are out of stock".')
print(""""I am sorry," he said, "the 'Transformers' toys are out of stock". """)

# String methods
mytext = "Happy new year World!"

print ("mytext.upper() = ", mytext.upper())
print ("mytext.lower() = ", mytext.lower())
print ("mytext.swapcase() = ", mytext.swapcase())
print ("mytext.capitalize() = ", mytext.capitalize())
print ("mytext.title() = ", mytext.title())
print ("mytext.strip() = ", mytext.strip())
print ("mytext.split() = ", mytext.split())

# String formatting
name ="Piro"
score = 30

print ("My name is %s and I scored %d percent!" %(name, score))

# Number coercion
number1 =12
number2 = 2.5
string1 = "10"

print (float(number1)) # number1 to float 
print (int(number2)) # number2 to integer 
print (int(string1) * number2) 
YoB = int(input("Enter your year of birth as YYYY: ")) 
age = 2025 - YoB
print ("You are %d years old!" %age)
