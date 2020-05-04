from hamcrest import *
from alt_list import reorder_alt_list

def test_single_element():
    assert_that(reorder_alt_list([ "a" ]), equal_to( [ "a" ]))


def test_two_elements():
    assert_that(reorder_alt_list([ "a", "b" ]), equal_to( [ "a", "b" ]))    

def test_three_elements():
    assert_that(reorder_alt_list([ "a", "b", "c" ]), equal_to( [ "a", "c", "b" ]))        