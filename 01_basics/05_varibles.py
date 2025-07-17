# Objects containing variables
# Variables are used to store data values in Python.
# Variables are created when you assign a value to them.
# Variables can be of different types, such as integers, floats, strings, and booleons
# Variables can be reassigned to different values or types.add()

a = 5  # Integer variable
b = 3.14  # Float variable  
c = "Hello, World!"  # String variable
d = True  # Boolean variable    
e = None  # NoneType variable
f = [1, 2, 3]  # List variable
g = (4, 5, 6)  # Tuple variable 
h = {7, 8, 9}  # Set variable
i = {"key": "value"}  # Dictionary variable
j = range(10)  # Range variable
k = bytearray(5)  # Bytearray variable
l = bytes(5)  # Bytes variable
m = memoryview(bytes(5))  # Memoryview variable
n = complex(1, 2)  # Complex number variable
o = frozenset([10, 20, 30])  # Frozenset variable
p = None  # Placeholder variable
q = NotImplemented  # NotImplemented variable

# types of variables
print("Integer variable:", a)


print("Float variable:", b)
print("String variable:", c)    
print("Boolean variable:", d)
print("NoneType variable:", e)  
print("List variable:", f)
print("Tuple variable:", g)
print("Set variable:", h)
print("Dictionary variable:", i)


type_of_h = type(h)
print("Set variable:", h, "of type", type_of_h)

type(a)  # Returns the type of variable a
print(type(a))  # Output: <class 'int'>     
print("Dictionary variable:", i)
print("Range variable:", j)

#rules to assign variables
# 1. Variable names must start with a letter or an underscore (_).
# 2. Variable names can contain letters, numbers, and underscores.
# 3. Variable names cannot start with a number. 
# 4. Variable names are case-sensitive (e.g., myVar and myvar are different variables).
# 5. Variable names cannot be a reserved keyword in Python (e.g., if, else, while, for, etc.).
# 6. Variable names should be descriptive and meaningful to improve code readability.
# 7. Variable names should not contain spaces.
# 8. Variable names should not use special characters (e.g., @, #, $, %, etc.).
# 9. Variable names should not be too long or too short.
# 10. Variable names should not be too similar to avoid confusion.
# 11. Variable names should not be too generic (e.g., var, data, etc.).
# 12. Variable names should not be too specific to avoid limiting their use.


fruits_baskest= ("apple")
print(fruits_baskest)

#furits_baskest = 5
#print("Number of fruits in the basket:", furits_baskest)
#print(type(furits_baskest))  # Output: <class 'int'>
#print("Type of fruits_baskest:", type(fruits_baskest))  # Output: <class 'tuple'>