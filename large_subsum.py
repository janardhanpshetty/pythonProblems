#!/usr/bin/env python
from __future__ import print_function


def main(arr):
    ''' To find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum '''
    max_so_far = 0 
    sum_ending_here = 0
    # Traverse each element 
    for i in range(len(arr)):
        sum_ending_here = sum_ending_here + arr[i]
        if sum_ending_here < 0:
            sum_ending_here = 0
        else:
            if sum_ending_here > max_so_far:
                max_so_far = sum_ending_here
            else:
                pass
    return max_so_far
  
if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3 ]
    tsum = main(arr)
    print("The largest subarray sum = ", tsum)
