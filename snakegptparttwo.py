

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

    def add_first(self, value):
        new_node = Node(value)
        if self.head is None:  # List is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def remove_last(self):
        if self.tail is None:  # List is empty
            return
        if self.tail == self.head:  # Only one element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

class Snake:
    def __init__(self, head_coordinates):
        self.body = DoublyLinkedList()
        self.body.add_first(head_coordinates)
        # Initial positions for the snake
        self.body.add_first((head_coordinates[0] - 1, head_coordinates[1]))
        self.body.add_first((head_coordinates[0] - 2, head_coordinates[1]))
        self.body.add_first((head_coordinates[0] - 3, head_coordinates[1]))
        self.direction = "Right"  # Initial direction

    def draw(self):
        # Draws the snake by iterating through its body
        dudraw.clear(dudraw.WHITE)
        current = self.body.head
        while current:
            dudraw.filled_rectangle(current.value[0], current.value[1], 0.5, 0.5)
            current = current.next

    def move(self):
        # Calculate new head position based on direction
        head_x, head_y = self.body.head.value
        if direction == "Right":
            new_head = (head_x + 1, head_y)
        if direction == "Left":
            new_head = (head_x - 1, head_y)
        if direction == "Up":
            new_head = (head_x, head_y + 1)
        if direction == "Down":
            new_head = (head_x, head_y - 1)

        # Add the new head and remove the tail to move the snake
        self.body.add_first(new_head)
        self.body.remove_last()

def on_press(key):
    global direction
    try:
        # Check which key is pressed and update the direction
        if dudraw.has_next_key_typed() and dudraw.next_key_typed()=='d':
            direction = "Right"
            print("Moving Right")
        if dudraw.has_next_key_typed() and dudraw.next_key_typed()=='a':
            direction = "Left"
            print("Moving Left")
        if dudraw.has_next_key_typed() and dudraw.next_key_typed()=='w':
            direction = "Up"
            print("Moving Up")
        if dudraw.has_next_key_typed() and dudraw.next_key_typed()=='s':
            direction = "Down"
            print("Moving Down")
    except AttributeError:
        # This catches any non-character key, such as special keys
        pass

def main():
    dudraw.set_canvas_size(400, 400)
    dudraw.set_x_scale(0, 20)
    dudraw.set_y_scale(0, 20)

    # Create a snake instance
    snake = Snake((6, 3))

    print(dir(dudraw))

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Main game loop
    while True:
        snake.move()
        snake.draw()
        dudraw.show(100)  # Controls the speed of the game loop


    

if __name__ == "__main__":
    main()
