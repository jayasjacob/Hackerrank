#!/bin/python3

import math
import os
import random
import re
import sys



class Multiset:

    def __init__(self):
        self.l = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass        #('pass' is a nothing operation. When it execute, nothing happens.)
        return self.l.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass
        if val in self.l:
            return  self.l.remove(val)
    
    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.l:
            return True
        else:
            return False

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.l)

if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()