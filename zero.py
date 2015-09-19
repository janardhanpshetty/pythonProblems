#!/usr/bin/env python
from __future__ import print_function


def czero(a, n):
    ''' Sum of two elements closest to zero '''
    minsum = abs(a[0] + a[1])
    first = a[0]
    second = a[1]
    for i in range(n):
        for j in range(n):
            if abs(a[i] + a[j]) < minsum:
                first = a[i]
                second = a[j]
    print("First element and second element =", first, second)

def main():
    #a = [15, 17, 16, 8, 6 , 3, 1]
    a = [1, 60, -20, 70, -80, 85]
    czero(a, len(a))

if __name__ == "__main__":
    main()
