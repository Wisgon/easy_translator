import pyperclip3 as pc

import time
from pynput.mouse import Listener, Button
from pynput.keyboard import Key, Controller


class AutoCopier:
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
        last_clipbord_txt = pc.paste()  # get last text of clipboard
        with self.__keyboard.pressed(Key.ctrl):  # press ctrl
            self.__keyboard.press("c")  # press c
            self.__keyboard.release("c")  # release c
        copy_word = pc.paste()
        # if make ctrl+shift+c may cause browser open dev tool
        # if copy_word == last_clipbord_txt:
        #     # maybe linux terminal ctrl+shift+c
        #     with self.__keyboard.pressed(Key.ctrl):  # press ctrl
        #         with self.__keyboard.pressed(Key.shift):  # press shift
        #             self.__keyboard.press("c")  # press c
        #             self.__keyboard.release("c")  # release c
        #     copy_word = pc.paste()
        pc.clear()
        pc.copy(last_clipbord_txt)  # recover clipbord
        print("###@", copy_word)

    def start_listen(self):
        if self.__listener is None or not self.__listener_alive:
            self.__listener = Listener(on_click=self.__on_click)  # init listener
            self.__listener.start()
            self.__listener_alive = True

    def stop_listen(self):
        if self.__listener is not None and self.__listener_alive:
            self.__listener.stop()
            self.__listener_alive = False

    # 等待线程终止
    def wait_to_stop(self):
        self.__listener.join()


# from pymouse import PyMouseEvent


# def fibo():
#     a = 0
#     yield a
#     b = 1
#     yield b
#     while True:
#         a, b = b, a + b
#         yield b


# class Clickonacci(PyMouseEvent):
#     def __init__(self):
#         PyMouseEvent.__init__(self)
#         self.fibo = fibo()

#     def click(self, x, y, button, press):
#         """Print Fibonacci numbers when the left click is pressed."""
#         if button == 1:
#             if press:
#                 print(next(self.fibo))
#         else:  # Exit if any other mouse button used
#             self.stop()

# import pyxhook
# import time


# def onclick(event):
#     print("###", event.Position)
#     return True


if __name__ == "__main__":
    auto_copier = AutoCopier()
    auto_copier.start_listen()
    auto_copier.wait_to_stop()
    # C = Clickonacci()
    # C.run()
    # hm = pyxhook.HookManager()
    # hm.MouseAllButtonsDown = onclick
    # hm.HookMouse()
    # hm.start()
    # while True:
    #     time.sleep(1)

    # import struct
    # import time

    # file = open("/dev/input/mice", "rb")

    # def getMouseEvent():
    #     buf = file.read(3)
    #     print(str(buf[0]))
    #     print(str(buf[1]))
    #     print(str(buf[2]))
    #     # button = ord(buf[0])
    #     # bLeft = button & 0x1
    #     # bMiddle = (button & 0x4) > 0
    #     # bRight = (button & 0x2) > 0
    #     x, y = struct.unpack("bb", buf[1:])
    #     print("x: %d, y: %d\n" % (x, y))

    # # return stuffs

    # while 1:
    #     getMouseEvent()

    #     time.sleep(1)
    # file.close()
