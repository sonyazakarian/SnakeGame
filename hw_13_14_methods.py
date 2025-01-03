

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def node_height(self):
        # Base case
        if not self:
            return -1
        # Recursive case
        left_height = self.left.node_height() if self.left else -1
        right_height = self.right.node_height() if self.right else -1
        return 1 + max(left_height, right_height)

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def tree_height(self):
        if not self.root:
            return -1
        return self.root.node_height()
    

