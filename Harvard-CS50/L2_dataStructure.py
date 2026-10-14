list = ["name","age","country"]
for i in list:
    print(i)
list.append("gender")
print(list)

copylist = list
copylist.append("hobby")
print(list)
print(copylist)

copylist = list.copy()
copylist.append("hobby")
print(list)
print(copylist)

dict = {
    "details": {
        "name": "sourav",
        "age": 22,
        "country": "india"
    },
    "hobby": {
        "name": "coding",
        "duration": "2 hours"
    },
    "skills": {
        "programming": ["python","java","c++"],
        "web development": ["html","css","javascript"]
    }

}

for key in dict:
    print(key)
    for subkey in dict[key]:
        print(subkey,dict[key][subkey])

# tuple,int,str are immutable data types in python,while list , dict , set are mutable data types in python .
tuple = (1,2,3,4,"india")
print(tuple)

try:
    tuple[0] = 0
except TypeError:
    print("tuple is immutable data type in python")
else:
    print(tuple)

try:
    list[0] = 0
except TypeError:
    print("list is mutable data type in python")
else:
    print(list)



