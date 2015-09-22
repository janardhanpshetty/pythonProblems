#!/usr/bin/env python
from __future__ import print_function


def main(a, b):
    '''Median of 2 sorted arrays '''
    i = j = k = 0
    result = []
    totlen = len(a) + len(b)
    if totlen == 0:
        return 0
    while len(result) != totlen:
        if len(a) == i:
            result += b[j:]
            break
        elif len(b) == j:
            result += a[i:]
            break
        elif a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    reslen = len(result)
    mid = reslen / 2
    if reslen % 2 != 0:
        return(result[mid])
    else:
        medi = (float(result[mid]) + float(result[mid - 1])) / 2.0
        return(medi)

if __name__ == "__main__":
    #a = [2, 13, 17, 18, 19, 20]
    #b = [1, 5, 7, 9, 26, 38]
    a = [1]
    b = [2]
    res = main(a, b)
    print(res)
