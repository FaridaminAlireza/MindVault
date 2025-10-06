def insertion_sort(numbers):

    if len(numbers) <=1:
        return numbers
    
    for i in range(1,len(numbers)):
        elm = numbers[i]
        j = i -1

        while(j>=0 and numbers[j] > elm):
            numbers[j+1] = numbers[j]
            j -= 1 
        
        numbers[j+1] = elm

    return numbers

# Example usage:
numbers = [9, 5, 1, 4, 3]
insertion_sort(numbers)
print(numbers)  # Output: [1, 3, 4, 5, 9]

# strictly speaking, returning the result is unnecessary
# for in-place sorting of mutable objects like lists.

# Time Complexity: O(n²)
# The reasonig:
# Outer loop → runs n times
# Inner loop → in worst case runs up to i times → sum of 1+2+…+n = n(n-1)/2 → O(n²)

# Space Complexity: 
# It is using only a few variables (elm, j) → O(1)





