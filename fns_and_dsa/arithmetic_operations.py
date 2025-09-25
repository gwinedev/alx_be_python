def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
            print(f"Division of number by zero is not allowed")
        return num1 / num2
