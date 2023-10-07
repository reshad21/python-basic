x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
# print(type(x))
# print(type(y))


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
# print(MYVAR);
myvar2 = "John"


#my-var = "john" #this is illegal way to declare a variable



# Camel Case
# myVariableName = "John"

# Pascal Case
# MyVariableName = "John"

# Snake Case
# my_variable_name = "John"


# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)



# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)


# x = "Python "
# y = "is "
# z = "awesome"
# print(x,y,z)

# x = 5
# y = "John"
# print(x+ y) TypeError: unsupported operand type(s) for +: 'int' and 'str'


# x = "awesome"

# def myfunc():
# #   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python  " + x)


# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)


# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)



# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# complex number #Note: You cannot convert complex numbers into another number type.
# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))






# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# b = "Hello, World!"
# print(b[2:5])

# a= "bangladesh";

# print(a[:3]) 


# b = "Hello, World!" #calculate 543
# print(b[-5:-2])


# import random
# print(random.randrange(1, 10))

# Python has a set of built-in methods that you can use on strings.

# a = "   Hello, World "
# print(a.upper())
# print(a.split())
# print(a.strip())
# print(a.replace("o","e"))



# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# List items are ordered, changeable, and allow duplicate values.

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# # It is also possible to use the list() constructor when creating a new list.
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# if "apple" in thislist:
#   print("yes")


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist.insert(1,"new fruit")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]

# for i in thislist:
#     print(i)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# [print(x) for x in thislist]

# thislist = ["apple", "banana", "cherry", "kiwi", "mango"]

# newList = []

# for i in thislist:
#     if "a" in i:
#       newList.append(i)

# print(newList)

# thislist = [10,20,30,1]
# newList =[]

# for i in thislist:
#     if i>1:
#         newList.append(i)

# print(newList)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newList = [x for x in fruits if "a" in x]

# newList = [x for x in fruits if x!="apple"]

# a = [x for x in range(10)]
# b = [x for x in range(10) if x<5]
# print(a)
# print(b)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# c = ['hello' for x in fruits]

# print(c);

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# c=[]

# for x in fruits:
#     if x == "banana":
#       c.append("orange")
#     else:
#        c.append(x)
# print(c)



# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# c = ["orange" if x == "banana" else x for x in fruits]
# print(c)


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# newTuple = list(thistuple)

# for x in newTuple:
#     if x == "apple":
#       newTuple.remove("apple")
#       newTuple.insert(0, "newfruits")
#     else:
#        newTuple

# thistuple = tuple(newTuple)
# print(thistuple)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, *yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# def my_func():
#     print("hello bangladesh")

# my_func()


# def sum(a,b):
#     return a+b

# print(sum(3,2))

# def result(*item):
#     return item[0] + item[1] + item[2] + item[3]

# print(result(20,10,20,50))

# def my_function(arr):
#     for x in arr:
#         print(x)

# my_function(["apple","banana","orange","mango","wiki"])


# lambda arguments : expression

# result = (lambda a,b: a+b)(4,5)
# print(result)


import datetime

# x = datetime.datetime.now()
# print(x)

x = datetime.datetime.now()
print(x.strftime("%X"))

num = [1,2,3,4,5,6]
result = list(filter(lambda x: x%2 ==0, num))
print(result)