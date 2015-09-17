#!/usr/bin/env python
from __future__ import print_function


def main():
    ''' Print all non-dup items in an array, all other items can repeat many times '''
    arr = [2, 2, 2, 2, 3, 4, 4, 5, 7, 7, 7, 8, 9, 9, 9, 9, 10, 11]
    repeat = 0;
    for i in range(len(arr)):
        if i == len(arr) - 1 and repeat == 0 :
            print("Unique element = ", arr[i])
            break
        if arr[i] == arr[i+1]:
            repeat = 1
        else:
            if not repeat:
                print("Unique element = ", arr[i])
            else:
                repeat = 0
            
 
if __name__ == "__main__":
    main()
