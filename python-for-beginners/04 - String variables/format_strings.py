# Ask the user for their first and last name
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# the capitalize function will return the string with 
# the first letter uppercase and the rest of the word lowercase
print ('Hello ' + first_name.capitalize() + ' ' \
       + last_name.capitalize())

# Ways to format string:
# output = 'Hello, {} {}'.format(first_name,last_name)
# output = 'Hello, {0} {1}'.format(first_name,last_name)
# output = 'Hello {1}, {0}'.format(first_name,last_name)
output = f'Hello, {first_name} {last_name}'
print(output)