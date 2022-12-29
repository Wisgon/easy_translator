import asyncio
import websockets
import json


async def hello():
    async with websockets.connect("ws://localhost:5679") as websocket:
        event = {"select_translate": "haha"}
        await websocket.send(json.dumps(event))
        data = await websocket.recv()
        print(data, "@@##")


if __name__ == "__main__":
    asyncio.run(hello())
