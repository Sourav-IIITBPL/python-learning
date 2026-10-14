#file input/output operations 

# write opeations

name = input("what is your name")

file = open("names.txt","a") # open function creates or opens a file in the specified mode. "a" mode is for appending data to the file."w" mode is for writing data to the file from starting point. "r" mode is for reading data from the file.
file.write(name + "\n") # write function writes the data to the file. "\n" is used to add a new line after the name.
file.close() # close function closes the file. It is important to close the file after writing to it to free up system resources.


name_list = ["sourav","rajeev","shyam"] # list of names to be written to the file.

with open("names.txt","a") as file: # with statement is used to open the file in the specified mode. It automatically closes the file after the block of code is executed.
    for name in name_list:
        file.write(f"{name}\n") # write function writes the data to the file. "\n" is used to add a new line after the name.


# read operations

with open("names.txt") as file:
    list = file.readlines() # readlines function reads the data from the file and returns it as a list of strings. Each string represents a line in the file.

for name in list:
    print(name.strip()) # strip function removes the leading and trailing whitespaces from the string. It is used to remove the new line character from the string.



read_list = []
with open("names.txt") as file:
    for line in file:
        read_list.append(line.strip()) # append function adds the string to the list. strip function removes the leading and trailing whitespaces from the string. It is used to remove the new line character from the string.

for name in sorted(read_list):
    print(name) # sorted function sorts the list in ascending order. It returns a new list and does not modify the original list.