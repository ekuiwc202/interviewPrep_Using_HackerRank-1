#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    p=arr[-1]
    p1=n-1
    while p1>0 and arr[p1-1] > p:
        arr[p1]=arr[p1-1]
        print(*arr)
        p1 -= 1
    arr[p1]=p
    print(*arr)
      
            
            
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
