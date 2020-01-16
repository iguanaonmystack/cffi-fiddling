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
    


if __name__ == '__main__':
    sys.exit(main(sys.argv))
