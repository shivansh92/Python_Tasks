# Q-1
try:
	print eval('Hello World')
except SyntaxError:
	print 'This is a Syntax Error.'
except SyntaxError,err:
	print 'Syntax Error %s (%s-%s): %s'%(err.filename,err.lineno,err.offset,err.text)
	print err

# Q-2
from sys import argv
input_filename=argv[1]

while True:
	try:
		text_object = open(input_filename,"r")
		print text_object.read()
		text_object.close()
		break
	except:
	 	print '\nYou entered incorrect filename.'
	 	input_filename=raw_input('\nEnter the filename again: ')

# Q-3
while True:
	try:
		num1=input('Enter a four digit number:')
		if (num1>999) and (num1<10000):
			print 'You entered correct number!'
		else:
			raise ValueError 
		break
	except ValueError:
		print 'Length is too short/long!!! Please provide only four digits.'

# Q-4
real_pwd = 'password'
real_username = 'dummyTest@gmail.com'

count=1
while count<4:
	username = raw_input('Enter username: ')
	pwd = raw_input('Enter password: ')
	if (username == real_username) and (pwd == real_pwd):
		print 'You entered correct credentials.'
		break
	else:
		print 'You entered incorrect credentials. Please enter again.'
		count+=1

# Q-5
text_object = open('/Users/shivanshmehta/Desktop/pythonTasks/Python_Tasks/read/read.txt','r')
lines = text_object.readlines()

for line in lines:
	temp=line.split()
	if len(temp)%2 ==0:
		print line
	else:
		continue
