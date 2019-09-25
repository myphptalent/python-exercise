# Demostrate the use of variable argument lists

#TODO: define a function that takes varaible arguments

def addition(*args):
    result = 0
    for arg in args:
        result+=arg
    return result    


def main():
    #TODO: pass different arguments
    print(addition(1,2,3,4,5))
    print(addition(2,4,6,8))


if __name__ =="__main__":
    main()