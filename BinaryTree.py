

"""

General Trees
Unlimited number of children per node 

Binary Trees
At most 2 children per node (0, 1, or 2 children)
They are ordered - so there is a "left child" and a "right child"

Binary Search Tree
Specific relationships between left child and right child. 
e.g. 

     5 
  3     8

could say left <= value <= right 

search in O(log2n)

search 1000 elements

Define binary trees:
empty tree 
or
root node with 2 trees as children
(structural recursion)

define linked list:
empty list
or 
node followed by another list


For TreeNode:
Will need something that points to left child, something that points to right child, and something that points to parent 

"""


class TreeNode:

    def __init__(self, value, parent, left, right):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def is_external(self)->bool:
        return self.left == None and self.right == None
    
    def is_internal(self)->bool:
        return not self.is_external()
    
    def is_leaf(self):
        return self.is_external()
    
    def set_value(self, value):
        self.value = value 

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()   # why is this necessary?

    # def ancestors(self):
      #   return self
        # return all of its ancestors
        # does this mean i have to implement a get prev node?
        # does he have office hours tomorrow?

    # def node_depth(self):
       #  return depth of node 

        # implemenet both iteratively and recursiley to he can see btoh ways 


class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0 

    def get_size(self)->int:
        return self.size
    
    def __str__(self):
        return f"Root: {self.root} "  +\
        f"\nLeft child: {self.root.left} " +\
        f"\nRight child: {self.root.right} " +\
        f"\nSize: {self.size} "
    
    def print_tree(self):
        if self.size == 0:
            return '[]'
        return self.print_tree_helper(self, self.root)
    
    def print_tree_helper(self, the_node):
        if the_node is None:
            return 'None'
        if the_node.is_external():
            return str(the_node)
        else:
            return str(the_node) + self.print_tree_helper(the_node.left) + self.print_tree_helper(the_node.right)

    def add_root(self, value):
        if self.root is not None:
            raise IndexError
        self.root = TreeNode(value, None, None, None)
        self.size += 1          # I'm confused how you can do this if we haven't already made a size variable to keep track. we have lol thats your answer  
        return self.root
    
    def add_left(self, parent, value):
        if parent is None:
            raise IndexError
        if parent.left is not None:   # If the parent already has a left child 
            raise IndexError 
        parent.left = TreeNode(value, parent, None, None)
        self.size += 1
        return parent.left

    def add_right(self, parent, value):
        if parent is None:
            raise IndexError
        if parent.right is not None:   # If the parent already has a left child 
            raise IndexError 
        parent.right = TreeNode(value, parent, None, None)
        self.size += 1
        return parent.right 

    # def depth_first_traversal

    # def breadth_first_traversal
    

def main():
    the_tree = BinaryTree()
    the_root = the_tree.add_root(10)
    the_left = the_tree.add_left(the_root, 8)
    the_left_left = the_tree.add_left(the_left, 3)
    the_left_right = the_tree.add_right(the_left, 9)
    the_right = the_tree.add_right(the_root, 15)
    the_right_right = the_tree.add_right(the_right, 23)
    print(the_tree)


"""
    the_tree = BinaryTree()
    the_root = the_tree.add_root(10)
    the_left = the_tree.add_left(the_root, 5)
    # every time you want to add something to your tree have to create a new variable for it
    the_right = the_tree.add_right(the_root, 15)

    left_of_the_first_left = the_tree.add_left(the_left, 20)
    right_of_the_first_left = the_tree.add_right(the_left, 30)

    print(the_tree)
"""

if __name__ == "__main__":
    main()


"""

# preclass 14

from BinaryTree import BinaryTree, TreeNode

my_tree = BinaryTree()
pat = my_tree.add_root("Pat")
chris = my_tree.add_left(pat, "Chris")
sam = my_tree.add_right(pat, "Sam")
jordan = my_tree.add_left(chris, "Jordan")  
# if its a leaf/external node (has no children), you dont really need to save it as a variable because 
# you won't need to access it again. but there's also no harm in saving it 
casey = my_tree.add_right(chris, "Casey")
charlie = my_tree.add_right(sam, "Charlie")
drew = my_tree.add_left(charlie, "Drew")

print(my_tree)
print(my_tree.get_size())



print(f"Pat node height: {pat.node_height()}")
print(f"Pat node depth: {pat.node_depth()}")
print(f"Drew node height: {drew.node_height()}")
print(f"Drew node depth: {drew.node_depth()}")
print(f"Tree height: {my_tree.tree_height()}")

"""


















