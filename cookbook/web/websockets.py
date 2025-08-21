"""
WebSocket Example in Python using the `websockets` library
This file contains BOTH a server and a client example with full explanations.
Run the server first in one terminal, then run the client in another.
"""

import asyncio
import websockets


# ============================================================
# 1. WEBSOCKET SERVER
# ============================================================

async def echo(websocket, path):
    """
    This function handles communication with ONE client.

    Parameters:
    - websocket: the connection to the client
    - path: the URL path the client used (e.g., /chat)
    """
    async for message in websocket:  # Wait for messages from the client
        print(f"Server received: {message}")

        # Send a response back to the client
        await websocket.send(f"Echo: {message}")


async def run_server():
    """
    Starts the WebSocket server on ws://localhost:8765
    - websockets.serve(...) tells Python to use `echo`
      whenever a client connects.
    - asyncio.Future() is just a never-ending task to
      keep the server running.
    """
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future()  # Run forever


# ============================================================
# 2. WEBSOCKET CLIENT
# ============================================================

async def run_client():
    """
    Connects to the server, sends a message, and waits for a reply.
    """
    uri = "ws://localhost:8765"  # Server address

    # `async with` ensures connection is closed automatically
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        await websocket.send("Hello from client!")
        print("Client sent: Hello from client!")

        # Wait for the server to reply
        response = await websocket.recv()
        print(f"Client received: {response}")


# ============================================================
# 3. MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    """
    To use this file:
    1. Open one terminal and run: python this_file.py server
    2. Open another terminal and run: python this_file.py client
    """

    import sys

    if len(sys.argv) != 2:
        print("Usage: python websocket_example.py [server|client]")
    elif sys.argv[1] == "server":
        asyncio.run(run_server())
    elif sys.argv[1] == "client":
        asyncio.run(run_client())
    else:
        print("Invalid argument. Use 'server' or 'client'.")


# pip install websockets
# python websocket_example.py server
# WebSocket server running on ws://localhost:8765
# python websocket_example.py client

# Client sent: Hello from client!
# Client received: Echo: Hello from client!

# -----------------

import asyncio
import websockets

# Keep track of connected clients
connected_clients = set()

async def chat_handler(websocket, path):
    # Register client
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")

            # Send message to all connected clients
            await asyncio.gather(*[
                client.send(f"[Chat] {message}")
                for client in connected_clients
                if client != websocket
            ])
    finally:
        # Remove client on disconnect
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(chat_handler, "localhost", 8765):
        print("Chat server running on ws://localhost:8765")
        await asyncio.Future()  # run forever

asyncio.run(main())

# ---------------------------

import asyncio
import websockets

async def chat_client(name):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(f"{name} joined the chat!")

        async def listen():
            async for msg in websocket:
                print(f"{name} received: {msg}")

        await listen()

asyncio.run(chat_client("Alice"))


# await pauses only when the thing you’re awaiting yields control back to the event loop.
# That typically happens during I/O operations:
# Waiting for network data (WebSockets, HTTP, DB query…)
# Waiting for disk reads/writes
# Timers (await asyncio.sleep())

# 👉 So async is designed for I/O-bound waiting, not CPU crunching.


import asyncio
from concurrent.futures import ProcessPoolExecutor

def heavy_cpu_task(x):
    # simulate heavy computation
    return sum(i*i for i in range(x))

async def main():
    loop = asyncio.get_running_loop()

    # Offload to a separate process
    result = await loop.run_in_executor(
        ProcessPoolExecutor(), heavy_cpu_task, 10**7
    )

    print("Result:", result)

asyncio.run(main())

# 👉 This way, CPU work happens outside the event loop,
# so the server can still handle WebSocket clients.

# Async tasks pause only on awaited I/O operations.
# CPU crunch or memory pressure can still block everything if not handled properly.

#--------------------------------

import asyncio
import aiohttp

async def fetch_page(session, url):
    print(f"Starting request: {url}")
    async with session.get(url) as response:
        # This 'await' pauses until the network response arrives
        text = await response.text()
        print(f"Finished request: {url}")
        return len(text)

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/delay/2",  # simulates a 2s slow response
        "https://httpbin.org/delay/3",  # simulates a 3s slow response
    ]

    async with aiohttp.ClientSession() as session:
        # Start all requests concurrently
        tasks = [fetch_page(session, url) for url in urls]

        results = await asyncio.gather(*tasks)
        print("Page sizes:", results)

asyncio.run(main())

# What happens here

# Each session.get(url) is network I/O (waiting for server reply).
# await response.text() pauses the coroutine while data is downloaded.
# During that pause, the event loop runs other tasks.
# Because we gather them, all requests start together.
# The slowest one (delay/3) takes ~3s, but all others finish as soon as
# their response is ready.


# async for works with an asynchronous iterator 
# (something that produces values over time, with await in between).

import asyncio

class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count >= self.limit:
            raise StopAsyncIteration
        await asyncio.sleep(1)   # simulate waiting (I/O or delay)
        self.count += 1
        return self.count

async def main():
    async for number in AsyncCounter(3):
        print("Got:", number)

asyncio.run(main())


# async with works with an asynchronous context manager,
#  where entering/exiting the block may require await.

import asyncio

class AsyncResource:
    async def __aenter__(self):
        print("Connecting...")
        await asyncio.sleep(1)   # simulate connection delay
        print("Connected")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Closing connection...")
        await asyncio.sleep(1)
        print("Closed")

async def main():
    async with AsyncResource() as resource:
        print("Using resource inside the block")

asyncio.run(main())

# async for = asynchronous iteration (each step can await).
#async with = asynchronous context manager (enter/exit can await).
#Both are needed because async code often deals with things that take time
#  (network, streams, locks).

# Event Loop + OS Notifications

# Python’s asyncio event loop relies on the operating system to tell it when I/O is done.
# On Linux/Unix → it uses epoll / kqueue / select.
# On Windows → it uses I/O Completion Ports (IOCP).
# These are system calls that let you “register interest” in an event (e.g., when data arrives on this socket).
# So when you await websocket.recv() or await response.text():
# The event loop registers with the OS:
# “Wake me up when this socket has data available.”
# The coroutine is suspended.
# The event loop goes on to run other tasks.
# When the OS signals “data is ready,” the event loop resumes the suspended coroutine exactly where it left off.


# Async I/O isn’t about “checking repeatedly.”
# It’s about OS-level notifications.
# The event loop suspends your coroutine, waits for the OS to say “data ready,” then resumes it exactly where it left off.

