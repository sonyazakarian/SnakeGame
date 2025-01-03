"""

Sibling nodes - have the same parents

External node - has no children. also called leaf node, or leaf. 

internal node - has children. 

edge - a pair of nodes where 1 is the parent of the other. 

path - any sequence of nodes where any consecutive pair of nodes is a path. 
doesn't have to only go up or only go down, can go up and then down, as long as it follows the previously stated rule 
about any 2 in a row being connected (being a path)

ancestor - a node is an ancestor of another node if it lies on the path from that node to the root node 
descendant - opposite of ancestor
a node is a descendant of another node if that node is its ancestor

node depth - depth of a node is the number of its ancestors (not including itself)

height of a tree - maximum depth of its nodes
e.g. if there is a node that has 5 ancestors, and this is the node with the greatest depth, then the height of the tree is 5

if a tree has just the root node, then its height is 0. 

if a tree is empty, we will say it has a height -1. 

height of a node: thats the height of the subtree rooted at that node. (e.g. that node is the root node of the subtree)
i.e. say that node is the root node of the subtree. then the height of it is the max depth of the nodes in the subtree. 

branching factor of a tree - the max number of children that any node in the tree has 

binary tree - ORDERED tree (wonder why it has to be ordered) with a max of 2 children per each node. 
each node has at most a left child and a right child. (identified as left and right bc its ordered)


trees can be sorted in specific ways. 
e.g. for a specific binary tree, say each left child is less than the right child. 
AND the parent node is greater than left child but less than right child so that:
left child > parent node < right child 
makes it more efficient to search the tree for certain values when you organize it like this 
this is called a BINARY SEARCH TREE!

example of how binary search trees make searching more efficient is in the video, good example
and useful and easy to understand 


------------------------------------------------------------------------------------------------------------------------------

node height = number of descendants
node depth = number of ancestors






"""