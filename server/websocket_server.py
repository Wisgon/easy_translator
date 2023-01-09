import asyncio
import websockets
import json
import threading

from translator import Translator
from util import set_config


from word_selector import global_value

translator = Translator()
now_selected_word = ""
listener = None
response = {"msg": "", "data": {}}
now_websocket = None  # It's for the "listen_word_select_and_send" thread, because when client reconenct, websocket will be changed.


async def listen_word_select_and_send():
    global now_selected_word, response, now_websocket
    while True:
        now_selected_word, x, y = global_value[
            "word_queue"
        ].get()  # stuck here to wait select word,if word_selector had been stopped,it will stuck forever.
        response["msg"] = "selected word"
        response["data"] = {
            "now_selected_word": now_selected_word.decode(),  # decode byte to str
            "x": x,
            "y": y,
        }
        if now_websocket.closed is False:
            await now_websocket.send(json.dumps(response))


async def input_translate(websocket, word):
    # need translate word
    result = translator.translate(word)
    response["msg"] = "success"
    response["data"] = {"result": result}
    await websocket.send(json.dumps(response))


async def stop_select_word(websocket):
    # stop select word
    global global_value
    global_value["word_selector"].stop_listen()
    set_config("listen_select_word", False)
    response["msg"] = "stoped"
    await websocket.send(json.dumps(response))


async def start_select_word(websocket):
    # stop select word
    global global_value
    global_value["word_selector"].start_listen()
    # set to config
    set_config("listen_select_word", True)
    response["msg"] = "started"
    await websocket.send(json.dumps(response))


async def select_translate(websocket):
    global global_value, now_selected_word
    print(f"$$${global_value}")
    result = translator.translate(now_selected_word)
    response["msg"] = "success"
    response["data"] = {"result": result}
    await websocket.send(json.dumps(response))


async def handler(websocket):
    """
    Handle a connection and dispatch it according to who is connecting.

    """
    global listener, now_websocket
    now_websocket = websocket
    if listener is None:
        # the listener has no need to stop, because when stop word_selector, the queue has no input.
        listener = threading.Thread(
            target=asyncio.run, args=(listen_word_select_and_send(),)
        )
        listener.start()
    async for message in websocket:
        print(f"#####{message}")
        try:
            event = json.loads(message)
        except Exception as e:
            print("something wrong " + str(e))
            await websocket.send("something wrong:" + str(e))
        else:
            if "stop_select_word" == event["type"]:
                await stop_select_word(websocket)
            elif "start_select_word" == event["type"]:
                await start_select_word(websocket)
            elif "input_translate" == event["type"]:
                await input_translate(websocket, event["data"]["value"])
            elif "select_translate" == event["type"]:
                # First player starts a new game.
                await select_translate(websocket)
        print("$$$end")


async def server():
    async with websockets.serve(handler, "localhost", 5679):
        print("listening at port 5679~~")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(server())
