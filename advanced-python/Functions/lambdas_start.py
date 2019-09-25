# Use lambda as in-place function

def CelsisusToFahrenhite(temp):
    return (temp*9/5)+32

def FahrenhiteToCelsisus(temp):
    return (temp-32)*5/9

def main():
    
    ctemps = [0,12,34,100]
    ftemps = [32,65,100,212]
    #TODO: use regular functions to convert temps
    print(list(map(CelsisusToFahrenhite,ctemps)))
    print(list(map(FahrenhiteToCelsisus, ftemps)))
    
    #TODO: use lamdas to accomplish the same thing
    print(list(map(lambda t: (t*9/5)+32, ctemps)))
    print(list(map(lambda t: (t-32)*5/9, ftemps)))



    


if __name__ =="__main__":
    main()