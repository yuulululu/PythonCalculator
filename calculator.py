import math


def calculate(a, op, b):
    operations = {
        "+": lambda x, y: x+y,
        "-": lambda x, y: x-y,
        "*": lambda x, y: x*y,
        "/": lambda x, y: x/y,
        "%": lambda x, y: x%y,
        "^": lambda x, y: math.pow(x, y),
    }

    if op not in operations:
        raise ValueError("There is no this syntax")
    if op in "/%" and b == 0:
        raise ZeroDivisionError("Can't Divide with 0")

    return operations[op](a, b)

def main():
    while True:
            try:
                a = float(input("First Number: "))
                op = input("Syntax(+ - * / % ^): ").strip()
                b = float(input("Second Number: "))
                print(f"Sum: {calculate(a, op, b):g}")
            except ValueError as e:
                print(e if "Syntax" in str(e) else "Please insert the right syntax.")
            except ZeroDivisionError as e:
                print(e)

            if input("Calculate more?(y/n): ").strip().lower() != "y":
                break

if __name__ == "__main__":
    main()
