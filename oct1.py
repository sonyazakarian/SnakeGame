

import numpy as np

class ArrayList:

    def __init__(self):
        self.container_size = 10
        self.size = 0
        self.the_array = np.empty(self.container_size, dtype=int) # Creates an array with 10 blocks for integers.

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.the_array[index]
    
    def set(self, index, value):
        self.check_valid_index(index)
        result = self.the_array[index]
        self.the_array[index] = value
        return result 
    
    def check_valid_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        self.expand_array()
        for i in range(self.size, index, -1):
            self.the_array[i] = self.the_array[i - 1]
        self.the_array[index] = value    
        self.size += 1

    def append(self, value):
        # Adds value at the end of the array.
        self.expand_array()
        self.the_array[self.size] = value
        self.size += 1
    
    def expand_array(self):
        if self.size == self.container_size:
            # Double the container size
            new_container_size = self.container_size * 2
            new_array = np.empty(new_container_size, dtype=int)
            # Copy elements to new array
            for i in range(self.size):
                new_array[i] = self.the_array[i]
            self.the_array = new_array
            self.container_size = new_container_size

def main():
    arr = ArrayList()
    print(f"Initial size: {arr.get_size()}")
    arr.append(5)
    arr.append(10)
    arr.append(15)
    print(f"Size after appending elements: {arr.get_size()}")
    print(f"The array contents: {arr.the_array[:arr.get_size()]}")
    
    arr.insert(0, 20)
    print(f"The array after inserting 20 at index 0: {arr.the_array[:arr.get_size()]}")

if __name__ == '__main__':
    main()
