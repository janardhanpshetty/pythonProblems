#!/usr/bin/env python
from __future__ import print_function


def rotateone(arr, n):
    ''' rotate one element left shift '''
    for i in range(n - 1):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
    return(arr)


def rotate_all(arr, n, d):
    for i in range(d):
        res = rotateone(arr, n)
    return(res)


def main():
    arr = [1, 2, 4, 5, 6, 8]
    n = len(arr)
    d = 3
    # Complexity (n * d)
    print(rotate_all(arr, n, d))

if __name__ == "__main__":
    main()
