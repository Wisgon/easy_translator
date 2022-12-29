import asyncio
import websockets
import json

from translator import Translator
from util import set_config


from word_selector import global_value

translator = Translator()


async def input_translate(websocket, word):
    # need translate word
    result = translator.translate(word)
    await websocket.send(result)


async def stop_select_word(websocket):
    # stop select word
    global global_value
    global_value["word_selector"].stop_listen()
    set_config("listen_select_word", False)
    await websocket.send("stoped")


async def start_select_word(websocket):
    # stop select word
    global global_value
    global_value["word_selector"].start_listen()
    # set to config
    set_config("listen_select_word", True)
    await websocket.send("started")


async def select_translate(websocket):
    global global_value
    print(f"$$${global_value}")
    result = translator.translate(global_value["now_selected_word"])
    await websocket.send(result)


async def handler(websocket):
    """
    Handle a connection and dispatch it according to who is connecting.

    """
    # Receive and parse the "init" event from the UI.
    message = await websocket.recv()
    try:
        event = json.loads(message)
    except Exception as e:
        await websocket.send("something wrong:" + str(e))
    else:
        if "stop_select_word" in event:
            await stop_select_word(websocket)
        elif "start_select_word" in event:
            await start_select_word(websocket)
        elif "input_translate" in event:
            await input_translate(websocket, event["input_translate"])
        elif "select_translate" in event:
            # First player starts a new game.
            await select_translate(websocket)


async def server():
    async with websockets.serve(handler, "localhost", 5679):
        print("listening at port 5679~~")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(server())
