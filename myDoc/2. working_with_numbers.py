# Print the actual number
print(2) # Whole Number
print(2.2) # Decimal Number
print(-2)
print(-2.2)

# Arithmetics
print(2 + 2)   # Plus
print(2 + 2.2)

print(2 * 2 )  # Multiplication
print(2 * -2) 

print(2 * 2 + 2) 
print(2 * (2 + 2)) # Parenthesis

print(10 % 3) # Modulos  gives the remainder, 10/3 remains 1

# Store Number inside a Variable 

num = 7
print(num)

# Convert Number to string
# Note you can't use number and string together, so you need to convert the number to string
print(str(num))  #Note, the actual number is now string
print(str(num) + " is the first letter of my name")

# Absolute Value
num = -4, -4.34
print(abs(num[0]), abs(num[1]))

# raise to Power
num = 5
print(pow(num, 2))

# Maximum Number
print(max(num, 2, 4))

# Mininum Number
print(min(num, 2, 4))

# Round Number 
num = 4.1
print(round(num))

# Floor Number. Note: this will remove any .int
# Note: you need to import math to use code below
from math import *

print(floor(num))

# Ceil Number. Round the number as long as there's int above 0
print(ceil(num))

# Square Root of a number
print(sqrt(num))