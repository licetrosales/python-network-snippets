# List and tuples
list1 = ["January", "Four", 2025, 11.56, "Heaven"]
tuple1 = ("a", "Sydney", "1900", 3.1416, 0.01, "Pathon")
tuple2 = "x", "empire", "lego", 1, 2.0, 7
print (list1)
print (tuple1)
print (tuple2)

# Accessing values in lists and tuples
print (list1[0:2])
print (list1 [2:])
print (tuple1[1:5])
print (tuple2[0:-1])

# Updating list objects
list1 = ["March", "Five", 2015, 20.20, "Heaven"]
print ("Old list1: ", list1)
list1[0] = "November"
list1[-1] = "Hell"
list1.append("Computer")
print ("New list1: ",list1)

# Deleting list objects
print ("Old list1: ", list1)
del list1[2]
list1.remove("Five")
print ("New list1: ",list1)
