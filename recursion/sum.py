#!/usr/bin/python3
# returns the sum of all numbers in an array

def summer(arr):
    if arr == []: return 0
    else:         return arr[0] + summer(arr[1:])

print(summer([2, 4, 6])) # => 12
