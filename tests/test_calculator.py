import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from calculator import add, subtract, multiply, divide, power


def test_basic_operations():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(4, 6) == 24
    assert divide(9, 3) == 3


def test_power():
    assert power(2, 8) == 256
    assert power(5, 0) == 1
