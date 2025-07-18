def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    while True:
        num1 = float(input("What is the first number?: "))
        should_continue = True
        while should_continue:
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What is the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
            choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation, or 'exit' to quit: ")
            if choice == 'y':
                num1 = answer
            elif choice == 'n':
                should_continue = False
            else:
                return

calculator()