import pytest

class Calculator:
    def add(self, a, b):
        return a + b

calc=(Calculator())

print(calc.add(1, 1))
print(calc.add(1.0,2.5))
print(calc.add(0,0))
print(calc.add(-5,-6))


def test_answer():
    assert calc.add(1, 1) == 2

def test_answer2():
    assert calc.add(1.0,2.5) == 3.5
    
def test_answer3():
    assert calc.add(0,0) == 0

def test_answer4():
    assert calc.add(-5,-6) == -11

