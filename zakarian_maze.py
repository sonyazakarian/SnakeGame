

"""
Sonya Zakarian
Data Structures and Algorithms, Project 3
October 13, 2024


"""


import random 
import dudraw
from enum import Enum

class Stack:

    def __init__(self):
        self.data = []   # Will use a Python list as the data structure

    def push(self, v):
        self.data.append(v)  # Add element to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.data.pop()  # Remove and return the top element
        raise IndexError("Empty stack")

    def top(self):
        if not self.is_empty():
            return self.data[-1]  # Return the top element without removing it
        raise IndexError("Empty stack")

    def size(self):
        return len(self.data)  # Return the size of the stack

    def is_empty(self):
        return len(self.data) == 0  # Return True if the stack is empty

    def __str__(self):
        return str(self.data)  # Return string representation of the stack


class Queue:

    def __init__(self):
        self.data = [] # Will also use a Python list as the data structure

    def enqueue(self, v):
        self.data.append(v)  # Add element to the top of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)      # Remove and return first element of the queue, if queue is not empty
        raise IndexError("Empty queue")  
    
    def first(self):
        if not self.is_empty():
            return self.data[0]         # Return first element of the queue without removing it, if queue is not empty
        raise IndexError("Empty queue") 
    
    def size(self):
        return len(self.data)           # Return size of the queue
    
    def is_empty(self):
        return len(self.data) == 0      # Return True if queue is empty
    
    def __str__(self):
        return str(self.data)           # Return string representation of the queue


class Maze: 

    
    class CellValue(Enum):
        # Sets possible cell values as Wall, Open, or Explored
        WALL = 0
        OPEN = 1
        EXPLORED = 2
        
    class Cell:

        # Initializes Cell class with attributes row and col
        def __init__(self,row,col):
            self.row = row
            self.col = col 

        # String method
        def __str__(self):
            return(f"{self.row}, {self.col}")

    # Initialized Maze class with attributes width, height, and grid  
    def __init__(self, width, height):
        self.width = width 
        self.height = height 
        self.grid = [[Maze.CellValue.WALL for _ in range(width)] for _ in range(height)]


    def draw(self):

        # Clears before drawing each time to create an animation
        dudraw.clear(dudraw.WHITE)
        
        row_count = 0
        col_count = 0
        x_step = 1 / self.width # x-step: how far you'll move horizontically each time you increment column
        y_step = 1 / self.height # y-step: how far you'll move vertically each time you increment row
        x_start = x_step / 2    # x-coordinate of your first square
        y_start = y_step / 2    # y-coordinate of your first square
        half_width = x_step / 2
        half_length = y_step / 2

        # Nested for loop to draw the grid square by square
        for row in self.grid:
            for col in row:
                if col == Maze.CellValue.WALL: # If a wall cell, draw a black rectangle with a white border 
                    dudraw.set_pen_color(dudraw.BLACK)
                    dudraw.filled_rectangle(x_start + x_step * col_count, y_start + y_step * row_count, half_width, half_length)
                    dudraw.set_pen_color(dudraw.WHITE)
                    dudraw.rectangle(x_start + x_step * col_count, y_start + y_step * row_count, half_width, half_length)
                   
                elif col == Maze.CellValue.OPEN:
                    
                    dudraw.set_pen_color(dudraw.WHITE)  # If an open cell, draw a white rectangle
                    dudraw.filled_rectangle(x_start + x_step * col_count, y_start + y_step * row_count, half_width, half_length)
                    dudraw.set_pen_color(dudraw.WHITE)
                    dudraw.rectangle(x_start + x_step * col_count, y_start + y_step * row_count, half_width, half_length)
                
                else:
                    
                    dudraw.set_pen_color(dudraw.GREEN)  # If an explored cell, draw a green rectangle with a white border 
                    dudraw.filled_rectangle(x_start + x_step * col_count, y_start + y_step * row_count, half_width, half_length)
                    dudraw.set_pen_color(dudraw.WHITE)
                    dudraw.rectangle(x_start + x_step * col_count, y_start + y_step * row_count, half_width, half_length)

                col_count += 1
            
            col_count = 0 
          
            row_count += 1  
            # After each iteration of the for loop:
            # Row_count increases by 1, so you move up a row
            # Col_count resets to 0, so you can restart at left of grid for each new column
     

        # Show each drawing for 1 milisecond
        dudraw.show(1)


    def generate_maze(self, start_row, start_col):


        # Create an empty stack, create current_cell and set to open, then push current_cell to stack

        stack = Stack()
        current_cell = Maze.Cell(start_row, start_col) 
        self.grid[start_row][start_col] = Maze.CellValue.OPEN  
        stack.push(current_cell)   
     


        while not stack.is_empty():
           
            current_cell = stack.pop()

            # Re-draw the canvas after each time something is taken off the stack, to create the animation
            self.draw()

            current_cell_row = current_cell.row
            current_cell_col = current_cell.col

            
            neighbors = []

            # Initialize neighboring_cells to be the 4 cells that are either 2 cells above, below, to the left, or to the right of current_cell
            neighboring_cells = [Maze.Cell(current_cell_row + 2, current_cell_col + 0), Maze.Cell(current_cell_row + 0, current_cell_col + 2), Maze.Cell(current_cell_row -2, current_cell_col + 0), Maze.Cell(current_cell_row + 0, current_cell_col - 2)]
            


            for cell in neighboring_cells:
                row = cell.row
                col = cell.col


                # Sets neighboring cell, and corresponding "in between cell", to open
                if self.is_in_grid(row,col) and self.is_wall(row,col):
                    self.grid[row][col] = Maze.CellValue.OPEN    
                    neighbor = Maze.Cell(row,col)
                    between = self.get_between(current_cell,neighbor)
                    self.grid[between.row][between.col] = Maze.CellValue.OPEN
                    neighbors.append(neighbor)
                

            random.shuffle(neighbors)
            
        
            for neighbor in neighbors:
                stack.push(neighbor)
              

    def solve_maze(self,start_row,start_col):

        # Create an empty queue, initialize current_cell and set to explored, enqueue current_cell onto queue

        queue = Queue()
        current_cell = Maze.Cell(start_row,start_col)
        goal = Maze.Cell(self.width - 2, self.height - 2)
        self.grid[start_row][start_col] = Maze.CellValue.EXPLORED
        queue.enqueue(current_cell)

        while not queue.is_empty():
          
            current_cell = queue.dequeue()
            self.draw()

            # initializes list of the cells either 1 above, below, left, or right of current_cell
            between_cells = [Maze.Cell(current_cell.row + 1, current_cell.col + 0), Maze.Cell(current_cell.row + 0, current_cell.col + 1), Maze.Cell(current_cell.row - 1, current_cell.col + 0), Maze.Cell(current_cell.row + 0, current_cell.col - 1)]
            
            # If we find the goal cell
            if self.grid[current_cell.row][current_cell.col] == self.grid[goal.row][goal.col]:
                return "We found the target"
            
            for cell in between_cells:
                if self.grid[cell.row][cell.col] == Maze.CellValue.OPEN:
                    self.grid[cell.row][cell.col] = Maze.CellValue.EXPLORED
                    
                    queue.enqueue(cell)

    def is_in_grid(self, row, col):     # Method to determine whether a cell is contained in the grid
        if row >= 0 and row < self.width and col >= 0 and col < self.height:
            return True   
        else:
            return False  
        
    def is_wall(self, row, col):        # Method to determine if cell value is Wall for a particular cell
        if self.grid[row][col] == Maze.CellValue.WALL:
            return True                
        else:
            return False              
        
    def get_between(self,current,neighbor):  # Method to determine the cell in between two cells (current and neighbor)

        if current.row == neighbor.row:   
            new_col = int((current.col + neighbor.col) / 2)   
            return Maze.Cell(current.row, new_col) 
         # Keep the row value if it is the same for current and neighbor, change the column value to the average of current.col and neighbor.col
        
        if current.col == neighbor.col:
            new_row = int((current.row + neighbor.row) / 2)
            return Maze.Cell(new_row, current.col)
        # Keep the column value if it is the same for current and neighbor, change the row value to the average of current.row and neighbor.row

if __name__ == "__main__":

    # Create canvas
    dudraw.set_canvas_size(400,400)
    dudraw.set_x_scale(0,1)
    dudraw.set_y_scale(0,1)

    
    # Generate, solve, and draw maze
    my_maze = Maze(39,39)
    my_maze.generate_maze(3,3)

    my_maze.solve_maze(3,3)

    my_maze.draw()

    dudraw.show(float("inf"))


