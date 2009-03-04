#-*-coding: utf-8-*-
"""Control Class"""

from . import cobject
from . import user
from . import kernel
from . import keys
from . import wintypes as wt

class control(cobject.cobject):
    """Methods an attributes that control native windows."""

    def __init__(self, parent, text, style, classname, w, h, x=0, y=0,
                   menu=None):

        cobject.cobject.__init__(self)

        hinstance = kernel.get_module_handle()
        self.__handle = user.create_window(None, classname, text, style, x, y, w, h,
                                  parent, menu, hinstance, None)

        if self.__handle == None:
            raise Exception("Unable to create control.")

        self.__app_proc = self.subclass_wndproc(self._wndproc_)
        self.__parent = parent
        if parent != None:
            parent.add_child(self)


    def subclass_wndproc(self, routine):
        """Add your own window procedure to the control. Advanced usage only."""
        self.__wndproc = wt.WndProc(routine)
        oldproc = user.set_window_long(self, user.GWL_WNDPROC, self.__wndproc)
        return oldproc

    def _mouseargs_(self, wparam, lparam):
        # Construct parameters for a mouse event from the Windows message
        x = user.loword(lparam)
        y = user.hiword(lparam)
        control = (wparam & user.MK_CONTROL) != 0
        lbutton = (wparam & user.MK_LBUTTON) != 0
        mbutton = (wparam & user.MK_MBUTTON) != 0
        rbutton = (wparam & user.MK_RBUTTON) != 0
        shift = (wparam & user.MK_SHIFT) != 0
        return {'control':control, 'lbutton':lbutton, 'mbutton':mbutton,
                'rbutton':rbutton, 'shift':shift, 'position':cobject.position(x,y)}

    def _wndproc_(self, handle, msg, wparam, lparam):
        # Process messages and dispatch events.
        if handle != self.handle:
            return user.call_window_proc(self.__app_proc, handle, msg, wparam,
                                     lparam)

        if msg == user.WM_DESTROY:
            self.fire('destroyed')

        elif msg == user.WM_MOVE:
            pos = cobject.position(user.loword(lparam), user.hiword(lparam))
            self.fire('position-changed', position=pos)
            return 0

        elif msg == user.WM_SIZE:
            size = cobject.size(user.loword(lparam), user.hiword(lparam))
            self.fire('size-changed', size=size)
            return 0

        elif msg == user.WM_SETFOCUS:
            self.fire('got-focus')
            return 0

        elif msg == user.WM_KILLFOCUS:
            self.fire('lost-focus')
            return 0

        elif msg == user.WM_ENABLE:
            if wparam:
                self.fire('enabled')
            else:
                self.fire('disabled')

        elif msg == user.WM_CHAR:
            char = chr(wparam)
            self.fire('key-character', character=char)

        elif msg == user.WM_KEYDOWN:
            shift, ctrl, alt = keys.get_control_key_states()

            self.fire('key-down', code=wparam, shift=shift, control=ctrl,
                      alt=alt)

        elif msg == user.WM_KEYUP:
            shift, ctrl, alt = keys.get_control_key_states()

            self.fire('key-up', code=wparam, shift=shift, control=ctrl,
                      alt=alt)

        elif msg == user.WM_MOUSEMOVE:
            args = self._mouseargs_(wparam, lparam)

            self.fire('mouse-move', **args)

        elif msg == user.WM_LBUTTONDOWN:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'left'

            self.fire('mouse-down', **args)

        elif msg == user.WM_MBUTTONDOWN:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'middle'

            self.fire('mouse-down', **args)

        elif msg == user.WM_LBUTTONDOWN:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'right'

            self.fire('mouse-down', **args)

        elif msg == user.WM_LBUTTONUP:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'left'

            self.fire('mouse-up', **args)

        elif msg == user.WM_MBUTTONUP:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'middle'

            self.fire('mouse-up', **args)

        elif msg == user.WM_LBUTTONUP:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'right'

            self.fire('mouse-up', **args)

        elif msg == user.WM_LBUTTONDBLCLK:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'left'

            self.fire('mouse-double-click', **args)

        elif msg == user.WM_MBUTTONDBLCLK:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'middle'

            self.fire('mouse-double-click', **args)

        elif msg == user.WM_LBUTTONDBLCLK:
            args = self._mouseargs_(wparam, lparam)
            args['button'] = 'right'

            self.fire('mouse-double-click', **args)

        elif msg == user.WM_MOUSEWHEEL:
            args = self._mouseargs_(wparam, lparam)
            units = wt._short(wparam >> 16).value / 120.0
            if units < 0:
                args['units'] = units * -1
                args['direction'] = 'backward'
            else:
                args['units'] = units
                args['direction'] = 'forward'

            self.fire('mouse-scroll', **args)

        return user.call_window_proc(self.__app_proc, handle, msg, wparam,
                                     lparam)

    def _find_top_level_(self):
        # Find the grandest parent of the control using recursion
        if self.parent == None:
            return self
        else:
            return self.parent._find_top_level_()

    def capture_mouse(self):
        """
           Receive all mouse events regardless of whether the mouse is over the
           control

        """
        return user.set_capture(self)

    @staticmethod
    def release_mouse_capture():
        """Take away mouse capture from which ever control has it."""
        return user.release_capture()

    def has_mouse_capture(self):
        """Return True is the control has mouse capture."""
        return user.get_capture() == self.__handle

    def enable(self, enabling=True):
        """Enable or disable the control."""
        return user.enable_window(self, enabling)

    def focus(self):
        """Grab keyboard focus for the control."""
        return user.set_focus(self)

    def set_text(self, text):
        """Set the text of the control."""
        return user.set_window_text(self, text)

    def get_text(self):
        """Get the text of the control."""
        return user.get_window_text(self)

    def set_size(self, width, height):
        """Set the size of the control in pixels."""
        pos = self.get_position()
        return user.move_window(self, pos.x, pos.y, width, height, True)

    def get_size(self):
        """Return the pixel-size of the control as a named tuple."""
        rect = wt.Rect()
        user.get_window_rect(self, rect)
        return cobject.size(rect.right - rect.left, rect.bottom - rect.top)

    def set_position(self, x, y):
        """Set the position of the control relative to its parent."""
        size = self.get_size()
        user.move_window(self, x, y, size.width, size.height, True)

    def get_position(self):
        """Get the position of the control relative to its parent."""
        rect = wt.Rect()
        point = wt.Point()
        user.get_window_rect(self, rect)
        point.x = rect.left
        point.y = rect.top

        top = self._find_top_level_()
        print(top)
        user.screen_to_client(top, point)
        return cobject.position(point.x, point.y)


    #FIXME use font classes -- need some help on this and fonts in general
    # It even uses an absolute font size! :(
    def _set_font(self, face, size=16):
        lf = ws.LogFont()
        lf.lfFaceName = face
        lf.lfHeight = size
        hfont = g.create_font_indirect(lf)
        return user.send_message(self, u.WM_SETFONT, hfont, 0)

    @property
    def _as_parameter_(self):
        return self.__handle

    @property
    def handle(self):
        return self.__handle

    @property
    def parent(self):
        return self.__parent

    @property
    def size(self):
        return self.get_size()

    @size.setter
    def size(self, value):
        self.set_size(value[0], value[1])

    @property
    def position(self):
        return self.get_position()

    @position.setter
    def position(self, value):
        self.set_position(value[0], value[1])

    @property
    def is_enabled(self):
        return user.is_window_enabled(self)

    @is_enabled.setter
    def is_enabled(self, value):
        self.enable(value)

    @property
    def text(self):
        return self.get_text()

    @text.setter
    def text(self, value):
        self.set_text(value)
