import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    j = 0
    end = n-1
    while i < end:
        if (i+2 <= end) and (c[i+2] == 0):
            i += 2
            j += 1 
        elif c[i+1] == 0:
            i += 1
            j += 1
    return j

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
