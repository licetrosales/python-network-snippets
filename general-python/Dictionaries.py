# Creating a dictionary
myDict = {"ID": 22, "name":"Juan Lozano", "score": 70, "Grade": "C"}

dict1 = dict([(1,"cats"), (2,"radios"), (3, "flowers")])
class_ranking = dict({1:"Person 1", 2:"Person 2", 3:"Person 3"})
print (myDict)
print (dict1)
print (class_ranking)

# Accessing elements
print (myDict["name"])
print (myDict["score"])
print (myDict.get("score"))
print (myDict.get("scoretest"))

# Updating the dictionary
print ("Old myDict: ", myDict)
myDict["Grade"] = "B"
del myDict["ID"]
myDict["name"] = "Luz Paz"
print ("New myDict: ", myDict)

# Erase all elements in a dictionary
print ("Original values of dict1: ", dict1)
dict.clear(dict1)
print ("Clearing all the dictionary entries oof dict1: ", dict1)
