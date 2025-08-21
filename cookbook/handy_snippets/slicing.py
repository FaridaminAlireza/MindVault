# Reversing a string in Python using slicing 

s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # Output: !dlrow ,olleH

s = "Hello, world!"
reversed_s = ''.join(reversed(s))
print(reversed_s)  # Output: !dlrow ,olleH

# reversed(s) returns an iterator that goes through the string backward.
# ''.join(...) converts it back to a string.
