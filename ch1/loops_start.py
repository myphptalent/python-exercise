#
# Example file for working with loops
#

def main():
    x=0

    # Define a while loop

    #while (x<5):
    #    print(x)
    #    x=x+1

    # Define a for loop
    # for x in range(5,10):
    #     print(x)

    # Use a for loop over the collection
    # days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    # for d in days:
    #     print(d)

    # use the break and continue statement
    # for x in range(5,10):
    #     #if(x==7): break
    #     if (x%2==0) : continue
    #     print(x)

    # using the enumerate() function to get index
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
     print(i, d)







if __name__ == "__main__":
  main()