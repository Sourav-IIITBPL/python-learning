# packages are the third party libraries . we need to install them using pip (python package manager) before we can use them in our code . 
# once we have installed the package we can import it in our code and use its functions and classes .

import cowsay
import sys

print(cowsay.char_names)  # list of all names as strings

print(cowsay.cow("hello world "+sys.argv[1])) 
# sys.argv is a list that contains the command line arguments passed to the script . the first element of the list is the name of the script and the rest of the elements are the arguments passed to the script . in this case we are passing the first argument to the cowsay.cow() function which will be printed by the cow .

print(cowsay.tux("hello world "+sys.argv[1])) 

print(cowsay.trex("hello world "+sys.argv[1])) 

print(cowsay.turtle("hello world "+sys.argv[1])) 

for name in cowsay.char_names:
    getattr(cowsay, name)("hello world " + sys.argv[1])