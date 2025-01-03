


from DoublyLinkedList import DoublyLinkedList
import numpy
import random




class Item: 
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def __str__(self):
        return f"{self.key}: {self.value}"
    
    def __repr__(self):
        return str(self)
    
    def set_value(self, new_value):
        old_value = self.value
        self.value = new_value
        return old_value
    

class HashMap:
    PRIMES = (251)

    def __init__(self):
        self.init_table(16)

    def init_table(self, new_capacity):
        self.the_table = numpy.empty(new_capacity, dtype = DoublyLinkedList)
        self.PRIMES

        finall

        # Create the buckets
        for i in range(len(self.the_table)):
            self.the_table[i] = DoublyLinkedList()


    def load_factor(self):
        return self.size / len(self.the_table)
    
    def expand_table(self):
        if self.load_factor() >= 0.75:
            old_items = self.items()
            self.init_table(2 * len(self.the_table))
            for i in old_items:
                self.put(i)

    def hash_and_compress(self,k):
        return((hash(k) * self.a + self.b) % self.prime)
    

def main():
    the_map = HashMap()
    with open( 'baby_names2016.txt', 'r') as infile:
        for line in infile:
            data = line.rstrip().split(' ')
            the_map.put(data[0], int(data[1]))

    the_map.output_table_info()






"""

pseudocode

if load_factor > 0.75:

    create table with twice current size

    for every element in current table:
        hash them into new larger table 

    make new table the current table 
    

"""




    for i in range(100):
        the_map.put(i, random.randint(1,500))


    
