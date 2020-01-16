#!/usr/bin/env python3
import sys

from _plotter_cffi import ffi, lib

def main(args):
    # cffi converts bytestrings to char * for us
    lib.hello(b"there");

    # create some numbers
    numbers = ffi.new("int[]", 10)
    # note: NOT ffi.new("int *", 10) -- cffi just ignores the second param and
    # allocates 1 item because WHYYYYYY.
    # And "int[]" gets you a _pointer_ to memory big enough for the number of
    # items given. THANKS CFFI
    for i in range(10):
        numbers[i] = i * 3; # * 3 just for some variation
    lib.numbers(numbers, 10)

    # now to build an equivalent structure to the plotter.c test...
    xdepth = 2
    ydepth = 3
    zdepth = 4
    allocator = ffi.new_allocator(lib.mymalloc, lib.myfree)
    data = allocator("int**[]", xdepth)
    owned_memory = [data] # Needed to avoid freeing memory when the cffi python container goes out of scope
    print(data)
    for i in range(xdepth):
        inner_data = allocator("int*[]", ydepth)
        owned_memory.append(inner_data)
        data[i] = inner_data
        for j in range(ydepth):
            inner_inner_data = allocator("int[]", zdepth)
            owned_memory.append(inner_inner_data)
            data[i][j] = inner_inner_data
            for k in range(zdepth):
                data[i][j][k] = (i * 100) + (j * 10) + (k);
    lib.plot(data, xdepth, ydepth, zdepth)
    print(owned_memory)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
