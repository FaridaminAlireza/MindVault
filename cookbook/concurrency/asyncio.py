# Async / Await in Python
# Declares a coroutine function 
# (like a "special" function that can pause itself and let others run).

async def foo():
    return 42
#  When you call an async function,
#  it doesn’t run immediately — it gives you a coroutine object.

print(foo())  # <coroutine object foo at ...>

# To actually run it, you need the event loop (via await or asyncio.run()).

# await

# Think of await as:
# 👉 "Pause here, run the awaited thing, then continue when it’s done."

# It only works inside an async def.

import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)  # pretend "waiting" (like network or file I/O)
    print(f"Task {name} finished")

async def main():
    print("Running tasks...")
    await task("A")   # This pauses here for 2s, then continues
    await task("B")   # Runs AFTER task A finishes

asyncio.run(main())

# Running tasks...
# Task A started
# Task A finished   (after 2s)
# Task B started
# Task B finished   (after 2s)

# it feels like blocking: the current coroutine is
# paused until each task is finished, one after the other.

# Because in that example, you only started one coroutine at a time.
# The event loop can do other work while you’re awaiting — but you didn’t
# give it any other tasks to juggle.
# So while task("A") is sleeping (await asyncio.sleep(2)),
# the event loop could run another coroutine… but none exist yet.
# Task B isn’t started until later.

# await does block the current coroutine (it stops and waits).
# But it does not block the event loop.
# → While one coroutine is paused, the loop can run other coroutines.

# How to make them overlap?
# You need to start multiple tasks first, then await them together.

import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)  # Pause this coroutine
    print(f"Task {name} finished")

async def main():
    # Start tasks concurrently
    t1 = asyncio.create_task(task("A"))
    t2 = asyncio.create_task(task("B"))

    # Now both are "scheduled" immediately
    await t1
    await t2

    # Shorter way with asyncio.gather
    # Instead of manually creating tasks:
    # await asyncio.gather(task("A"), task("B"))

asyncio.run(main())



import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)  # Pause this coroutine for 2 seconds
    print(f"Task {name} finished")

async def main():
    # Run tasks concurrently
    await asyncio.gather(task("A"), task("B"))

asyncio.run(main())


# asyncio.run()
# This starts the event loop.
# It runs the given coroutine until it’s finished.

async def hello():
    print("Hello async")

asyncio.run(hello())

# -----------------------------------------
import asyncio

async def download_file(n):
    print(f"Downloading file {n}...")
    await asyncio.sleep(2)   # Simulate network delay
    print(f"File {n} downloaded")
    return f"file{n}.txt"

async def main():
    # Run downloads concurrently
    results = await asyncio.gather(download_file(1), download_file(2), download_file(3))
    print("All done:", results)

asyncio.run(main())
