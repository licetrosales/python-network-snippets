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
