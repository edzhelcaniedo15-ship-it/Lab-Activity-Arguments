def compute(operation, num1, num2=1):
    """Performs basic arithmetic based on the operation string."""
    operation = operation.lower() # Standardize input
    
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"

print("\n--- Part 5 Output ---")
# 1. Positional arguments for addition
print(f"Task 1: {compute('add', 5, 10)}")

# 2. Keyword arguments for multiplication
print(f"Task 2: {compute('multiply', num1=3, num2=4)}")

# 3. Use default for subtraction (20 - 1 = 19)
print(f"Task 3: {compute('subtract', 20)}")

# 4. Invalid operation
print(f"Task 4: {compute('divide', 10, 2)}")