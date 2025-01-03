

import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def set_value(self, value):
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

    def node_height(self, node):
        if node is None:
            return -1
        return node.height

    def _rotate_right(self, x):
        y = x.left
        tree_two = y.right
        y.right = x
        y.right.parent = y
        x.left = tree_two
        if x.left is not None:
            x.left.parent = x
        self.recalc_node_height(x)
        self.recalc_node_height(y)
        return y
    

    def _rotate_left(self, x):
        y = x.right
        tree_two = y.left
        y.left = x
        y.left.parent = y
        x.right = tree_two
        if x.right is not None:
            x.right.parent = x
        self.recalc_node_height(x)
        self.recalc_node_height(y)
        return y

    def _rebalance_right(self, z):
        if self.node_height(z.right) - self.node_height(z.left) > 1:
            y = z.right
            if self.node_height(y.right) >= self.node_height(y.left):
                z = self._rotate_left(z)
            else:
                z.right = self._rotate_right(z.right)
                z.right.parent = z
                z = self._rotate_left(z)
        return z

    def _rebalance_left(self, z):
        if self.node_height(z.left) - self.node_height(z.right) > 1:
            y = z.left
            if self.node_height(y.left) >= self.node_height(y.right):
                z = self._rotate_right(z)
            else:
                z.left = self._rotate_left(z.left)
                z.left.parent = z
                z = self._rotate_right(z)
        return z

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_list(self, a_list):
        for elem in a_list:
            self.add(elem)

    def recalc_node_height(self, node):
        node.height = 1 + max(self.node_height(node.left), self.node_height(node.right))

    def add(self, val) -> None:
        self.root = self._add_recursive(self.root, val)
        self.root.parent = None

    def _add_recursive(self, node, val):
        if node is None:
            self.size += 1
            return TreeNode(val)
        elif val < node.value:
            node.left = self._add_recursive(node.left, val)
            node.left.parent = node
            self.recalc_node_height(node)
            node = self._rebalance_left(node)
        elif val > node.value:
            node.right = self._add_recursive(node.right, val)
            node.right.parent = node
            self.recalc_node_height(node)
            node = self._rebalance_right(node)
        return node

    def discard(self, val) -> None:
        self.root = self._discard_recursive(self.root, val)
        if self.root:
            self.root.parent = None

    def _discard_recursive(self, node, val) -> None:
        if node is None:
            return None
        elif val < node.value:
            node.left = self._discard_recursive(node.left, val)
            if node.left is not None:
                node.left.parent = node
            self.recalc_node_height(node)
            node = self._rebalance_right(node)
        elif val > node.value:
            node.right = self._discard_recursive(node.right, val)
            if node.right is not None:
                node.right.parent = node
            self.recalc_node_height(node)
            node = self._rebalance_left(node)
        else:
            # val is found at node
            if node.is_external():
                self.size -= 1
                return None
            if node.left is None:
                self.size -= 1
                return node.right
            if node.right is None:
                self.size -= 1
                return node.left

            # node has two children
            pred = node.left
            while pred.right is not None:
                pred = pred.right
            # copy value from pred
            node.value = pred.value
            # remove the value from pred
            node.left = self._discard_recursive(node.left, pred.value)

        return node

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
        smallest = self.root
        while smallest.left is not None:
            smallest = smallest.left
        return smallest.value

    def max(self):
        if self.root is None:
            return None
        largest = self.root
        while largest.right is not None:
            largest = largest.right
        return largest.value


    def pretty_print_with_lines(node, level=0, pos=0, width=80):
        """Pretty prints the tree with connecting lines."""
        if node is None:
            return [" " * width]

        if node.is_leaf():
            line = f"{' ' * pos}{str(node.value):^{width - pos}}"
            return [line]

        # Recursive calls to print left and right subtrees
        left = pretty_print_with_lines(node.left, level + 1, pos, width // 2)
        right = pretty_print_with_lines(node.right, level + 1, width // 2, width // 2)

        # Add the root node
        root = [f"{' ' * pos}{str(node.value):^{width - pos}}"]

        # Add the connecting lines
        connector = [" " * pos]
        if node.left:
            connector[0] += f"{' ' * (width // 4)}{'/'}"
        else:
            connector[0] += " " * (width // 4)

        if node.right:
            connector[0] += f"{' ' * (width // 4)}{'\\'}"

        # Combine all parts
        return root + connector + [l + r for l, r in zip(left, right)]


    def print_tree(tree):
        if tree.root is None:
            print("Tree is empty.")
            return

        lines = pretty_print_with_lines(tree.root)
        for line in lines:
            print(line)



# Main Function for Testing
def main():
    tree = TreeSet()
    tree.add_list([4, 2, 6, 1, 3, 5, 7])
    print("Initial tree:")
    print_tree(tree)

    while True:
        try:
            val = int(input("What do you wish to delete? "))
            tree.discard(val)
            print_tree(tree)
            print(f"Tree size: {tree.get_size()}")
        except ValueError:
            print("Invalid input. Enter an integer.")


if __name__ == "__main__":
    main()
    