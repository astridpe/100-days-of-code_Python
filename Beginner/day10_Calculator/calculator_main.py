from replit import clear
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    first_number = float(input("What\'s the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What\'s the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation \n").lower()

        if choice == "y":
            first_number = answer
        elif choice == "n":
            should_continue = False


calculator()
