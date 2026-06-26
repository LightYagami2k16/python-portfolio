# Simple Calculator
# My first Python project!

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: You can't divide by zero!"
    return a / b

def show_menu():
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Main program
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break
    elif choice in ["1", "2", "3", "4"]:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} x {num2} = {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {result}")
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
