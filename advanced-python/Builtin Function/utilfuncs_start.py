# Demostrate the built-in utility functions

def main():
    # Use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]

    # TODO: any() will return true if any of the sequance values are true
    print(any(list1))

    #TODO: all() will return true if all of the sequance values are true
    print(all(list1))

    #TODO: min(),max() funciton

    print("min:", min(list1) )
    print("max:", max(list1) )

    #TODO: sum funciton

    print("Sum :", sum(list1))




if __name__ == "__main__":
    main()