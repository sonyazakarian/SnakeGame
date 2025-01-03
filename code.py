
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
            return str(node.element())
        
        # Recursive case: process left subtree, operator, and right subtree
        left_expr = self._str_helper(self.left(node))
        right_expr = self._str_helper(self.right(node))
        
        return f"({left_expr}{node.element()}{right_expr})"
        
    def evaluate(self, node) -> float:
        # Base case: if the node is a leaf, return its value as a float
        if node.is_leaf():
            return float(node.element())
        
        # Recursive case: evaluate left and right subtrees
        left_value = self.evaluate(self.left(node))
        right_value = self.evaluate(self.right(node))
        
        # Determine the operation based on the node's element and apply it
        if node.element() == '+':
            return left_value + right_value
        elif node.element() == '-':
            return left_value - right_value
        elif node.element() == '*':
            return left_value * right_value
        elif node.element() == '/':
            return left_value / right_value
        else:
            raise ValueError("Unknown operator: " + node.element())
        
def main():
    the_tree = ExpressionTree()
    print(the_tree)

        

if __name__ == "__main__":
    main()



"""

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
            return str(node.element())
        
        # Recursive case: process left subtree, operator, and right subtree
        left_expr = self._str_helper(self.left(node))
        right_expr = self._str_helper(self.right(node))
        
        return f"({left_expr}{node.element()}{right_expr})"
        
    def evaluate(self, node) -> float:
        # Base case: if the node is a leaf, return its value as a float
        if node.is_leaf():
            return float(node.element())
        
        # Recursive case: evaluate left and right subtrees
        left_value = self.evaluate(self.left(node))
        right_value = self.evaluate(self.right(node))
        
        # Determine the operation based on the node's element and apply it
        if node.element() == '+':
            return left_value + right_value
        elif node.element() == '-':
            return left_value - right_value
        elif node.element() == '*':
            return left_value * right_value
        elif node.element() == '/':
            return left_value / right_value
        else:
            raise ValueError("Unknown operator: " + node.element())


















"""

