#x= 9
#y= 9.9
#z = "Hello"

#implicit conversion
#x= x*y

#print(type(x)) 
#print(type(y)) 
#print(type(z)) 

#print(x)

#print("The type of x is:", type(x))

# explicit conversion
#x = int(x)  # convert x to integer
#print(type(x))  # <class 'int'>
#y = float(y)  # convert y to float
#print(type(y))  # <class 'float'>

age = input("How old are you? ")
#18age = int (age)  # convert input to integer
print(age, type(int(age))) # print(type(age))  # <class 'int'>
print("You are", age, "years old")  # print the age
