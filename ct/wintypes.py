#-*-coding:utf-8-*-
"""Proxy of Windows Data types."""

import ctypes

__win64 = False

# Primaries

_bool = ctypes.c_int
byte = ctypes.c_ubyte
char = ctypes.c_char
callback = ctypes.WINFUNCTYPE
dword = ctypes.c_uint32
dword32 = ctypes.c_uint32
dword64 = ctypes.c_uint64
float = ctypes.c_float

if __win64:
    half_ptr = ctypes.c_int
else:
    half_ptr = ctypes.c_short

handle = ctypes.c_void_p
_int = ctypes.c_int

if __win64:
    int_ptr = ctypes.c_int64
else:
    int_ptr = ctypes.c_int

int64 = ctypes.c_int64
_long = ctypes.c_long

if __win64:
    longlong = ctypes.c_int64
else:
    longlong = ctypes.c_double

if __win64:
    long_ptr = ctypes.c_int64
else:
    long_ptr = ctypes.c_long

long32 = ctypes.c_int32
long64 = ctypes.c_int64

lpcstr = ctypes.c_char_p
lpcvoid = ctypes.c_void_p
lpcwstr = ctypes.c_wchar_p

lpstr = lpcstr
lpvoid = lpcvoid
lpwstr = lpcwstr

pchar = ctypes.c_char_p

_short = ctypes.c_short

struct = ctypes.Structure
union = ctypes.Union

uchar = ctypes.c_ubyte
uint = ctypes.c_uint

if __win64:
    uint_ptr = ctypes.c_uint64
else:
    uint_ptr = ctypes.c_uint

uint32 = ctypes.c_uint
uint64 = ctypes.c_uint64

ulong = ctypes.c_ulong
ulonglong = ctypes.c_ulonglong

if __win64:
    ulong_ptr = ctypes.c_uint64
else:
    ulong_ptr = ctypes.c_ulong

ulong32 = ctypes.c_uint
ulong64 = ctypes.c_uint64
ushort = ctypes.c_ushort

wchar = ctypes.c_wchar
word = ctypes.c_ushort

winapi = ctypes.WINFUNCTYPE


# Secondaries
atom = word
boolean = byte
colorref = dword
dwordlong = ulonglong
dword_ptr = ulong_ptr

haccel = handle
hbitmap = handle
hbrush = handle
hcolorspace = handle
hconv = handle
hconvlist = handle
hcursor = handle
hdc = handle
hddedata = handle
hdesk = handle
hdrop = handle
hdwp = handle
henhmetafile = handle
hfile = handle
hfont = handle
hgdiobj = handle
hglobal = handle
hhook = handle
hicon = handle
hinstance = handle
hkey = handle
hkl = handle
hlocal = handle
hmenu = handle
hmetafile = handle
hmodule = hinstance
hmonitor = handle
hpalette = handle
hpen = handle
hresult = handle
hrgn = handle
hsz = handle
hwinsta = handle
hwnd = handle

langid = word
lcid = dword
lctype = dword
lgrpid = dword

lparam = long_ptr
lresult = long_ptr

usn = longlong

wparam = uint_ptr

# Callbacks
WndProc = callback(lresult, hwnd, uint, wparam, lparam)

#structs
class WndClassEx(struct):
    _fields_ = [('cbSize', uint),
                ('style', uint),
                ('lpfnWndProc', WndProc),
                ('cbClsExtra', _int),
                ('cbWndExtra', _int),
                ('hInstance', hinstance),
                ('hIcon', hicon),
                ('hCursor', hcursor),
                ('hbrBackground', hbrush),
                ('lpszMenuName', lpcwstr),
                ('lpszClassName', lpcwstr),
                ('hIconSm', hicon)]

class Point(struct):
    _fields_ = [('x', _long),
                ('y', _long)]

class Rect(struct):
    _fields_ = [('left', _long),
                ('top', _long),
                ('right', _long),
                ('bottom', _long)]

class Msg(struct):
    _fields_ = [('hwnd', hwnd),
                ('message', uint),
                ('wParam', wparam),
                ('lParam', lparam),
                ('time', dword),
                ('pt', Point)]

class PaintStruct(struct):
    _fields_ = [('hdc', hdc),
                ('fErase', _bool),
                ('rcPaint', Rect),
                ('fRestore', _bool),
                ('fIncUpdate', _bool),
                ('rgbReserved', byte * 32)]

class CreateStruct(struct):
    _fields_ = [('lpCreateParams', lpvoid),
                ('hInstance', hinstance),
                ('hMenu', hmenu),
                ('hwndParent', hwnd),
                ('cy', _int),
                ('cx', _int),
                ('y', _int),
                ('x', _int),
                ('style', _long),
                ('lpszName', lpcwstr),
                ('lpszClass', lpcwstr),
                ('dwExStyle', dword)]

class LogFont(struct):
    _fields_ = [('lfHeight', _long),
                ('lfWidth', _long),
                ('lfEscapement', _long),
                ('lfOrientation', _long),
                ('lfWeight', _long),
                ('lfItalic', byte),
                ('lfUnderline', byte),
                ('lfStikeOut', byte),
                ('lfCharSet', byte),
                ('lfOutPrecision', byte),
                ('lfClipPecision', byte),
                ('lfPitchAndFamily', byte),
                ('lfFaceName', ctypes.c_wchar * 32)]


