#!/usr/bin/python3
# returns the maximum number in an array

def maximum(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]: return arr[0]
        else: return arr[1]
    else:
        temp_max = maximum(arr[1:])
        if arr[0] > temp_max: return arr[0]
        else: return temp_max

print(maximum([2, 8, 3, 4, 1, 0, -9, 42, 3, 333, 54.3, -1823]))
