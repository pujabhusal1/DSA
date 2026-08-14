def get_sum(a, b):
    """
    Returns the sum of two numbers.
    Inputs are always in the range -10000 to 10000

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b

# Variety of test cases to validate the function
assert(get_sum(-200, 200) == 0)
assert(get_sum(1000, -999) == 1)  
assert(get_sum(-8888, 2) == -8886)# Normal case
assert(get_sum(-100000, 100000 == 0))
assert(get_sum(10, 7000) == 7010)


# Boundary Value test
assert(get_sum(-10000, 5000) == -5000)
assert(get_sum(8000, 100) == 8100)
assert(get_sum(2000, - 9000) == -7000)