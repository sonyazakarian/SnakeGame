

"""


Hash tables allow us to search, add, and remove keys and values in expected Constant time O(1)

Is a hash table a map or a set?

keys are distributed "randomly" in a hash table in the sense that we randomly pick a hash function to do the sorting 


For certain actions though where you don't know where the key is that you're looking for, it will take O(n)
because you'll have to go through the whole table, and this could take max "n" because you have n elements of course. 

examples of such actions that would take O(n) runtime:
find the smallest key in the table
find the largest key in the table 
given a key, find the first key less than or equal to that key. 
given a key, find all keys greater than that key. 
etc.

Operations that can be done on a Map or a Set:
min(), max(), floor(), ceiling(), lower(k), higher(k)
min(), max(): This returns the smallest or largest KEY     (why wouldn't it also return the smallest or largest value?)
floor(k): This returns the first key smaller than or equal to k, raises an error if this key doesn't exist
ceiling(k): This returns the first key greater than or equal to k, raises an error if this key doesn't exist 
* floor and ceiling might be mixed up
lower(k), higher(k) : same thing as floor() and ceiling() but doesn't include the equality, strictly less than or greater than

e.g. 

my_set = {(2,'A), (5,'B'), (9, 'C')}
min(my_set) = 2      * not (2, 'A')?

my_set.ceiling(4) = returns first element greater than 4 
my_set.ceiling(
)


our goal is a new ADT where we can slightly compromise the lookup, add, remove time not being O(1) anymore, 
but all these other operations like min(), max(), whatever will be a lot faster

Sorted array seems good, because min and max is O(1) because it's sorted from increasing to decreasing order so you 
just pull the first element for min and last element for max. but add remove will take way too much time 
but the sorted part is really good. we want to keep that because it makes min max easier as well as binary search!

ideal would be some sort of linked structure that is sorted. 

enter the Binary Search Tree 

an ordered/sorted binary tree:
for every node: all the keys in the left subtree of the root are LESS than the root and all the keys of the right subtree are GREATER than the root 

the smallest key in any subtree is the leftmost node 
the largest key is the rightmost node 

try to perform an in order traversal of the tree
inorder traversal is literally just left to right 
nevermind, kind of, its left then root then right
in order traversal of the tree:
5 7 10 15 20 30 35 40 50 


for a map or set: remove, search, or add all require a search in the first place. 
for search is obvious 
for remove you have to search for the key to remove
for add you have to search the ADT to make sure that key isn't already there 

trees are defined recursively 



"""

