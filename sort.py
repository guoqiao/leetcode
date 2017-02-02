"""
Sorting algorithms.

All ascend(from small to big).
"""

import time


def timeme(func):
    def wrapper(*args, **kwargs):
        start = int(round(time.time() * 1000))
        result = func(*args, **kwargs)
        end = int(round(time.time() * 1000))
        print('{}: {}ms'.format(func.__name__, end - start))
        return result
    return wrapper


def bubble(a):
    """
    Move biggest one to last.

    Full compare and swap.
    """
    n = len(a)
    for i in range(0, n):
        for j in range(1, n-i):
            if a[j-1] > a [j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


def insertion(a):
    """
    Insert current one into previous sorted ones.

    Less compare, full swap.
    """
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
    return a


def selection(a):
    """
    Find biggest one and put into current position.

    Full compare, few swap[at most n-1].
    """
    n = len(a)
    for i in range(0, n-1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[i]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
    return a


if __name__ == '__main__':
    sorts = [bubble, insertion, selection]
    for sort in sorts:
        assert sort([1]) == [1]
        assert sort([2,1]) == [1,2]
        assert sort([9,5,7,4,1]) == [1,4,5,7,9]

        a = list(range(1000, 0, -1))  # worst case
        timeme(sort)(a)
