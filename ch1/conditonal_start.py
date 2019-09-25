#
# Example file for  working with conditonal statements
#

def main():
 a, b = 1000, 1000

 # Conditional flow uses with if,elif, else

 if ( a < b ) :
   st = "a is less than b"
 elif (a==b):
	 st = "a is equal to b"
 else:
   st = "a is greater than b"
 print(st)


 # Conditional statement c is equal to a
 
 st = "a is less than b" if (a<b) else "b is greaten than a or equal to a"
 
 print(st)




 
if __name__ == "__main__":
  main()
