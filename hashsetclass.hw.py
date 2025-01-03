


class HashSet:
    PRIMES = [97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    def __init__(self):
        self._init_table(16)  # Initialize the hash table with 16 buckets

    def _init_table(self, new_capacity):
        self.table = [[] for _ in range(new_capacity)]  # List of empty lists (buckets)
        self.size = 0
        self.capacity = new_capacity

    def get_size(self):
        return self.size

    def discard(self, v):
        index = self._hash_and_compress(v)
        if v in self.table[index]:
            self.table[index].remove(v)
            self.size -= 1

    def contains(self, v):
        index = self._hash_and_compress(v)
        return v in self.table[index]

    def add(self, v):
        if not self.contains(v):
            if self.size / self.capacity > 0.75:
                self._expand_table()
            index = self._hash_and_compress(v)
            self.table[index].append(v)
            self.size += 1

    def union(self, B):
        union_set = HashSet()
        for bucket in self.table:
            for v in bucket:
                union_set.add(v)
        for v in B:
            union_set.add(v)
        return union_set

    def intersection(self, B):
        intersection_set = HashSet()
        for bucket in self.table:
            for v in bucket:
                if v in B:
                    intersection_set.add(v)
        return intersection_set

    def difference(self, B):
        difference_set = HashSet()
        for bucket in self.table:
            for v in bucket:
                if v not in B:
                    difference_set.add(v)
        return difference_set

    def __iter__(self):
        for bucket in self.table:
            for value in bucket:
                yield value

    def __str__(self):
        elements = [str(v) for bucket in self.table for v in bucket]
        return "{" + ", ".join(elements) + "}"

    def _hash_and_compress(self, v):
        hash_value = hash(v)
        return hash_value % self.capacity

    def _expand_table(self):
        old_table = self.table
        new_capacity = self.capacity * 2
        self._init_table(new_capacity)
        for bucket in old_table:
            for value in bucket:
                self.add(value)

class Driver:

    def __init__(self, female_file, male_file):
        self.female_file = female_file
        self.male_file = male_file

    def load_names(self, file_name):
        names = HashSet()

        with open(file_name, 'r') as file:
            for line in file:
                name = line.split()[0]
                names.add(name)
        
        return names 
    
    def find_common_names(self):
        female_names = self.load_names(self.female_file)
        male_names = self.load_names(self.male_file)

        common_names = female_names.intersection(male_names)
        number_of_common_names = common_names.get_size()

        print(f"Common names: {common_names}")
        print(f"Number of common names: {number_of_common_names}")




if __name__ == "__main__":

    new = HashSet()
    print(new)

    new.add(1)
    new.add(2)
    new.add(3)

    # print(new)

    # new.discard(1)

    print(new)

    # print(new.contains(1))

    # print(new.get_size())

    print("union, intersection, and difference")

    print(new.union({1,2,3,4,5}))

    print(new.intersection({1,2,3,4,5}))

    print(new.difference({1,2}))


    homework_driver = Driver('femaleNames2016.txt', 'maleNames2016.txt')
    homework_driver.find_common_names()




    