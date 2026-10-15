import re

name = input("Enter your full name: ").strip()

matches = re.split(r"\,\s*",name, flags=re.IGNORECASE) # this re.split method/function returns a list of strings after breaking the given string by the specified separator, in this case, a comma followed by zero or more spaces.

if(len(matches) == 2):
    name = matches[1]+" "+matches[0]
    print(matches)
    print(f"hi, {name}")

else:
    print(f"hi, {name}")
