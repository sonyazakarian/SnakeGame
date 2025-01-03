 


"""
A Set is an ADT
you can't have copies in a set
sets are out of order 


Union 
Doubly Linked List


Set A = 11, 22, 33, 46, 82
Set B = 9, 11, 22, 46, 82, 100, 112

Find union of both Sets; all elements of both sets without any duplicates included 

Iterate through second set to check if element is already in first set 
If the element is not present, it gets added to the first set 


We have Set A = 11, 22, 33, 46, 82
Go through Set B and for each one have to decide if it should be added to Set A or not (which all the end will become the Union set)
Set B = 9, 11, 22, 46, 82, 100, 112









9? Yes, because it's not in Set A. 
11? No, because it is already in Set A. 
22? No, because it is already in Set A. 
46? No, because it is already in Set A. 
100? Yes, because it's not in Set A. 
112? Yes, because it's not in Set A. 

Set A becomes = 9, 11, 22, 33, 46, 82, 100, 112

Is this not just O(n)?

It should be O(n^2) where n is the size of each list. Shouldn't you say O(n*m) instead?



Difference between a Map and a Set


map - UNIQUE keys associated with a value

both sets and maps are made up of UNIQUE values. hence you have to traverse the whole thing for an operation.
this makes List ADTS a bad choice for Map or Set, because e.g. for a DLL you have to walk the whole list, O(n), to traverse it to the end. 






Hash the keys [0,5,10,15,...,40] into a table of size 10. 
p = 13, a = 4, b = 8. 




Suppose a hash table has N=11 buckets. 
Hashcodes are compressed using the MAD method, with p=13, a=2, b=3.

Draw the hash table for storing a map with the following entries. 
Assume that the first value in the pair is the hash code for the key k.

(1, A), (4, C), (5, P), (9, L)


hash code meaning just what you input for k in the equation 




What is the maximum number of nodes in a binary tree with height 10?


What is the maximum number of nodes in a binary tree with height 1?
3

What is the maximum number of nodes in a binary tree with height 2?
7

What is the maximum number of nodes in a binary tree with height 3?
15

What is the maximum number of nodes in a binary tree with height 4?

What is the maximum number of nodes in a binary tree with height 5?

What is the maximum number of nodes in a binary tree with height 6?










For each of the following processes, give its runtime complexity 
(assume each process was implemented efficiently, give the average case, not worst case)

1. Appending an element to the end of an ArrayList O(1) 

2. Inserting an element at the beginning of an ArrayList O(n) 

3. Inserting an element at the second-to-last position of a Singly-Linked-List O(n) 

4. Inserting an element at the second-to-last position of a Doubly-Linked-List O(1) 

5. Appending n elements to the end of a Singly-Linked-List O(n^2) 

6. Inserting n elements, each at the beginning of a ArrayList. 
Including time for expansion, assuming that a geometric expansion algorithm is used O(n^2) 

7. Inserting a random value into an AVL tree. O(log n) 

8. Inserting n elements in sorted order into a (non-balanced) Binary Search Tree O(n^2) 

9. Inserting n random elements into a (non-balanced) Binary Search Tree O(n*log n) 

10. Removing n elements from a HashMap O(n) 





balanced tree run time O(logn)





arraylist initialized to capacity 1
(1 space)

1,2,3,4 added to arraylist

1. 
full 
make it bigger 1 _ - then 1 2. 
now copy that 1 2 _ _.

twice 


first answer: 2 


times it expanded so far
4


16

second answer: 4





1 through 4 appended. how many reassignments?
2. (2^2 = 4.)

1 through 16 appended. how many reassignments?
4. (2^4 = 16.)

1 through n appended. how many reassignments?
   (2^? = n).


"""