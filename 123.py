def test_addition():
    assert 1 + 1 == 2
    print("Addition test passed!")

def test_subtraction():
    assert 5 - 3 == 2
    print("Subtraction test passed!")

def test_multiplication():
    assert 3 * 4 == 12
    print("Multiplication test passed!")

def test_division():
    assert 10 / 2 == 5
    print("Division test passed!")

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    print("\nAll tests passed successfully!")
