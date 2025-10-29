def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        The arithmetic mean of the numbers
        
    Example:
        values = [1.5, 2.5, 3.5, 4.5] -> 3.0
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
        
    return sum(numbers) / len(numbers)

values = [1.5, 2.5, 3.5, 4.5]
result = calculate_average(values)
print(f"The average is: {result}")
# Hi this indicates custom guidelines working
