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

