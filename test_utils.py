import pytest
import utils

def test_add_positive():
    assert utils.add(2, 3) == 5

def test_add_negative():
    assert utils.add(-1, -1) == -2

def test_factorial_zero_one():
    assert utils.factorial(0) == 1
    assert utils.factorial(1) == 1

def test_factorial_normal():
    assert utils.factorial(5) == 120

def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        utils.factorial(-2)

def test_is_prime_small():
    assert utils.is_prime(2)
    assert utils.is_prime(3)
    assert not utils.is_prime(1)
    assert not utils.is_prime(0)

def test_is_prime_composite():
    assert not utils.is_prime(9)
    assert not utils.is_prime(15)
    assert utils.is_prime(13)

def test_normalize_text():
    assert utils.normalize_text("  hello   world  ") == "hello world"

def test_parse_int_safe_valid():
    assert utils.parse_int_safe("10") == 10

def test_parse_int_safe_invalid():
    assert utils.parse_int_safe("abc", default=-1) == -1

def test_unique_sorted():
    assert utils.unique_sorted([3,1,2,3]) == [1,2,3]

def test_fibonacci_base():
    assert utils.fibonacci(0) == 0
    assert utils.fibonacci(1) == 1
    assert utils.fibonacci(2) == 1

def test_fibonacci_normal():
    assert utils.fibonacci(7) == 13

def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        utils.fibonacci(-3)

def test_merge_dicts():
    a = {"x":1, "y":2}
    b = {"y":20, "z":3}
    assert utils.merge_dicts(a,b) == {"x":1, "y":20, "z":3}

def test_max_subarray_sum_all_positive():
    assert utils.max_subarray_sum([1,2,3]) == 6

def test_max_subarray_sum_mixed():
    assert utils.max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_max_subarray_sum_empty():
    assert utils.max_subarray_sum([]) == 0

def test_max_subarray_sum_single_negative():
    assert utils.max_subarray_sum([-5]) == -5
