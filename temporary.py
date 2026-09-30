# You can import modules in Python using the import statement.
# For example, you can import the math module to perform mathematical operations.
import math

#########################################################################################################################

# print() function is used to display output to the console.
print("Hello, world!")

# print() with end parameter:
print("Hello", end="\n")
# The end parameter specifies what to print at the end of the output. By default, it is a newline character.

# print() with sep parameter:
print("Hello", "World", sep=", ")
# The sep parameter specifies the separator between multiple values. In this case, it is a comma followed by a space.

# print() by concatenating strings using + operator
print("We are learning " + "Python")

# print() with format. The curly braces {} are used as placeholders
# !!!print("The numbers are {} and {}", format(10, str(10)), end="\n")

#########################################################################################################################

A = 64
print("The square root of", A, "is", math.sqrt(A))
# The math.sqrt() function calculates the square root of a number.
# In this case, it calculates the square root of 64, which is 8.0.

#########################################################################################################################

# Numeric Data Types in Python:
# 1. int: Represents integer values (whole numbers such as 42).
# 2. float: Represents floating-point numbers (decimal values such as 3.14).
# 3. complex: Represents complex numbers (numbers with a real and imaginary part such as 3+4j).
integer1 = 42
float1 = 3.14
complex1 = 3 + 4j
# You can perform arithmetic operations on these numeric data types.

#########################################################################################################################

# String Data Type:
# Represents a sequence of characters (textual data such as "Hello").
# Strings can be enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
string1 = "Hello"
string2 = "World"
string3 = string1 + string2
string4 = " "
string5 = (string1 + string4) * 3  # Repetition of strings

print(string1 + ", " + string2)  # Concatenation of strings
print(string1 + string4 + string2)  # Output: Hello World
print(string3)  # Output: HelloWorld
print(string5)  # Output: HelloHelloHello

#########################################################################################################################

# type() function is used to determine the data type of a variable or value.
print(type(integer1))  # Output: <class 'int'>
print(type(float1))  # Output: <class 'float'>
print(type(complex1))  # Output: <class 'complex'>

#########################################################################################################################

# input() function is used to take user input from the console.
# The input() function always returns the input as a string.
input1 = input("Enter your name: ")
print("Hello, " + input1 + "!")  # Concatenating the input with a greeting message.

# to convert the input to an integer, you can use the int() function.
input2 = int(input("Enter your age: "))
print(
    "You are " + str(input2) + " years old."
)  # Converting the integer input back to a string for concatenation.

# You can also convert the input to a float using the float() function.
input3 = float(input("Enter your height in meters: "))
print(
    "Your height is " + str(input3) + " meters."
)  # Converting the float input back to a string for concatenation.

#########################################################################################################################

# Arithmatic Operators in Python:
# 1. Addition (+): Adds two numbers together.
# 2. Subtraction (-): Subtracts one number from another.
# 3. Multiplication (*): Multiplies two numbers together.
# 4. Division (/): Divides one number by another and returns a float.
# 5. Floor Division (//): Divides one number by another and returns the largest integer less than or equal to the result.
# 6. Modulus (%): Returns the remainder of a division operation.
# 7. Exponentiation (**): Raises one number to the power of another.

print("Addition:", 10 + 3)  # Output: 13
print("Subtraction:", 10 - 3)  # Output: 7
print("Multiplication:", 10 * 3)  # Output: 30
print("Division:", 10 / 3)  # Output: 3.3333333333333335
print("Floor Division:", 10 // 3)  # Output: 3
print("Modulus:", 10 % 3)  # Output: 1
print("Exponentiation:", 10**3)  # Output: 1000
