#-*-coding: utf-8-*-
"""Control Class"""

from . import control
from . import user

class container(control.control):
    """Base class for logical container of other controls."""

    def __init__(self, parent, text, style, classname, w, h,
                 x=0, y=0):

        control.control.__init__(self, parent, text, style, classname, w, h, x, y)
        self.__children = []

    def add_child(self, child):
        if self.fire('adding-child', child=control, total=len(self.__children)):
            return False
        self.__children.append(control)
        self.fire('child-added', child=control, total=len(self.__children))
        return True

    def remove_child(self, control):
        if self.fire('removing-child', child=control, total=len(self.__children)):
            return False
        self.__children.remove(control)
        self.fire('child-removed', child=control, total=len(self.__children))
        return False

    def _wndproc_(self, handle, message, wparam, lparam):
        if message == user.WM_COMMAND:
            if lparam != 0:
                child = self._find_(lparam)
                if child != None:
                    child._notify_(user.hiword(wparam))

        return control.control._wndproc_(self, handle, message, wparam, lparam)

    def __iter__(self):
        for child in self.__children:
            yield child

    def __getitem__(self, index):
        return self.__children[index]

    def _find_(self, handle):
        for child in self:
            if child._handle_ == handle:
                return child
        else:
            return None
