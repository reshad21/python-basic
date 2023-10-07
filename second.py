# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
# print(x, y, z)
# print(x,y,z)


# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# fruits = ["apple", "banana", "cherry"]
# x, y = fruits
# print(x)
# print(y)
# now you get error



# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

"""
Multiline string
"""

# a = "Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."
# print(a)
# now we get error


# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)


# a = "Hello, World!"
# print(len(a))

"""
string formation
a.upper()
a.lower()
a.len()
a.strip()
a.split()
a.replace("World","Reshad")

"free" in text
"free" not in text
"""

# txt = "The best things in life are free!"
# print("free" in txt)


# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")


# txt = "The best things in life are free!"
# print("expensive" not in txt)

# a = "Hello, World!"
# print(a.upper())

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"


# a = "Hello, World!"
# print(a.replace("World", "Reshad"))


"""
slicing string
"""

# b = "Hello, World!"
# print(b[0:5])
# first 5ta item nibe

# b = "Hello, World!"
# print(b[:5])
# shortcut system to start with 0 item

# b = "Hello, World!"
# print(b[2:])
# first 2 item delete from the string 


# b = "Hello, World!"
# print(b[-5:-2])


"""
Formate string
"""

# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# TypeError: can only concatenate str (not "int") to str

# age = 36
# txt = "My name is John, I am " + str(age)
# print(txt)


# Use the format() method to insert numbers into strings:
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))


# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))


# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# txt = "We are the so-called "Vikings" from the north."
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)


"""
Python list
"""
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.["john","dow","mina", 22, "mina"]
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.("john","dow","mina", 22)
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.{"john","dow","mina", 22}
# Dictionary is a collection which is ordered** and changeable. No duplicate members.{age:22, name:"john"}