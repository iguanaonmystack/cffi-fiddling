#!/usr/bin/env python3

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef('''
    void plot(int *** data, int xdepth, int ydepth, int zdepth); 
''')
ffibuilder.set_source("_pi_cffi",
"""
     #include "plotter.h"
""",
     libraries=[])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
