#Use iterator functions like enumerate, zip, inter, next

def main():
    #Define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysfr = ["Dim", "Lun", "Mar", "Mer", "Jeu","Ven", "Sam"]

    #TODO: Use iter to create an iterator over a collection
    #i = iter(days)
    #print(next(i))  # Sun
    #print(next(i))  # Mon
    #print(next(i))  # Tue

    #TODO: iterate using a function and sentinel
    #with open("textfile.txt", "r") as fp:
    #    for line in iter(fp.readline, ''):
    #        print(line)

    #TODO: use regular iteration on the days
    #for d in days:
    #    print(d)      

    #for d in range(len(days)):
    #    print(d, days[d])

    #TODO: using enumerate reduces code and provide a counter
    #for i,d in enumerate(days, start=1):
    #    print(i, d)

    #TODO: Use zip to combine sequences
    for m in zip(days, daysfr):
        print(m)





if __name__ == "__main__":
    main()