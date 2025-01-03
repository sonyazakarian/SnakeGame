
"""
def mystery_method(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]



# a: suppose that mystery_method() takes in a SinglyLinkedList as an argument
def mystery_method(l):
    # Assume that 'l' contains 'n' elements
    while not l.is_empty():
        l.remove_first()

# e.g. let's say l is a list that is 7 elements long
# so while l is not empty (l is 7) remove first
# then remove 2nd





# b: #suppose that mystery_method() takes in a SinglyLinkedList as an argument
def mystery_method(l):
    # Assume that 'l' contains 'n' elements
    while not l.is_empty():
        l.remove_last()


# c: suppose that mystery_method() takes in a DoublyLinkedList as an argument
def mystery_method(l):
    # Assume that 'l' contains 'n' elements
    while not l.is_empty():
        l.remove_first()


# d: suppose that mystery_method() takes in a DoublyLinkedList as an argument
def mystery_method(l):
    # Assume that 'l' contains 'n' elements
    while not l.is_empty():
        l.remove_last()


# e: suppose that mystery_method() takes in a CircularDoublyLinkedList as an argument
def mystery_method(l):
    # Assume that 'l' contains 'n' elements
    while not l.is_empty():
        l.delete_cursor()

# o1

#suppose that mystery_method() takes in a CircularDoublyLinkedList as an argument
def mystery_method(l):
    # Assume that 'l' contains 'n' elements
    while not l.is_empty():
        l.advance_cursor(3)
        l.delete_cursor()




total = 0
for i in range(1,9):
    print("Julia")
    total += 1
print(total)
    


    first question has to be right 




total = 0
n = 10
for i in range(1,n+1):
    for j in range(i):
        total += 1

print(total)

"""

import random 
def mystery_function():
    n = int(input("How large an array would you like?"))
    array = [random.random() for i in range(n)]

    outer_loop_ran = 0
    inner_loop_ran = 0

    for i in range(1,n+1):
        outer_loop_ran += 1
        for j in range(i):
            inner_loop_ran += 1
            array[j] += 1
    return array 

result = mystery_function()
