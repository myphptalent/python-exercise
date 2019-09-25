# Strings and bytes are not interchangable
# Strings contains unicode, bytes are raw 8-bits values

def main():

    string = "Python is interesting."
    # string with encoding 'utf-8'
    arr = bytes(string, 'utf-8')
    print(arr)

    s = "This is a string"
    print(s)


if __name__ == "__main__":
    main()