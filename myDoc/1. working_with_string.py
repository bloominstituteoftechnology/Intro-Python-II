# Working With String
print("Vincent Adeniji")  # Horizontal
print("Vincent\Adeniji")  # Back Slash
print("Vincent\nAdeniji") # New Line / Vertical
print("Vincent\'Adeniji") #
print("Vincent\"Adeniji") #

# String Variable
name = "Vincent Adeniji"
print(name)

# Concatination
name = "Vincent Adeniji \n"
school = "Lambda School"
print(name + school)

# Function - a block of code that would perform a specific operation - modify, get info 
school = 'Lambda Academy'
upperSchool = 'LAMBDA'
lowerSchool = 'lambda'

print(school.upper(), '22')   # Make the string UpperCase
print(school.upper().isupper(), '23')  # Make the string UpperCase, is the String UpperCase? output: True
print(school.lower(), '24')
print(school.lower().islower(), '25')
print(school.isupper(), '26')
print(school.islower(), '27')
print(upperSchool.isupper(), '28')
print(lowerSchool.islower(), '29')

print(len(school), 'length') # Length of the string
print(school[0]) # print the first letter
print(school.index('Lambda')) # Shows the index of the string. Note: only output the index of the first letter in the variable
print(school.replace('Academy', 'School')) # Replace
