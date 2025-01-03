

import random

class TreeNode :

    def __init__( self, value ) :
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
            
    def set_value( self, value ) :
        self.value = value

    def is_external( self ) :
        return self.left is None and self.right is None
    
    def is_internal( self ) :
        return not self.is_external()
    
    def is_leaf( self ) :
        return self.is_external()
    
    def __str__( self ) :
        return str( self.value )
    
    def __repr__( self ) :
        return str( self )
    
class TreeSet :

    def __init__( self ) :
        self.root = None
        self.size = 0

    def node_height( self, node ) :
        if node is None :
            return -1
        return node.height
    
    def _rotate_right( self, x ) :
        y = x.left
        tree_two = y.right
        y.right = x
        y.right.parent = y
        x.left = tree_two
        if x.left is not None :
            x.left.parent = x
        self.recalc_node_height( x )
        self.recalc_node_height( y )
        return y
    
    def _rotate_left( self, x ) :
        y = x.right
        tree_two = y.left
        y.left = x
        y.left.parent = y
        x.right = tree_two
        if x.right is not None :
            x.right.parent = x
        self.recalc_node_height( x )
        self.recalc_node_height( y )
        return y
    
    def _rebalance_right(self, z):
        # Ensure rebalance is needed
        if self.node_height(z.right) - self.node_height(z.left) > 1:
            y = z.right
            if self.node_height(y.right) >= self.node_height(y.left):
                # Case RightRight
                z = self._rotate_left(z)
            else:
                # Case RightLeft
                z.right = self._rotate_right(z.right)
                z.right.parent = z
                z = self._rotate_left(z)
        return z

    

    def _rebalance_left(self, z):
        # Ensure rebalance is needed
        if self.node_height(z.left) - self.node_height(z.right) > 1:
            y = z.left
            if self.node_height(y.left) >= self.node_height(y.right):
                # Case LeftLeft
                z = self._rotate_right(z)
            else:
                # Case LeftRight
                z.left = self._rotate_left(z.left)
                z.left.parent = z
                z = self._rotate_right(z)
        return z

    
    def get_size( self ) :
        return self.size
    
    def is_empty( self ) :
        return self.size == 0
    
    def add_list( self, a_list ) :
        for elem in a_list :
            self.add( elem )

    def recalc_node_height( self, node ) :
        node.height = 1 + max( self.node_height(node.left),
        self.node_height(node.right) )

    def add( self, val ) -> None :
        self.root = self._add_recursive( self.root, val )
        self.root.parent = None

    def _add_recursive( self, node, val ) :
        if node is None :
            self.size += 1
            return TreeNode( val )
        elif val < node.value :
            node.left = self._add_recursive( node.left, val )
            node.left.parent = node
            self.recalc_node_height( node )
            node = self._rebalance_left( node )
        elif val > node.value :
            node.right = self._add_recursive( node.right, val )
            node.right.parent = node
            self.recalc_node_height( node )
            node = self._rebalance_right( node )
        return node
    
    def discard( self, val ) -> None :
        self.root = self._discard_recursive( self.root, val )
        self.root.parent = None

    def _discard_recursive( self, node, val ) -> None :
        if node is None :
            return None
        elif val < node.value :
            node.left = self._discard_recursive( node.left, val )
            if node.left is not None :
                node.left.parent = node
            self.recalc_node_height( node )
            node = self._rebalance_right( node )
        elif val > node.value :
            node.right = self._discard_recursive( node.right, val )
            if node.right is not None :
                node.right.parent = node
            self.recalc_node_height( node )
            node = self._rebalance_left( node )
        else :
            # val is found at node
            if node.is_external() :
                # node is leaf
                self.size -= 1
                return None
            if node.left is None :
                # node has only one right child
                self.size -= 1
                return node.right
            if node.right is None :
                # node has only one left child
                self.size -= 1
                return node.left
            
            # node has two children
            pred = node.left

            while pred.right is not None :
                pred = pred.right
            # copy value from pred
            node.value = pred.value
            # remove the value from pred
            node.left = self._discard_recursive( node.left, pred.value )

        return node
    
    def contains( self, val ) -> bool :
        return self._contains_recursive( self.root, val )
    
    def _contains_recursive( self, node, val ) -> bool :
        if node is None :
            return False
        if node.value == val :
            return True
        if val < node.value :
            return self._contains_recursive( node.left, val )
        if val > node.value :
            return self._contains_recursive( node.right, val )
        
    def _copy( self ) :
        result = TreeSet()
        self._copy_recursive( self.root, result )
        return result
    
    def _copy_recursive( self, node, result ) :
        if node is not None :
            result.add( node.value )
        self._copy_recursive( node.left, result )
        self._copy_recursive( node.right, result )

    def union( self, other ) :
        result = TreeSet()
        self._copy_recursive( self.root, result )
        other._copy_recursive( other.root, result )
        return result
    
    def intersection( self, other ) :
        pass

    def difference( self, other ) :
        pass

    def min( self ) :
        if self.root is None :
            return None
        smallest = self.root
        while smallest.left is not None :
            smallest = smallest.left
        return smallest.value
    
    def max( self ) :
        if self.root is None :
            return None
        largest = self.root
        while largest.right is not None :
            largest = largest.right
        return largest.value
    
    def _recursive_str( self, node, level ) :
        if node is None :
            return ''
        return level * ' ' + str( node ) + '\n' + self._recursive_str(node.left,
        level+1) + self._recursive_str(node.right, level+1)
    
    def __str__( self ) :
        return self._recursive_str( self.root, 0 )

def main() :
    tree = TreeSet()
    tree.add_list( [1,2,3,4,5,6,7,8,9,10] )
    #for i in range( 40 ) :
    # tree.add( random.randint(1,100 ) )
    print( tree )
    while True :
        val = int( input( 'What do you wish to delete? ') )
        tree.discard( val )
        print( tree )
        print( f'Tree size: {tree.get_size()}' )

if __name__ == '__main__' :
    main()
