

value = [1,1,1,1,2,3,4,5]
print(value[1])

# Insert method is used to insert element into the list with index posission
value.insert(1, "Rajni")
print(value)

# append method is used to add the element at last posission into the list
value.append("shiv")
print(value)

# pop method is used to delete the last element from the list
value.pop()
print(value)

# delete the element from the list which is required posission
del value[1]
print(value)

# update the element which is required posission
value[1] = "Rajni"
print(value)

# ********************* Slicing *******************
#prnt first three element
print(value[0:3])

#print all element from the list
print(value[:])

#print all element except last element
print(value[:-1])

#prnt first element from the list
print(value[:1])

#print all element from the first posisson
print(value[1:])

#**************************************************************


#print repeated element count which is required
p=(value.count(1))
print(p)
p=(value.count(3))
print(p)
p=(value.count("Rajni"))
print(p)

# Sort method is used to sort the elements in the list
value1 = [1,4,5,3,2,8,9,5,0,3,7,1]
value1.sort()
print(value1)

# reverse method is used to reverse the elements in the list
value1.reverse()
print(value1)

# sort method is used to sort the string
str = ["a","z","t","b","u"]
str.sort()
print(str)

# reverse method used to reverse the string
str.reverse()
print(str)

# reverse a string using for loop
str1 = "Rajanikant"
rstr = ""
for i in str1:
    rstr = i + rstr
print(rstr)



