# csv file handling 

import csv
from os import read

# write operations

name = input("what is your name ")
home = input("what is your home ")
job = input("what is your job ")

with open("names.csv","a",newline="") as file: # newline="" is used to prevent adding extra new lines in the csv file.
    writer = csv.writer(file) # csv.writer function creates a writer object that can be used to write data to the csv file.
    writer.writerow([name,home,job]) # writerow function writes a single row of data to the csv file. The data is passed as a list. 

dict = [{"name":"sourav","home":"New Delhi", "job":"developer"},{"name":"rajeev","home":"mumbai","job":"manager"},{"name":"shyam","home":"kolkata", "job":"analyst"}] # list of dictionaries to be written to the csv file.

with open("names.csv","w",newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home", "job"])
    writer.writeheader()
    writer.writerows(dict)

# read operations

read_list = []
file = open("names.csv")
for line in file:
    data = line.strip().split(",") # split function splits the string into a _ of strings based on the specified delimiter. In this case, the delimiter is ",". strip function removes the leading and trailing whitespaces from the string. It is used to remove the new line character from the string.
    read_list.append({"name":data[0], "home":data[1], "job":data[2]}) # append function adds the dictionary to the list. The dictionary is created using the data from the list.
file.close()

for data in sorted(read_list, key=lambda x: x["name"],reverse = True): # sorted function sorts the list of dictionaries based on the specified key. The key is a lambda function that returns the value of the "name" key in the dictionary. reverse=True is used to sort the list in descending order.
    print(f"{data['name']} is from {data['home']} and works as a {data['job']}.") # f-string is used to format the string. The values of the keys in the dictionary are accessed using the square bracket notation.

# read operations using csv module

read_list = []
with open("names.csv") as file:
    reader = csv.DictReader(file) # csv.DictReader function creates a reader object that can be used to read data from the csv file. It returns each row as a dictionary.
    for row in reader:
        read_list.append(row)

for data in sorted(read_list, key=lambda x: x["job"]): # sorted function sorts the list of dictionaries based on the specified key. The key is a lambda function that returns the value of the "name" key in the dictionary.
    print(f"{data['name']} works as a {data['job']} and is from {data['home']}.") # f-string is used to format the string. The values of the keys in the dictionary are accessed using the square bracket notation.

