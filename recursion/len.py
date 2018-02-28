#!/usr/bin/python3
# returns the number of elements in an array

def size(arr):
    if arr == []: return 0
    else:         return 1 + size(arr[1:])

print(size([2, 4, 6, 8, 10, 12])) # => 6
