#!/usr/bin/env python
from __future__ import print_function


def main():
    ''' Print non-dup item in an array, all other items are repeated twice '''
    arr = [1, 1, 3, 3, 4, 4, 6, 6, 7, 7, 8, 9, 9]
    for i in range(0, len(arr), 2):
        if arr[i] != arr[i+1]:
             print("The dup item = ", arr[i])
             break
 
if __name__ == "__main__":
    main()
