
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
    # returns True if the DLL is empty
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
     # sets head to new node
    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
     # sets tail to new node
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
        # Draws the initial food at a randomly selected position within the grid size
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(self.position[0], self.position[1], 0.5, 0.5)
    def redraw(self, snake):
        # Redraws the food every time the snake "eats" it
        while True:
            # Generates random coordinates for food within the grid
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
    def display_score(self, score):
        dudraw.clear(dudraw.GREEN)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.text(17,17,f"Score: {score}")
class Snake:
    def __init__(self, head_coordinates, grid_size):
        self.body = DoublyLinkedList()
        self.body.add_first(head_coordinates)
        self.grid_size = grid_size
        # Initial positions for the snake (body will start as 4 squares long)
        self.body.add_first((head_coordinates[0] - 1, head_coordinates[1]))
        self.body.add_first((head_coordinates[0] - 2, head_coordinates[1]))
        self.body.add_first((head_coordinates[0] - 3, head_coordinates[1]))
        self.direction = "Right"  # Initial direction
    def draw(self):
        # Draw the snake body
        current = self.body.head
        is_head = True
        while current:
            # Draw head
            if is_head:
                dudraw.set_pen_color(dudraw.DARK_GREEN)
                dudraw.filled_rectangle(current.value[0], current.value[1], 0.5, 0.5)
                # Eyes
                dudraw.set_pen_color(dudraw.WHITE)
                dudraw.filled_circle(current.value[0] - 0.15, current.value[1] + 0.15, 0.1)
                dudraw.filled_circle(current.value[0] + 0.15, current.value[1] + 0.15, 0.1)
                # Tongue
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
        # Method to change direction of snake based on key press
        # Checks to ensure the snake cannot do a "180" direction change (i.e. can't go left to right)
        if dudraw.has_next_key_typed():
            key = dudraw.next_key_typed()
            if key == 'd' and self.direction != "Left":
                self.direction = "Right"
            elif key == 'a' and self.direction != "Right":
                self.direction = "Left"
            elif key == 'w' and self.direction != "Down":
                self.direction = "Up"
            elif key == 's' and self.direction != "Up":
                self.direction = "Down"
    def move(self):
        self.set_direction()
        # Calculate new head position based on direction
        head_x, head_y = self.body.head.value
        new_head = (head_x, head_y)
        if self.direction == "Right":
            new_head = (head_x + 1, head_y)
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
            tail_x, tail_y = self.body.tail.value
            prev_tail_x, prev_tail_y = self.body.tail.prev.value
            if tail_x < prev_tail_x:  # Direction = right
                # Extend snake by setting new tail to a node 1 to the left of the current tail
                new_tail = (tail_x - 1, tail_y)
            elif tail_x > prev_tail_x:  # Direction = left
                # Extend snake by setting new tail to a node 1 to the right of the current tail
                new_tail = (tail_x + 1, tail_y)
            elif tail_y < prev_tail_y:  # Direction = up
                # Extend snake by setting new tail to a node 1 below the current tail
                new_tail = (tail_x, tail_y - 1)
            elif tail_y > prev_tail_y:  # Direction = down
                # Extend snake by setting new tail to a node 1 above the current tail
                new_tail = (tail_x, tail_y + 1)
            self.body.add_last(new_tail)
            food.redraw(self)  # Redraws food in a different location
            return True
            # food.display_score(self, score)
    def check_boundary(self):
        # Purpose is to end game if the snake head goes beyond any of the walls
        if self.body.head.value[0] > self.grid_size or self.body.head.value[0] < 0 or self.body.head.value[1] > self.grid_size or self.body.head.value[1] < 0:
            return True
    def check_self_collision(self):
        # Purpose is to end game if the snake head collides with any other part of itself
        current = self.body.head.next.next.next
        collision = False
        while current:
            if current.value[0] == self.body.head.value[0] and current.value[1] == self.body.head.value[1]:
                collision = True
                break
            current = current.next
        return collision
def main():
    # Create canvas
    dudraw.set_canvas_size(400, 400)
    grid_size = 20
    dudraw.set_x_scale(0, grid_size)
    dudraw.set_y_scale(0, grid_size)
    # Create a snake and food instance
    snake = Snake((6.5, 3.5), grid_size)
    food = Food(grid_size)
    score = 0  # Initialize score outside the loop
    # Main game loop
    while True:
        dudraw.clear(dudraw.GREEN)  # Clear the canvas for animation
        # Display "Play Snake!" title
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.text(10, 18, "Play Snake!")
        # Draw food, snake, and check for food collision
        food.draw()
        snake.draw()
        snake.move()
        # Check if food is eaten and update score
        if snake.check_and_eat_food(food):
            score += 1
            food.redraw(snake)  # Move food to a new position
        # Display updated score in the corner
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.text(17, 18, f"Score: {score}")
        # Update display and control game speed
        dudraw.show(100)  # Adjust this to control game speed
        # Break game loop if the snake collides with a wall or itself
        if snake.check_boundary() or snake.check_self_collision():
            break
    # Display Game Over message
    dudraw.set_pen_color(dudraw.RED)
    dudraw.text(10, 10, "CRASH. Game over.")
    dudraw.show(float("inf"))  # Keeps Game Over message on screen
if __name__ == '__main__':
    main()