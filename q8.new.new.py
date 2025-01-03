
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
    

def is_balanced(phrase: str):
    stack = Stack()

    for character in phrase:
        if character == '(' or character == '{' or character == '[':
            stack.push(character)

        if (character == ')' and stack.top() == '(' ) or (character == '}' and stack.top() == '{' ) or (character == ']' and stack.top() == '['):
            stack.pop(character)


    if stack.is_empty() == True:
        return True
    else:
        return False


if __name__=='__main__':
    example_string=input('What string would you like to test? ')
    print(is_balanced(example_string))



