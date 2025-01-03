"""

stack should be depth first
queue should be breadth first 

"""

class Stack:

    def __init__(self):
        self.data = []   # Will use a Python list as the data structure

    def push(self, v):
        self.data.append(v)  # Add element to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.data.pop()  # Remove and return the top element
        raise IndexError("Empty stack")

    def top(self):
        if not self.is_empty():
            return self.data[-1]  # Return the top element without removing it
        raise IndexError("Empty stack")

    def size(self):
        return len(self.data)  # Return the size of the stack

    def is_empty(self):
        return len(self.data) == 0  # Return True if the stack is empty

    def __str__(self):
        return str(self.data)  # Return string representation of the stack


class Queue:

    def __init__(self):
        self.data = [] # Will also use a Python list as the data structure

    def enqueue(self, v):
        self.data.append(v)  # Add element to the top of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)      # Remove and return first element of the queue, if queue is not empty
        raise IndexError("Empty queue")  
    
    def first(self):
        if not self.is_empty():
            return self.data[0]         # Return first element of the queue without removing it, if queue is not empty
        raise IndexError("Empty queue") 
    
    def size(self):
        return len(self.data)           # Return size of the queue
    
    def is_empty(self):
        return len(self.data) == 0      # Return True if queue is empty
    
    def __str__(self):
        return str(self.data)           # Return string representation of the queue

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

    def ancestors(self):
        return self
        return all of its ancestors
        does this mean i have to implement a get prev node?
        does he have office hours tomorrow?

    def node_depth(self):
        return depth of node 

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

    def depth_first_traversal(self):
        stack = []
        stack.append(self.root)
        result = ""
        while Stack:
            current = stack.pop()
            result += (str(current))
            if current.left is not None:
                stack.append((current.left))
            if current.right is not None:
                stack.append((current.left))

    def breadth_first_traversal
    

def main():
    the_tree = BinaryTree()
    the_root = the_tree.add_root(10)
    the_left = the_tree.add_left(the_root, 8)
    the_left_left = the_tree.add_left(the_left, 3)
    the_left_right = the_tree.add_right(the_left, 9)
    the_right = the_tree.add_right(the_root, 15)
    the_right_right = the_tree.add_right(the_right, 23)
    print(the_tree)


if __name__ == "__main__":
    main()



# depth first traversal
stack = [] # initializing a list. could initialize as empty, and then append Root to it
stack.append()
while Stack:
    current = Stack.pop()
    result += (str(current))
    if current.left is not None:
        stack.append((current.left))

        # and then repeat for right
        # technically should do right first, and then left 

# queue is basically same. but instead of popping at end, pop at zero. and then for that one, left and then right. 
# breadth first traversal 











