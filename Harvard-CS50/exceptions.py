

def main():
    user = input("what is your name ?")
    print(f"hello, {user}")
    x,y,operand = userPrompt()
    if operand == "+":
        print(f"{x} + {y} = {x+y}")
    elif operand == "-":
        print(f"{x} - {y} = {x-y}")
    elif operand == "*":
        print(f"{x} * {y} = {x*y}")
    elif operand == "/":
        if y == 0:
            print("division by zero is not allowed")
        else:
            print(f"{x} / {y} = {x/y}")
    else:
        print("Not Supported Operation")



def userPrompt():
    while True:
        try:
            x = int(input("enter a number "))
            y = int(input("enter another number "))
            operand = input("enter an operand (+,-,*,/) ")

            if operand not in ["+", "-", "*", "/"]:
                raise ValueError("operand")       # raise acts as an exception and it can be caught by except block . it takes an argument that is the error message that will be printed when the exception is raised . in this case we are raising a ValueError with the message "operand" when the user enters an invalid operand .

            return x, y, operand

        except ValueError as e:
            if str(e) == "operand":
                print("please enter a valid operand")
            else:
                print("please enter valid numbers")

main()

try :
    x = int(input("enter a number "))
except ValueError:
    print("please enter a valid number")

# this print works for vaild int input but for invalid input , this print will throw NameError because x is not defined or assigned any value 
# when the user enters an invalid input and the except block is executed . 
print(x)   