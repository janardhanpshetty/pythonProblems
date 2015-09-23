#!/usr/bin/env python
from __future__ import print_function


def rev(a):
    ''' Reverse of an array '''
    b = []
    for i in range(1, len(a) + 1):
        b.append(a[-i])
    return(b)

def main():
    a = [15, 17, 16, 8, 6 , 3, 1]
    b = rev(a)
    for i in b:
        print(i)

if __name__ == "__main__":
    main()
