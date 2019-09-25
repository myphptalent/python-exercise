#
# Example file for  working with functions
#

# Define a basic function

def func1():
    print("I am a functon")


# Function that takes arguments

def func2(arg1, arg2):
	print(arg1, "" , arg2)

# Function that return a value

def cube(x):
	return x*x*x

# Function with default value for an argument

def power(num, x=1):
	result = 1
	for i in range(x):
	    result = result * num
	return result

# Function with variable number of arguments
def mult_add(*args):
	result = 0
	for x in args:
		result = result + x
	return result	




#func1()
#print(func1())
#print(func1)

#func2(10, 20)
#print(cube(3))

#print(power(2))
#print(power(2, 3))
#print(power(x=3, num=2))

print(mult_add(2,3,4,5))


