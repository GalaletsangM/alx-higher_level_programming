#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a < 2:
        tuple_a = (0, 0)
    elif tuple_b < 2:
        tuple_b = (0, 0)

    results = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return results
