# In Python, a context manager is a way to allocate and release resources precisely
#  when you want to. It’s most commonly used with the with statement. The idea is:

# Enter: Do something when the block starts (e.g., open a file, acquire a lock).
# Exit: Clean up when the block ends, even if an exception happens
#  (e.g., close the file, release the lock).


# Example 1
# with open("file.txt", "r") as f:
#     data = f.read()
# file is automatically closed here


# Example 2
import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    original = os.getcwd()
    os.chdir(destination)
    try:
        yield
    finally:
        os.chdir(original)

with change_dir("/tmp"):
    print(os.getcwd())  # /tmp
# automatically goes back to original directory


# Example 3
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print("Elapsed:", time.time() - start)

with timer():
    time.sleep(1)


# Example 4
from contextlib import suppress

with suppress(FileNotFoundError):
    open("missing.txt")
# No error is raised


# Example 5 

import sqlite3

class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        # Open the connection
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.cursor  # return cursor to work with

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # Rollback if exception occurs
            self.conn.rollback()
        else:
            # Commit if no exception
            self.conn.commit()
        self.conn.close()
        # Do not suppress exceptions, propagate them
        return False

with DatabaseConnection("my_database.db") as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
# connection automatically committed and closed


# Using contextlib decorator
import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

with db_connection("my_database.db") as cursor:
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))


