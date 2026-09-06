def calculator():
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid number. Please try again.")

    while True:
        operator = input("Enter the operator (+, -, *, /): ")

        if operator in operations:
            break

        print("Invalid operator. Please choose +, -, *, or /.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid number. Please try again.")

    try:
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


while True:
    calculator()

    question = input("Do you want to continue? (y/n): ")

    if question.lower() != "y":
        print("Thank you for using the calculator!")
        print("Goodbye!")
        break