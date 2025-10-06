# Heap Sort is a comparison-based sorting algorithm that uses a binary
# heap data structure to sort elements. It is in-place but not stable.

# Idea: Build a max-heap from the array, then repeatedly extract the
# maximum element and place it at the end of the array.
# Heap type: Usually a max-heap for ascending order.

# Step 1: Build a Max-Heap
# Convert the array into a max-heap where parent ≥ children.
# Start from the last non-leaf node and heapify each node upwards.
# Heapify operation ensures the subtree rooted at a node satisfies the max-heap property.

# Step 2: Swap Max with Last Element
# Swap the root of the heap (maximum element) with the last element in the heap.
# Reduce the heap size by 1.

# Step 3: Heapify the Root
# Restore the max-heap property for the reduced heap.
# Repeat Steps 2–3 until the heap size becomes 1.


def heapify(arr, n, i):
    """
    Ensure the subtree rooted at index i is a max heap.
    :param arr: list of elements
    :param n: size of heap
    :param i: index of root
    """
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # left child index
    right = 2 * i + 2  # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)


# Time complexity: O(n log n)
# Space complexity: O(n)