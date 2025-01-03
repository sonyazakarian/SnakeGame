

import random
import dudraw  # Assuming dudraw is the library used for drawing the game

# Doubly Linked List Node
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

# Doubly Linked List for Snake Body
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return str(result)

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return removed_value
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Empty list")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return value

    def first(self):
        return self.head.value if self.head else None

    def last(self):
        return self.tail.value if self.tail else None

    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value if current else None


def dll_tester():
    # create a DoublyLinkedList
    test_list = DoublyLinkedList()
    
    # Testing list creation
    assert test_list.get_size() == 0, 'List should be empty to start!'
    
    # Testing add_first
    test_list.add_first(1)
    assert test_list.first() == 1, 'add_first needs adjustment!'
    assert test_list.last() == 1, 'add_first needs adjustment!'
    assert test_list.get_size() == 1, 'add_first needs adjustment!'
    
    test_list.add_first(2)
    assert test_list.first() == 2, 'add_first needs adjustment!'
    assert test_list.last() == 1, 'add_first needs adjustment!'
    assert test_list.get_size() == 2, 'add_first needs adjustment!'
    
    # Testing add_last
    test_list.add_last(3)
    assert test_list.first() == 2, 'add_last needs adjustment!'
    assert test_list.last() == 3, 'add_last needs adjustment!'
    assert test_list.get_size() == 3, 'add_last needs adjustment!'

    # Test remove_first
    assert test_list.remove_first() == 2, 'remove_first needs adjustment!'
    assert test_list.first() == 1, 'remove_first needs adjustment!'
    assert test_list.last() == 3, 'remove_first needs adjustment!'
    assert test_list.get_size() == 2, 'remove_first needs adjustment!'

    # Test remove_last
    assert test_list.remove_last() == 3, 'remove_last needs adjustment!'
    assert test_list.first() == 1, 'remove_last needs adjustment!'
    assert test_list.last() == 1, 'remove_last needs adjustment!'
    assert test_list.get_size() == 1, 'remove_last needs adjustment!'

    while not test_list.is_empty():
        test_list.remove_first()

    assert test_list.get_size() == 0, 'List should be empty after removing all values'

    for i in range(10):
        test_list.add_last(i + 1)

    # Test get method
    assert test_list.get(0) == 1, 'get(0) should return the element at the first index'
    assert test_list.get(5) == 6, 'get(5) should return the element at index 5'
    assert test_list.get(9) == 10, 'get(9) should return the element at the last index'

    print('All tests passed!')

# Run the tester function
dll_tester()