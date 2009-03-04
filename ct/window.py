#-*-coding: utf-8-*-
"""Window Class"""

from . import cobject
from . import container
from . import application
from . import user
from . import wintypes as wt

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

    def restore(self):
        self.show('normal')

    def toggle_minimized(self):
        if self.minimized:
            self.restore()
        else:
            self.minimized = True

    def toggle_maximized(self):
        if self.maximized:
            self.restore()
        else:
            self.maximized = True

    def get_position(self):
        rect = wt.Rect()
        user.get_window_rect(self, rect)
        return cobject.position(rect.left, rect.top)

    def reparent(self, new_parent):
        if self.parent == new_parent: return
        user.set_parent(self, new_parent)
        if new_parent != None:
            new_parent.add_child(self)
        if self.parent != None:
            self.parent.remove_child(self)
        self._control__parent = new_parent

    @property
    def minimized(self):
        return user.is_iconic(self)

    @minimized.setter
    def minimized(self, value):
        if value:
            self.show('minimized')
        else:
            self.show('restore')

    @property
    def maximized(self):
        return user.is_zoomed(self)

    @maximized.setter
    def maximized(self, value):
        if value:
            self.show('maximized')
        else:
            self.show('restore')
