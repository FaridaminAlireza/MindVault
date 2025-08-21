#Sort dict by value

my_dict = {'b': 3, 'a': 1, 'c': 2}

# Sorted by values desc
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]), reverse=True)
print(sorted_by_values)  # Output: {'a': 1, 'c': 2, 'b': 3}

