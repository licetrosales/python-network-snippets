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

# Arbitrary number of arguments
def user_info(name, size, *notes):
    """Assigning an arbitrary number of arguments to a function by placing an "*" in front of the argument"""
    print ("User name:", name, "Size:", size, "Notes:", notes)

user_info("Oscar", 32, "Lastname: Alvares")
user_info("Ana", 20, "email: ana@aol.com","Lastname: Perales")
user_info("Rob", 12)

# Arbitrary number of keyword
def products(prod_name, price, **kwargs):
    """Assingning an arbitrary number of keyword arguments to a function"""
    print ("Product name:", prod_name, "Price:", price)
    print ("Description:", kwargs)

products("Book", "$11", color = "Red", manufacturer = "Hunter Co.")
products("TV", "$101", color = "Black", maker = "LG", tpye = "IPS")
products("Toys", "$55", color = "yellow", origin = "China", serie = "X23", year = 2025)
