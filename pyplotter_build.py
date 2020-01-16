#!/usr/bin/env python3

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef('''
    void plot(int *** data, int xdepth, int ydepth, int zdepth); 
    void hello();
''')
ffibuilder.set_source("_plotter_cffi",
"""
     #include "plotter.h"
""",
     sources=['plotter.c'],
     libraries=[])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
