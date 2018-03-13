#!/usr/bin/python3

# cache.py - implementation of a cache 

import time

def computation_add(a, b):
    # computation_add() represents a function that does some type of computation
    # I'll add a sleep of 1 second to mimic the time/cost of computation
    print(f'computing {a} + {b}...')
    time.sleep(1)
    return a + b

cache = {}
def add(a, b):
    # add() uses a cache to avoid using the computation_add() function
    if cache.get(a+b):
        return cache[a+b]
    cache[a+b] = computation_add(a, b)
    return cache[a+b]

print(add(4, 5))
print(add(6, 9))
print(add(4, 5))
print(add(1, 9))
print(add(5, 4))
print(add(9, 6))
print(add(0, 3))
print(add(6, 5))
