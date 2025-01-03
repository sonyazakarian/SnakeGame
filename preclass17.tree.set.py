

class TreeNode:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None
        self.parent = None 

    def is_external(self):
        return self.left is None and self.right is None 

    def is_internal(self):
        return not self.is_external()
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self)
    
class TreeSet:

    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size 
    
    def is_empty(self):
        return self.size == 0
    
    def add_recursive(self,r,v):
        # recursive helper method that adds value v into the tree rooted at r
        # returns root of the tree after v is added 
        # r: root of the subtree, v: value to be added to the subtree
        # returns root of the subtree after insertions are completed
        if r is None:
            self.size += 1
            return TreeNode(v)
        elif v < r.value:
            r.left = self._add_recursive(r.left, v)
            r.left.parent = r
        elif v > r.value:
            r.right = self._add_recursive(r.right, v)
            r.right.parent = r
        return r
    
    def add(self,v)->None:
        self.root = self.add_recursive(self.root, v) # I don't understand it 

    def discard(self,val)->None:
        self.root = self._discard_recursive(self.root, val)

    def _discard_recursive(self, node, val) -> None:
        if node is None:
            return None
        elif val < node.value:
            node.left = self._discard_recursive(node.left, val)
            if node.left is not None:
                node.left.parent = node
        elif val > node.value:
            node.right = self._discard_recursive(node.right, val)
            if node.right is not None:
                node.right.parent = node 
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
                


    def contains(self,v)->bool:
        pass

    def union(self,other):
        pass

    def intersection(self,other):
        pass

    def difference(self,other):
        pass

    # order operations
    def min(self):
        pass 

    def max(self):
        pass 

    def _recursive_str(self, r, level):
        # base case, tree is empty return an empty string
        if r is None:
            return ""
        return level * "   " + str(r) + "\n" + self._recursive_str(r.left, level+1)+ self._recursive_str(r.right, level+1)
    
    def __str__(self):
        return self._recursive_str(self.root, 0)
    



















