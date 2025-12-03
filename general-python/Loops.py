# For- Loop
for x in range (0,6):
    print ("Iteration x =", x)

# While - Loop
iterations = 0
x = 1
xmax = eval(input("Enter the maximum integer for the number of iterations: "))
while x <= xmax:
    iterations += 1
    print (iterations)
    x +=1

print("the number of iterations is", iterations)

# Example while - loop 
my_text =  input("Enter a word to iterate: ")
iterations = int(input("Enter the number of times to iterate: "))
x = 1

while x <= iterations:
    print ( my_text, "x", x)
    x += 1

# Nested loops: determine prime numbers under 100
x = 2
while x < 100:
    y = 2
    while y * y <= x:
        if x % y == 0:
            break
        y += 1
    else:  # else clause on the while: runs if no break
        print(x, "is a prime number.")
    x += 1

print("Maximum number 100 reached.")

# Using loop control statements break
for letter in "Domingo":
    print ("Current letter:", letter)
    if letter == "n":
        break
print ("found letter:", letter)
