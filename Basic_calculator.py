# Basic Calculator Program

# Step 1: Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))  # Convert input to float for decimal support
num2 = float(input("Enter the second number: "))

# Step 2: Ask the user to choose a mathematical operation
operation = input("Enter an operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

# Step 3: Perform the chosen operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    # Division requires checking for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is undefined.")
else:
    # If an invalid operation is entered
    print("Invalid operation. Please enter +, -, *, or /.")
    # Addition
    num1: 12
    num2: 4
    operation: (+, -, *, /): +
