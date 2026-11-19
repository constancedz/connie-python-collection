def calculate_average(numbers):
    # Constraint: Cannot divide by zero if list is empty
    if not numbers:
        return 0.0
    
    return sum(numbers) / len(numbers)
