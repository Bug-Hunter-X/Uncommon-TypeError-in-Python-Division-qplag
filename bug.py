def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid data types for division!")
        return None

# Example usage:
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Cannot divide by zero! None
print(function_with_uncommon_error(10, "2")) # Output: Error: Invalid data types for division! None