import queue
import threading
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(0.5)

def consumer():
    while True:
        item = q.get()
        print(f"Consuming {item}")
        q.task_done()

threading.Thread(target=producer).start()
threading.Thread(target=consumer, daemon=True).start()

q.join()  # Wait until all items are processed

# Ensures safe communication between threads.
# If you’re not dealing with threads you can use collections.deque.