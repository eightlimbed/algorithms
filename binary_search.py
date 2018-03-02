#!/usr/bin/python3
# returns the index of item in an array, or None if it's not found.
# arr must be sorted.

def binary_search(arr, item):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] > item:
            hi = mid - 1
        elif arr[mid] < item:
            lo = mid + 1
        else: return mid
    return None

print(binary_search([1, 2, 4, 10, 12, 29, 56], 56))
print(binary_search([1, 2, 4, 10, 12, 29, 56], 7))
