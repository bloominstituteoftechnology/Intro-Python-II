num1 = float(input('Enter First Number: '))
operator = input('Enter operator: ')
num2 = float(input('Enter Second  Number: '))


if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / mum2)
elif operator == '%':
    print(num1 % num2)
elif operator == '^':
    print(num1 ** num2)
else: 
    print("Invalid Operator")
