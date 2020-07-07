# Q-1
num = raw_input("Enter Value:")
if num%3 == 0:
	print "Consultadd"
elif num%5 == 0:
	print "c"
elif num%3 == 0 and num%5 == 0:
	print "Consultadd Python Training"
else:
	pass

# Q-2
print 'Please select option: \n 1. Addition \n 2. Subtraction \n 3. Division \n 4. Multiplication \n 5. Average'
choice = input('Enter your choice number: ')

if (choice == 1):
	num1 = input('Enter 1st number: ')
	num2 = input('Enter 2nd number: ')
	result = num1 + num2
	if (result>0):
		print 'The addition is: ', result
	else: 
		print 'Zsa'
elif (choice == 2):
	num1 = input('Enter 1st number: ')
	num2 = input('Enter 2nd number: ')
	result = num1 - num2
	if (result>0):
		print 'The difference is: ', result
	else: 
		print 'Zsa'
elif (choice == 3):
	num1 = input('Enter 1st number: ')
	num2 = input('Enter 2nd number: ')
	result = num1 / num2
	if (result>0):
		print 'The result is: ', result
	else: 
		print 'Zsa'
elif (choice == 4):
	num1 = input('Enter 1st number: ')
	num2 = input('Enter 2nd number: ')
	result = num1 * num2
	if (result>0):
		print 'The product is: ', result
	else: 
		print 'Zsa'
elif (choice == 5):
	num1 = input('Enter 1st number: ')
	num2 = input('Enter 2nd number: ')
	num3 = input('Enter 3rd number: ')
	num4 = input('Enter 4th number: ')
	result = (num1 + num2 + num3 + num4)/4
	if (result>0):
		print 'The average is: ', result
	else: 
		print 'Zsa'

# Q-3
age = input('Enter age: ')
if(age >= 11):
	print 'You are eligible to see the Football match.'
	if (age <= 20) or (age >= 60):
		print ' Ticket price is $12.'
	else:
		print 'Ticket price is $20.'
else:
	print " You're not eligible to buy a ticket."

# Q-4
while True:
	num = input('Enter Value:')
	if num < 0:
		break
	else:
		print "Good Going"
print "Its Over"

# Q-5
for i in range(2000, 3201):
	if (i%7 == 0) and (i%5 != 0):
		print i
# Q-6

# Part-1
# The given code would result in an error as integer is not iterable

# Part-2
# The given code would will print values 0, 1 and 2. After that due to if condition, the while loop will break. 

# Part-3
# The gien code will print values 0,1,2,3, and 4. After that due to if condition, the while loop will break.

# Q-7 
for i in range(7):
	if ((i == 3) or (i == 6:)):
 		continue
	else:
 		print i

# Q-8
strVal = raw_input("Enter String: ")
letter = 0
digits = 0
for i in strVal:
	if i.isdidgit():
		digits +=1
	else:
		letters+=1
print "Letters ", letters
print "Digits ", digits

# Q-9
# Part-1
luckyNum = 5
while True:
	num = input("Enter Lucky Number: ")
	if num == luckyNum:
		break

# Part-2
luckyNum = 5
while True:
	num = input("Enter Lucky Number: ")
	if num == luckyNum:
		break
	else:
		answer = input("Do you want to guess again? (yes/no) ")
		if answer == "no":
			break

# Q-10
lucky_number = 5
counter=1
while counter<=5:
	print 'Type in the ', counter, 'number'
	number=input()
	if(number == lucky_number):
		print 'Good guess!'
	else:
		print 'Try again!'
	counter+=1
print 'Game over!'

# Q-11
lucky_number = 5
counter=1
while counter<=5:
	print 'Type in the ', counter, 'number'
	number=input()
	if(number == lucky_number):
		print 'Good guess!'
		break
	else:
		print 'Try again!'
	counter+=1
if(counter==6):
	print 'Sorry but that was not very successful!'
