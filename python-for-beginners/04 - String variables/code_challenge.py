# ask a user to enter their first name and store it in a variable
first_name = input("Please enter your first name: ")
# ask a user to enter their last name and store it in a variable
last_name = input("Please enter your last name: ")
# print their full name
# Make sure you have a space between first and last name
print("Hello " + first_name + ' ' + last_name)

# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase
print("Hello " + first_name.capitalize() + ' ' + last_name.capitalize())
