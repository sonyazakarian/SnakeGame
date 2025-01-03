
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
    


def is_balanced(phrase: str) -> bool:
    """
    Determines if the parentheses, square brackets, and curly braces in a string are properly balanced.
    
    Argument:
        phrase (str): This is the input string to check.
        
    Returns:
        bool: True if the string is balanced, False otherwise.
    """
    stack = Stack()

    bracket_map = {')': '(', '}': '{', ']': '['}

    for character in phrase:
        
        if character in bracket_map.values(): # If character is (, {, or [
            stack.push(character)
        
        elif character in bracket_map:       # If character is ), }, or ]
            if stack.is_empty() or stack.top() != bracket_map[character]:
                return False  
            stack.pop()  

    return stack.is_empty()  # True means balanced, false means unbalanced



if __name__ == '__main__':
    while True:
        example_string = input('What string would you like to test? ')
        print(is_balanced(example_string))
