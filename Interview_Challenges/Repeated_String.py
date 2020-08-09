import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    c = s.count('a')
    div=n//len(s)
    if n%len(s)==0:
        c= c*div
    else:
        m = n%len(s)
        c= c*div+s[:m].count('a')
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()