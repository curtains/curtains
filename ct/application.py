#-*-coding: utf-8-*-
"""Application Class"""

import ctypes

from . import cobject
from . import user
from . import wintypes as wt

class Application(cobject.cobject):


    instance = None
    def __init__(self):
        if Application.instance != None:
            raise Exception("You already have an application instance.")

        cobject.cobject.__init__(self)
        self.windowclassname = "CurtainsWindow"

        wndclass = wt.WndClassEx()
        wndclass.cbSize = ctypes.sizeof(wt.WndClassEx)
        wndclass.style = user.CS_HREDRAW | user.CS_VREDRAW
        wndclass.lpfnWndProc = wt.WndProc(self._wndproc_)
        wndclass.cbClsExtra = 0
        wndclass.cbWndExtra = 0
        wndclass.hInstance = None
        wndclass.hIcon = None
        wndclass.hCursor = user.load_image(None, user.OCR_NORMAL,
                                      user.IMAGE_CURSOR, 0, 0,
                                      wt.uint(user.LR_DEFAULTSIZE | user.LR_SHARED))
        wndclass.hbrBackground = user.COLOR_WINDOW + 1
        wndclass.lpszMenuName = None
        wndclass.lpszClassName = self.windowclassname

        if not user.register_class(wndclass):
            raise Exception("Could not register the window class.")
        self.__wndclass = wndclass




        self.__windows = {}

        Application.instance = self

    def _wndproc_(self, handle, message, wparam, lparam):

        if message == user.WM_CREATE:
            return 0

        elif message == user.WM_DESTROY:
            self.__windows.pop(handle)

        return user.def_window_proc(handle, message, wparam, lparam)

    def _attach_window_(self, window):
        key = window.handle
        self.__windows[key] = window

    def _find_handle_(self, handle):
        if handle in self.__windows.keys():
            return self.__windows[handle]

        for window in self.__windows:
            res = window._find_(handle)
            if res != None:
                return res

        else:
            return None

    def main_loop(self):
        msg = wt.Msg()
        while user.get_message(msg, None, 0, 0):
            user.translate_message(msg)
            user.dispatch_message(msg)

            if len(self.__windows) < 1:
                user.post_quit_message(0)

    def process_messages(self):
        msg = wt.Msg()
        while user.peek_message(msg, None, 0, 0):
            user.translate_message(msg)
            user.dispatch_message(msg)
