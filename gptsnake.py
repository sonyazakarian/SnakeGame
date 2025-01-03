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

# Snake Class
class Snake:
    def __init__(self, first_initial_position = (3,3), second_initial_position = (4,3), third_initial_position = (5,3), fourth_initial_position = (6,3)):
        self.body = DoublyLinkedList() # empty doubly linked list 
        self.body.add_first(first_initial_position)   # add first node as the initial position 
        # so all the nodes will just be positions and you'll add directions to move between them?
        self.body.add_last(second_initial_position)
        self.body.add_last(third_initial_position)
        self.body.add_last(fourth_initial_position)
        self.direction = (1, 0)  # Start moving to the right

    def change_direction(self, new_direction):
        self.direction = new_direction

    def move(self):
        head_x, head_y = self.body.first()
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.add_first(new_head)

        # to visualize : e.g. before the linked list was (3, 3)
        # lets say direction is (1,0)
        # adds new node (4,3)
        # now linked list is (4,3) (3,3)

        return self.body.remove_last()  # Remove tail segment unless snake grows

    def grow(self):
        tail = self.body.last()
        self.body.add_last(tail)  # Duplicate last segment to grow snake

    def check_collision(self):
        head = self.body.first()
        current = self.body.head.next
        while current:
            if current.value == head:
                return True
            current = current.next
        return False

# Food Class
class Food:
    def __init__(self, grid_size):
        self.position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

    def respawn(self, grid_size):
        self.position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

# Main Game Loop
def main():
    grid_size = 20
    limit = 20
    timer = 0
    snake = Snake()
    food = Food(grid_size)

    dudraw.set_canvas_size(400, 400)
    dudraw.set_x_scale(0, grid_size)
    dudraw.set_y_scale(0, grid_size)

    direction_map = {
        'w': (0, 1),  # Up
        'a': (-1, 0),  # Left
        's': (0, -1),  # Down
        'd': (1, 0)  # Right
    }

    while True:
        timer += 1
        dudraw.clear(dudraw.WHITE)

        # Check for user input
        if dudraw.has_next_key_typed():
            key = dudraw.next_key_typed()
            if key in direction_map:
                snake.change_direction(direction_map[key])

        # Move the snake only when the timer reaches the limit
        if timer == limit:
            timer = 0

            # Move the snake and check collisions
            tail_position = snake.move()
            if snake.check_collision():
                print("Game Over! Snake hit itself.")
                break

            # Check for wall collision
            head_x, head_y = snake.body.first()
            if not (0 <= head_x < grid_size and 0 <= head_y < grid_size):
                print("Game Over! Snake hit a wall.")
                break

            # Check for food consumption
            if snake.body.first() == food.position:
                snake.grow()
                food.respawn(grid_size)

        # Draw food
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_square(food.position[0], food.position[1], 0.5)

        # Draw snake
        dudraw.set_pen_color(dudraw.GREEN)
        current = snake.body.head
        while current:
            x, y = current.value
            dudraw.filled_square(x, y, 0.5)
            current = current.next

        dudraw.show(50)

if __name__ == "__main__":
    main()