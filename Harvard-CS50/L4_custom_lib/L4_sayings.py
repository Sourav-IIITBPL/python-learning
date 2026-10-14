def main():
    hello("hi user")
    goodbye("see you soon user")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__": 
     # this is a special variable that is set to "__main__" when the script is run directly . 
     # it is used to check if the script is being run directly or being imported as a module .
     #  if the script is being run directly , the code inside the if block will be executed .
     #  if the script is being imported as a module , the code inside the if block will not be executed .
    main()