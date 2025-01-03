"""
Sonya Zakarian
Project 1: The Game of Snake
October 28, 2024 (Extended deadline for submission)
"""
import dudraw
import random

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
            self
