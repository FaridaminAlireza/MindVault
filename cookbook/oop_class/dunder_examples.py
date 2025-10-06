class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for x in Countdown(3):
    print(x)  # 3, 2, 1



class FileOpener:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileOpener('data.txt') as f:
    print(f.read())


class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"

hello = Greeter("Hello")
print(hello("Alice"))  # "Hello, Alice!"


class Repeater:
    def __init__(self, value, count):
        self.value = value
        self.count = count

    def __getitem__(self, index):
        if 0 <= index < self.count:
            return self.value
        raise IndexError

    def __len__(self):
        return self.count

r = Repeater('X', 5)
print(len(r))       # 5
print(r[2])         # 'X'



class MagicDemo:
    # ⚙️ Lifecycle
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return super().__new__(cls)
    def __init__(self, value):
        print("__init__ called")
        self.value = value
    def __del__(self):
        print("__del__ called")

    # 📝 Representation
    def __repr__(self): return f"MagicDemo({self.value!r})"
    def __str__(self): return f"<Magic: {self.value}>"
    def __format__(self, spec): return f"formatted:{self.value}"

    # 📦 Attribute Access
    def __getattr__(self, name): return f"{name} not found"
    def __getattribute__(self, name):
        if name.startswith("x"): print(f"__getattribute__ for {name}")
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        print(f"Setting {name}={value}")
        super().__setattr__(name, value)
    def __delattr__(self, name):
        print(f"Deleting {name}")
        super().__delattr__(name)
    def __dir__(self): return ['value', 'extra']

    # 📚 Container-like
    def __len__(self): return 3
    def __getitem__(self, key): return f"item-{key}"
    def __setitem__(self, key, val): print(f"set item[{key}]={val}")
    def __delitem__(self, key): print(f"deleted item[{key}]")
    def __contains__(self, item): return item == "magic"
    def __iter__(self):
        self._i = 0
        return self
    def __next__(self):
        if self._i >= 3: raise StopIteration
        self._i += 1
        return self._i
    def __reversed__(self): return iter([3,2,1])

    # ⚡ Callable / Bool
    def __call__(self, *args, **kwargs): return "I was called!"
    def __bool__(self): return bool(self.value)

    # ⚖️ Comparisons
    def __eq__(self, other): return self.value == getattr(other, 'value', other)
    def __lt__(self, other): return self.value < getattr(other, 'value', other)
    def __le__(self, other): return self.value <= getattr(other, 'value', other)
    def __gt__(self, other): return self.value > getattr(other, 'value', other)
    def __ge__(self, other): return self.value >= getattr(other, 'value', other)
    def __ne__(self, other): return not self.__eq__(other)

    # ➕ Arithmetic
    def __add__(self, other): return self.value + other
    def __radd__(self, other): return other + self.value
    def __sub__(self, other): return self.value - other
    def __mul__(self, other): return self.value * other
    def __truediv__(self, other): return self.value / other

    # 🧠 Context Manager
    def __enter__(self): print("__enter__"); return self
    def __exit__(self, exc_type, exc_value, tb): print("__exit__")

    # 🧪 Misc
    def __index__(self): return int(self.value)
    def __hash__(self): return hash(self.value)

# Demo of how these get called
m = MagicDemo(5)
print(m)                        # __str__
print(repr(m))                  # __repr__
print(len(m))                   # __len__
print(m[1])                     # __getitem__
print("magic" in m)              # __contains__
print(bool(m))                   # __bool__
print(m == 5, m < 10)             # __eq__, __lt__
print(m + 3, 3 + m)               # __add__, __radd__
print([x for x in m])             # __iter__, __next__
print(list(reversed(m)))          # __reversed__
print(m())                         # __call__
with m as mm: print("inside with") # __enter__, __exit__


import threading

def compute():
    count = 0
    for i in range(10**7):
        count += i

threads = [threading.Thread(target=compute) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()


import threading
import time

def io_task():
    time.sleep(2)  # simulates I/O wait
    print("Done")

threads = [threading.Thread(target=io_task) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()


from multiprocessing import Pool
with Pool(4) as p:
    p.map(compute, range(4))




def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)


squares = (x*x for x in range(5))
for sq in squares:
    print(sq)


def echo():
    while True:
        received = (yield)
        print(f"Received: {received}")

c = echo()
next(c)             # Prime the coroutine
c.send("Hello")     # Output: Received: Hello
c.send("World")     # Output: Received: World

