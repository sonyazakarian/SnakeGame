

def is_balanced(phrase: str):
    left_parentheses = 0
    right_parentheses = 0
    left_brace = 0
    right_brace = 0
    left_bracket = 0
    right_bracket = 0
    for character in phrase:
        if character == '(':
            left_parentheses += 1


        if character == ')':
            right_parentheses += 1


        if character == '{':
            left_brace += 1


        if character == '}':
            right_brace += 1
            

        if character == '[':
            left_bracket += 1


        if character == ']':
            right_bracket += 1

    if left_parentheses == right_parentheses and left_brace == right_brace and left_bracket == right_bracket:
        return True
    else:
        return False
    

class Stack:

    def __init__(self):
        self.data = []   # Will use a Python list as the data structure

    def push(self, v):
        self.data.append(v)  # Add element to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.data.pop()  # Remove and return the top element
        raise IndexError("Empty stack")

    def top(self):
        if not self.is_empty():
            return self.data[-1]  # Return the top element without removing it
        raise IndexError("Empty stack")

    def size(self):
        return len(self.data)  # Return the size of the stack

    def is_empty(self):
        return len(self.data) == 0  # Return True if the stack is empty

    def __str__(self):
        return str(self.data)  # Return string representation of the stack
    

sonyas_stack = Stack()
sonyas_stack.push(4)
sonyas_stack.is_empty()


if __name__=='__main__':
    example_string=input('What string would you like to test? ')
    print(is_balanced(example_string))



