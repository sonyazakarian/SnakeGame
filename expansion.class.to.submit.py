


class ExpressionTree(BinaryTree):
    
    def __str__(self) -> str:
        return self._str_helper(self.root)
    
    def _str_helper(self, node) -> str:
        # Base case: if the node is a leaf, return its value
        if node is None:
            return ""
        if node.is_leaf():
            return str(node.value)  
        
        # Recursive case
        left_expr = self._str_helper(node.left) 
        right_expr = self._str_helper(node.right)  
        
        return f"({left_expr}{node.value}{right_expr})"  
        
    def evaluate(self, node) -> float:
        # Base case: if the node is a leaf, return its value as a float
        if node.is_leaf():
            return float(node.value)  
        
        # Recursive case: evaluate left and right subtrees
        left_value = self.evaluate(node.left)  
        right_value = self.evaluate(node.right) 
        
        if node.value == '+':  
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value