import re
url = input("Enter the URL ").strip()

if(username := re.search(r"^https?://(?:www\.)?twitter\.(?:com|in|co|org)/(?:[#?/])?(\w+).*$",url,flags=re.IGNORECASE)):
    print(username.group(1))
else:
    print("No username found")
