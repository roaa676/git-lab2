"""Simple calculator module."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 6 =", multiply(4, 6))
    print("9 / 3 =", divide(9, 3))
