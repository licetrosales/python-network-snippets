# Example of function to determine an even number
def EvenOrOdd(x):
    """This function determines whether a number is even or odd"""
    if (x%2 ==0):
        print(x, "is an even number.")
    else:
        print(x, "is an odd number.")
    return
  
# Calling the function
EvenOrOdd(8)
EvenOrOdd(11)

# Calling the faunction with eval
x = eval(input("Enter a number: "))
EvenOrOdd(x)

# Positional argument
def user_datails(age, location, name):
    """Example of positional arguments"""
    print("User's name is", name, "is", age, "years old," "lives in", location)

user_datails(21, "Italy", "Pol")
user_datails("Spain", "Luisa", 50)
