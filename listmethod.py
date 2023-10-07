### =========Only call the function======= ###
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits.clear()
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()


### ==========no return but take argument when function is calling +,- ========= ###
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList.append("jackfruit")
print(thisList)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")


### ============when call return value from function============= ###
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

### =============return value but take argument when call the function============== ###
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")


### =============different way============ ###
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)


