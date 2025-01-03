

import dudraw

import random 



class Node:

    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):          
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " ".join(values)
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size 
    
    def add_first(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
        self.size += 1

    def add_last(self,value):
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
            raise IndexError("Empty list")
        value_to_remove = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return value_to_remove
    

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Empty list")
        value_to_remove = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return value_to_remove
    
    def first(self):
        if self.is_empty():
            raise IndexError("Empty list")
        return self.head.value
    
    def last(self):
        if self.is_empty():
            raise IndexError("Empty list")
        return self.tail.value
        
    def search(self,value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        current = self.head
        for i in range(index):
            current = current.next
        return current.value
    

class Snake:


    def __init__(self, initial_position):
        self.body = DoublyLinkedList()
        self.body.add_first(initial_position)
        self.direction = "RIGHT"

    def change_direction(self, new_direction):
        self.direction = new_direction 

    def move(self):
        head_x, head_y = self.body.first()
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.add_first(new_head)
        return self.body.remove_last()
    
    def grow(self):
        tail = self.body.last()
        self.body.add_last(tail)  # Duplicate last segment to grow snake

    def check_collision(self):

        # this one i didnt really understand that well . actually i didnt understand it at all 

        head = self.body.first()
        current = self.body.head.next
        while current:
            if current.value == head:
                return True
            current = current.next
        return False
    

class Food:
    def __init__(self, grid_size):
        self.position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

    def respawn(self, grid_size):
        self.position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))



def main():
    grid_size = 20
    limit = 20
    timer = 0
    snake = Snake((grid_size // 2, grid_size // 2))
    food = Food(grid_size)

    dudraw.set_canvas_size(400,400)
    dudraw.set_x_scale(0, grid_size)
    dudraw.set_y_scale(0, grid_size)

    direction_map = {
        'w': (0,1),  # Up
        'a': (-1,0), # Left
        's': (0,-1), # Down 
        'd': (1,0)  # Right
    }

    while True:
        timer += 1 
        dudraw.clear(dudraw.WHITE)

        if dudraw.has_next_key_typed():
            key = dudraw.next_key_typed
            if key in direction_map:
                snake.change_direction(direction_map[key])


    

