def main():
    user = input("what is your name ?")
    userName(user)
    num1 = int(input("enter a number "))
    num2 = int(input("enter another number "))
    squared(num1,num2)


def userName(name="world"): # default value of parameter.
    print(f"hello, {name}")

def squared(x=1,y=1):
    print(f"{x} squared is {x**2}")
    print(f"{y} squared is {y**2}")

main()

x = int(input("enter a number "))

if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case x if x < 0:
        print("x is negative")
    case x if x > 0:
        print("x is positive")       
    case _:
        print("x is something else")

x = [1,3,5,7,9]

#lambda function is an anonymous function that can take any number of arguments but can only have one expression . it is defined using the lambda keyword . the syntax is lambda arguments: expression .
squared = map(lambda x: x**2,x)
print(list(squared))

user = input("what is your name ?")
if(user == "Alice" or user == "Bob"):
    print("hi Alice/Bob")
elif user == "Charlie" or user == "Dave":
    print("hi Charlie/Dave")
else:
    print("hi user")


for i in range(len(x)):
    print(x[i],sep=",",end=" ")

i = 0
while i < len(x):
    print(x[i],sep=",",end=" ")
    i += 1

myList = [1,2,3,4,5]
myModifiedList = map(lambda x: x**2, myList)
print(list(myModifiedList))

x = int(input("enter a number "))
y = int(input("enter another number "))
tuple = lambda x, y: (x**2, y**2)
print(tuple(x,y))