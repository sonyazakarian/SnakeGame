



import time

class ArrayList:
    def __init__(self):
        self.array = [None] * 10
        self.size = 0
        self.capacity = 10

    def append(self, value):
        if self.size == self.capacity:
            self.expand_array()
        self.array[self.size] = value
        self.size += 1

    def expand_array(self):
        # Geometric expansion (doubling capacity)
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

class ArrayListArithmetic(ArrayList):
    def expand_array(self):
        # Arithmetic expansion (adding 1000)
        self.capacity += 1000
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

def time_append(ArrayListClass, n, num_trials):
    total_time = 0
    for _ in range(num_trials):
        alist = ArrayListClass()
        start_time = time.time()
        for i in range(n):
            alist.append(i)
        total_time += (time.time() - start_time)
    return total_time / num_trials

if __name__ == "__main__":
    num_trials = 5  # Adjust this number for more accurate results
    
    print(f"n\t\telapsed_time_arithmetic\t\truntime_arithmetic\t\telapsed_time_geometric\t\truntime_geometric")
    
    for n in [100000, 200000, 400000, 800000]:
        # Time for ArrayListArithmetic
        time_arithmetic = time_append(ArrayListArithmetic, n, num_trials)
        runtime_arithmetic = time_arithmetic / num_trials
        
        # Time for ArrayList (Geometric expansion)
        time_geometric = time_append(ArrayList, n, num_trials)
        runtime_geometric = time_geometric / num_trials

        print(f"{n}\t\t{runtime_arithmetic:.6f}\t\t{runtime_geometric:.6f}\t")
