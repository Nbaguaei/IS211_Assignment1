class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisible by divide.
    """
    return sum(1 for num in numbers if num % divide == 0)

def test_list_divide():
    """
    Test list_divide function.
    """
    try:
        assert list_divide([1,2,3,4,5]) == 2
        assert list_divide([2,4,6,8,10]) == 5
        assert list_divide([30, 54, 63,98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1,2,3,4,5], 1) == 5
    except AssertionError:
        raise ListDivideException("Test failed")

# Run the test function if the script is executed directly
if __name__ == "__main__":
    test_list_divide()
    print("All tests passed successfully.")
