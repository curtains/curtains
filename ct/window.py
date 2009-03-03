#-*-coding: utf-8-*-
"""Window Class"""

from . import container
from . import application
from . import user

class Window(container.container):
    """Top level window control."""

    def __init__(self, title="Window", size=(-1, -1), pos=(-1, -1),
                 icon=None, parent=None):

        if application.Application.instance == None:
            raise Exception("You must create an application instance first.")

        w, h = size
        x, y = pos

        if w < 0:
            w = user.CW_USEDEFAULT
        if h < 0:
            h = user.CW_USEDEFAULT
        if x < 0:
            x = user.CW_USEDEFAULT
        if y < 0:
            y = user.CW_USEDEFAULT

        classname = application.Application.instance.windowclassname
        container.container.__init__(self, parent, title,
                                     user.WS_OVERLAPPEDWINDOW,
                                     classname, w, h, x, y)

        application.Application.instance._attach_window_(self)


    def _wndproc_(self, handle, message, wparam, lparam):

        if message == user.WM_CLOSE:
            if self.fire('closing'):
                return 0

        elif message == user.WM_SIZE:

            if wparam == user.SIZE_RESTORED:
                self.fire('resized', size=self.size)

            elif wparam == user.SIZE_MINIMIZED:
                self.fire('minimized')

            elif wparam == user.SIZE_MAXIMIZED:
                self.fire('maximized')

        return container.container._wndproc_(self, handle, message, wparam, lparam)

    def show(self, how=''):
        if how == 'normal':
            command = user.SW_SHOWNORMAL

        elif how == 'minimized':
            command = user.SW_SHOWMINIMIZED

        elif how == 'maximized':
            command = user.SW_SHOWMAXIMIZED

        elif how == 'hidden':
            command = user.SW_HIDE

        else:
            command = user.SW_SHOW
        return user.show_window(self, command)

    def update(self):
        return user.update_window(self.handle)

    def set_icon(self, icon, big=False):
        if icon == None: return
        self.__icon = i.load_icon(icon, size=(16, 16))
        if big:
            wparam = user.ICON_BIG
        else:
            wparam = user.ICON_SMALL
        user.send_message(self, u.WM_SETICON, wparam, self.__icon)
