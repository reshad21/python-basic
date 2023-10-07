# sum = 0
# for x in range(1,11):
#     if x%2==0:
#         print(x)
#         sum = sum + x
# print(sum)

# print("hello world")

# mylist = ["apple","banana","kiwi","orange","mango"]

# for i,x in enumerate(mylist):
#     print(i,x)
#     print(f"{i}-{x}")


digit = ["a","e","i","0","u","c"]
vowel = []
sum = 0

for x in digit:
    if x=="a":
        vowel.append(x)
        sum=sum+1
    elif x=="e":
        vowel.append(x)
        sum=sum+1
    elif x=="i":
        vowel.append(x)
        sum=sum+1
    elif x=="0":
        vowel.append(x)
        sum=sum+1
    elif x=="u":
        vowel.append(x)
        sum=sum+1

print(vowel)
print(sum)


input_string = input("Enter a string: ")
vowel_count = 0
consonant_count = 0
input_string = input_string.lower()

vowels = "aeiou"

for char in input_string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)