


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
    



class Snake:

    def __init__(self, snake_head):
        self.snake_head = snake_head

    def create_and_draw_and_move_snake_dll(self, head_coordinates, direction):
        while True:
            snake = DoublyLinkedList()
            snake.add_last(head_coordinates)
            snake.add_last((head_coordinates[0] - 1, head_coordinates[1]))
            snake.add_last((head_coordinates[0] - 2, head_coordinates[1]))
            snake.add_last((head_coordinates[0] - 3, head_coordinates[1]))

            # draw initial snake
            dudraw.clear(dudraw.WHITE)

            current = snake.head
            while current is not None:
                dudraw.filled_rectangle(current.value[0], current.value[1], 0.5, 0.5)
                current = current.next

        # move snake

            if direction == "Right":
                snake.head = snake.add_first((head_coordinates[0] + 1, head_coordinates[1]))
                snake.remove_last()

            dudraw.show(1)


def main():

    dudraw.set_canvas_size(400,400)
    dudraw.set_x_scale(0,20)
    dudraw.set_y_scale(0,20)

    snake = Snake((6,3))
    snake.create_and_draw_and_move_snake_dll((6,3), "Right")

    dudraw.show(float("inf"))


if __name__ == "__main__":
    main()













