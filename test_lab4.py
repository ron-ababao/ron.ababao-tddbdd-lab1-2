import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a*b

@pytest.fixture

def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Change the calculator's name
    base_calculator.name = "Changed Calculator"
    print("This calculator's name is " + base_calculator.name)
    
    assert True
    
def test_lab4_test2(base_calculator):
    print(f"This calculator's name is {base_calculator.name}")
    
    assert True

def test_answer_subtract(base_calculator):
    assert Calculator.subtract(base_calculator,3,5) == -2
    print(Calculator.subtract(base_calculator,3,5))
    assert Calculator.subtract(base_calculator,5,2) == 3
    print(Calculator.subtract(base_calculator,5,2))
    assert Calculator.subtract(base_calculator,3,3) == 0
    print(Calculator.subtract(base_calculator,3,3))
    assert Calculator.subtract(base_calculator,-4,-10) == 6
    print(Calculator.subtract(base_calculator,-4,-10))
    
def test_answer_multiply():
    assert Calculator.multiply(base_calculator,5,3) == 15
    print (Calculator.subtract(base_calculator,5,3))
    assert Calculator.multiply(base_calculator,1,6) == 6
    print (Calculator.subtract(base_calculator,1,6))
    assert Calculator.multiply(base_calculator,0,0) == 0
    print (Calculator.subtract(base_calculator,0,0))
    assert Calculator.multiply(base_calculator,2.5,2) == 5
    print(Calculator.subtract(base_calculator,2.5,2))
