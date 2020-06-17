#!/bin/python3

import os
import sys

def rotate_clock(x, y, z):
    return [[1, x - y, z + x + y], [0, 0, -1], [0, 1, 0],]

def rotate_anticlock(x, y, z):
    return [[1, z + x + y, -x + y], [0, 0, 1],[0, -1, 0],]

def matrix_multiply(a, b):
    c = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c

def multiply_anticlock(x, y, z, a):
    return [[a[0][i] + (z + x + y) * a[1][i] + (-x + y) * a[2][i] for i in range(3)], [a[2][i] for i in range(3)], [-a[1][i] for i in range(3)]]

def multiply_clock(x, y, k, a):
    return [[a[0][i] + (x - y) * a[1][i] + (k + x + y) * a[2][i] for i in range(3)], [-a[2][i] for i in range(3)], [a[1][i] for i in range(3)]]

#
# Complete the kingRichardKnights function below.
#
def kingRichardKnights(n, cmd, knights):
    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    n_cmd = []
    for count, c in enumerate(cmd):
        m = matrix_multiply([[1, c[0], c[1]]], identity)
        new_cmd = [m[0][1], m[0][2], c[2]]
        if (count % 4) == 1:
            new_cmd[0] -= c[2]
        elif (count % 4) == 2:
            new_cmd[0] -= c[2]
            new_cmd[1] -= c[2]
        elif (count % 4) == 3:
            new_cmd[1] -= c[2]
        n_cmd.append(new_cmd)
        identity = multiply_anticlock(c[0], c[1], c[2], identity)
    
    temp = {}
    for k in knights:
        i, j = (k // n) + 1, (k % n) + 1
        l = -1
        r = len(n_cmd)
        while r - l > 1:
            s = (l + r) // 2
            x, y, k = n_cmd[s]
            if (x <= i <= x + k and y <= j <= y + k):
                l = s
            else:
                r = s
        temp.setdefault(l, [])
        temp[l].append((i, j))
    answer = { k: k for k in temp.get(-1, [])}

    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1],]
    for count, c in enumerate(n_cmd):
        identity = multiply_clock(c[0], c[1], c[2], identity)
        for k in temp.get(count, []):
            m = matrix_multiply([[1, k[0], k[1]]], identity)
            answer[k] = [m[0][1], m[0][2]]

    result = []
    for k in knights:
        result.append(answer[(k // n) + 1, (k % n) + 1])
    return result

if __name__ == '__main__':

    # import sys
    # sys.stdin = open('input', 'r')

    n = 7
    s = 4

    cmd = [(1, 2, 4), (2, 3, 3), (3, 4, 1), (3, 4, 0)]
    knights = [0, 6, 9, 11, 24, 25, 48]

    
    print (kingRichardKnights(n, cmd, knights))
