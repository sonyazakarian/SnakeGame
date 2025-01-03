
import time 
import random


# algorithm 1


def sequential_search(lst):
    # Loop through each element in the list
    for x in lst:
        # Sequentially check for -x in the list
        for y in lst:
            if y == -x:
                return True
    return False

# Test examples
print(sequential_search([3, -4, 7]))    # Output: False
print(sequential_search([5, -7, 6, 3, 7]))  # Output: True
print(sequential_search([1,-1]))
print(sequential_search([1,2]))


# algorithm 2 


def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Algorithm 2: Binary Search on each element
def binary_search_alg(lst):
    for x in lst:
        if binary_search(lst, -x):
            return True
    return False

def two_pointer_search(lst):
    i, j = 0, len(lst) - 1
    while i < j:
        sum_val = lst[i] + lst[j]
        if sum_val == 0:
            return True
        elif sum_val < 0:
            i += 1
        else:
            j -= 1
    return False


# Test examples
print(binary_search([3, -4, 7]))    # Output: False
print(binary_search([5, -7, 6, 3, 7]))  # Output: True
print(binary_search([1,-1]))
print(binary_search([1,2]))

