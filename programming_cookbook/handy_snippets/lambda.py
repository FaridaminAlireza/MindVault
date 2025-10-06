# Notes on Lambda usage

# If your lambda gets longer than a single simple expression,
# it’s better to define a proper function:

# Hard to read
process = lambda x: x.strip().lower().replace(" ", "_")

# Clear
def process(x):
    return x.strip().lower().replace(" ", "_")

# Lambdas can only contain a single expression, not multiple statements:
lambda x: x + 1         # OK
# lambda x: print(x); x+1 # Invalid

# Debugging
# Lambdas don’t have a name — stack traces just show <lambda>,
# making debugging harder in large codebases.


# Functional (lambda)
result = list(map(lambda x: x**2, range(5)))

# Pythonic (comprehension)
result = [x**2 for x in range(5)]


#Usage For short, one-off functions
words = ["python", "is", "awesome"]
sorted_words = sorted(words, key=lambda w: len(w))

# Not necessary to create a seperate function.
def length(w):
    return len(w)
sorted(words, key=length)



