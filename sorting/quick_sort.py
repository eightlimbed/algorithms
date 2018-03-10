#!/usr/bin/python3
# an implementation of quicksort

def quicksort(array):

    # base case:
    if len(array) < 2: return array

    pivot = array[len(array)-1]
    left  = [elem for elem in array[:-1] if elem <= pivot]
    right = [elem for elem in array if elem > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

result = quicksort([1, 5, 6, 55, 923.4, 1239, 349, -239, 28, 28, 28, 120, 9, 423, 42, -33, -1, 9.3, 29, 3, 4])
print(result)
