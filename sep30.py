

import numpy as np
# what is numpy?

# when are office hours for this class?


class ArrayList:

    def __init__(self):
        self.container_size = 10
        self.size = 0
        self.the_array = np.empty(self.container_size, dtype=int) # creates an array with 10 blocks. we want all entries to be integer types. 


    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get(self,index):
        if index < 0 or index >= self.size:
            raise IndexError
        return self.the_array[index]
    
    def set(self,index,value):
        self.check_valid_index(index)
        result = self.the_array[index]
        self.the_array[index] = value
        return result 
    
    def check_valid_index(self,index):
        if index < 0 or index >= self.size:
            raise IndexError
        
    def insert(self,index,value):
        if index < 0 or index > self.size:
            raise IndexError
        self.expand_array()
        for i in range(self.size, index, -1):
            self.the_array[i] = self.the_array[i-1]
        self.the_array[index] = value    

    def expand_array(self):
        if self.size == self.container_size:
            self.container     


def main() :
    arr = ArrayList()
    print(arr.size())
    arr.append(5)
    arr.append(10)
    arr.append(15)
    print(arr.size())
    print(f"the array is: {arr}")
    arr.insert(0,20)
    print(f"the array is: {arr}")




if __name__ == '__main__' :
    main()
