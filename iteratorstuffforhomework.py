

class ArrayList:
    def __init__(self):
        self.capacity = 100  # Initial capacity
        self.size = 0        # Current number of elements
        self.array = [None] * self.capacity  # Internal array with initial capacity
    
    def append(self, value):
        if self.size == self.capacity:
            self._expand_array()  # Expand capacity if full
        self.array[self.size] = value  # Add new value
        self.size += 1  # Increase size
    
    def _expand_array(self):
        # Geometric expansion: double the capacity
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array  # Replace with expanded array
    
    def __iter__(self):
        return ArrayListIterator(self)  # Return iterator instance
    
    def __len__(self):
        return self.size  # Returns the number of elements in the array

class ArrayListIterator:
    def __init__(self, array_list):
        self.array_list = array_list  # Reference to the ArrayList
        self.current = 0  # Start at the first element
    
    def __iter__(self):
        return self  # Return itself as iterator
    
    def __next__(self):
        if self.current < self.array_list.size:
            value = self.array_list.array[self.current]  # Get current value
            self.current += 1  # Move to the next element
            return value  # Return current value
        else:
            raise StopIteration  # Stop iteration when done

def test_arraylist_iterator():
    array_list = ArrayList()
    
    # Append integers from 1 to 100
    for i in range(1, 101):
        array_list.append(i)
    
    # Use the iterator to calculate the sum of elements in ArrayList
    total = 0
    for num in array_list:
        total += num
    
    # Use algebraic formula for sum of first 100 integers: n(n+1)/2
    expected_sum = 100 * (100 + 1) // 2
    
    print(f"Total calculated using iterator: {total}")
    print(f"Expected total: {expected_sum}")
    
    # Verify that the calculated sum matches the expected sum
    assert total == expected_sum, "The sum does not match the expected value."

# Running the test driver
test_arraylist_iterator()

