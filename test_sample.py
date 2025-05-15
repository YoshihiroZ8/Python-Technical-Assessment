# test_sample.py
# A simple test file to demonstrate pytest functionality

def test_addition():
    """Test that addition works correctly."""
    assert 1 + 1 == 2
    
def test_string_methods():
    """Test string manipulation methods."""
    text = "hello world"
    assert text.upper() == "HELLO WORLD"
    assert text.capitalize() == "Hello world"
    assert "hello" in text
    
def test_list_operations():
    """Test list operations."""
    my_list = [1, 2, 3, 4, 5]
    assert len(my_list) == 5
    assert sum(my_list) == 15
    
# A function that will be tested
def multiply(a, b):
    return a * b

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, -1) == 1

