import math
from collections import Counter
x =math.ceil(10.4)
print(x)

x = [1,1,2,2,2,3,3,3,3,4,5,5,6,6]
counter = Counter(x)
print(counter)
print(counter[1])

for item, count in counter.items():
    print(item, count)
