#!/usr/bin/env python3
import sys

from _plotter_cffi import ffi, lib

def main(args):
    # use allocator instead of ffi.new, using plotter's debug malloc and free.
    allocator = ffi.new_allocator(lib.mymalloc, lib.myfree)

    # cffi converts bytestrings to char * for us
    lib.hello(b"there");
    print('creating mystring')
    lib.mystring = allocator('char[]', b'beep')
    # (this fails because the object created by ffi.new/allocator instantly gets gc'd, and it owned the memory)
    print('mystring assigned but now it has dud memory')
    my_string_in_python_dont_delete_me = allocator('char[]', b'beep')
    lib.mystring = my_string_in_python_dont_delete_me
    # Okay /now/ mystring has valid memory for the duration of this function
    print('Better!')

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
    owned_memory = [] # Needed to avoid freeing memory when the cffi python container goes out of scope
    print(lib.data)
    for i in range(xdepth):
        inner_data = allocator("int*[]", ydepth)
        owned_memory.append(inner_data)
        lib.data[i] = inner_data
        for j in range(ydepth):
            inner_inner_data = allocator("int[]", zdepth)
            owned_memory.append(inner_inner_data)
            lib.data[i][j] = inner_inner_data
            for k in range(zdepth):
                lib.data[i][j][k] = (i * 100) + (j * 10) + (k);
    lib.plot(xdepth, ydepth, zdepth)
    print(owned_memory)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
