import pytest
from L5_test import user_name,square,add,subtract,multiply,divide,modulus

# pytest = a test runner + assertion tool. It doesn't care what kind of test you write (unit, integration, API, e2e) — it just finds your test_*.py files, runs the functions, and checks your assert statements.

#pytest imports your file to find test_* functions. Any code at module level (like input()) runs before tests start — and pytest captures stdin to keep output clean. You can't interact with pytest mid-collection.

list = ["sourav","rajeev","shyam"]

def test_user_name():
     for name in list:
        assert user_name(name) == f"hello, {name}"

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

def test_add():
    assert add(2,3) == 5
    assert add(3,4) == 7
    assert add(4,5) == 9

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(10,4) == 6
    assert subtract(7,2) == 5

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(4,5) == 20
    assert multiply(6,7) == 42

def test_divide():
    assert divide(6,3) == 2
    assert divide(10,2) == 5
    assert divide(9,3) == 3

def test_modulus():
    assert modulus(5,3) == 2
    assert modulus(10,4) == 2
    assert modulus(7,2) == 1

def test_divide_by_zero():
    assert divide(5,0) == None
    assert divide(10,0) == None
    assert divide(7,0) == None

def test_str():
    with pytest.raises(TypeError):
            divide("5","2")
    with pytest.raises(TypeError):
            divide("10","2")
    with pytest.raises(TypeError):
            modulus("7","2")