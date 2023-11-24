# Sample project with solution
# Create a simple calculator in Python that can perform addition, subtraction, multiplication, and Division in Python.
# Solution:
# Print message for user to select the relevant operator for specific calculation
operator = input('''
Please type in the operator for calculation:
+ For Addition
- For Subtraction
* For Multiplication
/ For Division
''')

# Prompt the use to enter two numbers as input for calculation
operand_1 = int(input('Enter the first number: '))
operand_2 = int(input('Enter the second number: '))

# Specify conditional statements for calculator
# The first condition checks whether the user has entered '+' operator for addition
# If '+' operator is selected then add the two operands and display result
if operator == '+':
    print('{} + {} = '.format(operand_1, operand_2))
    print(operand_1 + operand_2)

# The second condition is specified using elif i.e. else if conditional statement.
# It checks whether the user has entered '-' operator for Subtraction
# If '-' operator is selected then subtract the two operands and display result
elif operator == '-':
    print('{} - {} = '.format(operand_1, operand_2))
    print(operand_1 - operand_2)

# The Third condition is specified using elif i.e. else if conditional statement.
# It checks whether the user has entered '*' operator for Multiplication
# If '*' operator is selected then multiply the two operands and display result
elif operator == '*':
    print('{} * {} = '.format(operand_1, operand_2))
    print(operand_1 * operand_2)

# The Fourth condition is again specified using elif i.e. else if conditional statement.
# It checks whether the user has entered '/' operator for Division
# If '/' operator is selected then divide the two operands and display result
elif operator == '/':
    print('{} / {} = '.format(operand_1, operand_2))
    print(operand_1 / operand_2)

# The last condition is specified using else conditional statement.
# This statement will be implemented when none of the above condition applies.
# Specifically, when user enters any other key from keyboard except '+', '-', '*' and '/'.
else:
    print('You have not typed a valid operator, please run the program again.')
