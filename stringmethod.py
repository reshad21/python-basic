# ==============return value from calling function============== #
# All string methods return new values. They do not change the original string.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x) 
# Hello, and welcome to my world.

txt = "banana"
x = txt.center(20)
print(x)

# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) #7

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) #7

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "hello world!"
x = txt.islower()
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

# call function
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))