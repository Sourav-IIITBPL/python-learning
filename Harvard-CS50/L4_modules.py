"""modules are files that contain functions and variables that can be used in other Python files.
They are used to organize code and make it reusable. Modules can be imported using the import statement.
The import statement can be used to import a module or specific functions and variables from a module.
 The syntax for importing a module is as follows:
import module_name
in other words, modules are libraries that contain functions and variables that can be used in other Python files.
"""

# these are the standard libraries of python that are available in python by default .
# we can use these libraries without installing them .
# these libraries are written in C and are compiled into bytecode that can be executed by the python interpreter .
# these libraries are written in C because C is a low-level language that can be used to write efficient code that can be executed quickly .
# these libraries are compiled into bytecode because bytecode is a low-level representation of the code that can be executed quickly by the python interpreter .

import random
import math, statistics
import sys       # this lib is used to get cli arguments passed to the script and also to exit the script with a message . sys.exit() is used to exit the script with a message . sys.argv is used to get the cli arguments passed to the script . sys.argv is a list of strings that contains the command line arguments passed to the script . the first element of the list is the name of the script and the rest of the elements are the arguments passed to the script .

print(
    random.randint(1, 10)
)  # random.randint(a,b) returns a random integer between a and b (inclusive).
print(
    random.choice(["apple", "banana", "cherry"])
)  # random.choice(sequence) returns a random element from the sequence.
print(
    random.sample(range(1, 100), 5)
)  # random.sample(population,k) returns a list of k unique elements chosen from the population sequence or set.
print(
    random.shuffle([1, 2, 3, 4, 5])
)  # random.shuffle(x) shuffles the sequence x in place.
print(
    random.uniform(1, 10)
)  # random.uniform(a,b) returns a random float between a and b (inclusive).

print(math.sqrt(16))  # math.sqrt(x) returns the square root of x.
print(math.factorial(5))  # math.factorial(x) returns the factorial of x.
print(math.pow(2, 3))  # math.pow(x,y) returns x raised to the power of y.

print(
    statistics.mean([1, 2, 3, 4, 5])
)  # statistics.mean(data) returns the mean of the data.
print(
    statistics.median([1, 2, 3, 4, 5])
)  # statistics.median(data) returns the median of the data.
print(
    statistics.mode([1, 2, 3, 4, 5, 1])
)  # statistics.mode(data) returns the mode of the data.
print(
    statistics.stdev([1, 2, 3, 4, 5])
)  # statistics.stdev(data) returns the standard deviation of the data.

print(
    sys.version
)  # sys.version returns the version of Python that is currently being used.
print(
    sys.platform
)  # sys.platform returns the platform on which Python is currently running.
print(
    sys.path
)  # sys.path returns a list of strings that specifies the search path for modules. It is initialized from the environment variable PYTHONPATH, plus an installation-dependent default.

# print("my name is ",sys.argv[1]) # sys.argv (sys argument vector) is a list of command line arguments passed to a Python script. The first element is the script name, and the rest are the arguments.
print(
    "my name is ", sys.argv[0]
)  # sys.argv[0] is the script name. sys.argv[1] is the first argument passed to the script. sys.argv[2] is the second argument passed to the script and so on.

try:
    print("my name is ", sys.argv[1])
except IndexError:
    print("too few arguments passed to the script. Please pass at least one argument.")

if len(sys.argv) < 2:
    print("too few arguments passed to the script. Please pass at least one argument.")
elif len(sys.argv) > 2:
    print("too many arguments passed to the script. Please pass only one argument.")
else:
    print("my name is ", sys.argv[1])
    print("script name is ", sys.argv[0])

if len(sys.argv) < 2:
    sys.exit("too few arguments passed to the script.")
print("my name is ", sys.argv[1])
print("script name is ", sys.argv[0])

if len(sys.argv) < 2:
    sys.exit("too few arguments.")

for items in sys.argv:
    print(items)

# this is slice notation . it is used to get a sublist of a list . in this case , we are getting a sublist of sys.argv from index 1 to the end of the list.
for items in sys.argv[1:]:
    print(items)


for items in sys.argv[1:-1]:
    print(items)
