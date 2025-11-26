# if statement
number = int(input("Enter a nummber to check if it is even: "))
if number % 2 == 0:
    print (number, "is an even number.")

# if - else statement
number2 = int(input("Enter a nummber to check if it is even: "))
if number2 % 2 ==0:
    print (number2, "is an even number.")
else:
     print (number2, "is an odd number.")

# if - elif - else statement
age = int(input("How old are you?")) 
if age < 0:
    print ("Age cannot be less than 0.")
elif age < 12:
    print ("You are a child")
elif age < 18:
    print ("You are not an adult")
elif age < 60:
    print ("You are an adult")
elif age < 100:
    print ("You are an senior citizen")
else:
    print ("You have entered an invalid age.")
