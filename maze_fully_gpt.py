


import random 
import dudraw
from enum import Enum

class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self, v):
        self.data.append(v)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        raise IndexError("Empty queue")
    
    def first(self):
        if not self.is_empty():
            return self.data[0]
        raise IndexError("Empty queue")
    
    def size(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0 # returns True if queue is empty
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.data = []  # Underlying data structure can be a Python list

    def push(self, v):
        self.data.append(v)  # Add element to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.data.pop()  # Remove and return the top element
        raise IndexError('Pop from an empty stack')

    def top(self):
        if not self.is_empty():
            return self.data[-1]  # Return the top element without removing it
        raise IndexError('Top from an empty stack')

    def size(self):
        return len(self.data)  # Return the size of the stack

    def is_empty(self):
        return len(self.data) == 0  # Return True if the stack is empty

    def __str__(self):
        return str(self.data)  # Return string representation of the stack



class Maze: 

    class CellValue(Enum):
        wall = 0
        open = 1
        explored = 2

    class Cell:
        def __init__(self,row,col):
            self.row = row
            self.col = col 

        def __str__(self):
            return(f"{self.row}, {self.col}")



    def __init__(self, width, height):
        self.width = width 
        self.height = height 
        self.grid = [[Maze.CellValue.wall for _ in range(width)] for _ in range(height)]




    def draw(self):
        dudraw.set_canvas_size(400,400)
        dudraw.clear(dudraw.WHITE)
        for row in self.grid:
            for cell in row:
                if cell == Maze.CellValue.wall:
                    print("*", end="") # Solid block
                elif cell == Maze.CellValue.open:
                    print(" ", end="") # Open block 
                else:
                    print(".", end = "") # Dot, for explored
            print()

    def generate_maze(self, start_row=1, start_col=1):
            stack = Stack()
            current_cell = Maze.Cell(start_row, start_col)
            self.grid[start_row][start_col] = Maze.CellValue.OPEN
            stack.push(current_cell)

            while not stack.is_empty():
                current_cell = stack.pop()
                neighbors = self.get_neighbors(current_cell)

                if neighbors:
                    # Push current cell back onto the stack if there are neighbors
                    stack.push(current_cell)

                    # Randomly shuffle the neighbors and select one
                    random.shuffle(neighbors)
                    chosen_neighbor = neighbors[0]

                    # Open up the path to the neighbor and the neighbor itself
                    self.remove_wall(current_cell, chosen_neighbor)
                    self.grid[chosen_neighbor.row][chosen_neighbor.col] = Maze.CellValue.OPEN

                    # Push the chosen neighbor onto the stack
                    stack.push(chosen_neighbor)

        def get_neighbors(self, cell):
            neighbors = []
            directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # Move by 2 cells to get neighbors
            for drow, dcol in directions:
                new_row = cell.row + drow
                new_col = cell.col + dcol

                if 0 <= new_row < self.height and 0 <= new_col < self.width:
                    if self.grid[new_row][new_col] == Maze.CellValue.WALL:
                        neighbors.append(Maze.Cell(new_row, new_col))

            return neighbors

        def remove_wall(self, cell1, cell2):
            wall_row = (cell1.row + cell2.row) // 2
            wall_col = (cell1.col + cell2.col) // 2
            self.grid[wall_row][wall_col] = Maze.CellValue.OPEN



def solve_maze(self):
        start = Maze.Cell(1, 1)
        goal = Maze.Cell(self.height - 2, self.width - 2)
        queue = Queue()
        queue.enqueue(start)
        self.grid[start.row][start.col] = Maze.CellValue.EXPLORED

        while not queue.is_empty():
            current_cell = queue.dequeue()

            if current_cell.row == goal.row and current_cell.col == goal.col:
                print("Maze solved!")
                return True  # Found the goal

            for neighbor in self.get_adjacent_neighbors(current_cell):
                if self.grid[neighbor.row][neighbor.col] == Maze.CellValue.OPEN:
                    self.grid[neighbor.row][neighbor.col] = Maze.CellValue.EXPLORED
                    queue.enqueue(neighbor)

        print("No solution found.")
        return False  # If we exit the loop, no solution was found

    def get_adjacent_neighbors(self, cell):
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Move by 1 cell to get adjacent neighbors
        for drow, dcol in directions:
            new_row = cell.row + drow
            new_col = cell.col + dcol

            if 0 <= new_row < self.height and 0 <= new_col < self.width:
                if self.grid[new_row][new_col] == Maze.CellValue.OPEN:
                    neighbors.append(Maze.Cell(new_row, new_col))

        return neighbors







"""
def generate_maze(self, start_row = 1, start_col = 1):
        stack = Stack()

        current_cell = Maze.Cell(start_row,start_col)
        self.grid[start_row][start_col] = Maze.CellValue.OPEN
        stack.push(current_cell)

        while not stack.is_empty():
            current_cell = stack.pop()
            neighbors = self.get_neighbors(current_cell)

            if neighbors:
                # Push current cell back onto the stack if there are neighbors
                stack.push(current_cell)

                # Randomly shuffle the neighbors and select one
                random.shuffle(neighbors)
                chosen_neighbor = neighbors[0]

                # Open up the path to the neighbor and the neighbor itself
                self.remove_wall(current_cell, chosen_neighbor)
                self.grid[chosen_neighbor.row][chosen_neighbor.col] = Maze.CellValue.OPEN

                # Push the chosen neighbor onto the stack
                stack.push(chosen_neighbor)

    def get_neighbors(self, cell):
        neighbors = []
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # Move by 2 cells
        for drow, dcol in directions:
            new_row = cell.row + drow
            new_col = cell.col + dcol

            if 0 <= new_row < self.height and 0 <= new_col < self.width:
                if self.grid[new_row][new_col] == Maze.CellValue.WALL:
                    neighbors.append(Maze.Cell(new_row, new_col))

        return neighbors


"""