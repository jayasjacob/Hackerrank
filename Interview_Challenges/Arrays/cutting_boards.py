import math
import os
import random
import re
import sys


# Complete the boardCutting function below.
def boardCutting(cost_y, cost_x):
    m=len(cost_y)-1
    n=len(cost_x)-1
    cost_y.sort(reverse=True)
    cost_x.sort(reverse=True)
    xSeg=1
    ySeg=1
    i=0
    j=0
    cost=0
    temp=0
    while(xSeg<=m+1 and ySeg<=n+1):
        if i<=m and j<=n:
            if cost_y[i]>=cost_x[j] :
                temp=cost_y[i]*ySeg
                cost+=temp
                xSeg+=1
                i+=1
            else:
                if j<=n:
                    temp=cost_x[j]*xSeg
                    cost+=temp
                    ySeg+=1
                    j+=1
        if i==m+1:
            while(j<=n):
                temp=cost_x[j]*xSeg
                cost+=temp
                ySeg+=1
                j+=1   
        if j==n+1:
            while(i<=m):
                temp=cost_y[i]*ySeg
                cost+=temp
                xSeg+=1
                i+=1
    return cost%(10**9+7)
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        mn = input().split()

        m = int(mn[0])

        n = int(mn[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close() 