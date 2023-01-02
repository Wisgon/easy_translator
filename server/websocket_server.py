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
send_data_template = {"msg": "", "data": {}}


def listen_word_select_and_send(websocket):
    global now_selected_word, send_data_template
    while True:
        now_selected_word, x, y = global_value["word_queue"].get()
        send_data_template["msg"] = "selected word"
        send_data_template["data"] = {
            "now_selected_word": now_selected_word,
            "x": x,
            "y": y,
        }
        websocket.send(json.dumps(send_data_template))


async def input_translate(websocket, word):
    # need translate word
    result = translator.translate(word)
    send_data_template["msg"] = "success"
    send_data_template["data"] = {"result": result}
    await websocket.send(json.dumps(send_data_template))


async def stop_select_word(websocket):
    # stop select word
    global global_value
    global_value["word_selector"].stop_listen()
    set_config("listen_select_word", False)
    send_data_template["msg"] = "stoped"
    await websocket.send(json.dumps(send_data_template))


async def start_select_word(websocket):
    # stop select word
    global global_value
    global_value["word_selector"].start_listen()
    # set to config
    set_config("listen_select_word", True)
    send_data_template["msg"] = "started"
    await websocket.send(json.dumps(send_data_template))


async def select_translate(websocket):
    global global_value, now_selected_word
    print(f"$$${global_value}")
    result = translator.translate(now_selected_word)
    send_data_template["msg"] = "success"
    send_data_template["data"] = {"result": result}
    await websocket.send(json.dumps(send_data_template))


async def handler(websocket):
    """
    Handle a connection and dispatch it according to who is connecting.

    """
    global listener
    if listener is None:
        # the listener has no need to stop, because when stop word_selector, the queue has no input.
        listener = threading.Thread(
            target=listen_word_select_and_send, args=(websocket,)
        )
        listener.start()
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
