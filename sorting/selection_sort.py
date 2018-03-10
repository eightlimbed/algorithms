#!/usr/bin/python3


def find_smallest(arr):
    """returns the index of the smallest number in an array"""
    smallest_num = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_idx = i
    return smallest_idx

def selection_sort(arr):
    """returns a sorted array"""
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr

example = [8, 4, 3, 3, 1, 0, 9, 10, 14, 23, 12, 8, 2]
print(find_smallest(example))
print(selection_sort(example))
