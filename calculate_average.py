def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        The arithmetic mean of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
        
    # Validate that all elements are actually numbers
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError(f"All elements must be numbers, got {type(num).__name__}")
        
    return sum(numbers) / len(numbers)

# Example usage
values = [1.5, 2.5, 3.5, 4.5]
result = calculate_average(values)
print(f"The average is: {result}")
# Hi this indicates custom guidelines working

