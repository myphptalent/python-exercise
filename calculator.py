
# Online Python - IDE, Editor, Compiler, Interpreter

def cal() :
    while True:
        try:
            cmd = input("Enter your mathematical expression (2+2,3-1,3*2,4/2 etc)?: ")
            res = eval(cmd)
            print(f"Your answer is: {res}")
            confirm = input("Do you want to continue? Yes/No:")
            if confirm != 'Yes':
                break
        except Exception as e:
            print(f"Error: {e}")
            print("Please enter correct expression.")

cal()
