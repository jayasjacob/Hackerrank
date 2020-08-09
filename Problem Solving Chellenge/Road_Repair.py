import math
import os
import random
import re
import sys


#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY crew_id
#  2. INTEGER_ARRAY job_id
#
def minnode(n, keyval, mstset): 
    mini = 999999999999
    mini_index = None
      
    # Loop through all the values of  
    # the nodes which are not yet  
    # included in MST and find the  
    # minimum valued one. 
    for i in range(n): 
        if (mstset[i] == False and 
            keyval[i] < mini):  
            mini = keyval[i] 
            mini_index = i 
    return mini_index 

def getMinCost(n, city):
    parent = [None] * n 
      
    # Array to store key value  
    # of each node.  
    keyval = [None] * n  
      
    # Boolean Array to hold bool  
    # values whether a node is 
    # included in MST or not.  
    mstset = [None] * n 
      
    # Set all the key values to infinite and  
    # none of the nodes is included in MST. 
    for i in range(n): 
        keyval[i] = 9999999999999
        mstset[i] = False
      
    # Start to find the MST from node 0.  
    # Parent of node 0 is none so set -1.  
    # key value or minimum cost to reach  
    # 0th node from 0th node is 0.  
    parent[0] = -1
    keyval[0] = 0
      
    # Find the rest n-1 nodes of MST. 
    for i in range(n - 1): 
      
        # First find out the minimum node  
        # among the nodes which are not yet  
        # included in MST.  
        u = minnode(n, keyval, mstset)  
      
        # Now the uth node is included in MST.  
        mstset[u] = True
      
        # Update the values of neighbor  
        # nodes of u which are not yet  
        # included in MST.  
        for v in range(n): 
            if (city[u][v] and mstset[v] == False and 
                city[u][v] < keyval[v]):  
                keyval[v] = city[u][v]  
                parent[v] = u 
      
    # Find out the cost by adding  
    # the edge values of MST.  
    cost = 0
    for i in range(1, n): 
        cost += city[parent[i]][i]  
    print(cost) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)

    fptr.write(str(result) + '\n')

    fptr.close()