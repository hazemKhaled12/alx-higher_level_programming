#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    def calc():
        if len(sys.argv) - 1 != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            sys.exit(1)

        if sys.argv[2] not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            solve_and_print(int(sys.argv[1]), int(sys.argv[3]), sys.argv[2])

    def solve_and_print(num, num2, op):
        result = 0
        if op == "+":
            result = add(num, num2)
        if op == "-":
            result = sub(num, num2)
        if op == "*":
            result = mul(num, num2)
        if op == "/":
            result = div(num, num2)
        print("{} {} {} = {}".format(num, op, num2, result))
        sys.exit(0)

    calc()
