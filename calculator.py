1# Simple Calculator

# Get user input
num1 = float(input("Enter first number: "))  # Ask for the first number
operator = input("Enter operation (+, -, *, /): ")  # Ask for the operation
num2 = float(input("Enter second number: "))  # Ask for the second number

# Perform operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
else:
    result = "Invalid operator!"

# Print result
print(f"{num1} {operator} {num2} = {result}")
