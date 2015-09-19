#!/usr/bin/env python
from __future__ import print_function


def secsmall(a, n, k):
    ''' Find k smallest elements '''
    first = second = a[0]
    for i in range(1, n):
        if a[i] < first:
            second = first
            first = a[i]
        elif a[i] < second:
            second = a[i] 
    print("Smallest = ", first, "and Second smallest = ", second )


def main():
    a = [15, 17, 16, 8, 6 , 3, 1]
    secsmall(a, len(a))

if __name__ == "__main__":
    main()
