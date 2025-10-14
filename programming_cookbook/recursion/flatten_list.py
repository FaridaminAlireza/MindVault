

# Recursive approach
def flatten_list(ls):
    
    flat_ls = []
    def flatten_list_fnc(inner_ls):

        for elm in inner_ls:
            if isinstance(elm, list):
                if elm:
                    flatten_list_fnc(elm)
            else:
                flat_ls.append(elm)

    flatten_list_fnc(ls)

    return flat_ls

x = [1,[[2,3],4],5,[[[[[6]]]]]]
print(flatten_list(x))


# Iterative approach using stack
def flatten_list_iterative(nested_list):
    stack = nested_list[::-1]  # reverse for LIFO behavior
    flat = []
    
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])  # push elements back in reverse order
        else:
            flat.append(item)
    
    return flat

x = [1,[[2,3],4],5,[[[[[6]]]]]]
print(flatten_list_iterative(x))