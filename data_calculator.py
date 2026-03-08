# Welcome Message
print("=" * 50)
print("Welcome to the Data Calculator!")
print("=" * 50)

#User Input Collection
first_number = float(input("Please enter the first number: "))
second_number = float(input("Please enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

#Conditional Logic for Operations
if operation == "+":
    result = first_number + second_number
    print(f"The result of {first_number} + {second_number} is: {result}")
elif operation == "-":
    result = first_number - second_number
    print(f"The result of {first_number} - {second_number} is: {result}")
elif operation == "*":
    result = first_number * second_number
    print(f"The result of {first_number} * {second_number} is: {result}")
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
        print(f"The result of {first_number} / {second_number} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")