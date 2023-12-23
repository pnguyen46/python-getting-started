# Ask a user to enter a number
first_number = input("Please enter a number: ")

# Ask a user to enter a second number
second_number = input("Please enter another number: ")

# Calculate the total of the two numbers added together
total = int(first_number) + int(second_number)
# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
output = f'{first_number} + {second_number} = {total}'
print(output)