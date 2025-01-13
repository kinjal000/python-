def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error! Division by zero."
    else:
        return "Invalid operation."

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (add, subtract, multiply, divide): ")
print("Result:", calculator(num1, num2, op))