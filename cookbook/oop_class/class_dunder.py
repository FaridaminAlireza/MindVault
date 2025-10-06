# __repr__(self)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

b = Book("Python Basics", "Alice")
print(b)           # Book(title='Python Basics', author='Alice')
print(repr(b))     # Book(title='Python Basics', author='Alice')


#__len__(self)
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["Song A", "Song B", "Song C"])
print(len(p))  # 3


# __eq__(self, other)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True


# __add__(self, other)
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __repr__(self):
        return f"Money({self.amount})"

m1 = Money(50)
m2 = Money(70)
print(m1 + m2)  # Money(120)


# __str__(self)
class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book(title='{self.title}')"

    def __str__(self):
        return f"📘 {self.title}"

b = Book("Python Basics")

print(repr(b))   #  -> developer friendly
print(str(b))    #  -> user friendly
print(b)         #  -> calls __str__

