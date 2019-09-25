# Example for files to work
def main():
    # Open a file for writing and create it if it does not exist.
    #f = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    #f = open("textfile.txt", "a")
    
    # Write some lines of data to the file
    #for i in range(10):
        #f.write("This is line "+ str(i)+"\r\n")

    #Close the file when it's done
    #f.close()

    # Open the file and read the whole file
    #f = open("textfile.txt", "r")
    #if f.mode == 'r':
    #   contents = f.read()
    #   print(contents)

    # Open the file and read file line by line
    f = open("textfile.txt", "r")
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)





if __name__ == "__main__":
    main()