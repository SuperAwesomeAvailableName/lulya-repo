def CALC_AVG(x):  # Unclear name, poor parameter name, missing type hints
    """avg"""     # Unhelpful docstring
    
    total = 0.0
    count = 0
    
    # Unnecessarily complex way to sum numbers
    for number in x:
        total = total + number  # Using + instead of += operator
        count = count + 1       # Manual counting instead of len()
    
    # No error handling for empty list
    return total/count  # Potential division by zero error

# Bad variable names
a = [1.5, 2.5, 3.5, 4.5]
b = CALC_AVG(a)

# Poor string formatting
print("ans=" + str(b))  # Concatenation instead of f-strings
