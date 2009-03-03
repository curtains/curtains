#-*-coding: utf-8-*-
"""Proxy of Win32 WinUser functions and constants."""

import sys
import ctypes

from . import wintypes as wt

ver = sys.getwindowsversion()[2]

# Macro Implementations
def hiword(lparam):
    return wt._short(lparam >> 16).value

def loword(lparam):
    return wt._short(lparam & 65535).value

# Function implementations

def call_window_proc(wndproc, hwnd, msg, wparam, lparam):
    ctypes.windll.user32.CallWindowProcW.restype = wt.lresult
    return ctypes.windll.user32.CallWindowProcW(wndproc, hwnd, msg,
                                                wparam, lparam)

def create_window(*args):
    ctypes.windll.user32.CreateWindowExW.restype = wt.hwnd
    return ctypes.windll.user32.CreateWindowExW(*args)

def dispatch_message(msg):
    ctypes.windll.user32.DispatchMessageW.restype = wt.lresult
    return ctypes.windll.user32.DispatchMessageW(ctypes.pointer(msg))

def def_window_proc(handle, message, wparam, lparam):
    ctypes.windll.user32.DefWindowProcW.restype = ctypes.c_long
    return ctypes.windll.user32.DefWindowProcW(handle, message, wparam, lparam)

def destroy_icon(icon):
    ctypes.windll.user32.DestroyIconW.restype = wt._bool
    return ctypes.windll.user32.DestroyIconW(icon)

def destroy_cursor(cursor):
    ctypes.windll.user32.DestroyCursorW.restype = wt._bool
    return ctypes.windll.user32.DestroyCursorW(cursor)

def enable_window(hwnd, enable):
    ctypes.windll.user32.EnableWindow.restype = wt._bool
    return ctypes.windll.user32.EnableWindow(hwnd, enable)

def get_capture():
    ctypes.windll.user32.GetCapture.restype = wt.hwnd
    return ctypes.windll.user32.GetCapture()

def get_client_rect(hwnd, rect):
    ctypes.windll.user32.GetWindowRect.restype = wt._bool
    return ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))

def get_message(msg, hwnd, filter_min, filter_max):
    ctypes.windll.user32.GetMessageW.restype = wt._bool
    return ctypes.windll.user32.GetMessageW(ctypes.byref(msg), hwnd, filter_min,
                                            filter_max)

def get_key_state(virtual_key):
    ctypes.windll.user32.GetKeyState.restype = wt._short
    return ctypes.windll.user32.GetKeyState(virtual_key)

def get_window_rect(hwnd, rect):
    ctypes.windll.user32.GetWindowRect.restype = wt._bool
    return ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))

def get_window_text(hwnd):
    max_count = get_window_text_length(hwnd) + 1 # For the null character.
    buffer = ctypes.create_unicode_buffer(max_count)
    ctypes.windll.user32.GetWindowTextW(hwnd, buffer, max_count)
    return ctypes.wstring_at(buffer)

def get_window_text_length(hwnd):
    return ctypes.windll.user32.GetWindowTextLengthW(hwnd)

def is_iconic(hwnd):
    ctypes.windll.user32.IsIconic.restype = wt._bool
    return ctypes.windll.user32.IsIconic(hwnd) != 0

def is_window_enabled(hwnd):
    ctypes.windll.user32.IsWindowEnabled.restype = wt._bool
    return ctypes.windll.user32.IsWindowEnabled(hwnd) != 0

def is_zoomed(hwnd):
    ctypes.windll.user32.IsZoomed.restype = wt._bool
    return ctypes.windll.user32.IsZoomed(hwnd) != 0

def load_image(*args):
    ctypes.windll.user32.LoadImageW.restype = wt.handle
    return ctypes.windll.user32.LoadImageW(*args)

def move_window(hwnd, x, y, w, h, repaint):
    ctypes.windll.user32.MoveWindow.restype = wt._bool
    return ctypes.windll.user32.MoveWindow(hwnd, x, y, w, h, repaint)

def peek_message(msg, hwnd, filter_min, filter_max):
    ctypes.windll.user32.PeekMessageW.restype = wt._bool
    return ctypes.windll.user32.PeekMessageW(ctypes.byref(msg), hwnd, filter_min,
                                            filter_max)

def post_quit_message(code):
    ctypes.windll.user32.PostQuitMessage(code)

def register_class(wndclassex):
    ctypes.windll.user32.RegisterClassExW.restype = wt.atom
    return ctypes.windll.user32.RegisterClassExW(ctypes.byref(wndclassex))

def release_capture():
    ctypes.windll.user32.ReleaseCapture.restype = wt._bool
    return ctypes.windll.user32.ReleaseCapture

def screen_to_client(hwnd, point):
    ctypes.windll.user32.ScreenToClient.restype = wt._bool
    return ctypes.windll.user32.ScreenToClient(hwnd, ctypes.byref(point))

def send_message(hwnd, message, wparam, lparam):
    ctypes.windll.user32.SendMessageW.restype = wt.lresult
    return ctypes.windll.user32.SendMessageW(hwnd, message, wparam, lparam)

def set_capture(hwnd):
    ctypes.windll.user32.SetCapture.restype = wt.hwnd
    return ctypes.windll.user32.SetCapture(hwnd)

def set_focus(hwnd):
    ctypes.windll.user32.SetFocus.restype = wt.hwnd
    return ctypes.windll.user32.SetFocus(hwnd)

def set_parent(child, parent):
    ctypes.windll.user32.SetParent.restype = wt.hwnd
    return ctypes.windll.user32.SetParent(child, parent)

def set_window_long(hwnd, index, new_long):
    ctypes.windll.user32.SetWindowLongW.restype = wt._long
    return ctypes.windll.user32.SetWindowLongW(hwnd, index, new_long)

def set_window_text(hwnd, string):
    ctypes.windll.user32.SetWindowTextW.restype = wt._bool
    return ctypes.windll.user32.SetWindowTextW(hwnd, string)

def show_window(handle, command):
    ctypes.windll.user32.ShowWindow.argtypes = [wt.hwnd, wt._int]
    ctypes.windll.user32.ShowWindow.restype = wt._bool
    return ctypes.windll.user32.ShowWindow(handle, command)

def translate_message(msg):
    ctypes.windll.user32.TranslateMessage.restype = wt._bool
    return ctypes.windll.user32.TranslateMessage(ctypes.pointer(msg))

def update_window(handle):
    ctypes.windll.user32.UpdateWindow(handle)


#----Class Styles----
CS_VREDRAW          = 0x0001
CS_HREDRAW          = 0x0002
CS_DBLCLKS          = 0x0008
CS_OWNDC            = 0x0020
CS_CLASSDC          = 0x0040
CS_PARENTDC         = 0x0080
CS_NOCLOSE          = 0x0200
CS_SAVEBITS         = 0x0800
CS_BYTEALIGNCLIENT  = 0x1000
CS_BYTEALIGNWINDOW  = 0x2000
CS_GLOBALCLASS      = 0x4000

CS_IME              = 0x00010000
CS_DROPSHADOW       = 0x00020000
#----End Class Styles----

#----OEM Resources----
OBM_CLOSE           = wt.ushort(32754)
OBM_UPARROW         = wt.ushort(32753)
OBM_DNARROW         = wt.ushort(32752)
OBM_RGARROW         = wt.ushort(32751)
OBM_LFARROW         = wt.ushort(32750)
OBM_REDUCE          = wt.ushort(32749)
OBM_ZOOM            = wt.ushort(32748)
OBM_RESTORE         = wt.ushort(32747)
OBM_REDUCED         = wt.ushort(32746)
OBM_ZOOMD           = wt.ushort(32745)
OBM_RESTORED        = wt.ushort(32744)
OBM_UPARROWD        = wt.ushort(32743)
OBM_DNARROWD        = wt.ushort(32742)
OBM_RGARROWD        = wt.ushort(32741)
OBM_LFARROWD        = wt.ushort(32740)
OBM_MNARROW         = wt.ushort(32739)
OBM_COMBO           = wt.ushort(32738)
OBM_UPARROWI        = wt.ushort(32737)
OBM_DNARROWI        = wt.ushort(32736)
OBM_RGARROWI        = wt.ushort(32735)
OBM_LFARROWI        = wt.ushort(32734)

OBM_OLD_CLOSE       = wt.ushort(32767)
OBM_SIZE            = wt.ushort(32766)
OBM_OLD_UPARROW     = wt.ushort(32765)
OBM_OLD_DNARROW     = wt.ushort(32764)
OBM_OLD_RGARROW     = wt.ushort(32763)
OBM_OLD_LFARROW     = wt.ushort(32762)
OBM_BTSIZE          = wt.ushort(32761)
OBM_CHECK           = wt.ushort(32760)
OBM_CHECKBOXES      = wt.ushort(32759)
OBM_BTNCORNERS      = wt.ushort(32758)
OBM_OLD_REDUCE      = wt.ushort(32757)
OBM_OLD_ZOOM        = wt.ushort(32756)
OBM_OLD_RESTORE     = wt.ushort(32755)


OCR_NORMAL          = wt.ushort(32512)
OCR_IBEAM           = wt.ushort(32513)
OCR_WAIT            = wt.ushort(32514)
OCR_CROSS           = wt.ushort(32515)
OCR_UP              = wt.ushort(32516)
OCR_SIZENWSE        = wt.ushort(32642)
OCR_SIZENESW        = wt.ushort(32643)
OCR_SIZEWE          = wt.ushort(32644)
OCR_SIZENS          = wt.ushort(32645)
OCR_SIZEALL         = wt.ushort(32646)
OCR_NO              = wt.ushort(32648)
OCR_HAND            = wt.ushort(32649)
OCR_APPSTARTING     = wt.ushort(32650)


OIC_SAMPLE          = wt.ushort(32512)
OIC_HAND            = wt.ushort(32513)
OIC_QUES            = wt.ushort(32514)
OIC_BANG            = wt.ushort(32515)
OIC_NOTE            = wt.ushort(32516)
OIC_WINLOGO         = wt.ushort(32517)
OIC_WARNING         = OIC_BANG
OIC_ERROR           = OIC_HAND
OIC_INFORMATION     = OIC_NOTE
if ver >= 6000:
    OIC_SHIELD      = wt.ushort(32518)

IMAGE_BITMAP        = 0
IMAGE_ICON          = 1
IMAGE_CURSOR        = 2
IMAGE_ENHMETAFILE   = 3

LR_DEFAULTCOLOR     = 0x00000000
LR_MONOCHROME       = 0x00000001
LR_COLOR            = 0x00000002
LR_COPYRETURNORG    = 0x00000004
LR_COPYDELETEORG    = 0x00000008
LR_LOADFROMFILE     = 0x00000010
LR_LOADTRANSPARENT  = 0x00000020
LR_DEFAULTSIZE      = 0x00000040
LR_VGACOLOR         = 0x00000080
LR_LOADMAP3DCOLORS  = 0x00001000
LR_CREATEDIBSECTION = 0x00002000
LR_COPYFROMRESOURCE = 0x00004000
LR_SHARED           = 0x00008000
#----End OEM Resources----

#----Window styles----
WS_OVERLAPPED       = 0x00000000
WS_POPUP            = 0x80000000
WS_CHILD            = 0x40000000
WS_MINIMIZE         = 0x20000000
WS_VISIBLE          = 0x10000000
WS_DISABLED         = 0x08000000
WS_CLIPSIBLINGS     = 0x04000000
WS_CLIPCHILDREN     = 0x02000000
WS_MAXIMIZE         = 0x01000000
WS_CAPTION          = 0x00C00000
WS_BORDER           = 0x00800000
WS_DLGFRAME         = 0x00400000
WS_VSCROLL          = 0x00200000
WS_HSCROLL          = 0x00100000
WS_SYSMENU          = 0x00080000
WS_THICKFRAME       = 0x00040000
WS_GROUP            = 0x00020000
WS_TABSTOP          = 0x00010000

WS_MINIMIZEBOX      = 0x00020000
WS_MAXIMIZEBOX      = 0x00010000

WS_OVERLAPPEDWINDOW = (WS_OVERLAPPED     | \
                       WS_CAPTION        | \
                       WS_SYSMENU        | \
                       WS_THICKFRAME     | \
                       WS_MINIMIZEBOX    | \
                       WS_MAXIMIZEBOX)

WS_TILED            = WS_OVERLAPPED
WS_ICONIC           = WS_MINIMIZE
WS_SIZEBOX          = WS_THICKFRAME
WS_TILEDWINDOW      = WS_OVERLAPPEDWINDOW

WS_POPUPWINDOW      = (WS_POPUP          | \
                       WS_BORDER         | \
                       WS_SYSMENU)

WS_CHILDWINDOW      = (WS_CHILD)
#----End Window Styles----

#-------------Button Styles-------------
BS_PUSHBUTTON = 0x00000000
BS_DEFPUSHBUTTON = 0x00000001
BS_CHECKBOX = 0x00000002
BS_AUTOCHECKBOX = 0x00000003
BS_RADIOBUTTON = 0x00000004
BS_3STATE = 0x00000005
BS_AUTO3STATE = 0x00000006
BS_GROUPBOX = 0x00000007
BS_USERBUTTON = 0x00000008
BS_AUTORADIOBUTTON = 0x00000009
BS_PUSHBOX = 0x0000000A
BS_OWNERDRAW = 0x0000000B
BS_TYPEMASK = 0x0000000F
BS_LEFTTEXT = 0x00000020
BS_TEXT = 0x00000000
BS_ICON = 0x00000040
BS_BITMAP = 0x00000080
BS_LEFT = 0x00000100
BS_RIGHT = 0x00000200
BS_CENTER = 0x00000300
BS_TOP = 0x00000400
BS_BOTTOM = 0x00000800
BS_VCENTER = 0x00000C00
BS_PUSHLIKE = 0x00001000
BS_MULTILINE = 0x00002000
BS_NOTIFY = 0x00004000
BS_FLAT = 0x00008000
BS_RIGHTBUTTON = BS_LEFTTEXT
BS_SPLITBUTTON = 0x0000000C
BS_DEFSPLITBUTTON = 0x0000000D
BS_COMMANDLINK = 0x0000000E
BS_DEFCOMMANDLINK = 0x0000000F
#-------------End Button Style---------
#--------Button Notify-----------
BN_CLICKED = 0
BN_PAINT = 1
BN_DISABLE = 4
BN_DOUBLECLICKED = 5
BN_SETFOCUS = 6
BN_KILLFOCUS = 7
#-------End Button Notify---------

#----Extended Window Styles----
WS_EX_DLGMODALFRAME     = 0x00000001
WS_EX_NOPARENTNOTIFY    = 0x00000004
WS_EX_TOPMOST           = 0x00000008
WS_EX_ACCEPTFILES       = 0x00000010
WS_EX_TRANSPARENT       = 0x00000020
WS_EX_MDICHILD          = 0x00000040
WS_EX_TOOLWINDOW        = 0x00000080
WS_EX_WINDOWEDGE        = 0x00000100
WS_EX_CLIENTEDGE        = 0x00000200
WS_EX_CONTEXTHELP       = 0x00000400
WS_EX_RIGHT             = 0x00001000
WS_EX_LEFT              = 0x00000000
WS_EX_RTLREADING        = 0x00002000
WS_EX_LTRREADING        = 0x00000000
WS_EX_LEFTSCROLLBAR     = 0x00004000
WS_EX_RIGHTSCROLLBAR    = 0x00000000

WS_EX_CONTROLPARENT     = 0x00010000
WS_EX_STATICEDGE        = 0x00020000
WS_EX_APPWINDOW         = 0x00040000


WS_EX_OVERLAPPEDWINDOW  = (WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE)
WS_EX_PALETTEWINDOW     = (WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST)
WS_EX_LAYERED           = 0x00080000


WS_EX_NOINHERITLAYOUT   = 0x00100000
WS_EX_LAYOUTRTL         = 0x00400000
WS_EX_COMPOSITED        = 0x02000000
WS_EX_NOACTIVATE        = 0x08000000
#----End Extended Window Styles----

#--------------------colors---------------------
COLOR_SCROLLBAR         =0
COLOR_BACKGROUND        =1
COLOR_ACTIVECAPTION     =2
COLOR_INACTIVECAPTION   =3
COLOR_MENU              =4
COLOR_WINDOW            =5
COLOR_WINDOWFRAME       =6
COLOR_MENUTEXT          =7
COLOR_WINDOWTEXT        =8
COLOR_CAPTIONTEXT       =9
COLOR_ACTIVEBORDER      =10
COLOR_INACTIVEBORDER    =11
COLOR_APPWORKSPACE      =12
COLOR_HIGHLIGHT         =13
COLOR_HIGHLIGHTTEXT     =14
COLOR_BTNFACE           =15
COLOR_BTNSHADOW         =16
COLOR_GRAYTEXT          =17
COLOR_BTNTEXT           =18
COLOR_INACTIVECAPTIONTEXT =19
COLOR_BTNHIGHLIGHT      =20

COLOR_3DDKSHADOW        =21
COLOR_3DLIGHT           =22
COLOR_INFOTEXT          =23
COLOR_INFOBK            =24

COLOR_HOTLIGHT          =26
COLOR_GRADIENTACTIVECAPTION =27
COLOR_GRADIENTINACTIVECAPTION =28
COLOR_MENUHILIGHT       =29
COLOR_MENUBAR           =30

COLOR_DESKTOP           =COLOR_BACKGROUND
COLOR_3DFACE            =COLOR_BTNFACE
COLOR_3DSHADOW          =COLOR_BTNSHADOW
COLOR_3DHIGHLIGHT       =COLOR_BTNHIGHLIGHT
COLOR_3DHILIGHT         =COLOR_BTNHIGHLIGHT
COLOR_BTNHILIGHT        =COLOR_BTNHIGHLIGHT
#-------------------End colors--------------------

#----CreateWindow Flags----
CW_USEDEFAULT       =  0x80000000
#----End CreateWindow----

#-----(Get|Set)WindowLong---------
GWL_WNDPROC = -4
GWL_HINSTANCE = (-6)
GWL_HWNDPARENT = (-8)
GWL_STYLE = (-16)
GWL_EXSTYLE = (-20)
GWL_USERDATA = (-21)
GWL_ID = (-12)
#--------------------------------

#----ShowWindow Flags----
SW_HIDE             = 0
SW_SHOWNORMAL       = 1
SW_NORMAL           = 1
SW_SHOWMINIMIZED    = 2
SW_SHOWMAXIMIZED    = 3
SW_MAXIMIZE         = 3
SW_SHOWNOACTIVATE   = 4
SW_SHOW             = 5
SW_MINIMIZE         = 6
SW_SHOWMINNOACTIVE  = 7
SW_SHOWNA           = 8
SW_RESTORE          = 9
SW_SHOWDEFAULT      = 10
SW_FORCEMINIMIZE    = 11
SW_MAX              = 11

#----WM_SHOWWINDOW Message----
SW_PARENTCLOSING    = 1
SW_OTHERZOOM        = 2
SW_PARENTOPENING    = 3
SW_OTHERUNZOOM      = 4
#----End ShowWindow----

#----WM_SIZE wParams-------
SIZE_RESTORED       = 0
SIZE_MINIMIZED      = 1
SIZE_MAXIMIZED      = 2
SIZE_MAXSHOW        = 3
SIZE_MAXHIDE        = 4
#-----End WM_SIZE-----------

#----WM_SETICON params------
ICON_SMALL = 0
ICON_BIG = 1
#-----End WM_SETICON--------

#-----Bit masks for mouse messages----
MK_LBUTTON = 0x0001
MK_RBUTTON = 0x0002
MK_SHIFT = 0x0004
MK_CONTROL = 0x0008
MK_MBUTTON = 0x0010
MK_XBUTTON1 = 0x0020
MK_XBUTTON2 = 0x0040
#------End mouse messages------------

#-----Window Messages------
WM_NULL = 0x0000
WM_CREATE = 0x0001
WM_DESTROY = 0x0002
WM_MOVE = 0x0003
WM_SIZE = 0x0005
WM_ACTIVATE = 0x0006
WM_SETFOCUS = 0x0007
WM_KILLFOCUS = 0x0008
WM_ENABLE = 0x000A
WM_CLOSE = 0x0010
WM_SETICON = 0x0080
WM_SETFONT = 0x0030
WM_COMMAND = 0x0111
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_CHAR = 0x0102
WM_DEADCHAR = 0x0103
WM_MOUSEMOVE = 0x0200
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
WM_LBUTTONDBLCLK = 0x0203
WM_RBUTTONDOWN = 0x0204
WM_RBUTTONUP = 0x0205
WM_RBUTTONDBLCLK = 0x0206
WM_MBUTTONDOWN = 0x0207
WM_MBUTTONUP = 0x0208
WM_MBUTTONDBLCLK = 0x0209
WM_MOUSEWHEEL = 0x020A
WM_MOUSEHWHEEL = 0x020E
