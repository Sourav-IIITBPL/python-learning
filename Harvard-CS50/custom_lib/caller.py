import sys
from sayings import goodbye, hello

if len(sys.argv) < 2:
    sys.exit("too few arguments passed to the script. Please pass at least one argument.")

name = sys.argv[1]
print(hello(name))
print(goodbye(name))