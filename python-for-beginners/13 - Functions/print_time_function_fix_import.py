# Import datetime class from datetime library to simplify calls to datetime.now()
from datetime import datetime

# Create a function called print_time
# This function will print the message and current time
# Pros:
#  - make code more readable and easier to maintain
#  - reduce rework and limit the chance of bugs
#  - code encapsulation
def print_time():
    print('task completed')
    print(datetime.now())
    print()

first_name = 'Susan'
# Call print_time() function to display message and current time
print_time()

for x in range(0,10):
    print(x)
# Call print_time() function to display message and current time
print_time()