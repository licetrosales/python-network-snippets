# Import the math module
import math
r = float(input("Enter the radius of the circle: \n"))
area = (math.pi*r*r)
print ( "Radius", r, sep = ": ", end = "cm.\n")
print ( "Area", area, sep = ": ", end = "sq.cm.\n")

# Import modules
import sys
for path in sys.path:
    print(path)         #This will show you all the directories Python is using to search for modules.
