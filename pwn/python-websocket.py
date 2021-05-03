"""This script is meant to send and recieve data using a websocket
"""

import asyncio
import websockets

URI = "ws://localhost:3001"


async def recv(ws):
    data = await ws.recv()
    return data.decode()


async def send(ws, data):
    print(f"[+] Sending\n{data}")
    await ws.send(data)


async def pwn():
    async with websockets.connect(URI) as ws:
        print(await recv(ws))
        await send(ws, "hello!")
        print(await recv(ws))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(pwn())
