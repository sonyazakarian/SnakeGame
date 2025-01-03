

import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def set_value(self,value):
        self.value = value 

    def is_external(self):
        return self.left is None and self.right is None 
    
    def is_internal(self):
        return not self.is_external()
    
    def is_leaf(self):
        return self.is_external()
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self)
    
class TreeSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def node_height(self,node):
        if node is None:
            return -1
        return node.height
    
    # Has to be done from bottom to top of tree (starting at level of leaf node)
    # Only works if height of children have been calculated accurately
    def recalculate_node_height(self,node):
        node.height = 1 + max(self.node_height(node.left), self.node_height(node.right))
        return node.height
    

    # review rotate code for understanding
    def rotate_left(self,x):
        y = x.left
        t2 = y.right

        y.right = x
        y.right.parent = y

        x.left = t2
        if x.left is not None:
            x.left.parent = x

        self.recalculate_node_height(x)
        self.recalculate_node_height(y)

        return y

    def rotate_right(self,x):
        y = x.right
        t2 = y.left

        y.left = x
        y.left.parent = y

        x.right = t2
        if x.right is not None:
            x.right.parent = x

        self.recalculate_node_height(x)
        self.recalculate_node_height(y)

        return y
    

        #       z
    #    y 
    #  x 
    # Case 1: Left Left

    #        z
    #   y 
    #        x
    # Case 2: Left Right
    
    # Rebalancing methods: Restructure the tree if needed
    # Return root of new subtree at the end 
    
    def rebalance_left(self, z):
        # This is called if you're adding left, so left side must be greater than right side 
        if self.node_height(z.left) - self.node_height(z.right) > 1:
            y = z.left
            if self.node_height(y.left)  >= self.node_height(y.right):
                # Then they are equal on both sides or we are in the Case Left Left
                # Either way want to use Case Left Left because it's easier
                z = self.rotate_right(z)
            else:
                # Then Case Left Right 
                z.left = self.rotate_left(z.left)
                z.left.parent = z

                # Now do same as Left Left because we rotated it to be Left Left
                z = self.rotate_right(z)
        return z 
    
    def rebalance_right(self, z):
        # Covers case RightRight or RightLeft
        if self.node_height(z.right) - self.node_height(z.left) > 1:
            y = z.right
            if self.node_height(y.right)  >= self.node_height(y.left):
                # Case RightRight
                z = self.rotate_left(z)
            else:
                # Case RightLeft
                z.right = self.rotate_right(z.right)
                z.right.parent = z

                z = self.rotate_left(z)

        return z 
    
    def add(self,v)->None:
        self.root = self.add_recursive(self.root, v) 
        self.root.parent = None 
        # If you change the root in the rotation, you NEED to make sure that the new root has no parent
 
    def add_recursive(self,r,v):
        # recursive helper method that adds value v into the tree rooted at r
        # returns root of the tree after v is added 
        # r: root of the subtree, v: value to be added to the subtree
        # returns root of the subtree after insertions are completed
        if r is None:
            self.size += 1
            return TreeNode(v)
        elif v < r.value:
            r.left = self.add_recursive(r.left, v)
            r.left.parent = r
            self.recalculate_node_height(r)
            r = self.rebalance_left(r)
        elif v > r.value:
            r.right = self.add_recursive(r.right, v)
            r.right.parent = r
            self.recalculate_node_height(r) 
            r = self.rebalance_right(r)
        return r
    


    def discard(self,val)->None:
        self.root = self._discard_recursive(self.root, val)
        self.root.parent = None

    def discard_recursive(self, node, val) -> None:
        if node is None:
            return None
        elif val < node.value:
            node.left = self.discard_recursive(node.left, val)
            if node.left is not None:
                node.left.parent = node
            self.recalculate_node_height(node)   # NEWLY ADDED LINE
            node = self.rebalance_right(node)    # NEWLY ADDED LINE
        elif val > node.value:
            node.right = self.discard_recursive(node.right, val)
            if node.right is not None:
                node.right.parent = node 
            self.recalculate_node_height(node)
            node = self.rebalance_left(node)
        else:
            # val is found at node 
            if node.is_external():
                # node is leaf
                self.size -= 1
                return None
            if node.left is None:
                # node has only one right child 
                self.size -= 1
                return node.right
            if node.right is None:
                # node has only one left child 
                self.size -= 1
                return node.left
            
            # node has two children 
            pred = node.left
            while pred.right is not None:
                pred = pred.right
            # copy value from pred 
            node.value = pred.value
            # remove the value from pred 
            node.left = self.discard_recursive(node.left, pred.value)  # why node.left??

        return node 
    
    def add_list(self,a_list):
        for elem in a_list:
            self.add(elem)
    
    def contains(self, val) -> bool:
        return self._contains_recursive(self.root, val)
    
    def _contains_recursive(self, node, val) -> bool:
        if node is None:
            return False
        if node.value == val:
            return True
        if val < node.value:
            return self._contains_recursive(node.left, val) 
        if val > node.value:
            return self._contains_recursive(node.right, val)
    
    def min(self):
        if self.root is None:
            return None  
        return self._min_recursive(self.root)

    def _min_recursive(self, node):
        if node.left is None:
            return node.value
        return self._min_recursive(node.left)

    def max(self):
        if self.root is None:
            return None  
        return self._max_recursive(self.root)

    def _max_recursive(self, node):
        if node.right is None:
            return node.value
        return self._max_recursive(node.right)

    def recursive_helper(self, node):
        if node is None:
            return
        self.recursive_helper(node.left)
        print(node.value)
        self.recursive_helper(node.right)

    def print_sorted(self):
        self.recursive_helper(self.root)

    def __str__(self):
        return self._recursive_str(self.root, 0)
    
    # i dont have recursive str

    #  questionable method 
    def _recursive_str(self, node, level=0):
        result = ""
        if node is not None:
            result += " " * (4 * level) + str(node.value) + "\n"  # Indent based on level
            result += self._recursive_str(node.left, level + 1)   # Process left subtree
            result += self._recursive_str(node.right, level + 1)  # Process right subtree

            # + '\n' + self._recursive_str(node.left, level+1) + self._recursive_str(node.right, level+1)
        return result
    
    def _recursive_str(self, node, level=0):
        if node is not None:
            result += " " * (4 * level) + str(node.value) + "\n"  # Indent based on level
            result += self._recursive_str(node.left, level + 1)   # Process left subtree
            result += self._recursive_str(node.right, level + 1)  # Process right subtree
        return result



def main():
    tree = TreeSet()
    tree.add_list( [1,2,3] )

    print(tree)

    # while True:
    #     val = int(input('What do you wish to delete?'))



if __name__ == '__main__':
    main()






    """
    def _copy(self):
        result = TreeSet()
        result = self._copy_recursive(self.root, result)
        return result
    
    def _copy_recursive(self, node):

        
    def union(self, other):
        result = TreeSet()


    def intersection(self,other):

        """


        


    
