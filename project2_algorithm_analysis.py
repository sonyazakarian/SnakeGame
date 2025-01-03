


import time
import random
from typing import List

# algorithm 1: sequential search

def sequential_search(lst: List[int]):
    for x in lst:
        for y in lst:
            if y == -x:
                return True
    return False

# algorithm 2: binary search

def binary_search(lst: List[int], target: int):
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

def binary_search_alg(lst: List[int]):
    for x in lst:
        if binary_search(lst, -x):
            return True
    return False

# algorithm 3: two-pointer search

def two_pointer_search(lst: List[int]):
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

# generate a list of POSITIVE integers and sort
# here we know that all algorithms should return false because there will be no matching positive and negative pairs

def generate_positive_list(n):
    lst = random.sample(range(1, 1000000), n)
    random.shuffle(lst)
    lst.sort()
    return lst

# run a function to track the runtime of each algorithm for the random list of positive ints

def time_algorithms_for_false():
    sizes = [5000, 10000, 20000, 40000, 80000]
    results = []

    for n in sizes:
        lst = generate_positive_list(n)
        
        start_time = time.time()
        sequential_search(lst)
        seq_time = time.time() - start_time

        start_time = time.time()
        binary_search_alg(lst)
        bin_time = time.time() - start_time

        start_time = time.time()
        two_pointer_search(lst)
        two_time = time.time() - start_time

        results.append((n, seq_time, bin_time, two_time))

    return results

results = time_algorithms_for_false()


# print table with outputs vs. runtime 

print(f"{'Input Size':<10} {'Sequential Search Time':<25} {'Binary Search Time':<25} {'Two-pointer Time':<25}")
for n, seq_time, bin_time, two_time in results:
    print(f"{n:<10} {seq_time:<25.5f} {bin_time:<25.5f} {two_time:<25.5f}")

# testing code for random cases
print(sequential_search([-7,7]))
print(binary_search_alg([1,1,2,3,4,-4]))
print(binary_search_alg([1,1,2,3,4]))
print(two_pointer_search([1,1,2,3,4]))
print(two_pointer_search([-7,7]))

