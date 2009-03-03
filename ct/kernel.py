#-*-coding: utf-8-*-

import ctypes

from . import wintypes as wt

def get_module_handle(module_name=None):
    ctypes.windll.kernel32.GetModuleHandleW.restype = wt.hmodule
    return ctypes.windll.kernel32.GetModuleHandleW(module_name)
