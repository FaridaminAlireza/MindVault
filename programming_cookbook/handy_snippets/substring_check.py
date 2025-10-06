# Check if a Python string contains another string.

text = "Hello, world!"
if "world" in text:
    print("Found!")
else:
    print("Not found!")


text = "Hello, world!"
if text.find("world") != -1:
    print("Found!")
else:
    print("Not found!")

