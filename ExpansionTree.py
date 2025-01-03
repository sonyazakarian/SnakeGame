from BinaryTree import BinaryTree

class ExpressionTree(BinaryTree):
    
    def __str__(self) -> str:
        # Use a helper function to generate the string representation of the expression
        return self._str_helper(self.root)
    
    def _str_helper(self, node) -> str:
        # Base case: if the node is a leaf, return its value
        if node is None:
            return ""
        if node.is_leaf():
            return str(node.value)  # Changed from node.element() to node.value
        
        # Recursive case: process left subtree, operator, and right subtree
        left_expr = self._str_helper(node.left)  # Assuming node.left gives the left child
        right_expr = self._str_helper(node.right)  # Assuming node.right gives the right child
        
        return f"({left_expr}{node.value}{right_expr})"  # Changed from node.element() to node.value
        
    def evaluate(self, node) -> float:
        # Base case: if the node is a leaf, return its value as a float
        if node.is_leaf():
            return float(node.value)  # Changed from node.element() to node.value
        
        # Recursive case: evaluate left and right subtrees
        left_value = self.evaluate(node.left)  # Assuming node.left gives the left child
        right_value = self.evaluate(node.right)  # Assuming node.right gives the right child
        
        # Determine the operation based on the node's element and apply it
        if node.value == '+':  # Changed from node.element() to node.value
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value
     
def _main():
    tree = ExpressionTree()

    r = tree.add_root("-")
    rl = tree.add_left(r, "/")
    rll = tree.add_left(rl, "*")
    rlll = tree.add_left(rll, "+")
    rllll = tree.add_left(rlll, "3")
    rlllr = tree.add_right(rlll, "1")
    rllr = tree.add_right(rll, "3")
    rlr = tree.add_right(rl, "+")
    rlrl = tree.add_left(rlr, "-")
    rlrll = tree.add_left(rlrl, "9")
    rlrlr = tree.add_right(rlrl, "5")
    rlrr = tree.add_right(rlr, "2")
    rr = tree.add_right(r, "+")
    rrl = tree.add_left(rr, "*")
    rrll = tree.add_left(rrl, "3")
    rrlr = tree.add_right(rrl, "-")
    rrlrl = tree.add_left(rrlr, "7")
    rrlrr = tree.add_right(rrlr, "4")
    rrr = tree.add_right(rr, "6")

    print(tree, end='')
    print('=',tree.evaluate(tree.root))


if __name__ == '__main__':
    _main()