
# basic caluclator..

def main():
    name = input("enter your name ")
    print(user_name(name))
    
    num1 = int(input("enter a number "))
    num2 = int(input("enter another number "))

    print(f"square of {num1} is {square(num1)}")
    print(f"square of {num2} is {square(num2)}")
    print(f"sum of {num1} and {num2} is {add(num1,num2)}")
    print(f"difference of {num1} and {num2} is {subtract(num1,num2)}")
    print(f"product of {num1} and {num2} is {multiply(num1,num2)}")
    print(f"quotient of {num1} and {num2} is {divide(num1,num2)}")
    print(f"remainder of {num1} and {num2} is {modulus(num1,num2)}")

def user_name(name="world"): # default value of parameter.
    return f"hello, {name}"

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("division by zero is not allowed")
        return None

def modulus(x,y):
    try:
        return x%y
    except ZeroDivisionError:
        print("modulus by zero is not allowed")
        return None



def square(n):
    return n*n


if __name__ == "__main__":
    main()