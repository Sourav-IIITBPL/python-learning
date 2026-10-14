from L5_test import square,add,subtract,multiply,divide,modulus
def main():
    num1 = int(input("enter the first number to test "))
    num2 = int(input("enter the second number to test "))
    test_square(num1,num2)
    test_add(num1,num2)
    test_subtract(num1,num2)
    test_multiply(num1,num2)
    test_divide(num1,num2)
    test_modulus(num1,num2)


def test_square(num1,num2):
    try:
        assert square(num1) == num1*num1
        assert square(num2) == num2*num2
        print("square function passed the test")
    except AssertionError:
        print("square function failed the test")

def test_add(num1,num2):
    try:
        assert add(num1,num2) == num1+num2
        print("add function passed the test")
    except AssertionError:
        print("add function failed the test")

def test_subtract(num1,num2):
    try:
        assert subtract(num1,num2) == num1-num2
        print("subtract function passed the test")
    except AssertionError:
        print("subtract function failed the test")

def test_multiply(num1,num2):
    try:
        assert multiply(num1,num2) == num1*num2
        print("multiply function passed the test")
    except AssertionError:
        print("multiply function failed the test")

def test_divide(num1,num2):
    try:
        assert divide(num1,num2) == num1/num2
        print("divide function passed the test")
    except AssertionError:
        print("divide function failed the test")

def test_modulus(num1,num2):
    try:
        assert modulus(num1,num2) == num1%num2
        print("modulus function passed the test")
    except AssertionError:
        print("modulus function failed the test")


if __name__ == "__main__":
    main()
    