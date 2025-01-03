
def is_balanced(s: str) -> bool:
    """
    Determines if the parentheses, square brackets, and curly braces in the input string are balanced.

    Args:
        s (str): The input string containing brackets and other characters.
    
    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    # Dictionary to map closing brackets to their corresponding opening brackets
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    # Stack to hold the opening brackets
    stack = []

    for char in s:
        if char in matching_bracket.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in matching_bracket.keys():
            # If it's a closing bracket, check if it matches the top of the stack
            if not stack or stack.pop() != matching_bracket[char]:
                return False

    # If the stack is empty, all brackets were matched
    return not stack

# Driver code to test the function
if __name__ == '__main__':
    example_string = input('What string would you like to test? ')
    print(is_balanced(example_string))