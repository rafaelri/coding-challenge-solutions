from fibonacci_dp import fibonacci
from hamcrest import *

def test_fibonnaci_zero():
    assert_that(fibonacci(0), equal_to(0))

def test_fibonnaci_one():
    assert_that(fibonacci(1), equal_to(1))

def test_fibonnaci_two():
    assert_that(fibonacci(2), equal_to(1))

def test_fibonnaci_three():
    assert_that(fibonacci(3), equal_to(2))