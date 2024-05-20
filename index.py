from __future__ import print_function
from ctypes import *

lib = cdll.LoadLibrary("./main.dll")

lib.CallFn.argtypes = []
lib.CallFn.restype = None

print("lib.CallFn() = %s" % lib.CallFn())
