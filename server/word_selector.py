import pyperclip3 as pc

import time
from pynput.mouse import Listener, Button
from pynput.keyboard import Key, Controller


class WordSelector:
    __press_xy = (0, 0)  # mouse position when press mouse

    def __init__(self):
        self.__keyboard = Controller()  # keyboard controller
        self.__last_click_time = 0
        self.__listener = None
        self.__listener_alive = False

    def __on_click(self, x, y, button, pressed):
        if button == Button.left:  # click left button
            if pressed:  # press left button
                print("press left~~~")
                if time.time() - self.__last_click_time < 1:  # double click
                    time.sleep(0.5)  # make sure text had been selected
                    self.__get_selected()  # word selection event, copy
                self.__press_xy = (x, y)  # record mouse postion
                self.__last_click_time = time.time()
            else:  # release left button
                if self.__press_xy != (
                    x,
                    y,
                ):  # press position is different from release position, then copy word
                    time.sleep(0.5)
                    self.__get_selected()  # word selection event, copy

    def __get_selected(self):
        global now_selected_word
        last_clipbord_txt = pc.paste()  # get last text of clipboard
        with self.__keyboard.pressed(Key.ctrl):  # press ctrl
            self.__keyboard.press("c")  # press c
            self.__keyboard.release("c")  # release c
        now_selected_word = pc.paste()
        pc.clear()
        pc.copy(last_clipbord_txt)  # recover clipbord

    def start_listen(self):
        if self.__listener is None or not self.__listener_alive:
            self.__listener = Listener(on_click=self.__on_click)  # init listener
            self.__listener.start()
            self.__listener_alive = True

    def stop_listen(self):
        if self.__listener is not None and self.__listener_alive:
            self.__listener.stop()
            self.__listener_alive = False

    def wait_to_stop(self):
        self.__listener.join()
