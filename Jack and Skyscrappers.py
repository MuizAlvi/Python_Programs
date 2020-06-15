import os

def solve(arr):
    arr.append(2**64)
    paths = i = 0
    stack = []
    x = {}
    while i < len(arr):
        if stack == [] or arr[i] <= stack[-1]:
            stack.append(arr[i])
            if arr[i] in x:
                x[arr[i]] += 1
            else:
                x[arr[i]] = 1
            i += 1
        else:
            top = stack.pop()
            if top in x and top < arr[i]:
                paths += x[top] * (x[top] - 1)
                del x[top]
    return paths
