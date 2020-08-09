#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(a):
    if (len(a) < 2):
        return len(a)
    best = 1
    bestlower = 1
    besthigher = 1
    for i in range(1,len(a)):
        if(a[i] == a[i-1]):
             bestlower = bestlower + 1
             besthigher = besthigher +1
        elif (a[i] - 1 == a[i-1]):
            bestlower = 1 + besthigher
            besthigher = 1
        elif (a[i]+1 == a[i-1]):
            besthigher = 1+bestlower
            bestlower = 1 
        else:
            bestlower = 1
            besthigher = 1
        best = max(best, bestlower , besthigher)
    return best
    # Write your code here
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
