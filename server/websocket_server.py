import asyncio
import websockets

from util import translate


async def controller(websocket):
    command = await websocket.recv()
    if command == "stop_select_word":
        # stop select word
        global word_selector
        word_selector.stop_listen()
        await websocket.send("stoped")
    elif command.startswith("translate"):
        # need translate word
        word = command.split("#")[-1]
        result = translate(word)
        await websocket.send(result)


async def main_window_message():
    async with websockets.serve(controller, "localhost", 5680):
        await asyncio.Future()  # run forever


async def translator(websocket):
    global now_selected_word
    result = translate(now_selected_word)
    await websocket.send(result)


async def result_sender():
    async with websockets.serve(translator, "localhost", 5679):
        await asyncio.Future()
