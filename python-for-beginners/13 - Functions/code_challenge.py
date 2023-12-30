# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received
# 
# 
# alternative solution
# def calculator(first_number,second_number,operator):
#     if operator == '+':
#         return first_number + second_number
#     elif operator == '-':
#         return max(first_number,second_number) - min(first_number,second_number)
#     else:
#         return 'Invalid operator received'
def calculator(first_number,second_number,operation):
    if(operation.upper() == 'ADD'):
        return (float(first_number) + float(second_number))
    elif operation.upper() == 'SUBTRACT':
        return (float(first_number) - float(second_number))
    else:
        return ('Invalid operation please specify ADD or SUBTRACT')

print('Adding 6 + 4 = ' + str(calculator(6,4,'add')))

print('Subtracting 6 - 4 = ' + str(calculator(6,4,'subtract')))

print('Dividing 6 / 4 = ' + str(calculator(6,4,'divide')))