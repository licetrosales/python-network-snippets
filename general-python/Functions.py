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

# Optional or defaulted arguments
def greeting(name, timeofday = "morning"):
    """This function generates a user greeting including the user name.
    Time of the day can be entered by the user."""
    print("Good " + timeofday, name + "!")
    return

greeting(name = "Laura", timeofday = "afternoon")
greeting(name = "Mauro")

# Keyword arguments
def user_details(age, size, location):
    """This function shows how keyword aruments can be used."""
    print ("User is", age, "year old,", "size", size, "and lives in", location)
    return

user_details(location = "Peru", age = 10, size = 32)
user_details( age = 21, location = "Colonia", size = 203)
