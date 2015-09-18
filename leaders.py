#!/usr/bin/env python
from __future__ import print_function


def leader(a, n):
    ''' All elements towards right are less '''
    if n:
        for i in range(n):
            if i == n - 1:
                print(a[i])
                break
            j = i + 1
            if a[i] > a[j]:
                k = j + 1
                flag = 1
                while(k < (n - 1)):
                    if a[i] > a[k]:
                        k += 1
                    else:
                        flag = 0
                        break
                if flag:
                    print(a[i])

def main():
    a = [15, 17, 16, 8, 6 , 3, 1]
    # result leaders are 17, 5 and 2
    leader(a, len(a))

if __name__ == "__main__":
    main()
