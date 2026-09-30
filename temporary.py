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
print("The numbers are {} and {}", format(10), end="\n")

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
