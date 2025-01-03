

"""
check if i did the preclass 

Set ADT

Mathematical set = group of objects 

Set = group of unique objects

Interface:
- __init__
- __str__ 
- add(e)
- discard(e)
- get_size(e)
- contains(e)
- union(T)      # all elements in either set. T is a parameter, T is the other set we're comparing to. 
- intersection(T)   # all elements in both sets. 
- difference(T)     # elements in self, not in T


"""

class SetList:
    def __init__(self):
        self.elements = []

    def add(self, element):
        if not element in self.elements:
            self.elements.append(element)
        # figure out if i did this right, look at it again 

    def contains(self, element):
        return element in self.elements
    
    def get_size(self):
        return len(self.elements)
    

    def __str__(self):   
        result = '{'
        for value in self.elements:
            result += f'{value}, '
        result = result.rstrip(',')
        result += '}'
        return result 
    

    def discard(self, value):
        try:
            self.elements.remove(value)
        except:
            return
    
    def union(self, set: list[int]):
        union_of_values = []
        for element in self.elements:
            union_of_values.append(element)
        for value in set:
            if value not in union_of_values:
                union_of_values.append(value)
        return union_of_values
    

    def intersection(self, set: list[int]):
        intersection_of_values = []
        for element in self.elements:
            if element in set:
                intersection_of_values.append(element)
        return intersection_of_values
    
    def difference(self, set: list[int]):
        difference_of_values = []
        for element in self.elements:
            if element in set:
                pass
            else:
                difference_of_values.append(element)
        return difference_of_values

def main():
    foo = SetList()
    foo.add(3)
    foo.add(4)
    foo.add(5)
    foo.add(6)
    foo.discard(6)
    foo.add(10)
    foo.add(12)
    
    print(foo)

    print(foo.intersection([1,4,5,10]))

    print(foo.union([1,4,5,10]))

    print(foo)

    print(foo.difference([1,2,3,4,5]))

if __name__ == '__main__':
    main()

            








