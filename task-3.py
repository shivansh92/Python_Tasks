# Q-1
List = [1,2,1.5,'hello','consultadd',2+5j, 3j, 100,'wolrd',25.669]

# Q-2
List = [1,2,3,4,5]
List[1:3]
List[:2]
List[::2]

# Q-3
import math
List = [1,2,3,4,5]
print "Sum is: ", sum(List)
print "Product is: "math.prod(List)

# Q-4
List = [1,2,3,4,5]
print "Maximum is: ", max(List)
print "Minimum is: "min(List)

# Q-5
List = [1,2,3,4,5,6,7,8,9,10]
newList = []
for i in List:
	if i%2 != 0:
		continue
	else:
		newList.append(i)
		List.remove(i)

# Q-6
squareList = []
newList = []
for i in range(1:31):
	squareList.append(i*i)
newList = squareList[:5]
newList.extend(squareList[-5:])

# Q-7
List = [[1,3,5,7,9,10],[2,4,6,8]]
output_list = []
for i in List:
	for j in i:
		output_list.append(j)
print "Output Data: ", output_list

# Q-8
a = {1:10,2:20}
b = {3:30,4:40}
new  = {}
new.update(a)
new.update(b)
print "New Dictionary is: ", new

# Q-9
newDict = {}
n = input("Enter Range: ")
for i in range(1,n+1):
	newDict[i] = i*i

# Q-10
seq = input("Enter CSV values: ").split(',')
print "List is: ", seq
print "Tuple is: ", tuple(seq)


