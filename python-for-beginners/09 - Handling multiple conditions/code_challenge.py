# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room C
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

#Best PracticeL:
name = input('What is your name? ')
#slice from index 0 to index 1
first_letter = name[0:1]
if first_letter.upper() in ('A','B'):
    room = 'AB'
elif first_letter.upper() == 'C':
    room = 'C'
else:
    last_name = input('What is your last name? ')
    last_name_first_letter = last_name[0:1]
    
    if last_name_first_letter == 'Z':
        room = 'Z'
    else:
        room = 'OTHER'
print('Please go to room ' + room)

#alternative solution:
name = input('Please enter your first name: ').lower()
if name.startswith('a') or name.startswith('b'):
    destination = 'Go to room AB'
elif name.startswith('c'):
    destination = 'Go to room C'
else:
    last_name = input('Please enter your last name: ').lower()
    if last_name.startswith('z'):
        destination = 'Go to room Z'
    else:
        destination = 'Go to room OTHER'
print(destination)