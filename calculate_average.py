    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        The arithmetic mean of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    nums = [1.5, 2.5, 3.5, 4.5]
    result = calculate_average(nums)
    print(f"The average is: {result}")


# Hello, I am AmazonReviewAgent, an AI assistant helping with code reviews!

# Hi this indicates custom guidelines working
