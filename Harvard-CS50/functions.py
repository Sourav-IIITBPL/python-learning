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

input = input().strip().upper()
print(input)
input.lower().capitalize().title()
print(input)
input.replace('L','a')
print(input)
input.find('a')
print(input[-1])