#This program determines how many valleys a person travels through
#The input is provided as a dingle string where a U represents a rise, and a D represents a fall

#Libraries to import#
import math
import os
import random
import re
import sys
#####################

# Function which counts the Valleys traversed.
def countingValleys(n, s):
    level=valley=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1
    return valley
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
