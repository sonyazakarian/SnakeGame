

import dudraw
want to just make a food square 

should be 1 yellow square 


class Food:
    def __init__(self, head_coordinates):
        self.body = DoublyLinkedList()
        self.body.add_first(head_coordinates)
        # This will just create a doubly linked list with 1 node, which is some coordinates given by user. e.g. (7,7)

    def draw(self):
        dudraw.filled_rectangle(random.randint(0, grid_size -1), random.randint(0, grid_size - 1))
        


        current = self.body.head
        dudraw.filled_rectangle(current.value[0], current.value[1], 0.5, 0.5)

    

# gpt 
class Food:
    def __init__(self, grid_size):
        self.position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

    def respawn(self, grid_size):
        self.position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))