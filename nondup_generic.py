#!/usr/bin/env python
from __future__ import print_function


def main():
    ''' Print all non-dup items in an array, all other items can repeat many times '''
    arr = [2, 2, 2, 10, 11, 12, 12]
    repeat = 0;
    for i in range(len(arr)):
        if i == len(arr) - 1 and not repeat:
            print("Unique element = ", arr[i])
            break
        if i == len(arr) - 1 and repeat:
           pass
        if i < len(arr) - 1: 
            if arr[i] == arr[i+1]:
                repeat = 1
            else:
                if not repeat:
                    print("Unique element = ", arr[i])
                else:
                    repeat = 0

 
if __name__ == "__main__":
    main()
