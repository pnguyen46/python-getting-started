from datetime import datetime,timedelta
# print today's date
current_date = datetime.now()
print('Today date: ' + str(current_date))

# print yesterday's date
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday date: ' + str(yesterday))

# ask a user to enter a date
user_input = input('Please enter a date (dd/mm/yyyy):')
user_date = datetime.strptime(user_input,'%d/%m/%Y')

# print the date one week from the date entered
one_week = timedelta(weeks=1)
earlier_date = current_date - one_week
print('One week from the entered date: ' + str(earlier_date))


