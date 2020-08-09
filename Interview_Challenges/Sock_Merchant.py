import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    count = 1
    color = ar[0]

    for i in range(1,n):
        if(ar[i]==color):
            count+=1
        else:
            pairs += int(count/2)
            count = 1
            color= ar[i]
    
    pairs += int(count/2)
            
    return pairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()