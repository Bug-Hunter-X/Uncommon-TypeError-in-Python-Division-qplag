def function_with_uncommon_error_solution(a, b):
    try:
        if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
            raise TypeError("Invalid data types for division!")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

#Example Usage
print(function_with_uncommon_error_solution(10,2)) #Output 5.0
print(function_with_uncommon_error_solution(10,0)) #Output Error: Cannot divide by zero! None
print(function_with_uncommon_error_solution(10,"2")) #Output Error: Invalid data types for division! None