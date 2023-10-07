# for x in range(10):
#     print(x+1)

# sum = 0
# for x in range(10):
#     if x%2==0:
#         print(x)
#         sum = sum + x
# print(sum)

# print("hello world")

# mylist = ["apple","banana","kiwi","orange","mango"]

# for i,x in enumerate(mylist):
#     print(i,x)
#     print(f"{i}-{x}")


# digit = ["a","e","i","0","u","c"]
# vowel = []
# sum = 0

# for x in digit:
#     if x=="a":
#         vowel.append(x)
#         sum=sum+1
#     elif x=="e":
#         vowel.append(x)
#         sum=sum+1
#     elif x=="i":
#         vowel.append(x)
#         sum=sum+1
#     elif x=="0":
#         vowel.append(x)
#         sum=sum+1
#     elif x=="u":
#         vowel.append(x)
#         sum=sum+1

# print(vowel)
# print(sum)


# input_string = input("Enter a string: ")
# vowel_count = 0
# consonant_count = 0
# input_string = input_string.lower()

# vowels = "aeiou"

# for char in input_string:
#     if char.isalpha():
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)


# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# num3 = int(input("enter third number: "))

# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num1 and num2>num3:
#     print(num2)
# else: 
#     print(num3)

# number = [10,90,30,60,50]
# max = number[0]
# for x in number:
#     if x > max:
#         max = x
# print(max)

# number = [10,90,30,60,5,50]
# min = number[0]

# for x in number:
#     if x<min:
#         min = x
# print(min)

# a = "hello world"

# for x in a:
#     if x != " ":
#         print(x)


# number = []
# for x in range(4):
#     if x>len(number):
#         takenumber = input("Enter number")
#         number.append(takenumber)
#         print(number)


# factorial number calculation

# num=1
# for x in range(1,5):
#     num = num*x
# print(num)


# result = 1
# for i in range(1, 5):  
#     result *= i
# print("The factorial of 4 is:", result)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(4)
# print("The factorial of 4 is:", result)

# person = {
#     "name": "reshad",
#     "age": 65,
#     "skills": ["css", "python", "javascript"],
#     "education": {
#             "HSC": 5,
#             "BSC": 3.57
#         }
# }
# print(len(person))
# print(person["education"]["BSC"])
# print(type(person["education"]["BSC"]))


number = int(input("enter marks: "))
# print(type(number))

if number in range(80,101):
    print(f"your markes is: {number} and you get A+")
elif number in range(70,80):
    print(f"your markes is: {number} and you get A")
elif number in range(60,70):
    print(f"your markes is: {number} and you get A-")
elif number in range(50,60):
    print(f"your markes is: {number} and you get B")
elif number in range(40,50):
    print(f"your markes is: {number} and you get C")
elif number in range(33,40):
    print(f"your markes is: {number} and you get D")
else:
    print(f"your markes is: {number} and you Failed")