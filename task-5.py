# Q-1
input_values=[23,44,35,70,14,22,90,78,21,42,7]
print input_values
def check_divisibility(input_values):
	def result(input_values):
		for i in input_values:
 			if (i%3 != 0) and (i%7 == 0):
 				return i
 	return result
res = check_divisibility(input_values)
print res

#''''''working - normal code
input_values=[23,44,35,70,14,22,90,78,21,42,7]
for i in input_values:
	if (i%3 != 0) and (i%7 == 0):
		print i




input_values=[23,44,35,70,14,22,90,78,21,42,7]
print '\nList of inputted values are: ', input_values

res=filter(lambda x:(x%3!=0) and (x%7==0), input_values)
print '\nValues that are not divisible by 3 and is multiple of 7 are: ', res



# Q-2
#'''''WORKING CODE (Map function in traditional function)
def multiple_element (list1):
	res=map(lambda x:x*x,list1)
	print 'Output is: ', res

input_values=[9,8,7,6,5,4,3,2]
print '\nInput is: ', input_values
multiple_element(input_values)


def multiple_element(i):
	return i*i

input_values=[9,8,7,6,5,4,3,2]
print '\nInput is: ', input_values
res=map(multiple_element, input_values)
print 'Output is: ', res


# ###### from internet with decorator
def a(x):
	def b(y):
		print ' this is b'
		print y
		return x+y
	print x
	print 'this is a'
	return b

add_15=a(15)
print add_15(10)

# Q-3
input_val=['d','P','S','q','t','Z']
upper_val=[x for x in input_val if x.isupper()]
print upper_val

# Q-4
student_name=['Tom','Leslie','Ron','Ben','Chris']
student_subject=['Entrepreneur','Politics','Woodworking','Accounting','Health']

output={ k:v for (k,v) in zip(student_name,student_subject)}
print 'Output is: ', output

# Q-5
# Yield: The yield statement suspends function's execution and sends a value back to the caller, but retains enough state to enable fucntion to resume where it is left off.

# Next: the next() function returns the next item from the iterator.

# Generators: Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

# Q-6
def reverse_string(mystring):	
	for i in range(len(mystring)-1,-1,-1):
		yield mystring[i]

input_string='Consultadd Training'
for ch in reverse_string(input_string):
	print ch

# Q-7
def plus_one(number):
    return number + 1
add_one = plus_one
print add_one(7)
