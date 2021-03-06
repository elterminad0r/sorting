"""
Bubble sort in Python
"""

from sort_util import *

def bubble_sort(l):
    length = sorted_start = len(l)
    made_swap = True
    while made_swap:
        made_swap = False
        for i in range(sorted_start - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                made_swap = True
        sorted_start -= 1

if __name__ == "__main__":
    main(bubble_sort)
