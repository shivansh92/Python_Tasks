# Q-1
inputString = raw_input("Enter string input: ")
revStr = inputString[::-1]
print "The reversed String is: %s" %revStr

# Q-2
def caseCount(inputString):
	lowerCount = 0
	upperCount = 0
	for i in inputString:

		if i.islower():
			lowerCount += 1
		elif i.isupper():
			upperCount += 1
		else:
			continue
	print "The lowercase count is: %d" %lowerCount
	print "The uppercase count is: %d" %upperCount

inputString = raw_input('Enter input String: ')
caseCount(inputString)

# Q-3
def getUniqueList(inputList):
	return list(set(inputList))

inputList = [1,1,1,1,2,3,3,3,4,4,5,6,7,8,8,8,8]
uniqueList = getUniqueList(inputList)
print "The unique element list is: " uniqueList

# Q-4
print "Enter a hyphen separated sequence of words:"
lst=[n for n in raw_input().split('-')]  
lst.sort()
print "Sorted:"
print '-'.join(lst)

# Q-5
lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break;
for sentence in lines:
	print sentence

# Q-6
def calculateSum (a,b):
	s = int(a) + int(b)
	return s 
num1 = "10"
num2 = "20"
Sum = calculateSum (num1, num2)

print "Sum = ", Sum

# Q-7
def maxLengthStr(str1,str2):
	if len(str1) > len(str2):
		print "Max Length String: " str1
	elif len(str2) > len(str1):
		print "Max Length String: " str2
	else:
		print str1 "\n" str2

str1 = 'abddefghi'
str2 = 'abcdef'
maxLengthStr(str1, str2)

# Q-8
def generateSquareTuple():
	inputTuple = tuple()
	for i in range(1,21):
		inputTuple.append(i**2)

generateSquareTuple()

# Q-9
def showNumbers(limit):

	for i in range(limit + 1):
		if i%2 != 0:
			print i "ODD"
		else:
			print i "EVEN"

limit = int(input('Enter Limit: '))

showNumbers(limit)

# Q-10  
is_even = lambda x: x % 2 == 0
input_list=[]
for i in range(1,21):
	input_list.append(i)
output_list=filter(is_even, input_list)

# Q-11
input_list=[1,2,3,4,5,6,7,8,9,10]
even_numbers=filter(lambda x: x%2 == 0, input_list)

map_list=map(lambda x: x**2,even_numbers)
print map_list

# Q-12
def divide_func(num,den):

	try:
		res=num/den
		print 'Result is: ',res
	except:
		print 'Denominator cannot be zero.'

num1=input('enter numerator:')
num2=input('enter denominator')
divide_func(num1,num2)

# Q-13
import functools

input_list=[[1,2,3],[4,5,6],[7,8]]
print '\nInput list is:',input_list

result=reduce(lambda x,y: x+y, input_list)
print '\nFlattened list is: ',result

# Q-14(i)
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print k
# The output for this code is 2.

# Q-14(ii)
def a():
    try:
        f(x, 4)
    finally:
        print 'after f'
    print 'after f?'
a()
# This code will throw an error.
