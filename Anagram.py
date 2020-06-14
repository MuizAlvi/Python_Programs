import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    from collections import Counter
    count = 0
    if len(s)%2 != 0: 
        return -1
    else:
        s1 = Counter(s[:len(s)//2])
        s2 = Counter(s[len(s)//2:])
        for i in s2:
            comp = s2[i] - s1.get(i,0)
            if comp > 0:
                count += comp
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
