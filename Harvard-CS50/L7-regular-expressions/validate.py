import re
email = input("Enter you email Id ").strip()

if(re.search(r"^\w+@\w+\.(com|org|net)$",email,flags=re.IGNORECASE)):
    print("Valid Email Id")
else:
    print("Invalid Email Id")