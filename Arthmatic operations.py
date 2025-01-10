# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division carefully to avoid division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero is not allowed)"

# Display the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")

Output:
Enter the first number: 4
Enter the second number: 3
Addition: 4.0 + 3.0 = 7.0
Subtraction: 4.0 - 3.0 = 1.0
Multiplication: 4.0 * 3.0 = 12.0
Division: 4.0 / 3.0 = 1.3333333333333333

