# Advanced iteration funcitons in the itertools package
import itertools

def testFunction(x):
        return x < 40

def main():
    #TODO: cycle iterator can be used to clycle over a collection
    seq1 = ["Joe", "Jhon", "Mike"]
    cycle1 = itertools.cycle(seq1)
    #print(next(cycle1))
    #print(next(cycle1))
    #print(next(cycle1))
    #print(next(cycle1))

    #TODO: use count to create a simple counter
    count1 = itertools.count(100,10)
    #print(next(count1))
    #print(next(count1))
    #print(next(count1))

    #TODO: use chain to connect sequences together
    x=itertools.chain("ABCD", "12345")
    print(list(x))

    #TODO: dropdown and takewhile will return values untill
    #a certain conditon met that stops them
    vals = [10,20,30,40,50,40,30]
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))




if __name__ =="__main__":
    main()