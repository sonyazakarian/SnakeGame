

import dudraw  # Assuming dudraw is the library used for drawing the game
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

class Food:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.position = (random.randint(1, grid_size - 1) - 0.5, random.randint(1, grid_size - 1) - 0.5)

    def draw(self):
        # SHOULD CLEAN THIS UP. 
        # IDEALLY WOULD SAY GRID_SIZE INSTEAD OF 20, BUT THATS A VARIABLE FROM THE DRIVER, SO
        # IDK HOW TO PROPERLY CALL THAT. 
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(self.position[0], self.position[1], 0.5, 0.5)

    def redraw(self, snake):
        while True:
            # Generate random coordinates for food within the grid
            random_x_pos = random.randint(1, self.grid_size - 1) - 0.5
            random_y_pos = random.randint(1, self.grid_size - 1) - 0.5

            # Check if this position overlaps with any part of the snake
            current = snake.body.head
            collision = False
            while current:
                if current.value[0] == random_x_pos and current.value[1] == random_y_pos:
                    collision = True
                    break
                current = current.next

            # If no collision, set new position and exit loop
            if not collision:
                self.position = (random_x_pos, random_y_pos)
                break

class Snake:
    def __init__(self, head_coordinates, grid_size):
        self.body = DoublyLinkedList()
        self.body.add_first(head_coordinates)
        self.grid_size = grid_size
        self.body.add_first((head_coordinates[0] - 1, head_coordinates[1]))
        self.body.add_first((head_coordinates[0] - 2, head_coordinates[1]))
        self.body.add_first((head_coordinates[0] - 3, head_coordinates[1]))
        self.direction = None  # No initial direction until the user presses a key
        self.moving = False  # Variable to track if the snake is moving

    def draw(self):
            
        # Draw the snake body
        current = self.body.head
        is_head = True

        while current:
            # Set color for head or body
            if is_head:
                dudraw.set_pen_color(dudraw.DARK_GREEN)
                dudraw.filled_rectangle(current.value[0], current.value[1], 0.5, 0.5)
                
                # Draw eyes (two small white circles)
                dudraw.set_pen_color(dudraw.WHITE)
                dudraw.filled_circle(current.value[0] - 0.15, current.value[1] + 0.15, 0.1)
                dudraw.filled_circle(current.value[0] + 0.15, current.value[1] + 0.15, 0.1)

                # Draw tongue (small red rectangle)
                dudraw.set_pen_color(dudraw.RED)
                if self.direction == "Up":
                    dudraw.filled_rectangle(current.value[0], current.value[1] + 0.5, 0.1, 0.15)
                elif self.direction == "Down":
                    dudraw.filled_rectangle(current.value[0], current.value[1] - 0.5, 0.1, 0.15)
                elif self.direction == "Right":
                    dudraw.filled_rectangle(current.value[0] + 0.5, current.value[1], 0.15, 0.1)
                elif self.direction == "Left":
                    dudraw.filled_rectangle(current.value[0] - 0.5, current.value[1], 0.15, 0.1)
                
                is_head = False  # Move on to drawing the body
            else:
                # Set color and draw the rest of the snake body
                dudraw.set_pen_color(dudraw.DARK_GREEN)
                dudraw.filled_rectangle(current.value[0], current.value[1], 0.5, 0.5)
            
            current = current.next

    def set_direction(self):
        if dudraw.has_next_key_typed():
            key = dudraw.next_key_typed()
            if key in ['d', 's', 'a', 'w']:
                if key == 'd' and self.direction != "Left":
                    self.direction = "Right"
                elif key == 'a' and self.direction != "Right":
                    self.direction = "Left"
                elif key == 'w' and self.direction != "Down":
                    self.direction = "Up"
                elif key == 's' and self.direction != "Up":
                    self.direction = "Down"
                self.moving = True  # Start moving when the user presses a key

    def move(self):

        self.set_direction()

        # Calculate new head position based on direction
        head_x, head_y = self.body.head.value
        new_head = (head_x, head_y)
        if self.direction == "Right":
            new_head = (head_x + 1, head_y)
            # NEW
            # new_head = (head_x + 2, head_y)
            # new_head = (head_x + 3, head_y)
            # new_head = (head_x + 4, head_y)
        if self.direction == "Left":
            new_head = (head_x - 1, head_y)
        if self.direction == "Up":
            new_head = (head_x, head_y + 1)
        if self.direction == "Down":
            new_head = (head_x, head_y - 1)

        # Add the new head and remove the tail to move the snake
        self.body.add_first(new_head)
        self.body.remove_last()


        # here add something to check if the boundaries are ok

    def check_and_eat_food(self,food):
    
        if self.body.head.value[0] == food.position[0] and self.body.head.value[1] == food.position[1]:
            

            # extend the snake 

            tail_x, tail_y = self.body.tail.value       
            prev_tail_x, prev_tail_y = self.body.tail.prev.value
                
            if tail_x < prev_tail_x:
                # then its moving to the right
                new_tail = (tail_x - 1, tail_y)

            elif tail_x > prev_tail_x:
                # then its moving to the left
                new_tail = (tail_x + 1, tail_y)

            elif tail_y < prev_tail_y:
                # then its moving up
                new_tail = (tail_x, tail_y - 1)

            elif tail_y > prev_tail_y:
                # then its moving down
                new_tail = (tail_x, tail_y + 1)

            self.body.add_last(new_tail)

            food.redraw(self)  # switched order here
            
    def check_boundary(self):
        if self.body.head.value[0] > self.grid_size or self.body.head.value[0] < 0 or self.body.head.value[1] > self.grid_size or self.body.head.value[1] < 0:
            return True


        # if self.body.head.value[0] > self.grid_size or self.body.head.value[0] < 0 or self.body.head.value[1] > self.grid_size or self.body.head.value[1] < 0:
            # print("Game over") this works but its not really what i want
            # dudraw.set_pen_color(dudraw.RED) 
            # dudraw.text(10,10, "CRASH. Game over.")
           #  dudraw.show()
            # return # what is the point of this



        # if self.head.value is 19.5 or more or 0.5 or less:
           #  end the game 

    def check_self_collision(self):
        # checks to make sure game ends if snake collides with itself
        
        current = self.body.head.next.next.next
        collision = False
        while current:
            if current.value[0] == self.body.head.value[0] and current.value[1] == self.body.head.value[1]:
                collision = True
                break
            current = current.next

        return collision


def main():
    dudraw.set_canvas_size(400, 400)

    grid_size = 20
    dudraw.set_x_scale(0, grid_size)
    dudraw.set_y_scale(0, grid_size)

    # Create a snake instance
    snake = Snake((6.5, 3.5), grid_size)
    food = Food(grid_size)

    # Main game loop
    while True:
        dudraw.clear(dudraw.WHITE)
        food.draw()
        snake.draw()
        snake.move()
        snake.check_and_eat_food(food)
        dudraw.show(100)

        if snake.check_boundary() or snake.check_self_collision():
            break 

    dudraw.set_pen_color(dudraw.RED)
    dudraw.text(10, 10, "CRASH. Game over.")
    dudraw.show(float("inf"))

if __name__ == "__main__":
    main()