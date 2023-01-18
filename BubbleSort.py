#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
      numSwaps=0
      k=1
      needNext=True
      while k<len(a) and needNext:
          needNext=False;
          for j in range(len(a)-k):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                numSwaps+=1
                needNext=True
          k+=1
      print(f"Array is sorted in {numSwaps} swaps.")
      print(f"First Element: {a[0]}")
      print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
