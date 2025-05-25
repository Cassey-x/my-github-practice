num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))
operator: str = input("Enter the operator ['+', '-', '*', '/']: ")


match operator:
    case "+":
        result: float | None = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = None
        if num2 == 0:
            print("You tried to divide by zero which is invalid")
        else:
            result = num1 / num2
    case _:
        result = None
        print("invalid operator")

if result is None:
    print("No result for you you fool.")
else:
    print("result =", result)