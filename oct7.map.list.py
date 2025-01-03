

"""
Talking about 2 abstract data types: maps and 

Map ADT  (some call this the Dictionary ADT. some people also call them Associations.)
- Association between keys and values
- Key must be unique 
- Index on Data


Interface:
- get_size
- get(key)
- put(key, value)
- remove(key)
- keys()
- values()
items - ()

Today we will implement this using Python lists. It is not the most efficient way to do this, but good to just understand the interface. 


"""


class MapList :
    def __init__(self):
        self.elements = []

    def get_size(self):
        return len(self.elements)

    def get(self, key_to_find):
        for (key, value) in self.elements:
            if key == key_to_find:
                return value 
        raise KeyError
        
    def put(self, key, value):
        try:
            val = self.get(key)   # is this taking out a value for the key we want to change if its already there?
            self.elements.remove((key,val))
            self.elements.append((key,value))  # and then here its just adding that new value?
        except KeyError:
            self.elements.append((key,value))

    def remove(self, key_to_remove):
        match = 0
        for (key, value) in self.elements:
            if key == key_to_remove:
                self.elements.remove((key,value))
                match += 1
        if match == 0:
            return None


    def keys(self):
        result = []
        for (key,value) in self.elements:
            result.append(key)
        return result 

    def values(self):
        result = []
        for (key,value) in self.elements:
            result.append(value)
        return result 


    def items(self):
        result = []
        for (key,value) in self.elements:
            result.append((key,value))
        return result 


    def __str__(self):   
        result = '{'
        for (key,value) in self.elements:
            result += f'({key}:{value})'
        result = result.rstrip(',')
        result += '}'
        return result 


    def key_iter(self):
        return iter(self.keys())

    def value_iter(self):
        return iter(self.values())
    
    def item_iter(self):
        return iter(self.items())


def main():
    foo = MapList()
    foo.put('a', 1)
    foo.put('b', 1)
    foo.put('c', 3)
    for k in foo.keys():
        print(k)
    for k in foo.key_iter():
        print(k)
    print(foo)

    print(next(foo.key_iter()))

    print(foo.keys())

    print(foo)

    foo.remove('a')

    print(foo)

    foo.remove('d')

    print(foo)


if __name__ == '__main__':
    main()