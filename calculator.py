import re
from typing import Tuple

def calculate(a: float, b: float, operation: str) -> float:
    """Perform a single arithmetic operation on two numbers."""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Invalid operation")


def parse_expression(expression: str) -> Tuple[float, float, str]:
    pattern = r"^\s*(-?(?:\d+(?:\.\d+)?|\.\d+))\s*([+\-*/])\s*(-?(?:\d+(?:\.\d+)?|\.\d+))\s*$"
    
    match = re.match(pattern, expression)
    if not match:
        raise ValueError(
            'Invalid expression format. Use: number operator number (e.g. 2+3). '
            'Use "." as decimal separator. Thousands separators are not supported.'
        )

    a_str, operation, b_str = match.groups()
    return float(a_str), float(b_str), operation


def main() -> None:
    print("Simple Calculator Program")

    while True:
        expression = input("Enter expression (e.g. 2+3) or q to quit: ").strip()

        if expression.lower() == "q":
            print("Goodbye!")
            break

        try:
            a, b, operation = parse_expression(expression)
            result = calculate(a, b, operation)
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
