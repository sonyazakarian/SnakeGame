

def quiz_function(n):
    result = 0        # C1
    for i in range(n):     # nC2
        for j in range(5): # 5n * C3
            result += i + 2 * j   # 5n * C4
    return result 

# C1 + nC2 + 5nC3 + 5nC4

# C1 + (C2 + 5C3 + 5C4)n

# Answer is O(n)





