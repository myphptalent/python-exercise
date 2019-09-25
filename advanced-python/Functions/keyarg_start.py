#Demostrate the use of keyword-only arguments

#use keyword-only arguments to help ensure code clarity

def myFunction(arg1, arg2, *, suppressExceptions=False):
    pass

def main():
    #try to call the function without the keywords
    #myFunction(1,2,True)
    #Exception has occurred: TypeError
    #myFunction() takes 2 positional arguments but 3 were given
     
    myFunction(1,2,suppressExceptions=True)


if __name__ =="__main__":
    main()
