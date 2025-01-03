

import sys
sys.setrecursionlimit(100000)

import TreeSet
from time import time


def main():
    # Create instances of both trees
    les_mis_tree = TreeSet.TreeSet()
    dutch_words_tree = TreeSet.TreeSet()

    # Scan Les Mis file and add each word to the BST (also time this operation)
    start_time_les_mis = time()
    with open('LesMiserables.txt', 'r') as file:
        for word in file:
            les_mis_tree.add(word)
    stop_time_les_mis = time()

    # Scan Dutch words file and add each word to the BST (also time this operation)
    start_time_dutch_words = time()
    with open('nederlands_short.txt', 'r') as file:
        for word in file:
            dutch_words_tree.add(word)
    stop_time_dutch_words = time()

    # Total time taken to create BSTs for each file
    elapsed_time_les_mis = stop_time_les_mis - start_time_les_mis 
    elapsed_time_dutch_words = stop_time_dutch_words - start_time_dutch_words

    print(elapsed_time_les_mis)
    print(elapsed_time_dutch_words)

    # Values we get: 0.105 seconds for the Les Mis Tree, 14.827 seconds for the Dutch words tree
    # We find that the elapsed time for the Dutch words tree is over 100 times longer than the elapsed time for Les Mis. 
    # This is because the Dutch words tree is sorted alphabetically, so it will create a highly unbalanced tree with height = number of words. 
    # Whereas the Les Mis Tree is unsorted, so it will lead to a more random and even distribution, creating a more balanced and subsequently more efficient tree. 
    # The Big-O notation for the Dutch words tree is O^(n^2), whereas the Big-O notation for the Les Mis tree is O(logn)


if __name__ == '__main__':
    main()

