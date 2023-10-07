# formatting string
num1 = 10
num2 = 20
print(num1)
# print(f"{num1} + {num2} = {num1+num2}")

# print("rashed uzzaman reshad ", end="")
# print("01787170612")

# control statement
# conditional control statement
# loop control statement

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-2])


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# 2 index shoo abong 5 index ar ag porjonto sa kata nibe
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# insertion of the list

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry","wiki"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry","wiki"]
# thislist[:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry","wiki"]
# thislist[:4] = ["watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
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
# for x in thislist:
#   print(x)


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = ['hello' for x in fruits]

# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# print("1") if 2 > 3 else print("2") if(7!=7) else print ("3") if(8>9) else print("4") if(1) else print("5")

# a= 20
# b= 10

# if condition:
#   pass
# elif condition:
#   pass

# a = (4,5,6,0)
# a.add(5)

a = (4,5,6,0)
(x,y) = a
print(x)
