province = input("What province do you live in? ")
tax = 0

#'or' combined multiple condition into a single condition
#use '\' for new line 
if province == 'Alberta' \
   or province == 'Nunavut':
	tax = 0.05
elif province == 'Ontario':
	tax = 0.13
else:
	tax = 0.15
print(tax)
