def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list[float]): List of numbers to average
        
    Returns:
        float: The arithmetic mean of the numbers
        
    Raises:
        ValueError: If the list is empty
        
    Example:
        >>> values = [1.5, 2.5, 3.5, 4.5]
        >>> result = calculate_average(values)
        >>> print(f"The average is: {result}")
        The average is: 3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
        
    return sum(numbers) / len(numbers)
