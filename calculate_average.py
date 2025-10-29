def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    nums = [1.5, 2.5, 3.5, 4.5]
    result = calculate_average(nums)
    print(f"The average is: {result}")

