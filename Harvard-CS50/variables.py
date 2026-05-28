# getting input from user 
""" multi line comments.
this is multi line comments 
"""

name = input("what is your name ?");   # input function generally takes text as input . 
print("hi",name,name);
print("hi"+name+name);
print(type(name))
a = 34.5
print(type(a))
a = "me"
print(type(a))
a = 34
print(type(a))

country = input("what is your country ?")

# sep and end are two default parameters of print function . sep defines (default sep = " ") " " separation 
# b/w two differnt elements and end defines (default end="\n") newline in print function .

print("my country",country, sep="?",end="??")
print(country)
print("india")

print("my country \"india\"")
print('my country "india"')

print("my country is {country}")
print(f"my country is {country}")

i = input().strip().upper()
print(i)
i.lower().capitalize().title()
print(i)
i.replace('L','a')
print(i)
i.find('a')
print(i[-1])

x = float(input("enter a number "))
y = float(input("enter another number "))

# round round off the number to given decimal places, default is 0 decimal places . another way is to use format function to round off the number to given decimal places .
# that is format(x,".2f") will round off x to 2 decimal places and return a string . or f("{x:.2f}") will round off x to 2 decimal places and return a string .

z = round(x+y)
print(z)
z = round(x+y,3)
print(z)
print(f"{x:.2f} + {y:.2f} = {z:.2f}")
print(f"{z:,}")

