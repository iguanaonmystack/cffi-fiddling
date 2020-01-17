#!/usr/bin/env python3

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef('''
    extern char * mystring;
    void plot(int *** data, int xdepth, int ydepth, int zdepth);
    void hello(char * name);
    void numbers(int * data, size_t size);
    void *mymalloc(size_t size);
    void myfree(void *ptr);
''')
ffibuilder.set_source("_plotter_cffi",
"""
    #include "plotter.h"
""",
    sources=['plotter.c'],
    libraries=[])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
