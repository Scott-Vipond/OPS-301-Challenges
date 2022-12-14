age = 20
price = 19.95
first_name = "Scott"
is_online = False

print ("Hellow World")
print(age)

patient_name = "John Smith"
age = 20
new_patient = True

name = input("What is your name? ")
print("Hello " + name)


birth_year = input("Enter your birth year: ")
int(birth_year)
age = 2022 - int(birth_year)
print(age)


int() #convert to integer
float() #convert to decimal
bool() #convert to boolean
str() #convert to string


print("Please enter two number to add")
first_number = input ("First: ") # can use float(input("First :")) rather than calling float below!
second_number = input ("Second: ") # can use float(input("First :")) rather than calling float below!
sum = float(first_number) + float(second_number) # can use int(), but will produce error if decimal is entered
# if using float(input("First: ")) above, the sum line would read - sum = fisrt_number + second_number
print("Sum: " + str(sum)) # str(sum) converts the float numbers to a string to concate with "Sum: "


course = 'Python for Beginners'
# Index   012345 using to illustrate where characters are in the index
print(course)
print(course.upper())
print(course.lower())
print(course.find('y')) # this will find the first index of the character, output is 1 as the Index of the char
print(course.replace('for', '4')) # will replease for with 4 in output
print('Python' in course) # will return boolean value of search


print(10 / 3) # decimal
print(10 // 3) # integer
print(10 % 3) # will show remainder
print(10 ** 3) # to the power of...


x = 10
x = x + 3 # will return 13
x += 3 # will return 13, same as above line, augmented assignment operator
x -= 3 # will return 7
x *= 3 # will return 30

x = 3>2
print(x) #o out put is True, boolean
> # greater than
>= # greather than or equal to
< # less than
<= # less than or equal to
== # equal to 
!= # not equal to


price = 25
print(price > 10 and price < 30) # output is true because both are true

price = 5
print(price > 10 or prince < 30) # output is true becuae one is true because using or
print(not price > 10) # using not will return True rather than False


temperature = 35
if temparature > 30:
    print("It's a hot day")
    print("Drinke plenty of water") # indentation represents a block of code rather than {} in other languagues
elif temparture > 20: # tempurature between 20 and 30
    print("It's a nice day")
elif temparature > 10: # temparature between 10 and 20
    print("It's a bit cold")
else: # tempurature below 10
    print("It's cold!")
print("Done")


Weight
(K)g or (L)bs:
Weight in Kg: xxx
print("What is your weight? ")
weight = float(input("Weight"))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K": # ensures even if lower case is used string can be read correctly
    converted = weight / 0.45
    print("Weight in :Lbs:" + str(converted)) # need str to change float variable converted to string
else: 
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted)) # need str to change float variable converted to string
print("Done")


i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 1
while i <= 5:
    print(i * "*") # will print an * for each iteration on a different line * ** *** **** *****
    i = i + 1


names = ["John", "Bob", "Sam", "Mary", "Scott"] # [] denotes a list
print(names(0)) # prints the index of lists, will display John
print(names(-1)) # prints last item of list
print (names[0:3]) # prints first three names


numbers = [1, 2, 3, 4, 5]
numbers.append(6) # adds 6 to the end of the list
numbers.insert(0, -1) # adds -1 to the beginning of the list
numbers.remove(3) # removes 3 from the list
numbers.clear() # clears the list
print(1 in numbers) # will return boolean based on information, for this it would be True
print(len(numbers)) # returns the number of elements in the list, for this 5


numbers = [1, 2, 3, 4, 5]
print(numbers) # out put would be [1, 2, 3, 4, 5]

for item in numbers: # for loop
    print(item) # returns each item in the list on separate lines

i = 0
while i < len(numbers):    # determines the length of numbers
    print(numbers[i])
    i = i + 1 # prints the same as the for loop, each item in the list on separate lines, just longer code


numbers = range(5) # returns a range object, starting at 0 up to but not including final number
print(numbers) # output is range(0,5)

for number in numbers:
    print(number) # output is 0, 1, 2, 3, 4 on separate lines

numbers = range(5, 10) # generates 5, 6, 7, 8, 9 and does not inlcude 10
numbers = range(5, 10, 2) # generates 5, 7, 9 - the last number is the step of the range

for number in range(5):
    print(number) # is the same as the one defining the variable numbers above, just simplier!
                  # there is no need to store anything in the numbers variable

# tuples, like a list, but immutable, cannot change
numbers = [1, 2, 3] # list
numbers = (1, 2, 3) # tuple
