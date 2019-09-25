#
# Example file for variables
#

# Declare a variable and initialize it

f=0
#print(f)

# Redeclare the variable works

#f="abc"
#print(f)

# Error variables of different types can not be  combined

#print("This is a string " + str(123))


# Global versus local variables in function

def someFunction():
 f="def"
 print(f)

someFunction()
print(f)

