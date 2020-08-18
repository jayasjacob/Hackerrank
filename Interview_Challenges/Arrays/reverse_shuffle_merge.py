#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
def reverseShuffleMerge(s):
    left = Counter(s)
    keep = {char: int(freq / 2) for char, freq in left.items()}
    shuffle = {char: int(freq / 2) for char, freq in left.items()}
    result = []
    for char in reversed(s):
        if keep[char] > 0:
            while result and result[-1] > char and shuffle[result[-1]] > 0:
                removed = result.pop()
                keep[removed] += 1
                shuffle[removed] -= 1
            result.append(char)
            keep[char] -= 1
        else:
            shuffle[char] -= 1
    return (''.join(result))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
