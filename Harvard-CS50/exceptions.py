

def main():
    user = input("what is your name ?")
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
              return x, y, operand
         except ValueError:
             if  x is not int or y is not int:
                  print("please enter a valid number")
             else:
                  if operand not in ["+", "-", "*", "/"]:
                       print("please enter a valid operand") 


main()